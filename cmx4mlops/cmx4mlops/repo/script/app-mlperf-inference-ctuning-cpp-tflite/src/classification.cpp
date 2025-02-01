/*
 * Copyright (c) 2018 cTuning foundation.
 * See CK COPYRIGHT.txt for copyright details.
 *
 * See CK LICENSE for licensing details.
 * See CK COPYRIGHT for copyright details.
 */

#include <future>
#include <algorithm>
#include <numeric>

#include "loadgen.h"
#include "query_sample_library.h"
#include "system_under_test.h"
#include "test_settings.h"


#include "benchmark.h"

#include "tensorflow/lite/kernels/register.h"
#include "tensorflow/lite/model.h"

using namespace std;
using namespace CK;


template <typename TData, typename TInConverter, typename TOutConverter>
class TFLiteBenchmark : public Benchmark<TData, TInConverter, TOutConverter> {
public:
  TFLiteBenchmark(const BenchmarkSettings* settings, tflite::Interpreter* interpreter, int input_index)
    : Benchmark<TData, TInConverter, TOutConverter>(
      settings, interpreter->typed_tensor<TData>(input_index), interpreter->typed_output_tensor<TData>(0)) {
  }
};

class Program {
public:
  Program () {
    settings = new BenchmarkSettings(MODEL_TYPE::LITE);

    session = new BenchmarkSession(settings);

    cout << "\nLoading graph..." << endl;

    model = tflite::FlatBufferModel::BuildFromFile(settings->graph_file().c_str());
    if (!model)
      throw "Failed to load graph from file " + settings->graph_file();

    tflite::ops::builtin::BuiltinOpResolver resolver;
    tflite::InterpreterBuilder(*model, resolver)(&interpreter);
    if (!interpreter)
      throw string("Failed to construct interpreter");
    if (interpreter->AllocateTensors() != kTfLiteOk)
      throw string("Failed to allocate tensors");

    interpreter->SetNumThreads(settings->number_of_threads());

    int input_index = interpreter->inputs()[0];
    int output_index = interpreter->outputs()[0];
    auto input_type = interpreter->tensor(input_index)->type;
    auto output_type = interpreter->tensor(output_index)->type;
    if (input_type != output_type)
      throw format("Type of graph's input (%d) does not match type of its output (%d).",
                    int(input_type), int(output_type));

    switch (input_type) {
      case kTfLiteFloat32:
        if (settings->skip_internal_preprocessing)
          benchmark.reset(new TFLiteBenchmark<float, InCopy, OutCopy>(settings, interpreter.get(), input_index));
        else
          benchmark.reset(new TFLiteBenchmark<float, InNormalize, OutCopy>(settings, interpreter.get(), input_index));
        break;

      case kTfLiteUInt8:
        benchmark.reset(new TFLiteBenchmark<uint8_t, InCopy, OutDequantize>(settings, interpreter.get(), input_index));
        break;

      default:
        throw format("Unsupported type of graph's input: %d. "
                      "Supported types are: Float32 (%d), UInt8 (%d)",
                      int(input_type), int(kTfLiteFloat32), int(kTfLiteUInt8));
    }

    TfLiteIntArray* in_dims = interpreter->tensor(input_index)->dims;
    int in_num = in_dims->data[0];
    int in_height = in_dims->data[1];
    int in_width = in_dims->data[2];
    int in_channels = in_dims->data[3];
    cout << format("Input tensor dimensions (NHWC): %d*%d*%d*%d", in_num, in_height, in_width, in_channels) << endl;
    if (in_height != settings->image_size ||
        in_width != settings->image_size ||
        in_channels != settings->num_channels)
      throw format("Dimensions of graph's input do not correspond to dimensions of input image (%d*%d*%d*%d)",
                    settings->batch_size, settings->image_size, settings->image_size, settings->num_channels);

    TfLiteIntArray* out_dims = interpreter->tensor(output_index)->dims;
    int out_num = out_dims->data[0];
    int out_classes = out_dims->data[1];
    cout << format("Output tensor dimensions: %d*%d", out_num, out_classes) << endl;
    if (out_classes != settings->num_classes && out_classes != settings->num_classes+1)
      throw format("Unsupported number of classes in graph's output tensor. Supported numbers are %d and %d",
                    settings->num_classes, settings->num_classes+1);
    benchmark->has_background_class = out_classes == settings->num_classes+1;
  }

  ~Program() {
  }

  //bool is_available_batch() {return session? session->get_next_batch(): false; }

  void LoadNextBatch(const std::vector<mlperf::QuerySampleIndex>& img_indices) {
    auto vl = settings->verbosity_level;

    if( vl > 1 ) {
      cout << "LoadNextBatch([";
      for( auto idx : img_indices) {
        cout << idx << ' ';
      }
      cout << "])" << endl;
    } else if( vl ) {
      cout << 'B' << flush;
    }
    session->load_filenames(img_indices);
    benchmark->load_images( session );
    if( vl ) {
      cout << endl;
    }
  }

  void ColdRun() {
    auto vl = settings->verbosity_level;

    if( vl > 1 ) {
      cout << "Triggering a Cold Run..." << endl;
    } else if( vl ) {
      cout << 'C' << flush;
    }

    if (interpreter->Invoke() != kTfLiteOk)
      throw "Failed to invoke tflite";
  }

  int InferenceOnce(int img_idx) {
    benchmark->get_random_image( img_idx );
    if (interpreter->Invoke() != kTfLiteOk)
      throw "Failed to invoke tflite";
    return benchmark->get_next_result();
  }

  void UnloadBatch(const std::vector<mlperf::QuerySampleIndex>& img_indices) {
    auto b_size = img_indices.size();

    auto vl = settings->verbosity_level;

    if( vl > 1 ) {
      cout << "Unloading a batch[" << b_size << "]" << endl;
    } else if( vl ) {
      cout << 'U' << flush;
    }

    benchmark->unload_images(b_size);
    //benchmark->save_results( );
  }

  const int available_images_max() { return settings->list_of_available_imagefiles().size(); }
  const int images_in_memory_max() { return settings->images_in_memory_max; }

  BenchmarkSettings *settings;
private:
  BenchmarkSession *session;
  unique_ptr<IBenchmark> benchmark;
  unique_ptr<tflite::Interpreter> interpreter;
  unique_ptr<tflite::FlatBufferModel> model;
};


class SystemUnderTestSingleStream : public mlperf::SystemUnderTest {
public:
  SystemUnderTestSingleStream(Program *_prg) : mlperf::SystemUnderTest() {
    prg = _prg;
    query_counter = 0;
  };

  ~SystemUnderTestSingleStream() override = default;

  const std::string& Name() { return name_; }

  void IssueQuery(const std::vector<mlperf::QuerySample>& samples) override {

    ++query_counter;
    auto vl = prg->settings->verbosity_level;
    if( vl > 1 ) {
      cout << query_counter << ") IssueQuery([" << samples.size() << "]," << samples[0].id << "," << samples[0].index << ")" << endl;
    } else if ( vl ) {
      cout << 'Q' << flush;
    }

    std::vector<mlperf::QuerySampleResponse> responses;
    responses.reserve(samples.size());
    float encoding_buffer[samples.size()];
    int i=0;
    for (auto s : samples) {
      int predicted_class = prg->InferenceOnce(s.index);

      if( vl > 1 ) {
        cout << "Query image index: " << s.index << " -> Predicted class: " << predicted_class << endl << endl;
      } else if ( vl ) {
        cout << 'p' << flush;
      }

      /* This would be the correct way to pass in one integer index:
      */
//      int single_value_buffer[] = { (int)predicted_class };

      /* This conversion is subtly but terribly wrong
         yet we use it here in order to use Guenther's parsing script:
      */
      encoding_buffer[i] = (float)predicted_class;
      responses.push_back({s.id, uintptr_t(&encoding_buffer[i]), sizeof(encoding_buffer[i])});
      ++i;
    }
    mlperf::QuerySamplesComplete(responses.data(), responses.size());
  }

  void FlushQueries() override {
    auto vl = prg->settings->verbosity_level;
    if ( vl ) {
      cout << endl;
    }
  }

  void ReportLatencyResults(const std::vector<mlperf::QuerySampleLatency>& latencies_ns)  {

    size_t size = latencies_ns.size();
    uint64_t avg = accumulate(latencies_ns.begin(), latencies_ns.end(), uint64_t(0) )/size;

    std::vector<mlperf::QuerySampleLatency> sorted_lat(latencies_ns.begin(), latencies_ns.end());
    sort(sorted_lat.begin(), sorted_lat.end());

    cout << endl << "------------------------------------------------------------";
    cout << endl << "|            LATENCIES (in nanoseconds and fps)            |";
    cout << endl << "------------------------------------------------------------";
    size_t p50 = size * 0.5;
    size_t p90 = size * 0.9;
    cout << endl << "Number of queries run: " << size;
    cout << endl << "Min latency:                      " << sorted_lat[0]       << "ns  (" << 1e9/sorted_lat[0]         << " fps)";
    cout << endl << "Median latency:                   " << sorted_lat[p50]     << "ns  (" << 1e9/sorted_lat[p50]       << " fps)";
    cout << endl << "Average latency:                  " << avg                 << "ns  (" << 1e9/avg                   << " fps)";
    cout << endl << "90 percentile latency:            " << sorted_lat[p90]     << "ns  (" << 1e9/sorted_lat[p90]       << " fps)";

    if(!prg->settings->trigger_cold_run) {
      cout << endl << "First query (cold model) latency: " << latencies_ns[0]     << "ns  (" << 1e9/latencies_ns[0]       << " fps)";
    }
    cout << endl << "Max latency:                      " << sorted_lat[size-1]  << "ns  (" << 1e9/sorted_lat[size-1]    << " fps)";
    cout << endl << "------------------------------------------------------------ " << endl;
  }

private:
  std::string name_{"TFLite_SUT"};
  Program *prg;
  long query_counter;
};

class QuerySampleLibrarySingleStream : public mlperf::QuerySampleLibrary {
public:
  QuerySampleLibrarySingleStream(Program *_prg) : mlperf::QuerySampleLibrary() {
    prg = _prg;
  };

  ~QuerySampleLibrarySingleStream() = default;

  const std::string& Name() override { return name_; }

  size_t TotalSampleCount() override { return prg->available_images_max(); }

  size_t PerformanceSampleCount() override { return prg->images_in_memory_max(); }

  void LoadSamplesToRam( const std::vector<mlperf::QuerySampleIndex>& samples) override {
    prg->LoadNextBatch(samples);
    return;
  }

  void UnloadSamplesFromRam( const std::vector<mlperf::QuerySampleIndex>& samples) override {
    prg->UnloadBatch(samples);
    return;
  }

private:
  std::string name_{"TFLite_QSL"};
  Program *prg;
};

void TestSingleStream(Program *prg) {
  SystemUnderTestSingleStream sut(prg);
  QuerySampleLibrarySingleStream qsl(prg);

  const std::string mlperf_conf_path = getenv_s("CM_MLPERF_CONF");
  const std::string user_conf_path = getenv_s("CM_MLPERF_USER_CONF");
  const std::string audit_conf_path = getenv_opt_s("CM_MLPERF_INFERENCE_AUDIT_PATH","");

  std::string model_name = getenv_opt_s("CM_MODEL", "unknown_model");
  std::string logs_dir = getenv_opt_s("CM_MLPERF_LOADGEN_LOGS_DIR", "");

  const std::string scenario_string = getenv_s("CM_MLPERF_LOADGEN_SCENARIO");
  const std::string mode_string = getenv_s("CM_MLPERF_LOADGEN_MODE");

  std::cout << "Path to mlperf.conf : " << mlperf_conf_path << std::endl;
  std::cout << "Path to user.conf : " << user_conf_path << std::endl;
  std::cout << "Model Name: " << model_name << std::endl;
  std::cout << "LoadGen Scenario: " << scenario_string << std::endl;
  std::cout << "LoadGen Mode: " << ( mode_string != "" ? mode_string : "(empty string)" ) << std::endl;

  mlperf::TestSettings ts;

  // This should have been done automatically inside ts.FromConfig() !
  ts.scenario = ( scenario_string == "SingleStream")    ? mlperf::TestScenario::SingleStream
              : ( scenario_string == "MultiStream")     ? mlperf::TestScenario::MultiStream
              : ( scenario_string == "Server")          ? mlperf::TestScenario::Server
              : ( scenario_string == "Offline")         ? mlperf::TestScenario::Offline : mlperf::TestScenario::SingleStream;

  if( mode_string != "")
    ts.mode   = ( mode_string == "SubmissionRun")       ? mlperf::TestMode::SubmissionRun
              : ( mode_string == "accuracy")        ? mlperf::TestMode::AccuracyOnly
              : ( mode_string == "performance")     ? mlperf::TestMode::PerformanceOnly
              : ( mode_string == "findpeakperformance") ? mlperf::TestMode::FindPeakPerformance : mlperf::TestMode::SubmissionRun;

  if (ts.FromConfig(mlperf_conf_path, model_name, scenario_string)) {
    std::cout << "Issue with mlperf.conf file at " << mlperf_conf_path << std::endl;
    exit(1);
  }

  if (ts.FromConfig(user_conf_path, model_name, scenario_string)) {
    std::cout << "Issue with user.conf file at " << user_conf_path << std::endl;
    exit(1);
  }

  mlperf::LogSettings log_settings;
  log_settings.log_output.outdir = logs_dir;
  log_settings.log_output.prefix_with_datetime = false;
  log_settings.enable_trace = false;


  if (prg->settings->trigger_cold_run) {
    prg->ColdRun();
  }

  mlperf::StartTest(&sut, &qsl, ts, log_settings, audit_conf_path);
}

int main(int argc, char* argv[]) {
  try {
    Program *prg = new Program();
    TestSingleStream(prg);
    delete prg;
  }
  catch (const string& error_message) {
    cerr << "ERROR: " << error_message << endl;
    return -1;
  }
  return 0;
}
