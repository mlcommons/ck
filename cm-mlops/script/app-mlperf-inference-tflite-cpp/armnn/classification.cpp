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

#include "armnn/ArmNN.hpp"
#include "armnn/Exceptions.hpp"
#include "armnn/Tensor.hpp"
#include "armnn/INetwork.hpp"
#include "armnnTfLiteParser/ITfLiteParser.hpp"

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

class ArmNNBenchmark : public Benchmark<TData, TInConverter, TOutConverter> {
public:
    ArmNNBenchmark(const BenchmarkSettings* settings, TData *in_ptr, TData *out_ptr)
            : Benchmark<TData, TInConverter, TOutConverter>(settings, in_ptr, out_ptr) {
    }
};

armnn::InputTensors MakeInputTensors(const std::pair<armnn::LayerBindingId,
        armnn::TensorInfo>& input, const void* inputTensorData)
{
    return { {input.first, armnn::ConstTensor(input.second, inputTensorData) } };
}

armnn::OutputTensors MakeOutputTensors(const std::pair<armnn::LayerBindingId,
        armnn::TensorInfo>& output, void* outputTensorData)
{
    return { {output.first, armnn::Tensor(output.second, outputTensorData) } };
}

class Program {
public:
  Program () : runtime( armnn::IRuntime::Create(options) ) {

    bool use_neon                   = getenv_b("CM_MLPERF_TFLITE_USE_NEON");
    bool use_opencl                 = getenv_b("CM_MLPERF_TFLITE_USE_OPENCL");
    string input_layer_name         = getenv_s("CM_ML_MODEL_INPUT_LAYER_NAME");
    string output_layer_name        = getenv_s("CM_ML_MODEL_OUTPUT_LAYER_NAME");

    settings = new BenchmarkSettings(MODEL_TYPE::LITE);

    session = new BenchmarkSession(settings);

    armnnTfLiteParser::ITfLiteParserPtr parser = armnnTfLiteParser::ITfLiteParser::Create();

    // Optimize the network for a specific runtime compute device, e.g. CpuAcc, GpuAcc
    //std::vector<armnn::BackendId> optOptions = {armnn::Compute::CpuAcc, armnn::Compute::GpuAcc};
    std::vector<armnn::BackendId> optOptions = {armnn::Compute::CpuRef};
    if( use_neon && use_opencl) {
        optOptions = {armnn::Compute::CpuAcc, armnn::Compute::GpuAcc};
    } else if( use_neon ) {
        optOptions = {armnn::Compute::CpuAcc};
    } else if( use_opencl ) {
        optOptions = {armnn::Compute::GpuAcc};
    }

    cout << "\nLoading graph..." << endl;

    armnn::INetworkPtr network = parser->CreateNetworkFromBinaryFile(settings->graph_file().c_str());
    if (!network)
        throw "Failed to load graph from file";

    armnnTfLiteParser::BindingPointInfo inputBindingInfo = parser->GetNetworkInputBindingInfo(0, input_layer_name);
    armnnTfLiteParser::BindingPointInfo outputBindingInfo = parser->GetNetworkOutputBindingInfo(0, output_layer_name);

    armnn::TensorShape inShape = inputBindingInfo.second.GetShape();
    armnn::TensorShape outShape = outputBindingInfo.second.GetShape();
    std::size_t inSize = inShape[0] * inShape[1] * inShape[2] * inShape[3];
    std::size_t outSize = outShape[0] * outShape[1];

    armnn::IOptimizedNetworkPtr optNet = armnn::Optimize(*network, optOptions, runtime->GetDeviceSpec());

    runtime->LoadNetwork(networkIdentifier, std::move(optNet));

    armnn::DataType input_type = inputBindingInfo.second.GetDataType();
    armnn::DataType output_type = outputBindingInfo.second.GetDataType();
    if (input_type != output_type)
        throw format("Type of graph's input (%d) does not match type of its output (%d).", int(input_type), int(output_type));

    void* input = input_type == armnn::DataType::Float32 ? (void*)new float[inSize] : (void*)new uint8_t[inSize];
    void* output = output_type == armnn::DataType::Float32 ? (void*)new float[outSize] : (void*)new uint8_t[outSize];

    inputTensor = MakeInputTensors(inputBindingInfo, input);
    outputTensor = MakeOutputTensors(outputBindingInfo, output);

    switch (input_type) {
        case armnn::DataType::Float32:
            if (settings->skip_internal_preprocessing) {
                cout << "************* Type 1" << endl;
                benchmark.reset(new ArmNNBenchmark<float, InCopy, OutCopy>(settings, (float*)input, (float*)output));
            } else {
                cout << "************* Type 2" << endl;
                benchmark.reset(new ArmNNBenchmark<float, InNormalize, OutCopy>(settings, (float*)input, (float*)output));
            }
            break;

        case armnn::DataType::QAsymmU8:
            benchmark.reset(new ArmNNBenchmark<uint8_t, InCopy, OutDequantize>(settings, (uint8_t*)input, (uint8_t*)output));
            break;

        default:
            throw format("Unsupported type of graph's input: %d. "
                         "Supported types are: Float32 (%d), UInt8 (%d)",
                         int(input_type), int(armnn::DataType::Float32), int(armnn::DataType::QAsymmU8));
    }

    int out_num = outShape[0];
    int out_classes = outShape[1];
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

    if (runtime->EnqueueWorkload(networkIdentifier, inputTensor, outputTensor) != armnn::Status::Success)
        throw "Failed to invoke the classifier";
  }

  int InferenceOnce(int img_idx) {
    benchmark->get_random_image( img_idx );

    if (runtime->EnqueueWorkload(networkIdentifier, inputTensor, outputTensor) != armnn::Status::Success)
        throw "Failed to invoke the classifier";

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
  armnn::NetworkId networkIdentifier;
  armnn::OutputTensors outputTensor;
  armnn::InputTensors inputTensor;
  armnn::IRuntime::CreationOptions options;
  armnn::IRuntimePtr runtime;
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

  mlperf::StartTest(&sut, &qsl, ts, log_settings);
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
