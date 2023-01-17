<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Unsupported or invalid variation combinations](#unsupported-or-invalid-variation-combinations)
  * [ Input description](#input-description)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description

﻿This CM script provides a unified interface to prepare and run a modular version of the [MLPerf inference benchmark](https://arxiv.org/abs/1911.02549)
across diverse ML models, data sets, frameworks, libraries, run-time systems and platforms
using the [cross-platform automation meta-framework (MLCommons CM)](https://github.com/mlcommons/ck).

It is assembled from reusable and interoperable [CM scripts for DevOps and MLOps](../list_of_scripts.md)
being developed by the [open MLCommons taskforce on education and reproducibility](../mlperf-education-workgroup.md).

It is a higher-level wrapper to several other CM scripts modularizing the MLPerf inference benchmark:
* [Reference Python implementation](../app-mlperf-inference-reference)
* [Universal C++ implementation](../app-mlperf-inference-cpp)
* [TFLite C++ implementation](../app-mlperf-inference-tflite-cpp)
* [NVidia optimized implementation](app-mlperf-inference-nvidia)

See the current coverage of different models, devices and backends [here](README-extra.md#current-coverage).

See the development roadmap [here](https://github.com/mlcommons/ck/issues/536).

See extension projects to enable collaborative benchmarking, design space exploration and optimization of ML and AI Systems [here](https://github.com/mlcommons/ck/issues/627).

See [this SCC'23 tutorial](https://github.com/mlcommons/ck/blob/master/docs/tutorials/sc22-scc-mlperf.md) 
to use this script to run a reference (unoptimized) Python implementation of the MLPerf object detection benchmark 
with RetinaNet model, Open Images dataset, ONNX runtime and CPU target.

See this [CM script](../run-mlperf-inference-app) to automate and validate your MLPerf inference submission.

Get in touch with the [open taskforce on education and reproducibility at MLCommons](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)
if you need help with your submission or if you would like to participate in further modularization of MLPerf 
and collaborative design space exploration and optimization of ML Systems.


See [more info](README-extra.md).

#### Information

* Category: *Modular MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *app,vision,language,mlcommons,mlperf,inference,generic*
* Output cached?: *False*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=app,vision,language,mlcommons,mlperf,inference,generic(,variations from below) (flags from below)`

*or*

`cm run script "app vision language mlcommons mlperf inference generic (variations from below)" (flags from below)`

*or*

`cm run script d775cac873ee4231`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

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

</details>

#### CM modular Docker container
*TBD*
___
### Customization


#### Variations

  * Group "**implementation**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_cpp`
      - Environment variables:
        - *CM_MLPERF_CPP*: `yes`
        - *CM_MLPERF_IMPLEMENTATION*: `cpp`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * app,mlperf,cpp,inference
             * `if (CM_SKIP_RUN  != True)`
             * CM names: `--adr.['cpp-mlperf-inference', 'mlperf-inference-implementation']...`
             - CM script: [app-mlperf-inference-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp)
    * `_nvidia`
      - Environment variables:
        - *CM_MLPERF_IMPLEMENTATION*: `nvidia`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,mlperf,inference,nvidia,common-code
             - CM script: [get-mlperf-inference-nvidia-common-code](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-common-code)
           * get,mlperf,training,src
             - CM script: [get-mlperf-training-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-src)
           * get,generic-python-lib,_nvidia-pyindex
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_nvidia-tensorrt
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_pycuda
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_mlperf_logging
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_onnx
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * **`_reference`** (default)
      - Aliases: `_python`
      - Environment variables:
        - *CM_MLPERF_PYTHON*: `yes`
        - *CM_MLPERF_IMPLEMENTATION*: `reference`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * app,mlperf,reference,inference
             * `if (CM_SKIP_RUN  != True)`
             * CM names: `--adr.['python-reference-mlperf-inference', 'mlperf-inference-implementation']...`
             - CM script: [app-mlperf-inference-reference](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference)
    * `_tflite-cpp`
      - Environment variables:
        - *CM_MLPERF_TFLITE_CPP*: `yes`
        - *CM_MLPERF_CPP*: `yes`
        - *CM_MLPERF_IMPLEMENTATION*: `tflite-cpp`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * app,mlperf,tflite-cpp,inference
             * `if (CM_SKIP_RUN  != True)`
             * CM names: `--adr.['tflite-cpp-mlperf-inference', 'mlperf-inference-implementation']...`
             - CM script: [app-mlperf-inference-tflite-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-tflite-cpp)

    </details>


  * Group "**backend**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_deepsparse`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `deepsparse`
      - Workflow:
    * **`_onnxruntime`** (default)
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `onnxruntime`
      - Workflow:
    * `_pytorch`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `pytorch`
      - Workflow:
    * `_tf`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tf`
      - Workflow:
    * `_tflite`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tflite`
      - Workflow:
    * `_tvm-onnx`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tvm-onnx`
      - Workflow:
    * `_tvm-pytorch`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tvm-pytorch`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cpu`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `gpu`
      - Workflow:

    </details>


  * Group "**model**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_3d-unet-99`
      - Environment variables:
        - *CM_MODEL*: `3d-unet-99`
      - Workflow:
    * `_3d-unet-99.9`
      - Environment variables:
        - *CM_MODEL*: `3d-unet-99.9`
      - Workflow:
    * `_bert-99`
      - Environment variables:
        - *CM_MODEL*: `bert-99`
      - Workflow:
    * `_bert-99.9`
      - Environment variables:
        - *CM_MODEL*: `bert-99.9`
      - Workflow:
    * **`_resnet50`** (default)
      - Environment variables:
        - *CM_MODEL*: `resnet50`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,dataset-aux,imagenet-aux
             - CM script: [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)
        1. ***Read "post_deps" on other CM scripts***
           * run,accuracy,mlperf,_imagenet
             * `if (CM_MLPERF_LOADGEN_MODE in ['accuracy', 'all'] AND CM_MLPERF_ACCURACY_RESULTS_DIR  == on)`
             * CM names: `--adr.['mlperf-accuracy-script', 'imagenet-accuracy-script']...`
             - CM script: [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)
    * `_retinanet`
      - Environment variables:
        - *CM_MODEL*: `retinanet`
      - Workflow:
        1. ***Read "post_deps" on other CM scripts***
           * run,accuracy,mlperf,_openimages
             * `if (CM_MLPERF_LOADGEN_MODE in ['accuracy', 'all'] AND CM_MLPERF_ACCURACY_RESULTS_DIR  == on)`
             * CM names: `--adr.['mlperf-accuracy-script', 'openimages-accuracy-script']...`
             - CM script: [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)
    * `_rnnt`
      - Environment variables:
        - *CM_MODEL*: `rnnt`
      - Workflow:
        1. ***Read "post_deps" on other CM scripts***
           * run,accuracy,mlperf,_rnnt
             * `if (CM_MLPERF_LOADGEN_MODE in ['accuracy', 'all'] AND CM_MLPERF_ACCURACY_RESULTS_DIR  == on)`
             * CM names: `--adr.['mlperf-accuracy-script', 'rnnt-accuracy-script']...`
             - *Warning: no scripts found*

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_fp32`
      - Environment variables:
        - *CM_MLPERF_QUANTIZATION*: `False`
        - *CM_MLPERF_MODEL_PRECISION*: `float32`
      - Workflow:
    * `_int8`
      - Aliases: `_quantized`
      - Environment variables:
        - *CM_MLPERF_QUANTIZATION*: `True`
        - *CM_MLPERF_MODEL_PRECISION*: `int8`
      - Workflow:

    </details>


  * Group "**execution-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_fast`
      - Environment variables:
        - *CM_FAST_FACTOR*: `5`
        - *CM_OUTPUT_FOLDER_NAME*: `fast_results`
        - *CM_MLPERF_RUN_STYLE*: `fast`
      - Workflow:
    * **`_test`** (default)
      - Environment variables:
        - *CM_OUTPUT_FOLDER_NAME*: `test_results`
        - *CM_MLPERF_RUN_STYLE*: `test`
      - Workflow:
    * `_valid`
      - Environment variables:
        - *CM_OUTPUT_FOLDER_NAME*: `valid_results`
        - *CM_MLPERF_RUN_STYLE*: `valid`
      - Workflow:

    </details>


  * Group "**reproducibility**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_r2.1_default`
      - Environment variables:
        - *CM_RERUN*: `yes`
        - *CM_SKIP_SYS_UTILS*: `yes`
        - *CM_TEST_QUERY_COUNT*: `100`
      - Workflow:

    </details>


  * *Internal group (variations should not be selected manually)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_3d-unet_`
      - Workflow:
        1. ***Read "post_deps" on other CM scripts***
           * run,accuracy,mlperf,_3dunet
             * `if (CM_MLPERF_LOADGEN_MODE in ['accuracy', 'all'] AND CM_MLPERF_ACCURACY_RESULTS_DIR  == on)`
             * CM names: `--adr.['mlperf-accuracy-script', '3dunet-accuracy-script']...`
             - *Warning: no scripts found*
    * `_bert_`
      - Workflow:
        1. ***Read "post_deps" on other CM scripts***
           * run,accuracy,mlperf,_squad,_float32
             * `if (CM_MLPERF_LOADGEN_MODE in ['accuracy', 'all'] AND CM_MLPERF_ACCURACY_RESULTS_DIR  == on)`
             * CM names: `--adr.['squad-accuracy-script', 'mlperf-accuracy-script']...`
             - CM script: [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)

    </details>


  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_power`
      - Environment variables:
        - *CM_MLPERF_POWER*: `True`
        - *CM_SYSTEM_POWER*: `True`
      - Workflow:

    </details>


#### Unsupported or invalid variation combinations



* `_resnet50,_pytorch`
* `_retinanet,_tf`

#### Default variations

`_cpu,_onnxruntime,_reference,_resnet50,_test`

#### Input description

* --**hw_name** "Valid value - any system description which has a config file (under same name) defined [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-configs-sut-mlperf-inference/configs)"
* --**max_batchsize** "Maximum batchsize to be used"
* --**mode** "Valid values: {performance, accuracy}"
* --**num_threads** "Number of CPU threads to launch the application with"
* --**output_dir** "Location where the outputs are produced"
* --**regenerate_files** "Regenerates measurement files including accuracy.txt files even if a previous run exists. This option is redundant if `--rerun` is used"
* --**rerun** "Redo the run even if previous run files exist"
* --**scenario** "Valid values: {Offline, Server, SingleStream, MultiStream}"
* --**test_query_count** "Specifies the number of samples to be processed during a test run"

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "hw_name":...}
```

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* --**clean**=value --> **CM_MLPERF_CLEAN_SUBMISSION_DIR**=value
* --**count**=value --> **CM_MLPERF_LOADGEN_QUERY_COUNT**=value
* --**docker**=value --> **CM_RUN_DOCKER_CONTAINER**=value
* --**hw_name**=value --> **CM_HW_NAME**=value
* --**imagenet_path**=value --> **IMAGENET_PATH**=value
* --**max_amps**=value --> **CM_MLPERF_POWER_MAX_AMPS**=value
* --**max_batchsize**=value --> **CM_MLPERF_LOADGEN_MAX_BATCHSIZE**=value
* --**max_volts**=value --> **CM_MLPERF_POWER_MAX_VOLTS**=value
* --**mode**=value --> **CM_MLPERF_LOADGEN_MODE**=value
* --**new_tvm_model**=value --> **CM_MLPERF_DELETE_COMPILED_MODEL**=value
* --**ntp_server**=value --> **CM_MLPERF_POWER_NTP_SERVER**=value
* --**num_threads**=value --> **CM_NUM_THREADS**=value
* --**output_dir**=value --> **OUTPUT_BASE_DIR**=value
* --**power**=value --> **CM_SYSTEM_POWER**=value
* --**power_server**=value --> **CM_MLPERF_POWER_SERVER_ADDRESS**=value
* --**regenerate_files**=value --> **CM_REGENERATE_MEASURE_FILES**=value
* --**rerun**=value --> **CM_RERUN**=value
* --**scenario**=value --> **CM_MLPERF_LOADGEN_SCENARIO**=value
* --**target_latency**=value --> **CM_MLPERF_LOADGEN_TARGET_LATENCY**=value
* --**target_qps**=value --> **CM_MLPERF_LOADGEN_TARGET_QPS**=value
* --**test_query_count**=value --> **CM_TEST_QUERY_COUNT**=value

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "clean":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.

* CM_BATCH_COUNT: **1**
* CM_BATCH_SIZE: **1**
* CM_MLPERF_LOADGEN_MODE: **accuracy**
* CM_MLPERF_LOADGEN_SCENARIO: **Offline**
* CM_OUTPUT_FOLDER_NAME: **test_results**
* CM_MLPERF_RUN_STYLE: **test**
* CM_TEST_QUERY_COUNT: **10**
* CM_MLPERF_QUANTIZATION: **False**

</details>

___
### Script workflow, dependencies and native scripts

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,python
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,cuda
       * `if (CM_MLPERF_DEVICE  == gpu)`
       - CM script: [get-cuda-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-lib)
       - CM script: [get-cuda-toolkit](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-toolkit)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,sut,configs
       - CM script: [get-mlperf-inference-sut-configs](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference/_cm.yaml)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference/_cm.yaml)
___
### Script output
#### New environment keys (filter)

* **CM_MLPERF_***
#### New environment keys auto-detected from customize

* **CM_MLPERF_ACCURACY_RESULTS_DIR**
* **CM_MLPERF_CONF**
* **CM_MLPERF_LOADGEN_EXTRA_OPTIONS**
* **CM_MLPERF_LOADGEN_LOGS_DIR**
* **CM_MLPERF_LOADGEN_MODE**
* **CM_MLPERF_LOADGEN_QPS_OPT**
* **CM_MLPERF_LOADGEN_QUERY_COUNT**
* **CM_MLPERF_LOADGEN_SCENARIO**
* **CM_MLPERF_OUTPUT_DIR**
* **CM_MLPERF_RESULTS_DIR**
* **CM_MLPERF_RUN_STYLE**
* **CM_MLPERF_USER_CONF**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)