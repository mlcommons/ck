#include <cstddef>
#include <string>

#include "loadgen.h"
#include "test_settings.h"

#include "backend.h"
#include "onnxruntime_backend.h"
#include "device.h"
#include "model.h"
#include "sample_library.h"
#include "system.h"
#include <unistd.h>
#include <cstring>

class InputSettings {

    std::string getenv(const std::string& name,const std::string& default_value) {
        const char* value = std::getenv(name.c_str());
        return value ? value : default_value;
    }

public:
    InputSettings() {
        mlperf_conf_path = getenv("CM_MLC_MLPERF_CONF", "../inference/mlperf.conf");
        user_conf_path = getenv("CM_MLC_USER_CONF", "../inference/vision/classification_and_detection/user.conf");
        output_dir = getenv("CM_MLC_OUTPUT_DIR", ".");
        model_name = getenv("CM_ML_MODEL_NAME", "resnet50");
        model_path = getenv("CM_ML_MODEL_FILE_WITH_PATH", "");
        imagenet_preprocessed_path = getenv("CM_DATASET_PREPROCESSED_PATH","") + "/preprocessed/imagenet/NCHW";
        imagenet_val_path = getenv("CM_DATASET_AUX_PATH", "") + "/val.txt";
        scenario_name = getenv("CM_LOADGEN_SCENARIO", "Offline");
        mode_name = getenv("CM_LOADGEN_MODE", "PerformanceOnly");
        if (mode_name == "accuracy")
            mode_name = "AccuracyOnly";
        if (mode_name == "performance")
            mode_name = "PerformanceOnly";
        performance_sample_count = std::stol(getenv("CM_LOADGEN_PERFORMANCE_SAMPLE_COUNT", "1024"));
        batch_size = std::stol(getenv("CM_LOADGEN_MAX_BATCHSIZE", "1"));
        std::cout << "MLPerf Conf path: " << mlperf_conf_path << std::endl;
        std::cout << "User Conf path: " << user_conf_path << std::endl;
        std::cout << "Imagenet Preprocessed path: " << imagenet_preprocessed_path << std::endl;
        std::cout << "Scenario: " << scenario_name << std::endl;
        std::cout << "Mode: " << mode_name << std::endl;
        std::cout << "Batch size: " << batch_size << std::endl;
    }

    std::string mlperf_conf_path;
    std::string user_conf_path;
    std::string output_dir;
    std::string model_name;
    std::string model_path;
    std::string imagenet_preprocessed_path;
    std::string imagenet_val_path;
    std::string scenario_name;
    std::string mode_name;
    size_t performance_sample_count;
    size_t batch_size;
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
    if (test_settings.FromConfig(input_settings.mlperf_conf_path, input_settings.model_name, "Offline")) {
        std::cerr << "Could not read mlperf.conf at " << input_settings.mlperf_conf_path << std::endl;
        return 1;
    }
    if (test_settings.FromConfig(input_settings.user_conf_path, input_settings.model_name, "Offline")) {
        std::cerr << "Could not read user.conf at " << input_settings.user_conf_path << std::endl;
        return 1;
    }

    // configure log settings
    mlperf::LogSettings log_settings;
    log_settings.log_output.outdir = input_settings.output_dir;

    // build model
    std::shared_ptr<Model> resnet50 = std::make_shared<Model>();
    resnet50->model_path = input_settings.model_path;
    resnet50->num_inputs = 1;
    resnet50->input_names = {"input_tensor:0"};
    resnet50->input_shapes = {{3, 224, 224}};
    resnet50->input_sizes = {3 * 224 * 224 * sizeof(float)};
    resnet50->num_outputs = 1;
    resnet50->output_names = {"ArgMax:0"};
    resnet50->output_shapes = {{1}};
    resnet50->output_sizes = {sizeof(uint64_t)};
    resnet50->postprocess = [](void *response) {
        int64_t *argmax_result = static_cast<int64_t *>(response);
        (*argmax_result)--;
    };

    // build device
    std::shared_ptr<Device> device = std::make_shared<CPUDevice>();

    // get counts
    size_t max_sample_count =
        test_settings.max_query_count;
    size_t performance_sample_count =
        test_settings.performance_sample_count_override != 0 ?
        test_settings.performance_sample_count_override :
        input_settings.performance_sample_count;
    if (max_sample_count != 0)
        performance_sample_count =
            std::min(performance_sample_count, max_sample_count);

    // build backend
    std::shared_ptr<Backend> backend = std::make_shared<OnnxRuntimeCPUBackend>(
        resnet50, device, performance_sample_count, input_settings.batch_size,
        std::vector<ONNXTensorElementDataType>{ONNX_TENSOR_ELEMENT_DATA_TYPE_FLOAT});

    // build QSL
    std::shared_ptr<mlperf::QuerySampleLibrary> imagenet = std::make_shared<Imagenet>(
        backend, max_sample_count, input_settings.imagenet_preprocessed_path, input_settings.imagenet_val_path);

    // build SUT
    // recommend using QueueSUT for all scenarios except for StreamSUT for single-stream
    std::shared_ptr<mlperf::SystemUnderTest> sut = std::make_shared<QueueSUT>(backend);

    // start benchmark
    std::cerr << "starting benchmark" << std::endl;
    mlperf::StartTest(sut.get(), imagenet.get(), test_settings, log_settings);
}
