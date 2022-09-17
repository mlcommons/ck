#ifndef ONNXRUNTIME_BACKEND_H_
#define ONNXRUNTIME_BACKEND_H_

#include <memory>
#include <vector>
#include <cstring>

#include "onnxruntime_cxx_api.h"

#include "loadgen.h"

#include "backend.h"

class OnnxRuntimeCPUBackend : public Backend {
public:
    OnnxRuntimeCPUBackend(
            std::shared_ptr<Model> &model, std::shared_ptr<Device> &device,
            size_t performance_sample_count, size_t batch_size,
            const std::vector<ONNXTensorElementDataType> &input_types)
            : Backend(model, device, performance_sample_count, batch_size)
            , env(ORT_LOGGING_LEVEL_WARNING, "env"), input_types(input_types)
            , info_cpu{Ort::MemoryInfo::CreateCpu(OrtAllocatorType::OrtArenaAllocator, OrtMemTypeDefault)} {
        Ort::SessionOptions session_options;
        session_options.SetIntraOpNumThreads(1);
        session_options.SetExecutionMode(ExecutionMode::ORT_SEQUENTIAL);
        // FIXME: the resnet50 does not work with optimization level 3 (ORT_ENABLE_ALL)
        session_options.SetGraphOptimizationLevel(GraphOptimizationLevel::ORT_ENABLE_EXTENDED);

        for (size_t i = 0; i < device->NumConcurrency(); i++) {
            sessions.emplace_back(env, model->model_path.c_str(), session_options);
            bindings.emplace_back(sessions[i]);
        }
    }

    void RunInference(
            size_t concurrency_index,
            const std::vector<mlperf::QuerySample> &batch,
            std::vector<void *> &batch_data) override {
        Ort::Session &session = sessions[concurrency_index];
        Ort::IoBinding &binding = bindings[concurrency_index];
        for (size_t i = 0; i < model->num_inputs; i++) {
            size_t size = batch.size() * model->input_sizes[i];
            const std::vector<size_t> &shape = GetSampleShape(batch[0].index, i);
            std::vector<int64_t> input_shape;
            input_shape.push_back(batch.size());
            for (size_t dim : shape)
                input_shape.push_back(dim);
            ONNXTensorElementDataType input_type =
                session.GetInputTypeInfo(i).GetTensorTypeAndShapeInfo().GetElementType();
            Ort::Value value = Ort::Value::CreateTensor(
                info_cpu, batch_data[i], size, input_shape.data(), input_shape.size(), input_type);
            binding.BindInput(model->input_names[i].c_str(), value);
        }

        for (std::string &output : model->output_names)
            binding.BindOutput(output.c_str(), info_cpu);

        session.Run(Ort::RunOptions(), binding);

        std::vector<Ort::Value> outputs = binding.GetOutputValues();
        std::vector<mlperf::QuerySampleResponse> responses(batch.size());
        std::vector<std::vector<uint8_t>> response_buffers(batch.size());
        for (size_t i = 0; i < batch.size(); i++) {
            void *response;
            size_t output_size;
            if (model->num_outputs == 1) {
                response = outputs[0].GetTensorMutableData<uint8_t>() + i * model->output_sizes[0];
                output_size = model->output_sizes[0];
            } else {
                output_size = std::accumulate(model->output_sizes.begin(), model->output_sizes.end(), 0);
                response_buffers[i].resize(output_size);
                size_t offset = 0;
                for (size_t j = 0; j < model->num_outputs; j++) {
                    std::memcpy(
                        response_buffers[i].data() + offset,
                        outputs[j].GetTensorData<uint8_t>() + i * model->output_sizes[i],
                        model->output_sizes[j]);
                    offset += model->output_sizes[j];
                }
                response = response_buffers[i].data();
            }

            if (model->postprocess)
                model->postprocess(response);

            responses[i].id = batch[i].id;
            responses[i].data = reinterpret_cast<uintptr_t>(response);
            responses[i].size = output_size;
        }
        mlperf::QuerySamplesComplete(responses.data(), responses.size());

        binding.ClearBoundInputs();
        binding.ClearBoundOutputs();
    };

private:
    Ort::Env env;
    Ort::MemoryInfo info_cpu;
    std::vector<Ort::Session> sessions;
    std::vector<Ort::IoBinding> bindings;
    std::vector<ONNXTensorElementDataType> input_types;
};

#endif // ONNXRUNTIME_BACKEND_H_
