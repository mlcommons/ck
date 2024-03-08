#ifndef ONNXRUNTIME_BACKEND_H_
#define ONNXRUNTIME_BACKEND_H_

#include <memory>
#include <vector>
#include <cstring>

#include "onnxruntime_cxx_api.h"

#include "loadgen.h"

#include "backend.h"

class OnnxRuntimeBackend : public Backend {
public:
    OnnxRuntimeBackend(
            std::shared_ptr<Model> &model, std::shared_ptr<Device> &device,
            size_t performance_sample_count, size_t batch_size,
            bool use_cuda)
            : Backend(model, device, performance_sample_count, batch_size)
            , env(ORT_LOGGING_LEVEL_WARNING, "env") {
        for (size_t i = 0; i < device->NumMemory(); i++) {
            memory_infos.emplace_back(
                use_cuda ? "Cuda" : "Cpu",
                OrtAllocatorType::OrtArenaAllocator, i, OrtMemTypeDefault);
        }

        for (size_t i = 0; i < device->NumConcurrency(); i++) {
            Ort::SessionOptions session_options;
            // arm64 does not work with optimization level 3 (ORT_ENABLE_ALL)
            if (getenv("ORT_ENABLE_ALL", "") == "no")
                session_options.SetGraphOptimizationLevel(GraphOptimizationLevel::ORT_ENABLE_EXTENDED);

            const auto &api = Ort::GetApi();

            std::vector<const char *> keys{"device_id"};
            std::vector<const char *> values{std::to_string(i).c_str()};

            OrtCUDAProviderOptionsV2 *cuda_options = nullptr;
            if (use_cuda) {
                Ort::ThrowOnError(api.CreateCUDAProviderOptions(&cuda_options));

                Ort::ThrowOnError(api.UpdateCUDAProviderOptions(cuda_options, keys.data(), values.data(), keys.size()));

                Ort::ThrowOnError(api.SessionOptionsAppendExecutionProvider_CUDA_V2(
                    static_cast<OrtSessionOptions *>(session_options),
                    cuda_options));
            }

            sessions.emplace_back(env, model->model_path.c_str(), session_options);
            bindings.emplace_back(sessions[i]);

            if (use_cuda) {
                api.ReleaseCUDAProviderOptions(cuda_options);
	    }
        }
    }

    void RunInference(
            size_t concurrency_index,
            const std::vector<mlperf::QuerySample> &batch,
            std::vector<void *> &batch_data) override {
        Ort::Session &session = sessions[concurrency_index];
        Ort::IoBinding &binding = bindings[concurrency_index];
        size_t memory_index = device->GetMemoryIndex(concurrency_index);

        for (size_t i = 0; i < model->num_inputs; i++) {
            size_t size = batch.size() * GetSampleSize(batch.front().index, i);
            const std::vector<size_t> &shape = GetSampleShape(batch.front().index, i);
            std::vector<int64_t> input_shape;
            input_shape.push_back(batch.size());
            for (size_t dim : shape)
                input_shape.push_back(dim);
            ONNXTensorElementDataType input_type =
                session.GetInputTypeInfo(i).GetTensorTypeAndShapeInfo().GetElementType();
            Ort::Value value = Ort::Value::CreateTensor(
                memory_infos[memory_index],
                batch_data[i], size,
                input_shape.data(), input_shape.size(),
                input_type);
            binding.BindInput(model->input_names[i].c_str(), value);
        }

        for (std::string &output : model->output_names)
            binding.BindOutput(output.c_str(), memory_info_cpu);

        session.Run(Ort::RunOptions(), binding);

        std::vector<Ort::Value> outputs = binding.GetOutputValues();
        std::vector<mlperf::QuerySampleResponse> responses(batch.size());
        std::vector<std::vector<uint8_t>> response_buffers(batch.size());
        for (size_t i = 0; i < batch.size(); i++) {
            // get output data and shapes
            std::vector<void *> output_buffers(outputs.size());
            std::vector<std::vector<size_t>> output_shapes(outputs.size());
            for (size_t j = 0; j < outputs.size(); j++) {
                // assume ith position in output is ith sample in batch
                output_buffers[j] =
                    static_cast<uint8_t *>(outputs[j].GetTensorMutableData<void>())
                    + i * model->output_sizes[j];
                size_t rank = outputs[j].GetTensorTypeAndShapeInfo().GetDimensionsCount();
                std::vector<int64_t> output_shape(rank);
                outputs[j].GetTensorTypeAndShapeInfo().GetDimensions(output_shape.data(), rank);
                output_shapes[j].resize(rank);
                for (size_t k = 0; k < rank; k++)
                    output_shapes[j][k] = output_shape[k];
            }

            model->PostProcess(
                batch[i].index, output_buffers, output_shapes, response_buffers[i]);

            responses[i].id = batch[i].id;
            responses[i].data = reinterpret_cast<uintptr_t>(response_buffers[i].data());
            responses[i].size = response_buffers[i].size();
        }

        mlperf::QuerySamplesComplete(responses.data(), responses.size());

        binding.ClearBoundInputs();
        binding.ClearBoundOutputs();
    };

private:
    Ort::Env env;
    std::vector<Ort::Session> sessions;
    std::vector<Ort::IoBinding> bindings;
    std::vector<Ort::MemoryInfo> memory_infos;
    Ort::MemoryInfo memory_info_cpu{
        Ort::MemoryInfo::CreateCpu(OrtAllocatorType::OrtArenaAllocator, OrtMemTypeDefault)};
};

#endif // ONNXRUNTIME_BACKEND_H_
