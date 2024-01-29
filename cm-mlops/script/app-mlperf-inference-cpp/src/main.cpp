#include <cstddef>
#include <cstring>
#include <string>
#include <climits>

#include "loadgen.h"
#include "test_settings.h"
#include "common.h"
#include "backend.h"
#include "device.h"
#include "model.h"
#include "sample_library.h"
#include "system.h"
#ifdef CM_MLPERF_DEVICE_GPU
    #include "gpu_device.h"
#endif

#ifdef CM_MLPERF_BACKEND_ONNXRUNTIME
    #include "onnxruntime_backend.h"
#endif

class InputSettings {

public:
    InputSettings() {
        mlperf_conf_path = getenv("CM_MLPERF_CONF", "../inference/mlperf.conf");
        user_conf_path = getenv("CM_MLPERF_USER_CONF", "../inference/vision/classification_and_detection/user.conf");
        audit_conf_path = getenv("CM_MLPERF_INFERENCE_AUDIT_PATH", "");
        output_dir = getenv("CM_MLPERF_OUTPUT_DIR", ".");
        backend_name = getenv("CM_MLPERF_BACKEND", "onnxruntime");
        device_name = getenv("CM_MLPERF_DEVICE", "cpu");
        model_name = getenv("CM_MODEL", "resnet50");
        model_path = getenv("CM_ML_MODEL_FILE_WITH_PATH", "");
        dataset_preprocessed_path = getenv("CM_DATASET_PREPROCESSED_PATH", "");
        dataset_path = getenv("CM_DATASET_PATH", "");
        dataset_list = getenv("CM_DATASET_LIST", "");
        imagenet_val_path = getenv("CM_DATASET_AUX_PATH", "") + "/val.txt";
        scenario_name = getenv("CM_MLPERF_LOADGEN_SCENARIO", "Offline");
        mode_name = getenv("CM_MLPERF_LOADGEN_MODE", "PerformanceOnly");
        if (mode_name == "accuracy")
            mode_name = "AccuracyOnly";
        if (mode_name == "performance")
            mode_name = "PerformanceOnly";
        query_count_override = std::stol(getenv("CM_MLPERF_LOADGEN_QUERY_COUNT", "0"));
	query_count_override = 0;
        performance_sample_count = std::stol(getenv("CM_MLPERF_LOADGEN_PERFORMANCE_SAMPLE_COUNT", "0"));
        batch_size = std::stol(getenv("CM_MLPERF_LOADGEN_MAX_BATCHSIZE", "32"));
        std::cout << "MLPerf Conf path: " << mlperf_conf_path << std::endl;
        std::cout << "User Conf path: " << user_conf_path << std::endl;
        std::cout << "Dataset Preprocessed path: " << dataset_preprocessed_path << std::endl;
        std::cout << "Dataset List filepath: " << dataset_list << std::endl;
        std::cout << "Scenario: " << scenario_name << std::endl;
        std::cout << "Mode: " << mode_name << std::endl;
        std::cout << "Batch size: " << batch_size << std::endl;
        std::cout << "Query count override: " << query_count_override << std::endl;
        std::cout << "Performance sample count override in application: " << performance_sample_count << std::endl;
    }

    std::string mlperf_conf_path;
    std::string user_conf_path;
    std::string audit_conf_path;
    std::string output_dir;
    std::string backend_name;
    std::string device_name;
    std::string model_name;
    std::string model_path;
    std::string dataset_preprocessed_path;
    std::string dataset_path;
    std::string dataset_list;
    std::string imagenet_val_path;
    std::string scenario_name;
    std::string mode_name;
    size_t performance_sample_count;
    size_t batch_size;
    size_t query_count_override;
};

int main(int argc, const char *argv[]) {
    // configure test settings
    InputSettings input_settings;
    mlperf::TestSettings test_settings;
    test_settings.scenario =
        input_settings.scenario_name == "SingleStream" ? mlperf::TestScenario::SingleStream :
        input_settings.scenario_name == "MultiStream" ? mlperf::TestScenario::MultiStream :
        input_settings.scenario_name == "Server" ? mlperf::TestScenario::Server :
        input_settings.scenario_name == "Offline" ? mlperf::TestScenario::Offline :
        mlperf::TestScenario::SingleStream;
    test_settings.mode =
        input_settings.mode_name == "SubmissionRun" ? mlperf::TestMode::SubmissionRun :
        input_settings.mode_name == "AccuracyOnly" ? mlperf::TestMode::AccuracyOnly :
        input_settings.mode_name == "PerformanceOnly" ? mlperf::TestMode::PerformanceOnly :
        input_settings.mode_name == "FindPeakPerformance" ? mlperf::TestMode::FindPeakPerformance :
        mlperf::TestMode::SubmissionRun;

    // read test settings from mlperf.conf and user.conf
    if (test_settings.FromConfig(input_settings.mlperf_conf_path, input_settings.model_name, input_settings.scenario_name)) {
        std::cerr << "Could not read mlperf.conf at " << input_settings.mlperf_conf_path << std::endl;
        return 1;
    }
    if (test_settings.FromConfig(input_settings.user_conf_path, input_settings.model_name, input_settings.scenario_name)) {
        std::cerr << "Could not read user.conf at " << input_settings.user_conf_path << std::endl;
        return 1;
    }

    // configure log settings
    mlperf::LogSettings log_settings;
    log_settings.log_output.outdir = input_settings.output_dir;

    // build model
    std::shared_ptr<Model> model;
    if (input_settings.model_name == "resnet50") {
        model.reset(new Resnet50(input_settings.model_path, -1));
        // can change model params here
        // e.g. if (backend == "torch") {
        //          model.reset(new Resnet50(input_settings.model_path, 0));
        //          model->input_names = {"image"};
        //      }
    } else if (input_settings.model_name == "retinanet") {
        // onnx retinanet requires batch size 1
        if (input_settings.backend_name == "onnxruntime" && input_settings.batch_size != 1) {
            std::cerr << "onnx retinanet requires batch size 1"
                      << " (current batch size: " << input_settings.batch_size << ")" << std::endl;
            return 1;
        }
        model.reset(new Retinanet(input_settings.model_path, 800, 800, 0.05f));
    } else {
        std::cerr << "model (" << input_settings.model_name << ") not supported" << std::endl;
        return 1;
    }

    // build device
    std::shared_ptr<Device> device;
    if (input_settings.device_name == "cpu") {
        device.reset(new CPUDevice());
    } else if (input_settings.device_name == "gpu") {
#ifdef CM_MLPERF_DEVICE_GPU
        device.reset(new GPUDevice());
#endif
    } else {
        std::cerr << "device (" << input_settings.device_name << ") not supported" << std::endl;
	return 1;
    }

    // get counts
    if (input_settings.query_count_override != 0)
        test_settings.max_query_count = input_settings.query_count_override;
    size_t max_sample_count = test_settings.max_query_count;
    size_t performance_sample_count =
        test_settings.performance_sample_count_override != 0 ?
        test_settings.performance_sample_count_override :
        input_settings.performance_sample_count;

    if (performance_sample_count != 0) {//Its changed from user.conf
      //test_settings.performance_sample_count_override = performance_sample_count;
    }
    if (max_sample_count != 0)
        performance_sample_count =
            std::min(performance_sample_count, max_sample_count);
    if (max_sample_count == 0)
      max_sample_count = INT_MAX;
    // build backend
    std::shared_ptr<Backend> backend;
    if (input_settings.backend_name == "onnxruntime") {
#ifdef CM_MLPERF_BACKEND_ONNXRUNTIME
        backend.reset(new OnnxRuntimeBackend(
            model, device, performance_sample_count, input_settings.batch_size,
            input_settings.device_name == "gpu"));
#endif
    } else {
        std::cerr << "backend (" << input_settings.backend_name << ") not supported" << std::endl;
        return 1;
    }

    // build QSL
    std::shared_ptr<mlperf::QuerySampleLibrary> qsl;
    if (input_settings.model_name == "resnet50") {
        qsl.reset(new Imagenet(
            backend, max_sample_count,
            input_settings.dataset_preprocessed_path,
            input_settings.imagenet_val_path));
    } else if (input_settings.model_name == "retinanet") {
        qsl.reset(new Openimages(
            backend, max_sample_count,
            input_settings.dataset_preprocessed_path,
            input_settings.dataset_list));
    } else {
        std::cerr << "dataset for model ("
                  << input_settings.model_name << ") not supported" << std::endl;
        return 1;
    }

    // sanity check: common problem in workflow
    if (qsl->TotalSampleCount() == 0) {
        std::cerr << "error: 0 samples found in dataset" << std::endl;
        return 1;
    }
    if (qsl->PerformanceSampleCount() == 0) {
        std::cerr << "error: performance sample count = 0" << std::endl;
        return 1;
    }

    // build SUT
    // using QueueSUT for all scenarios except for StreamSUT for single-stream
    std::shared_ptr<mlperf::SystemUnderTest> sut;
    if (input_settings.scenario_name == "SingleStream") {
        sut.reset(new StreamSUT(backend));
    } else {
        sut.reset(new QueueSUT(backend));
    }

    // start benchmark
    std::cerr << "starting benchmark" << std::endl;
    mlperf::StartTest(sut.get(), qsl.get(), test_settings, log_settings, input_settings.audit_conf_path);
}
