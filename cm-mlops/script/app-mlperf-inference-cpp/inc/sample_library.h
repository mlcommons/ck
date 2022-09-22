#ifndef SAMPLE_LIBRARY_H_
#define SAMPLE_LIBRARY_H_

#include <cstddef>
#include <fstream>
#include <iostream>
#include <string>
#include <regex>
#include <vector>

#include "query_sample_library.h"

#include "backend.h"
#include "npy.h"

class SampleLibrary : public mlperf::QuerySampleLibrary {
public:
    SampleLibrary(
        const std::string &name, std::shared_ptr<Backend> &backend,
        size_t max_sample_count, size_t num_inputs)
            : name(name), backend(backend), max_sample_count(max_sample_count), num_inputs(num_inputs) {}

    const std::string &Name() override { return name; }
    size_t PerformanceSampleCount() override { return backend->PerformanceSampleCount(); }
    size_t TotalSampleCount() override {
        return max_sample_count != 0 ? std::min(max_sample_count, NumSamples()) : NumSamples();
    }

    void LoadSamplesToRam(const std::vector<mlperf::QuerySampleIndex> &samples) override {
        std::cerr << "loading samples to ram" << std::endl;
        for (size_t i = 0; i < samples.size(); i++) {
            mlperf::QuerySampleIndex sample = samples[i];
            std::vector<std::vector<uint8_t>> input_datas(num_inputs);
            std::vector<size_t> input_sizes(num_inputs);
            std::vector<std::vector<size_t>> input_shapes(num_inputs);
            for (size_t j = 0; j < num_inputs; j++) {
                GetSample(sample, j, input_datas[j], input_sizes[j], input_shapes[j]);
            }
            backend->LoadSampleToRam(sample, i, input_datas, input_sizes, input_shapes);
        }
        backend->FinishLoading();
    }

    void UnloadSamplesFromRam(const std::vector<mlperf::QuerySampleIndex> &samples) override {
        for (mlperf::QuerySampleIndex sample : samples)
            backend->UnloadSampleFromRam(sample);
    }

    virtual size_t NumSamples() = 0;

    virtual void GetSample(
        mlperf::QuerySampleIndex sample_index,
        size_t input_index,
        std::vector<uint8_t> &data,
        size_t &size,
        std::vector<size_t> &shape) = 0;

protected:
    std::shared_ptr<Backend> backend;
    size_t max_sample_count;
    size_t num_inputs;

private:
    std::string name{"SampleLibrary"};
};

class Imagenet : public SampleLibrary {
public:
    Imagenet(
        std::shared_ptr<Backend> &backend, size_t max_sample_count,
        std::string preprocessed_path, std::string val_map_path)
            : SampleLibrary("ImageNet", backend, max_sample_count, 1) {
        std::ifstream val_map(val_map_path);
        std::string line;
        std::regex val_map_regex("\\s*([\\.\\w]*)\\s+(\\d+)\\s*");
        while (std::getline(val_map, line)) {
            std::smatch match;
            std::regex_match(line, match, val_map_regex);
            std::string image_data_file = match[1];
            int64_t label = std::stoi(match[2]);
            std::string image_data_path = preprocessed_path + "/" + image_data_file + ".npy";

            std::ifstream f(image_data_path);
            if (f.good()) {
                image_data_paths.push_back(image_data_path);
                labels.push_back(label);
            }
        }
        std::cerr << "loaded imagenet with " << TotalSampleCount() << " samples" << std::endl;
    }

    size_t NumSamples() override {
        return image_data_paths.size();
    }

    void GetSample(
            mlperf::QuerySampleIndex sample_index,
            size_t input_index,
            std::vector<uint8_t> &data,
            size_t &size,
            std::vector<size_t> &shape) override {
        npy::NpyFile image_file(image_data_paths[sample_index]);
        std::vector<char> data_char;
        image_file.loadAll(data_char);
        data.assign(data_char.begin(), data_char.end());
        size = image_file.getTensorSize();
        shape = image_file.getDims();
    }

    int64_t GetLabel(mlperf::QuerySampleIndex sample_index) {
        return labels[sample_index];
    }

private:
    std::vector<std::string> image_data_paths;
    std::vector<int64_t> labels;
};

#endif // SAMPLE_LIBRARY_H_
