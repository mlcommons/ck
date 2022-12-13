/*
 * Copyright (c) 2022, NVIDIA CORPORATION. All rights reserved.
 * Copyright 2018 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/* Include necessary header files */
// Loadgen
#include "loadgen.h"

// TensorRT
#include "NvInfer.h"
#include "NvInferPlugin.h"
#include "logger.h"
#include "logging.h"

// LWIS
#include "lwis.hpp"
#include "lwis_buffers.h"

// Google Logging
#include <gflags/gflags.h>
#include <glog/logging.h>

// General C++
#include <chrono>
#include <dlfcn.h>
#include <iostream>
#include <memory>
#include <thread>

#include "callback.hpp"
#include "utils.hpp"

// Flags used by harness
#include "harness_flags.hpp"

#include "cuda_profiler_api.h"

/* Keep track of the GPU devices we are using */
std::vector<uint32_t> Devices;
std::vector<std::string> DeviceNames;

/* Helper function to actually perform inference using MLPerf Loadgen */
void doInference()
{
    // Configure the test settings
    mlperf::TestSettings test_settings;
    test_settings.scenario = scenarioMap[FLAGS_scenario];
    test_settings.mode = testModeMap[FLAGS_test_mode];

    gLogInfo << "mlperf.conf path: " << FLAGS_mlperf_conf_path << std::endl;
    gLogInfo << "user.conf path: " << FLAGS_user_conf_path << std::endl;
    test_settings.FromConfig(FLAGS_mlperf_conf_path, FLAGS_model, FLAGS_scenario);
    test_settings.FromConfig(FLAGS_user_conf_path, FLAGS_model, FLAGS_scenario);
    test_settings.server_coalesce_queries = true;

    // Configure the logging settings
    mlperf::LogSettings log_settings;
    log_settings.log_output.outdir = FLAGS_logfile_outdir;
    log_settings.log_output.prefix = FLAGS_logfile_prefix;
    log_settings.log_output.suffix = FLAGS_logfile_suffix;
    log_settings.log_output.prefix_with_datetime = FLAGS_logfile_prefix_with_datetime;
    log_settings.log_output.copy_detail_to_stdout = FLAGS_log_copy_detail_to_stdout;
    log_settings.log_output.copy_summary_to_stdout = !FLAGS_disable_log_copy_summary_to_stdout;
    log_settings.log_mode = logModeMap[FLAGS_log_mode];
    log_settings.log_mode_async_poll_interval_ms = FLAGS_log_mode_async_poll_interval_ms;
    log_settings.enable_trace = FLAGS_log_enable_trace;

    // Instantiate and configure our SUT
    lwis::ServerPtr_t sut = std::make_shared<lwis::Server>("LWIS_Server");

    lwis::ServerSettings sut_settings;
    sut_settings.EnableCudaGraphs = FLAGS_use_graphs;
    sut_settings.GPUBatchSize = FLAGS_gpu_batch_size;
    sut_settings.GPUCopyStreams = FLAGS_gpu_copy_streams;
    sut_settings.GPUInferStreams = FLAGS_gpu_inference_streams;

    sut_settings.DLABatchSize = FLAGS_dla_batch_size;
    sut_settings.DLACopyStreams = FLAGS_dla_copy_streams;
    sut_settings.DLAInferStreams = FLAGS_dla_inference_streams;

    if (FLAGS_dla_core != -1)
    {
        sut_settings.MaxGPUs = 0;
        sut_settings.MaxDLAs = 1; // no interface to specify which DLA
    }
    else
    {
        sut_settings.MaxDLAs = FLAGS_max_dlas;
    }
    sut_settings.EnableSpinWait = FLAGS_use_spin_wait;
    sut_settings.EnableDeviceScheduleSpin = FLAGS_use_device_schedule_spin;
    sut_settings.RunInferOnCopyStreams = FLAGS_run_infer_on_copy_streams;
    sut_settings.EnableDirectHostAccess = FLAGS_use_direct_host_access;
    sut_settings.EnableDequeLimit = FLAGS_use_deque_limit;
    sut_settings.Timeout = std::chrono::microseconds(FLAGS_deque_timeout_usec);
    sut_settings.EnableBatcherThreadPerDevice = FLAGS_use_batcher_thread_per_device;
    sut_settings.EnableCudaThreadPerDevice = FLAGS_use_cuda_thread_per_device;
    sut_settings.EnableStartFromDeviceMem = FLAGS_start_from_device;
    sut_settings.ForceContiguous
        = FLAGS_assume_contiguous || (test_settings.scenario == mlperf::TestScenario::MultiStream);
    sut_settings.CompleteThreads = FLAGS_complete_threads;
    sut_settings.UseSameContext = FLAGS_use_same_context;
    sut_settings.m_NumaConfig = parseNumaConfig(FLAGS_numa_config);
    sut_settings.m_GpuToNumaMap = getGpuToNumaMap(sut_settings.m_NumaConfig);
    sut_settings.EndOnDevice = FLAGS_end_on_device;

    lwis::ServerParams sut_params;
    sut_params.DeviceNames = FLAGS_devices;
    sut_params.EngineNames.resize(2);
    for (auto& engineName : splitString(FLAGS_gpu_engines, ","))
    {
        if (engineName == "")
            continue;
        std::vector<std::string> engines = {engineName};
        sut_params.EngineNames[0].emplace_back(engines);
    }
    for (auto& engineName : splitString(FLAGS_dla_engines, ","))
    {
        if (engineName == "")
            continue;
        std::vector<std::string> engines = {engineName};
        sut_params.EngineNames[1].emplace_back(engines);
    }

    // Instantiate our QSL
    std::cout << "Creating QSL." << std::endl;
    std::vector<std::string> tensor_paths = splitString(FLAGS_tensor_path, ",");
    std::vector<bool> start_from_device(tensor_paths.size(), FLAGS_start_from_device);
    const size_t padding = (test_settings.scenario == mlperf::TestScenario::MultiStream)
        ? test_settings.multi_stream_samples_per_query - 1
        : 0;
    std::shared_ptr<mlperf::QuerySampleLibrary> qsl;
    if (sut_settings.m_NumaConfig.empty())
    {
        // When NUMA is not used, create one QSL.
        auto oneQsl = std::make_shared<qsl::SampleLibrary>("LWIS_SampleLibrary", FLAGS_map_path,
            splitString(FLAGS_tensor_path, ","),
            FLAGS_performance_sample_count ? FLAGS_performance_sample_count
                                           : std::max(FLAGS_gpu_batch_size, FLAGS_dla_batch_size),
            padding, FLAGS_coalesced_tensor, start_from_device);
        sut->AddSampleLibrary(oneQsl);
        qsl = oneQsl;
    }
    else
    {
        // When NUMA is used, create one QSL per NUMA node.
        std::cout << "Using NUMA. Config: " << FLAGS_numa_config << std::endl;
        const int32_t nbNumas = sut_settings.m_NumaConfig.size();
        std::vector<qsl::SampleLibraryPtr_t> qsls;
        for (int32_t numaIdx = 0; numaIdx < nbNumas; numaIdx++)
        {
            // Use a thread to construct QSL so that the allocated memory is closer to that NUMA node.
            auto constructQsl = [&]() {
                std::this_thread::sleep_for(std::chrono::milliseconds(1));
                bindNumaMemPolicy(numaIdx, nbNumas);
                auto oneQsl = std::make_shared<qsl::SampleLibrary>("LWIS_SampleLibrary", FLAGS_map_path,
                    splitString(FLAGS_tensor_path, ","),
                    FLAGS_performance_sample_count ? FLAGS_performance_sample_count
                                                   : std::max(FLAGS_gpu_batch_size, FLAGS_dla_batch_size),
                    padding, FLAGS_coalesced_tensor, start_from_device);
                resetNumaMemPolicy();
                sut->AddSampleLibrary(oneQsl);
                qsls.emplace_back(oneQsl);
            };
            std::thread th(constructQsl);
            bindThreadToCpus(th, sut_settings.m_NumaConfig[numaIdx].second);
            th.join();
        }
        qsl = std::shared_ptr<qsl::SampleLibraryEnsemble>(new qsl::SampleLibraryEnsemble(qsls));
    }
    std::cout << "Finished Creating QSL." << std::endl;

    std::cout << "Setting up SUT." << std::endl;
    sut->Setup(sut_settings, sut_params); // Pass the requested sut settings and params to our SUT
    sut->SetResponseCallback(
        callbackMap[FLAGS_response_postprocess]); // Set QuerySampleResponse post-processing callback
    std::cout << "Finished setting up SUT." << std::endl;

    // Perform a brief warmup
    std::cout << "Starting warmup. Running for a minimum of " << FLAGS_warmup_duration << " seconds." << std::endl;
    auto tStart = std::chrono::high_resolution_clock::now();
    sut->Warmup(FLAGS_warmup_duration);
    double elapsed = std::chrono::duration<float>(std::chrono::high_resolution_clock::now() - tStart).count();
    std::cout << "Finished warmup. Ran for " << elapsed << "s." << std::endl;

    // Perform the inference testing
    std::cout << "Starting running actual test." << std::endl;
    cudaProfilerStart();
    mlperf::StartTest(sut.get(), qsl.get(), test_settings, log_settings);
    cudaProfilerStop();
    std::cout << "Finished running actual test." << std::endl;

    // Log device stats
    auto devices = sut->GetDevices();
    for (auto& device : devices)
    {
        const auto& stats = device->GetStats();

        std::cout << "Device " << device->GetName() << " processed:" << std::endl;
        for (auto& elem : stats.m_BatchSizeHistogram)
        {
            std::cout << "  " << elem.second << " batches of size " << elem.first << std::endl;
        }

        std::cout << "  Memcpy Calls: " << stats.m_MemcpyCalls << std::endl;
        std::cout << "  PerSampleCudaMemcpy Calls: " << stats.m_PerSampleCudaMemcpyCalls << std::endl;
        std::cout << "  BatchedCudaMemcpy Calls: " << stats.m_BatchedCudaMemcpyCalls << std::endl;
    }

    // Inform the SUT that we are done
    sut->Done();

    // Make sure CUDA RT is still in scope when we free the memory
    qsl.reset();
    sut.reset();
}

int main(int argc, char* argv[])
{
    // Initialize logging
    FLAGS_alsologtostderr = 1; // Log to console
    ::google::InitGoogleLogging("TensorRT mlperf");
    ::google::ParseCommandLineFlags(&argc, &argv, true);
    const std::string gSampleName = "Default_Harness";
    auto sampleTest = gLogger.defineTest(gSampleName, argc, const_cast<const char**>(argv));
    gLogger.reportTestStart(sampleTest);
    if (FLAGS_verbose)
    {
        setReportableSeverity(Severity::kVERBOSE);
    }
    else
    {
        setReportableSeverity(Severity::kINFO);
    }

    // Load all the needed shared objects for plugins.
    std::vector<std::string> plugin_files = splitString(FLAGS_plugins, ",");
    for (auto& s : plugin_files)
    {
        void* dlh = dlopen(s.c_str(), RTLD_LAZY);
        if (nullptr == dlh)
        {
            gLogError << "Error loading plugin library " << s << std::endl;
            return 1;
        }
    }

    // Perform inference
    doInference();

    // Report pass
    return gLogger.reportPass(sampleTest);
}
