#ifndef SAMPLE_LIBRARY_H_
#define SAMPLE_LIBRARY_H_

#include <cstddef>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <regex>
#include <vector>

#include "query_sample_library.h"

#include "backend.h"
#include "npy.h"

/**
 * SampleLibrary reads stored samples on request of LoadGen and passes
 * them to Backend. Derived classes specify how samples are read (e.g. from .npy files)
 */
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
        std::cerr << "loading samples to ram with total sample size: " << samples.size()<< std::endl;
        for (size_t i = 0; i < samples.size(); i++) {
            mlperf::QuerySampleIndex sample = samples[i];
            std::vector<std::vector<uint8_t>> input_datas(num_inputs);
            std::vector<size_t> input_sizes(num_inputs);
            std::vector<std::vector<size_t>> input_shapes(num_inputs);
            for (size_t j = 0; j < num_inputs; j++) {
                GetSample(sample, j, input_datas[j], input_sizes[j], input_shapes[j]);
            }
            backend->LoadSampleToRam(sample, input_datas, input_sizes, input_shapes);
        }
        backend->FinishLoading();
    }

    void UnloadSamplesFromRam(const std::vector<mlperf::QuerySampleIndex> &samples) override {
        for (mlperf::QuerySampleIndex sample : samples){
            backend->UnloadSampleFromRam(sample);
	}
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

class NumpyLibrary : public SampleLibrary {
public:
    /**
     * @brief Constructs a QSL with .npy files in a directory
     * 
     * @param backend backend to use
     * @param max_sample_count maximum library size (use 0 for unlimited size)
     * @param preprocessed_path path to directory containing .npy files
     * @param filenames filenames of npy files: <preprocessed_path>/<filename>
     */
    NumpyLibrary(
        std::shared_ptr<Backend> &backend, size_t max_sample_count,
        std::string preprocessed_path,
        const std::vector<std::string> &filenames)
            : SampleLibrary("NumpyLibrary", backend, max_sample_count, 1) {
        for (std::string filename : filenames) {
            std::string file_path = preprocessed_path + "/" + filename;

            std::ifstream f(file_path);
            if (f.good())
                file_paths.push_back(file_path);
        }
    }

    size_t NumSamples() override {
        return file_paths.size();
    }

    void GetSample(
            mlperf::QuerySampleIndex sample_index,
            size_t input_index,
            std::vector<uint8_t> &data,
            size_t &size,
            std::vector<size_t> &shape) override {
        npy::NpyFile data_file(file_paths[sample_index]);
        std::vector<char> data_char;
        data_file.loadAll(data_char);
        data.assign(data_char.begin(), data_char.end());
        size = data_file.getTensorSize();
        shape = data_file.getDims();
    }

private:
    std::vector<std::string> file_paths;
};

class Imagenet : public NumpyLibrary {
public:
    Imagenet(
        std::shared_ptr<Backend> &backend, size_t max_sample_count,
        std::string preprocessed_path, std::string val_map_path)
            : NumpyLibrary(
                backend, max_sample_count, preprocessed_path,
                ReadValMap(val_map_path)) {
        std::cerr << "loaded imagenet with " << TotalSampleCount() << " samples" << std::endl;
    }

private:
    static const std::vector<std::string> ReadValMap(std::string val_map_path) {
        std::vector<std::string> filenames;
        std::ifstream val_map(val_map_path);
        std::string line;
        std::regex val_map_regex(R"(\s*([\.\w]*)\s+(\d+)\s*)");
        while (std::getline(val_map, line)) {
            std::smatch match;
            std::regex_match(line, match, val_map_regex);
            std::string image_filename = match[1];
            int64_t label = std::stoi(match[2]);

            filenames.push_back(image_filename + ".npy");
        }
        return filenames;
    }
};

class Openimages : public NumpyLibrary {
public:
    Openimages(
        std::shared_ptr<Backend> &backend, size_t max_sample_count,
        std::string preprocessed_path, std::string annotations_path)
            : NumpyLibrary(
                backend, max_sample_count, preprocessed_path,
                ReadAnnotations(annotations_path, max_sample_count)) {
        std::cerr << "loaded openimages with " << TotalSampleCount() << " samples" << std::endl;
    }

private:
    static const std::vector<std::string> ReadAnnotations(
            std::string annotations_path, size_t max_sample_count) {
        std::vector<std::string> filenames;
        std::ifstream val_map(annotations_path);
        std::stringstream buffer;
        buffer << val_map.rdbuf();
        std::string annotations = buffer.str();

        std::regex image_regex(R"(\"file_name\": \"([^\"]*)\")");
        std::smatch match;

        while (std::regex_search(annotations, match, image_regex) && filenames.size() < max_sample_count) {
            std::string image_filename = match[1];

            filenames.push_back(image_filename + ".npy");
            annotations = match.suffix();
        }
        return filenames;
    }
};

#endif // SAMPLE_LIBRARY_H_
