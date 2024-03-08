/*
 * Copyright (c) 2018 cTuning foundation.
 * See CK COPYRIGHT.txt for copyright details.
 *
 * See CK LICENSE for licensing details.
 * See CK COPYRIGHT for copyright details.
 */

#pragma once

#include <stdio.h>
#include <stdlib.h>

#include <dirent.h>
#include <fstream>
#include <iostream>
#include <sstream>
#include <memory>
#include <string.h>
#include <thread>
#include <vector>
#include <map>

#define DEBUG(msg) std::cout << "DEBUG: " << msg << std::endl;

namespace CK {

enum MODEL_TYPE {
  LITE,
  TF_FROZEN
};


/// Load mandatory string value from the environment.
inline std::string getenv_s(const std::string& name) {
  const char *value = getenv(name.c_str());
  if (!value)
    throw "Required environment variable " + name + " is not set";
  return std::string(value);
}

inline std::string getenv_opt_s(const std::string& name, const std::string default_value) {
  const char *value = getenv(name.c_str());
  if (!value)
    return default_value;
  else
    return std::string(value);
}


/// Load mandatory integer value from the environment.
inline int getenv_i(const std::string& name) {
  const char *value = getenv(name.c_str());
  if (!value)
    throw "Required environment variable " + name + " is not set";
  return atoi(value);
}

/// Load mandatory float value from the environment.
inline float getenv_f(const std::string& name) {
  const char *value = getenv(name.c_str());
  if (!value)
    throw "Required environment variable " + name + " is not set";
  return atof(value);
}

/// Load an optional boolean value from the environment.
inline bool getenv_b(const char *name) {
    std::string value = getenv(name);

    return (value == "YES" || value == "yes" || value == "ON" || value == "on" || value == "1");
}

/// Dummy `sprintf` like formatting function using std::string.
/// It uses buffer of fixed length so can't be used in any cases,
/// generally use it for short messages with numeric arguments.
template <typename ...Args>
inline std::string format(const char* str, Args ...args) {
  char buf[1024];
  sprintf(buf, str, args...);
  return std::string(buf);
}

//----------------------------------------------------------------------

class Accumulator {
public:
  void reset() { _total = 0, _count = 0; }
  void add(float value) { _total += value, _count++; }
  float total() const { return _total; }
  float avg() const { return _total / static_cast<float>(_count); }
private:
  float _total = 0;
  int _count = 0;
};

//----------------------------------------------------------------------

class BenchmarkSettings {
public:
  const std::string images_dir = getenv_s("CM_DATASET_PREPROCESSED_PATH");
  const std::string available_images_file = getenv_s("CM_DATASET_PREPROCESSED_IMAGES_LIST");
  const bool skip_internal_preprocessing =  (getenv_opt_s("CM_DATASET_COMPRESSED", "off") ==  "off");
  const std::string result_dir = getenv_s("CM_MLPERF_OUTPUT_DIR");
  const std::string input_layer_name = getenv_s("CM_ML_MODEL_INPUT_LAYER_NAME");
  const std::string output_layer_name = getenv_s("CM_ML_MODEL_OUTPUT_LAYER_NAME");
  const int images_in_memory_max = getenv_i("CM_LOADGEN_BUFFER_SIZE");
  const int image_size = getenv_i("CM_DATASET_INPUT_SQUARE_SIDE");
  const int batch_size = 1;
  const int num_channels = 3;
  const int num_classes = 1000;
  const bool normalize_img = getenv_b("CM_ML_MODEL_NORMALIZE_DATA");

  const bool subtract_mean = getenv_b("CM_ML_MODEL_SUBTRACT_MEANS");
  const char *given_channel_means_str = getenv("CM_ML_MODEL_GIVEN_CHANNEL_MEANS");

  const bool trigger_cold_run = getenv_b("CM_MLPERF_LOADGEN_TRIGGER_COLD_RUN");

  const int verbosity_level = getenv_i("CM_VERBOSE");

  BenchmarkSettings(enum MODEL_TYPE mode = MODEL_TYPE::LITE) {

    if (given_channel_means_str) {
      std::stringstream ss(given_channel_means_str);
      for(int i=0;i<3;i++){
        ss >> given_channel_means[i];
      }
    }

    switch (mode)
    {
    case MODEL_TYPE::LITE:
      _graph_file = getenv_s("CM_ML_MODEL_FILE_WITH_PATH");
      break;

    case MODEL_TYPE::TF_FROZEN:
      _graph_file = getenv_s("CM_ML_MODEL_FILE_WITH_PATH");
      break;

    default:
      std::cout << "Unsupported MODEL_TYPE" << std::endl;
      exit(-1);
      break;
    };
    _number_of_threads = std::thread::hardware_concurrency();

    if (getenv_opt_s("CM_HOST_USE_ALL_CORES", "no") !=  "yes") {
        _number_of_threads = _number_of_threads < 1 ? 1 : _number_of_threads;
        _number_of_threads = !getenv("CM_HOST_CPU_TOTAL_CORES")
                         ? _number_of_threads
                         : getenv_i("CM_HOST_CPU_TOTAL_CORES");
        if (getenv_i("CM_HOST_CPU_TOTAL_CORES") && getenv_i("CM_HOST_CPU_THREADS_PER_CORE")) {
            _number_of_threads = getenv_i("CM_HOST_CPU_TOTAL_CORES") / getenv_i("CM_HOST_CPU_THREADS_PER_CORE");
        }
    }
    // Print settings
    std::cout << "Graph file: " << _graph_file << std::endl;
    std::cout << "Image dir: " << images_dir << std::endl;
    std::cout << "Image list: " << available_images_file << std::endl;
    std::cout << "Image size: " << image_size << std::endl;
    std::cout << "Image channels: " << num_channels << std::endl;
    std::cout << "Prediction classes: " << num_classes << std::endl;
    std::cout << "Result dir: " << result_dir << std::endl;
    std::cout << "How many images fit in memory buffer: " << images_in_memory_max << std::endl;
    std::cout << "Normalize: " << normalize_img << std::endl;
    std::cout << "Subtract mean: " << subtract_mean << std::endl;
    std::cout << "Run time preprocessing: " << !skip_internal_preprocessing << std::endl;
    std::cout << "Number of Threads: " << _number_of_threads << std::endl;
    if(subtract_mean && given_channel_means_str)
        std::cout << "Per-channel means to subtract: " << given_channel_means[0]
            << ", " << given_channel_means[1]
            << ", " << given_channel_means[2] << std::endl;

    // Create results dir if none
    auto dir = opendir(result_dir.c_str());
    if (dir)
      closedir(dir);
    else
      system(("mkdir " + result_dir).c_str());

    // Load list of images to be processed
    std::ifstream file(available_images_file);
    if (!file)
      throw "Unable to open the available image list file " + available_images_file;
    for (std::string s; !getline(file, s).fail();)
      _available_image_list.emplace_back(s);
    std::cout << "Number of available imagefiles: " << _available_image_list.size() << std::endl;
  }

  const std::vector<std::string>& list_of_available_imagefiles() const { return _available_image_list; }

  std::vector<std::string> _available_image_list;

  int number_of_threads() { return _number_of_threads; }

  std::string graph_file() { return _graph_file; }

  float given_channel_means[3];
private:
  int _number_of_threads;
  std::string _graph_file;
};

//----------------------------------------------------------------------

class BenchmarkSession {
public:
  BenchmarkSession(const BenchmarkSettings* settings): _settings(settings) {
  }

  virtual ~BenchmarkSession() {}

  const std::vector<std::string>& load_filenames(std::vector<size_t> img_indices) {
    _filenames_buffer.clear();
    _filenames_buffer.reserve( img_indices.size() );
    idx2loc.clear();

    auto list_of_available_imagefiles = _settings->list_of_available_imagefiles();
    auto count_available_imagefiles   = list_of_available_imagefiles.size();

    int loc=0;
    for (auto idx : img_indices) {
      if(idx<count_available_imagefiles) {
        _filenames_buffer.emplace_back(list_of_available_imagefiles[idx]);
        idx2loc[idx] = loc++;
      } else {
        std::cerr << "Trying to load filename[" << idx << "] when only " << count_available_imagefiles << " images are available" << std::endl;
        exit(1);
      }
    }

    return _filenames_buffer;
  }

  const std::vector<std::string>& current_filenames() const { return _filenames_buffer; }

  std::map<int,int> idx2loc;

private:
  const BenchmarkSettings* _settings;
  std::vector<std::string> _filenames_buffer;
};

//----------------------------------------------------------------------

template <typename TData>
class StaticBuffer {
public:
  StaticBuffer(int size, const std::string& dir): _size(size), _dir(dir) {
    _buffer = new TData[size];
  }

  virtual ~StaticBuffer() {
    delete[] _buffer;
  }

  TData* data() const { return _buffer; }
  int size() const { return _size; }

protected:
  const int _size;
  const std::string _dir;
  TData* _buffer;
};

//----------------------------------------------------------------------

class ImageData : public StaticBuffer<uint8_t> {
public:
  ImageData(const BenchmarkSettings* s): StaticBuffer(
    s->image_size * s->image_size * s->num_channels * (s->skip_internal_preprocessing ? sizeof(float) : sizeof(uint8_t)),
    s->images_dir) {}

  void load(const std::string& filepath, int vl) {
    //auto path = _dir + '/' + filename;
    auto path = filepath;
    std::ifstream file(path, std::ios::in | std::ios::binary);
    if (!file) throw "Failed to open image data " + path;
    file.read(reinterpret_cast<char*>(_buffer), _size);
    if( vl > 1) {
      std::cout << "Loaded file: " << path << std::endl;
    } else if ( vl ) {
      std::cout << 'l' << std::flush;
    }
  }
};

//----------------------------------------------------------------------

class ResultData : public StaticBuffer<float> {
public:
  ResultData(const BenchmarkSettings* s): StaticBuffer<float>(
    s->num_classes, s->result_dir) {}

  void save(const std::string& filename) {
    auto path = _dir + '/' + filename + ".txt";
    std::ofstream file(path);
    if (!file) throw "Unable to create result file " + path;
    for (int i = 0; i < _size; i++)
      file << _buffer[i] << std::endl;
  }

  int argmax() {
    int   arg_index = 0;
    float max_value = _buffer[0];

    for (int i = 1; i < _size; i++) {
      if (_buffer[i] > max_value) {
        arg_index = i;
        max_value = _buffer[i];
      }
    }

    return arg_index;
  }
};

//----------------------------------------------------------------------

class IBenchmark {
public:
  bool has_background_class = false;

  virtual ~IBenchmark() {}
  virtual void load_images(BenchmarkSession *session) = 0;
  virtual void unload_images(size_t num_examples) = 0;
  virtual void save_results() = 0;
  virtual int get_next_result() = 0;
  virtual void get_random_image(int img_idx) = 0;
};


template <typename TData, typename TInConverter, typename TOutConverter>
class Benchmark : public IBenchmark {
public:
  Benchmark(const BenchmarkSettings* settings, TData *in_ptr, TData *out_ptr): _settings(settings) {
    _in_ptr = in_ptr;
    _out_ptr = out_ptr;
    _in_converter.reset(new TInConverter(settings));
    _out_converter.reset(new TOutConverter(settings));
  }

  void load_images(BenchmarkSession *_session) override {
    session = _session;
    auto vl = _settings->verbosity_level;

    const std::vector<std::string>& image_filenames = session->current_filenames();

    int length = image_filenames.size();
    _current_buffer_size = length;
    _in_batch = new std::unique_ptr<ImageData>[length];
    _out_batch = new std::unique_ptr<ResultData>[length];
    int i = 0;
    for (auto image_file : image_filenames) {
      _in_batch[i].reset(new ImageData(_settings));
      _out_batch[i].reset(new ResultData(_settings));
      _in_batch[i]->load(image_file, vl);
      i++;
    }
  }

  void unload_images(size_t num_examples) override {
    for(size_t i=0;i<num_examples;i++) {
      delete _in_batch[i].get();
      delete _out_batch[i].get();
    }
  }

  void get_random_image(int img_idx) override {
    _in_converter->convert(_in_batch[ session->idx2loc[img_idx] ].get(), _in_ptr);
  }

  int get_next_result() override {
    int probe_offset = has_background_class ? 1 : 0;
    ResultData *next_result_ptr = _out_batch[_out_buffer_index++].get();
    _out_converter->convert(_out_ptr + probe_offset, next_result_ptr);
    _out_buffer_index %= _current_buffer_size;
    return next_result_ptr->argmax();
  }

  void save_results() override {
    const std::vector<std::string>& image_filenames = session->current_filenames();
    int i = 0;
    for (auto image_file : image_filenames) {
      _out_batch[i++]->save(image_file);
    }
  }

private:
  const BenchmarkSettings* _settings;
  BenchmarkSession* session;
  int _out_buffer_index = 0;
  int _current_buffer_size = 0;
  TData* _in_ptr;
  TData* _out_ptr;
  std::unique_ptr<ImageData> *_in_batch;
  std::unique_ptr<ResultData> *_out_batch;
  std::unique_ptr<TInConverter> _in_converter;
  std::unique_ptr<TOutConverter> _out_converter;
};

//----------------------------------------------------------------------

class IinputConverter {
public:
  virtual ~IinputConverter() {}
  virtual void convert(const ImageData* source, void* target) = 0;
};

//----------------------------------------------------------------------

class InCopy : public IinputConverter {
public:
  InCopy(const BenchmarkSettings* s) {}

  void convert(const ImageData* source, void* target) {
    uint8_t *uint8_target = static_cast<uint8_t *>(target);
    std::copy(source->data(), source->data() + source->size(), uint8_target);
  }
};

//----------------------------------------------------------------------

class InNormalize : public IinputConverter {
public:
  InNormalize(const BenchmarkSettings* s):
    _normalize_img(s->normalize_img),
    _subtract_mean(s->subtract_mean),
    _given_channel_means(s->given_channel_means),
    _num_channels(s->num_channels) {
  }

  void convert(const ImageData* source, void* target) {
    // Copy image data to target
    float *float_target = static_cast<float *>(target);
    float sum = 0;
    for (int i = 0; i < source->size(); i++) {
      float px = source->data()[i];
      if (_normalize_img)
        px = (px / 255.0 - 0.5) * 2.0;
      sum += px;
      float_target[i] = px;
    }
    // Subtract mean value if required
    if (_subtract_mean) {
      if(_given_channel_means) {
        for (int i = 0; i < source->size(); i++){
          float_target[i] -= _given_channel_means[i % _num_channels];    // assuming NHWC order!
	}
      } else {
        float mean = sum / static_cast<float>(source->size());
        for (int i = 0; i < source->size(); i++)
          float_target[i] -= mean;
      }
    }
  }

private:
  const bool _normalize_img;
  const bool _subtract_mean;
  const float *_given_channel_means;
  const int _num_channels;
};

//----------------------------------------------------------------------

class OutCopy {
public:
  OutCopy(const BenchmarkSettings* s) {}

  void convert(const float* source, ResultData* target) const {
    std::copy(source, source + target->size(), target->data());
  }
};

//----------------------------------------------------------------------

class OutDequantize {
public:
  OutDequantize(const BenchmarkSettings* s) {}

  void convert(const uint8_t* source, ResultData* target) const {
    for (int i = 0; i < target->size(); i++)
      target->data()[i] = source[i] / 255.0;
  }
};

} // namespace CK
