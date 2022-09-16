#ifndef BACKEND_H_
#define BACKEND_H_

#include <cstddef>
#include <iostream>
#include <map>
#include <memory>
#include <vector>

#include "loadgen.h"
#include "query_sample.h"

#include "device.h"
#include "model.h"

class Backend {
public:
    Backend(std::shared_ptr<Model> &model, std::shared_ptr<Device> &device,
            size_t performance_sample_count, size_t batch_size)
            : model(model), device(device)
            , performance_sample_count(performance_sample_count), batch_size(batch_size) {
        num_memory = device->NumMemory();
        num_inputs = model->num_inputs;
        num_samples_in_memory = 0;
        // have batch_size padding at the end that cycles back to beginning for contiguity
        size_t memory_capacity = performance_sample_count + batch_size;
        samples.resize(memory_capacity);
        sample_memory.resize(num_inputs);
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
        }
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
            size_t index_in_memory,
            const std::vector<std::vector<uint8_t>> &input_datas,
            const std::vector<size_t> &input_sizes,
            const std::vector<std::vector<size_t>> &input_shapes) {
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

            // write to memory
            for (size_t j = 0; j < num_memory; j++) {
                void *destination = GetMemoryAddress(input_index, j, index_in_memory);
                device->Write(j, destination, input_data);
            }
        }

        num_samples_in_memory++;
    }

    void FinishLoading() {
        // copy first batch to end of memory to form cycle
        std::cerr << "copying";
        for (size_t k = 0; k < batch_size - 1; k++) {
            samples[num_samples_in_memory] = samples[k];
            std::vector<std::vector<uint8_t>> data(num_inputs);
            for (size_t i = 0; i < num_inputs; i++)
                for (size_t j = 0; j < num_memory; j++)
                    device->Read(j, data[i], GetMemoryAddress(i, j, k), model->input_sizes[i]);
            // LoadSampleToRam increments num_samples_in_memory, so this copies samples[k] to end of memory
            LoadSampleToRam(samples[k].index, num_samples_in_memory, data, samples[k].size, samples[k].shape);
        }
        std::cerr << std::endl;

        // write suffices of samples vector to contiguity tree
        size_t memory_capacity = performance_sample_count + batch_size;
        for (size_t start = 0; start < memory_capacity; start++) {
            Trie *node = &batches;
            for (size_t end = start; end < std::min(start + batch_size, memory_capacity); end++) {
                node = &node->children[samples[end].index];
                node->index_in_memory = samples[start].index_in_memory;
            }
        }
    }

    void UnloadSampleFromRam(mlperf::QuerySampleIndex sample_index) {
        sample_map.erase(sample_index);
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
        std::cerr << "node " << concurrency_index
                  << " running batch #" << batch.front().index << "-#" << batch.back().index << std::endl;

        // batch pointer in memory [input_index]
        std::vector<void *> batch_data(num_inputs);
        
        // gather samples
        size_t memory_index = device->GetMemoryIndex(concurrency_index);
        for (size_t i = 0; i < num_inputs; i++) {
            // if input is contiguous, use input directly as batch address
            // otherwise, gather a batch to batch_memory
            if (contiguous) {
                batch_data[i] = GetMemoryAddress(i, memory_index, node->index_in_memory);
            } else {
                // copy data if not contiguous
                for (size_t k = 0; k < batch.size(); k++) {
                    const mlperf::QuerySample &sample = batch[k];
                    void *sample_address = GetMemoryAddress(i, memory_index, sample_map[sample.index].index_in_memory);
                    void *batch_sample_address = GetBatchMemoryAddress(i, memory_index, k);
                    device->Copy(memory_index, batch_sample_address, sample_address, model->input_sizes[i]);
                }
                batch_data[i] = batch_memory[i][memory_index];
            }
        }

        RunInference(concurrency_index, batch, batch_data);
    }

    void *GetMemoryAddress(size_t input_index, size_t memory_index, size_t index_in_memory) const {
        size_t offset = index_in_memory * model->input_sizes[input_index];
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

    // run inference on a batch of samples
    // concurrency_index is which device concurrency (device/core/thread) to run on
    // batch is the indices of the input
    // batch_data is pointer to inputs in the device memory
    // on finish, calls mlperf::QuerySamplesComplete
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
    // batch_memory[input_index][memory_index] points to working memory for a batch
    std::vector<std::vector<void *>> batch_memory;

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
    size_t num_samples_in_memory;
    // sample_map[sample_id] last recorded sample with sample_id in memory
    std::map<mlperf::QuerySampleIndex, Sample> sample_map;

    // tree for determining batch contiguity (substring tree trimmed to batch size)
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
            response[i].size = sizeof(float);
        }
        mlperf::QuerySamplesComplete(response.data(), response.size());
    }

private:
    // labels for ImageNet samples #1, #324
    float dummy_response{65.0f};
};

#endif // BACKEND_H_
