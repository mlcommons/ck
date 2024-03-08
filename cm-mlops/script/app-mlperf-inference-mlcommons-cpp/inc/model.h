#ifndef MODEL_H_
#define MODEL_H_

#include <cstddef>
#include <cstdint>
#include <string>
#include <vector>

#include "query_sample.h"

class Model {
public:
    Model(
        std::string model_path,
        size_t num_inputs, std::vector<std::string> input_names,
        std::vector<size_t> input_sizes, std::vector<std::vector<size_t>> input_shapes,
        size_t num_outputs, std::vector<std::string> output_names,
        std::vector<size_t> output_sizes, std::vector<std::vector<size_t>> output_shapes) :
        model_path(model_path),
        num_inputs(num_inputs), input_names(input_names), input_sizes(input_sizes), input_shapes(input_shapes),
        num_outputs(num_outputs), output_names(output_names), output_sizes(output_sizes), output_shapes(output_shapes) {}

    std::string model_path;

    size_t num_inputs;
    std::vector<std::string> input_names;
    // maximum size for memory allocation purpose
    std::vector<size_t> input_sizes;
    // input shape, if fixed
    std::vector<std::vector<size_t>> input_shapes;

    size_t num_outputs;
    std::vector<std::string> output_names;
    // output size & shape, if fixed
    std::vector<size_t> output_sizes;
    std::vector<std::vector<size_t>> output_shapes;

    /**
     * @brief Post-process raw output from model and store in LoadGen response
     *
     * @param index query sample index
     * @param raw raw outputs
     * @param raw_shapes shapes of corresponding outputs
     * @param response_buffer response buffer to write to
     */
    virtual void PostProcess(
        mlperf::QuerySampleIndex index,
        const std::vector<void *> &raw,
        const std::vector<std::vector<size_t>> &raw_shapes,
        std::vector<uint8_t> &response_buffer) = 0;
};

class Resnet50 : public Model {
public:
    Resnet50(std::string model_path, int64_t argmax_shift) :
        Model(
            model_path,
            1, {"input_tensor:0"}, {3 * 224 * 224 * sizeof(float)}, {{3, 224, 224}},
            1, {"ArgMax:0"}, {sizeof(int64_t)}, {{1}}),
        argmax_shift(argmax_shift) {}

    void PostProcess(
            mlperf::QuerySampleIndex index,
            const std::vector<void *> &raw,
            const std::vector<std::vector<size_t>> &raw_shapes,
            std::vector<uint8_t> &response_buffer) override {
        response_buffer.resize(sizeof(int64_t));
        int64_t *buffer = reinterpret_cast<int64_t *>(response_buffer.data());
        buffer[0] = *static_cast<int64_t *>(raw.front()) + argmax_shift;
    }

private:
    int64_t argmax_shift;
};

class Retinanet : public Model {
public:
    Retinanet(std::string model_path, size_t width, size_t height, float score_threshold) :
        Model(
            model_path,
            1, {"images"}, {3 * width * height * sizeof(float)}, {{3, width, height}},
            // no fixed output sizes/shapes
            3, {"boxes", "scores", "labels"}, {0, 0, 0}, {{0, 4}, {0}, {0}}),
        width(width), height(height),
        score_threshold(score_threshold) {}

    void PostProcess(
            mlperf::QuerySampleIndex index,
            const std::vector<void *> &raw,
            const std::vector<std::vector<size_t>> &raw_shapes,
            std::vector<uint8_t> &response_buffer) override {
        float *const boxes = static_cast<float *const>(raw.at(0));
        float *const scores = static_cast<float *const>(raw.at(1));
        int64_t *const labels = static_cast<int64_t *const>(raw.at(2));
        const std::vector<size_t> &boxes_shape = raw_shapes.at(0);
        const std::vector<size_t> &scores_shape = raw_shapes.at(1);
        const std::vector<size_t> &labels_shape = raw_shapes.at(2);

        size_t keep = 0;
        while (keep < scores_shape[0] && scores[keep] >= score_threshold)
            keep++;

        response_buffer.resize(7 * keep * sizeof(float));
        float *buffer = reinterpret_cast<float *>(response_buffer.data());
        for (size_t i = 0; i < keep; i++) {
            int64_t label = labels[i];
            float *const box = &boxes[4 * i];
            buffer[7 * i + 0] = static_cast<float>(index);
            buffer[7 * i + 1] = box[1] / 800.0f;
            buffer[7 * i + 2] = box[0] / 800.0f;
            buffer[7 * i + 3] = box[3] / 800.0f;
            buffer[7 * i + 4] = box[2] / 800.0f;
            buffer[7 * i + 5] = scores[i];
            buffer[7 * i + 6] = static_cast<float>(label);
        }
    }

private:
    size_t width;
    size_t height;
    float score_threshold;
};

#endif // MODEL_H_
