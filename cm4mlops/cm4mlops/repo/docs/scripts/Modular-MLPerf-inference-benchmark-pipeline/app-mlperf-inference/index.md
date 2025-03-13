# app-mlperf-inference
Automatically generated README for this automation recipe: **app-mlperf-inference**

Category: **[Modular MLPerf inference benchmark pipeline](..)**

License: **Apache 2.0**

Developers: [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh), [Thomas Zhu](https://www.linkedin.com/in/hanwen-zhu-483614189), [Grigori Fursin](https://cKnowledge.org/gfursin)
* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference/README-extra.md)


---

﻿This CM script provides a unified interface to prepare and run a modular version of the [MLPerf inference benchmark](https://arxiv.org/abs/1911.02549)
across diverse ML models, data sets, frameworks, libraries, run-time systems and platforms
using the [cross-platform automation meta-framework (MLCommons CM)](https://github.com/mlcommons/ck).

It is assembled from reusable and interoperable [CM scripts for DevOps and MLOps](../list_of_scripts.md)
being developed by the [open MLCommons taskforce on automation and reproducibility](../mlperf-education-workgroup.md).

It is a higher-level wrapper to several other CM scripts modularizing the MLPerf inference benchmark:
* [Reference Python implementation](../app-mlperf-inference-reference)
* [Universal C++ implementation](../app-mlperf-inference-cpp)
* [TFLite C++ implementation](../app-mlperf-inference-tflite-cpp)
* [NVidia optimized implementation](app-mlperf-inference-nvidia)

See [this SCC'23 tutorial](https://github.com/mlcommons/ck/blob/master/docs/tutorials/sc22-scc-mlperf.md) 
to use this script to run a reference (unoptimized) Python implementation of the MLPerf object detection benchmark 
with RetinaNet model, Open Images dataset, ONNX runtime and CPU target.

See this [CM script](../run-mlperf-inference-app) to automate and validate your MLPerf inference submission.

Get in touch with the [open taskforce on automation and reproducibility at MLCommons](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)
if you need help with your submission or if you would like to participate in further modularization of MLPerf 
and collaborative design space exploration and optimization of ML Systems.

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "app vision language mlcommons mlperf inference generic" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=app,vision,language,mlcommons,mlperf,inference,generic[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "app vision language mlcommons mlperf inference generic [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,vision,language,mlcommons,mlperf,inference,generic'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

    if r['return']>0:
        print (r['error'])

    ```


=== "Docker"
    ##### Run this script via Docker (beta)

    ```bash
    cm docker script "app vision language mlcommons mlperf inference generic[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * Group "**implementation**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_cpp`
              - Aliases: `_mil,_mlcommons-cpp`
               - ENV variables:
                   - CM_MLPERF_CPP: `yes`
                   - CM_MLPERF_IMPLEMENTATION: `mlcommons_cpp`
                   - CM_IMAGENET_ACCURACY_DTYPE: `float32`
                   - CM_OPENIMAGES_ACCURACY_DTYPE: `float32`
        * `_intel-original`
              - Aliases: `_intel`
               - ENV variables:
                   - CM_MLPERF_IMPLEMENTATION: `intel`
        * `_kilt`
              - Aliases: `_qualcomm`
               - ENV variables:
                   - CM_MLPERF_IMPLEMENTATION: `qualcomm`
        * `_nvidia-original`
              - Aliases: `_nvidia`
               - ENV variables:
                   - CM_MLPERF_IMPLEMENTATION: `nvidia`
                   - CM_SQUAD_ACCURACY_DTYPE: `float16`
                   - CM_IMAGENET_ACCURACY_DTYPE: `int32`
                   - CM_CNNDM_ACCURACY_DTYPE: `int32`
                   - CM_LIBRISPEECH_ACCURACY_DTYPE: `int8`
        * **`_reference`** (default)
              - Aliases: `_mlcommons-python,_python`
               - ENV variables:
                   - CM_MLPERF_PYTHON: `yes`
                   - CM_MLPERF_IMPLEMENTATION: `mlcommons_python`
                   - CM_SQUAD_ACCURACY_DTYPE: `float32`
                   - CM_IMAGENET_ACCURACY_DTYPE: `float32`
                   - CM_OPENIMAGES_ACCURACY_DTYPE: `float32`
                   - CM_LIBRISPEECH_ACCURACY_DTYPE: `float32`
                   - CM_CNNDM_ACCURACY_DTYPE: `int32`
        * `_tflite-cpp`
              - Aliases: `_ctuning-cpp-tflite`
               - ENV variables:
                   - CM_MLPERF_TFLITE_CPP: `yes`
                   - CM_MLPERF_CPP: `yes`
                   - CM_MLPERF_IMPLEMENTATION: `ctuning_cpp_tflite`
                   - CM_IMAGENET_ACCURACY_DTYPE: `float32`

        </details>


      * Group "**backend**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_deepsparse`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `deepsparse`
        * `_glow`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `glow`
        * `_ncnn`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `ncnn`
        * `_onnxruntime`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `onnxruntime`
        * `_pytorch`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `pytorch`
        * `_ray`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `ray`
        * `_tensorrt`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tensorrt`
        * `_tf`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tf`
        * `_tflite`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tflite`
        * `_tvm-onnx`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tvm-onnx`
        * `_tvm-pytorch`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tvm-pytorch`
        * `_tvm-tflite`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tvm-tflite`

        </details>


      * Group "**device**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_cpu`** (default)
               - ENV variables:
                   - CM_MLPERF_DEVICE: `cpu`
        * `_cuda`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `gpu`
        * `_qaic`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `qaic`
        * `_rocm`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `rocm`
        * `_tpu`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `tpu`

        </details>


      * Group "**model**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_3d-unet-99`
               - ENV variables:
                   - CM_MODEL: `3d-unet-99`
        * `_3d-unet-99.9`
               - ENV variables:
                   - CM_MODEL: `3d-unet-99.9`
        * `_bert-99`
               - ENV variables:
                   - CM_MODEL: `bert-99`
        * `_bert-99.9`
               - ENV variables:
                   - CM_MODEL: `bert-99.9`
        * `_dlrm-v2-99`
               - ENV variables:
                   - CM_MODEL: `dlrm-v2-99`
        * `_dlrm-v2-99.9`
               - ENV variables:
                   - CM_MODEL: `dlrm-v2-99.9`
        * `_efficientnet`
               - ENV variables:
                   - CM_MODEL: `efficientnet`
        * `_gptj-99`
               - ENV variables:
                   - CM_MODEL: `gptj-99`
        * `_gptj-99.9`
               - ENV variables:
                   - CM_MODEL: `gptj-99.9`
        * `_llama2-70b-99`
               - ENV variables:
                   - CM_MODEL: `llama2-70b-99`
        * `_llama2-70b-99.9`
               - ENV variables:
                   - CM_MODEL: `llama2-70b-99.9`
        * `_mobilenet`
               - ENV variables:
                   - CM_MODEL: `mobilenet`
        * **`_resnet50`** (default)
               - ENV variables:
                   - CM_MODEL: `resnet50`
        * `_retinanet`
               - ENV variables:
                   - CM_MODEL: `retinanet`
        * `_rnnt`
               - ENV variables:
                   - CM_MODEL: `rnnt`
        * `_sdxl`
               - ENV variables:
                   - CM_MODEL: `stable-diffusion-xl`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_bfloat16`
               - ENV variables:
                   - CM_MLPERF_QUANTIZATION: `False`
                   - CM_MLPERF_MODEL_PRECISION: `float32`
        * `_float16`
               - ENV variables:
                   - CM_MLPERF_QUANTIZATION: `False`
                   - CM_MLPERF_MODEL_PRECISION: `float32`
        * **`_float32`** (default)
              - Aliases: `_fp32`
               - ENV variables:
                   - CM_MLPERF_QUANTIZATION: `False`
                   - CM_MLPERF_MODEL_PRECISION: `float32`
        * `_int4`
               - ENV variables:
                   - CM_MLPERF_QUANTIZATION: `True`
                   - CM_MLPERF_MODEL_PRECISION: `int4`
        * `_int8`
              - Aliases: `_quantized`
               - ENV variables:
                   - CM_MLPERF_QUANTIZATION: `True`
                   - CM_MLPERF_MODEL_PRECISION: `int8`
        * `_uint8`
               - ENV variables:
                   - CM_MLPERF_QUANTIZATION: `True`
                   - CM_MLPERF_MODEL_PRECISION: `uint8`

        </details>


      * Group "**execution-mode**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_fast`
               - ENV variables:
                   - CM_FAST_FACTOR: `5`
                   - CM_OUTPUT_FOLDER_NAME: `fast_results`
                   - CM_MLPERF_RUN_STYLE: `fast`
        * **`_test`** (default)
               - ENV variables:
                   - CM_OUTPUT_FOLDER_NAME: `test_results`
                   - CM_MLPERF_RUN_STYLE: `test`
        * `_valid`
               - ENV variables:
                   - CM_OUTPUT_FOLDER_NAME: `valid_results`
                   - CM_MLPERF_RUN_STYLE: `valid`

        </details>


      * Group "**reproducibility**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_r2.1_default`
               - ENV variables:
                   - CM_SKIP_SYS_UTILS: `yes`
                   - CM_TEST_QUERY_COUNT: `100`
        * `_r3.0_default`
               - ENV variables:
                   - CM_SKIP_SYS_UTILS: `yes`
        * `_r3.1_default`
        * `_r4.0_default`
               - ENV variables:
                   - CM_ENV_NVMITTEN_DOCKER_WHEEL_PATH: `/opt/nvmitten-0.1.3-cp38-cp38-linux_x86_64.whl`
        * `_r4.1_default`
               - ENV variables:
                   - CM_ENV_NVMITTEN_DOCKER_WHEEL_PATH: `/opt/nvmitten-0.1.3b0-cp38-cp38-linux_x86_64.whl`

        </details>


      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_power`
               - ENV variables:
                   - CM_MLPERF_POWER: `yes`
                   - CM_SYSTEM_POWER: `yes`

        </details>


      * Group "**batch_size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_batch_size.#`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_MAX_BATCHSIZE: `#`

        </details>


      * Group "**loadgen-scenario**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_multistream`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `MultiStream`
        * **`_offline`** (default)
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `Offline`
        * `_server`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `Server`
        * `_singlestream`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `SingleStream`

        </details>


    ##### Default variations

    `_cpu,_float32,_offline,_reference,_resnet50,_test`
=== "Input Flags"


    #### Input Flags

    * --**scenario:** MLPerf inference scenario {Offline,Server,SingleStream,MultiStream} (*Offline*)
    * --**mode:** MLPerf inference mode {performance,accuracy} (*accuracy*)
    * --**test_query_count:** Specifies the number of samples to be processed during a test run
    * --**target_qps:** Target QPS
    * --**target_latency:** Target Latency
    * --**max_batchsize:** Maximum batchsize to be used
    * --**num_threads:** Number of CPU threads to launch the application with
    * --**hw_name:** Valid value - any system description which has a config file (under same name) defined [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-configs-sut-mlperf-inference/configs)
    * --**output_dir:** Location where the outputs are produced
    * --**rerun:** Redo the run even if previous run files exist (*True*)
    * --**regenerate_files:** Regenerates measurement files including accuracy.txt files even if a previous run exists. This option is redundant if `--rerun` is used
    * --**adr.python.name:** Python virtual environment name (optional) (*mlperf*)
    * --**adr.python.version_min:** Minimal Python version (*3.8*)
    * --**adr.python.version:** Force Python version (must have all system deps)
    * --**adr.compiler.tags:** Compiler for loadgen (*gcc*)
    * --**adr.inference-src-loadgen.env.CM_GIT_URL:** Git URL for MLPerf inference sources to build LoadGen (to enable non-reference implementations)
    * --**adr.inference-src.env.CM_GIT_URL:** Git URL for MLPerf inference sources to run benchmarks (to enable non-reference implementations)
    * --**quiet:** Quiet run (select default values for all questions) (*False*)
    * --**readme:** Generate README with the reproducibility report
    * --**debug:** Debug MLPerf script
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--clean=value`  &rarr;  `CM_MLPERF_CLEAN_SUBMISSION_DIR=value`
    * `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
    * `--debug=value`  &rarr;  `CM_DEBUG_SCRIPT_BENCHMARK_PROGRAM=value`
    * `--docker=value`  &rarr;  `CM_RUN_DOCKER_CONTAINER=value`
    * `--gpu_name=value`  &rarr;  `CM_NVIDIA_GPU_NAME=value`
    * `--hw_name=value`  &rarr;  `CM_HW_NAME=value`
    * `--imagenet_path=value`  &rarr;  `IMAGENET_PATH=value`
    * `--max_amps=value`  &rarr;  `CM_MLPERF_POWER_MAX_AMPS=value`
    * `--max_batchsize=value`  &rarr;  `CM_MLPERF_LOADGEN_MAX_BATCHSIZE=value`
    * `--max_volts=value`  &rarr;  `CM_MLPERF_POWER_MAX_VOLTS=value`
    * `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
    * `--multistream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY=value`
    * `--ntp_server=value`  &rarr;  `CM_MLPERF_POWER_NTP_SERVER=value`
    * `--num_threads=value`  &rarr;  `CM_NUM_THREADS=value`
    * `--offline_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS=value`
    * `--output_dir=value`  &rarr;  `OUTPUT_BASE_DIR=value`
    * `--power=value`  &rarr;  `CM_MLPERF_POWER=value`
    * `--power_server=value`  &rarr;  `CM_MLPERF_POWER_SERVER_ADDRESS=value`
    * `--readme=value`  &rarr;  `CM_MLPERF_README=value`
    * `--regenerate_files=value`  &rarr;  `CM_REGENERATE_MEASURE_FILES=value`
    * `--rerun=value`  &rarr;  `CM_RERUN=value`
    * `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
    * `--server_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_SERVER_TARGET_QPS=value`
    * `--singlestream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY=value`
    * `--target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_LATENCY=value`
    * `--target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_QPS=value`
    * `--test_query_count=value`  &rarr;  `CM_TEST_QUERY_COUNT=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_MLPERF_LOADGEN_MODE: `accuracy`
    * CM_MLPERF_LOADGEN_SCENARIO: `Offline`
    * CM_OUTPUT_FOLDER_NAME: `test_results`
    * CM_MLPERF_RUN_STYLE: `test`
    * CM_TEST_QUERY_COUNT: `10`
    * CM_MLPERF_QUANTIZATION: `False`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "app vision language mlcommons mlperf inference generic [variations]" [--input_flags] -j
```