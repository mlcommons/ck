#ifndef BACKEND_H_
#define BACKEND_H_

#include <cstddef>
#include <cstdint>
#include <iostream>
#include <map>
#include <memory>
#include <vector>
#include <cstring>
#include <mutex>

#include "loadgen.h"
#include "query_sample.h"

#include "device.h"
#include "model.h"

/**
 * The Backend base class manages how samples are stored in memory,
 * receives queries from SUT and issues them to derived classes via RunInference.
 *
 * For memory storage, on calls to LoadSampleFromRam() from the QSL, loaded samples are
 * stored contiguously into each device memory. The Backend class retains the
 * location of every sample in device memory.
 *
 * When SUT issues a batch to run on a device concurrency, the backend class retrieves
 * the location in memory of this batch, and passes this to RunInference implemented by
 * derived classes (e.g. OnnxRuntimeBackend).
 */
class Backend {
public:
    Backend(std::shared_ptr<Model> &model, std::shared_ptr<Device> &device,
            size_t performance_sample_count, size_t batch_size)
            : model(model), device(device)
            , performance_sample_count(performance_sample_count), batch_size(batch_size)
            , num_memory(device->NumMemory()), num_inputs(model->num_inputs)
            , batch_memory_mutex(num_memory) {
        // have batch_size padding at the end that cycles back to beginning for contiguity
        size_t memory_capacity = performance_sample_count + batch_size;
        samples.resize(memory_capacity);
        sample_memory.resize(num_inputs);
        sample_memory_size.resize(num_inputs, 0);
        sample_memory_offset.resize(num_inputs);
        batch_memory.resize(num_inputs);
        for (size_t i = 0; i < num_inputs; i++) {
            sample_memory[i].resize(num_memory);
            batch_memory[i].resize(num_memory);
            for (size_t j = 0; j < num_memory; j++) {
                sample_memory[i][j] =
                    device->Alloc(j, model->input_sizes[i] * memory_capacity);
                // working memory for an incontiguous batch
                batch_memory[i][j] =
                    device->Alloc(j, model->input_sizes[i] * batch_size);
            }
            sample_memory_offset[i].resize(memory_capacity, 0);
        }

        if (performance_sample_count == 0)
            std::cerr << "warning: performance sample count = 0" << std::endl;
    }

    virtual ~Backend() {
        for (size_t i = 0; i < num_inputs; i++) {
            for (size_t j = 0; j < num_memory; j++) {
                device->Free(j, sample_memory[i][j]);
                device->Free(j, batch_memory[i][j]);
            }
        }
    }

    size_t NumConcurrency() const {
        return device->NumConcurrency();
    }

    size_t PerformanceSampleCount() const {
        return performance_sample_count;
    }

    size_t MaxBatchSize() const {
        return batch_size;
    }

    // load input to device memory
    void LoadSampleToRam(
            mlperf::QuerySampleIndex sample_index,
            const std::vector<std::vector<uint8_t>> &input_datas,
            const std::vector<size_t> &input_sizes,
            const std::vector<std::vector<size_t>> &input_shapes) {
        size_t index_in_memory = num_samples_in_memory;
        Sample sample;
        sample.index = sample_index;
        sample.shape = input_shapes;
        sample.size = input_sizes;
        sample.index_in_memory = index_in_memory;

        samples[index_in_memory] = sample;
        sample_map[sample_index] = sample;

        for (size_t input_index = 0; input_index < num_inputs; input_index++) {
            const std::vector<uint8_t> &input_data = input_datas[input_index];
            size_t input_size = input_sizes[input_index];

            if (sample_memory_size[input_index] + input_size >
                (performance_sample_count + batch_size) * model->input_sizes[input_index])
                std::cerr << "warning: memory exceeded; try increasing model->input_sizes" << std::endl;

            // write to end of memory
            sample_memory_offset[input_index][index_in_memory] = sample_memory_size[input_index];
            sample_memory_size[input_index] += input_size;
            for (size_t j = 0; j < num_memory; j++) {
                void *destination = GetMemoryAddress(input_index, j, index_in_memory);
                device->Write(j, destination, input_data);
            }
        }

        num_samples_in_memory++;
    }

    void FinishLoading() {
        return; //This probably needs a FinishUnLoading counterpart
        // copy first batch to end of memory to form cycle
        for (size_t k = 0; k < batch_size - 1; k++) {
            size_t index_in_memory = k % performance_sample_count;
            std::vector<std::vector<uint8_t>> data(num_inputs);
            for (size_t i = 0; i < num_inputs; i++)
                device->Read(
                    0, data[i], GetMemoryAddress(i, 0, index_in_memory), samples[index_in_memory].size[i]);
            // LoadSampleToRam copies samples[index_in_memory] to end of memory
            LoadSampleToRam(
                samples[index_in_memory].index, data,
                samples[index_in_memory].size, samples[index_in_memory].shape);
        }
        // write substrings of samples vector to contiguity tree

        for (size_t start = 0; start < num_samples_in_memory; start++) {
            Trie *node = &batches;
            for (size_t end = start; end < std::min(start + batch_size, num_samples_in_memory); end++) {
                node = &node->children[samples[end].index];
                node->index_in_memory = samples[start].index_in_memory;
            }
        }
    }

    void UnloadSampleFromRam(mlperf::QuerySampleIndex sample_index) {
        for (size_t i = 0; i < num_inputs; i++)
            sample_memory_size[i] -= GetSampleSize(sample_index, i);
        batches.children.erase(sample_index);
        num_samples_in_memory--;
    }

    void IssueBatch(
            size_t concurrency_index,
            const std::vector<mlperf::QuerySample> &batch) {
        // determine contiguity
        bool contiguous = true;
        Trie *node = &batches;
        for (const mlperf::QuerySample &sample : batch) {
            auto next = node->children.find(sample.index);
            if (next != node->children.end()) {
                node = &next->second;
            } else {
                contiguous = false;
                break;
            }
        }
        // std::cerr << "node " << concurrency_index
        //           << " running batch #" << batch.front().index << "-#" << batch.back().index
        //           << " (" << (contiguous ? "contiguous" : "incontiguous") << ")" << std::endl;

        // batch pointer in memory [input_index]
        std::vector<void *> batch_data(num_inputs);

        // gather samples
        size_t memory_index = device->GetMemoryIndex(concurrency_index);
        // might use batch_memory
        std::unique_lock<std::mutex> batch_memory_lock{batch_memory_mutex[memory_index], std::defer_lock};
        for (size_t i = 0; i < num_inputs; i++) {
            // if input is contiguous, use input directly as batch address
            // otherwise, gather a batch to batch_memory
            if (contiguous) {
                batch_data[i] = GetMemoryAddress(i, memory_index, node->index_in_memory);
            } else {
                // copy data if not contiguous
                batch_memory_lock.lock();
                for (size_t k = 0; k < batch.size(); k++) {
                    const mlperf::QuerySample &sample = batch[k];
                    void *sample_address = GetMemoryAddress(i, memory_index, sample_map[sample.index].index_in_memory);
                    void *batch_sample_address = GetBatchMemoryAddress(i, memory_index, k);
                    device->Copy(memory_index, batch_sample_address, sample_address, GetSampleSize(sample.index, i));
                }
                batch_data[i] = batch_memory[i][memory_index];
            }
        }

        RunInference(concurrency_index, batch, batch_data);
    }

    void *GetMemoryAddress(size_t input_index, size_t memory_index, size_t index_in_memory) const {
        size_t offset = sample_memory_offset[input_index][index_in_memory];
        return static_cast<uint8_t *>(sample_memory[input_index][memory_index]) + offset;
    }

    void *GetBatchMemoryAddress(size_t input_index, size_t memory_index, size_t index_in_memory) const {
        size_t offset = index_in_memory * model->input_sizes[input_index];
        return static_cast<uint8_t *>(batch_memory[input_index][memory_index]) + offset;
    }

    const std::vector<size_t> &GetSampleShape(mlperf::QuerySampleIndex sample_index, size_t input_index) {
        return sample_map[sample_index].shape[input_index];
    }

    size_t GetSampleSize(mlperf::QuerySampleIndex sample_index, size_t input_index) {
        return sample_map[sample_index].size[input_index];
    }

    void SetDeviceConcurrencyIndex(size_t concurrency_index) {
        device->SetConcurrencyIndex(concurrency_index);
    }

    /**
     * @brief Runs inference on a batch of samples and calls mlperf::QuerySamplesComplete
     * 
     * @param concurrency_index which device concurrency (device/core/thread) to run on
     * @param batch the indices of the input
     * @param batch_data pointer to inputs in the device memory
     */
    virtual void RunInference(
        size_t concurrency_index,
        const std::vector<mlperf::QuerySample> &batch,
        std::vector<void *> &batch_data) = 0;

protected:
    std::shared_ptr<Model> model;
    std::shared_ptr<Device> device;
    size_t performance_sample_count;
    size_t batch_size;
    size_t num_memory;
    size_t num_inputs;

private:
    // sample_memory[input_index][memory_index] points to loaded input buffer in device memory
    std::vector<std::vector<void *>> sample_memory;
    // sample_memory_size[input_index] is current # bytes in this buffer
    std::vector<size_t> sample_memory_size;
    // sample_memory_offset[input_index][index_in_memory] is the offset to a sample input
    std::vector<std::vector<size_t>> sample_memory_offset;
    // batch_memory[input_index][memory_index] points to working memory for a batch
    std::vector<std::vector<void *>> batch_memory;

    // batch_memory_mutex[memory_index] is mutex for using batch_memory
    std::vector<std::mutex> batch_memory_mutex;

    // smallest unit of input stored in memory
    struct Sample {
        mlperf::QuerySampleIndex index;
        size_t index_in_memory;
        // sample data and sizes indexed by input_index
        std::vector<std::vector<size_t>> shape;
        std::vector<size_t> size;
    };
    // information of samples currently in memory (ordered)
    std::vector<Sample> samples;
    // number of samples currently in memory
    size_t num_samples_in_memory{0};
    // sample_map[sample_id] last recorded sample with sample_id in memory
    std::map<mlperf::QuerySampleIndex, Sample> sample_map;

    // tree for determining batch contiguity (index tree)
    struct Trie {
        // index_in_memory is location of a contiguous batch from root to this node
        size_t index_in_memory;
        std::map<mlperf::QuerySampleIndex, Trie> children;
    };
    Trie batches;
};

class DummyBackend : public Backend {
public:
    DummyBackend(
        std::shared_ptr<Model> &model, std::shared_ptr<Device> &device,
        size_t performance_sample_count, size_t batch_size)
        : Backend(model, device, performance_sample_count, batch_size) {}

    void RunInference(
            size_t concurrency_index,
            const std::vector<mlperf::QuerySample> &batch,
            std::vector<void *> &batch_data) override {
        size_t size = batch.size();
        std::vector<mlperf::QuerySampleResponse> response(size);
        for (size_t i = 0; i < size; i++) {
            response[i].id = batch[i].id;
            response[i].data = reinterpret_cast<uintptr_t>(&dummy_response);
            response[i].size = sizeof(int64_t);
        }
        mlperf::QuerySamplesComplete(response.data(), response.size());
    }

private:
    // labels for ImageNet samples #1, #324
    int64_t dummy_response{65};
};

#endif // BACKEND_H_
