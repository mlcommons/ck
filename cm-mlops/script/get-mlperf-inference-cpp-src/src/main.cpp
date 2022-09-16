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
#include <cstring>

const std::string MLPERF_CONF_PATH = "../inference/mlperf.conf";
const std::string USER_CONF_PATH = "../inference/vision/classification_and_detection/user.conf";
const std::string OUTPUT_DIR = "./output";
const std::string MODEL_NAME = "resnet50";
const std::string MODEL_PATH = "/Users/zhw/CM/repos/local/cache/3eb8ab95a84d4a11/resnet50_v1.onnx";
const std::string IMAGENET_PREPROCESSED_PATH = "../inference/vision/classification_and_detection/preprocessed/imagenet/NCHW";
const std::string IMAGENET_VAL_MAP_PATH = "/Users/zhw/CM/repos/local/cache/32997aa67948409c/images/val_map.txt";
const std::string SCENARIO_NAME = "Offline";
const std::string MODE_NAME = "PerformanceOnly";
const size_t PERFORMANCE_SAMPLE_COUNT = 1024;
const size_t BATCH_SIZE = 32;

int main(int argc, const char *argv[]) {
    // configure test settings
    mlperf::TestSettings test_settings;
    test_settings.scenario =
        SCENARIO_NAME == "SingleStream" ? mlperf::TestScenario::SingleStream :
        SCENARIO_NAME == "MultiStream" ? mlperf::TestScenario::MultiStream :
        SCENARIO_NAME == "Server" ? mlperf::TestScenario::Server :
        SCENARIO_NAME == "Offline" ? mlperf::TestScenario::Offline :
        mlperf::TestScenario::SingleStream;
    test_settings.mode =
        MODE_NAME == "SubmissionRun" ? mlperf::TestMode::SubmissionRun :
        MODE_NAME == "AccuracyOnly" ? mlperf::TestMode::AccuracyOnly :
        MODE_NAME == "PerformanceOnly" ? mlperf::TestMode::PerformanceOnly :
        MODE_NAME == "FindPeakPerformance" ? mlperf::TestMode::FindPeakPerformance :
        mlperf::TestMode::SubmissionRun;

    // read test settings from mlperf.conf and user.conf
    if (test_settings.FromConfig(MLPERF_CONF_PATH, MODEL_NAME, "Offline")) {
        std::cerr << "Could not read mlperf.conf at " << MLPERF_CONF_PATH << std::endl;
        return 1;
    }
    if (test_settings.FromConfig(USER_CONF_PATH, MODEL_NAME, "Offline")) {
        std::cerr << "Could not read user.conf at " << USER_CONF_PATH << std::endl;
        return 1;
    }

    // configure log settings
    mlperf::LogSettings log_settings;
    log_settings.log_output.outdir = OUTPUT_DIR;

    // build model
    std::shared_ptr<Model> resnet50 = std::make_shared<Model>();
    resnet50->model_path = MODEL_PATH;
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

    // build backend
    std::shared_ptr<Backend> backend = std::make_shared<OnnxRuntimeCPUBackend>(
        resnet50, device, PERFORMANCE_SAMPLE_COUNT, BATCH_SIZE,
        std::vector<ONNXTensorElementDataType>{ONNX_TENSOR_ELEMENT_DATA_TYPE_FLOAT});

    // build QSL
    std::shared_ptr<mlperf::QuerySampleLibrary> imagenet = std::make_shared<Imagenet>(backend, IMAGENET_PREPROCESSED_PATH, IMAGENET_VAL_MAP_PATH);

    // build SUT
    // recommend using QueueSUT for all scenarios except for StreamSUT for single-stream
    std::shared_ptr<mlperf::SystemUnderTest> sut = std::make_shared<QueueSUT>(backend);

    // start benchmark
    std::cerr << "starting benchmark" << std::endl;
    mlperf::StartTest(sut.get(), imagenet.get(), test_settings, log_settings);
}
