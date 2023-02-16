<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM GUI](#cm-gui)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! Use `README-extra.md` to add more info.*

### Description

This script is a CM wrapper to the official [Nvidia submission code](https://github.com/mlcommons/inference_results_v2.1/tree/master/closed/NVIDIA) used for 2.1 MLPerf inference round. 

This script will automatically call the Nvidia script to [add a custom system](https://github.com/mlcommons/inference_results_v2.1/tree/master/closed/NVIDIA#adding-a-new-or-custom-system).

Nvidia working directory is given by `CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH` variable which can be seen by running 
```bash
cm run script --tags=get,nvidia,common-code,_custom --out=json
```


Requirements: You need to have CUDA, cuDNN and TensorRT installed on your system. 

If CUDA is not detected, CM should download and install it automatically when you run the workflow.

For x86 machines, you can download the tar files for cuDNN and TensorRT and install them using the following commands
```bash
cm run script --tags=get,cudnn --input=<PATH_TO_CUDNN_TAR_FILE>
```

```bash
cm run script --tags=get,tensorrt --input=<PATH_TO_TENSORRT_TAR_FILE>
```

On other systems you can do a package manager install and then CM should pick up the installation automatically during the workflow run.

Nvidia run configuration values for each model-sceraio for known systems are stored in `__init__.py` files under configs directory. For custom systems these are stored under `custom.py` files. When custom config files are generated they override the default config values with empty ones (not desirable). So, you'll probably need to open the custom config file and comment out the overrides. Typically `gpu_batch_size` and `offline_expected_qps` are enough for an offline scenario run on a typical single GPU system.

<details>

```bash
arjun@phoenix:~/CM/repos/local/cache/84cc898e307e466d/inference_results_v2.1/closed/NVIDIA$ tree configs
```

```
configs
├── 3d-unet
│   ├── __init__.py
│   ├── Offline
│   │   ├── custom.py
│   │   └── __init__.py
│   └── SingleStream
│       ├── custom.py
│       └── __init__.py
├── bert
│   ├── __init__.py
│   ├── Offline
│   │   ├── custom.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── custom.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── __pycache__
│   │   └── __init__.cpython-310.pyc
│   ├── Server
│   │   ├── custom.py
│   │   └── __init__.py
│   └── SingleStream
│       ├── custom.py
│       └── __init__.py
├── configuration.py
├── dlrm
│   ├── __init__.py
│   ├── Offline
│   │   ├── custom.py
│   │   └── __init__.py
│   └── Server
│       ├── custom.py
│       └── __init__.py
├── error.py
├── __pycache__
│   ├── configuration.cpython-310.pyc
│   └── error.cpython-310.pyc
├── resnet50
│   ├── __init__.py
│   ├── MultiStream
│   │   ├── custom.py
│   │   └── __init__.py
│   ├── Offline
│   │   ├── custom.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── custom.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── __pycache__
│   │   └── __init__.cpython-310.pyc
│   ├── Server
│   │   ├── custom.py
│   │   └── __init__.py
│   └── SingleStream
│       ├── custom.py
│       ├── __init__.py
│       └── __pycache__
│           ├── custom.cpython-310.pyc
│           └── __init__.cpython-310.pyc
├── retinanet
│   ├── __init__.py
│   ├── MultiStream
│   │   ├── custom.py
│   │   └── __init__.py
│   ├── Offline
│   │   ├── custom.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── custom.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── __pycache__
│   │   └── __init__.cpython-310.pyc
│   ├── Server
│   │   ├── custom.py
│   │   └── __init__.py
│   └── SingleStream
│       ├── custom.py
│       └── __init__.py
├── rnnt
│   ├── __init__.py
│   ├── Offline
│   │   ├── custom.py
│   │   └── __init__.py
│   ├── Server
│   │   ├── custom.py
│   │   └── __init__.py
│   └── SingleStream
│       ├── custom.py
│       └── __init__.py
├── ssd-mobilenet
│   ├── __init__.py
│   ├── MultiStream
│   │   ├── custom.py
│   │   └── __init__.py
│   ├── Offline
│   │   ├── custom.py
│   │   └── __init__.py
│   └── SingleStream
│       ├── custom.py
│       └── __init__.py
└── ssd-resnet34
    ├── __init__.py
    ├── MultiStream
    │   ├── custom.py
    │   └── __init__.py
    ├── Offline
    │   ├── custom.py
    │   └── __init__.py
    ├── Server
    │   ├── custom.py
    │   └── __init__.py
    └── SingleStream
        ├── custom.py
        └── __init__.py

    
```
</details>

#### Information

* Category: *Modular MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *reproduce,mlcommons,mlperf,inference,harness,nvidia-harness,nvidia*
* Output cached?: *False*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help

```cm run script --help```

#### CM CLI

`cm run script --tags=reproduce,mlcommons,mlperf,inference,harness,nvidia-harness,nvidia(,variations from below) (flags from below)`

*or*

`cm run script "reproduce mlcommons mlperf inference harness nvidia-harness nvidia (variations from below)" (flags from below)`

*or*

`cm run script bc3b17fb430f4732`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,mlcommons,mlperf,inference,harness,nvidia-harness,nvidia'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>


#### CM GUI

```cm run script --tags=gui --script="reproduce,mlcommons,mlperf,inference,harness,nvidia-harness,nvidia"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=reproduce,mlcommons,mlperf,inference,harness,nvidia-harness,nvidia) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_batch_size.#`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `None`
        - *CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE*: `None`
      - Workflow:
    * `_dla_batch_size.#`
      - Environment variables:
        - *CM_MLPERF_NVIDIA_HARNESS_DLA_BATCH_SIZE*: `None`
      - Workflow:

    </details>


  * Group "**backend**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_tensorrt`** (default)
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tensorrt`
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
        - *CM_MLPERF_DEVICE_LIB_NAMESPEC*: `cudart`
      - Workflow:

    </details>


  * Group "**model**"
    <details>
    <summary>Click here to expand this section.</summary>

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
    * `_retinanet`
      - Environment variables:
        - *CM_MODEL*: `retinanet`
        - *CM_SKIP_MODEL_DOWNLOAD*: `True`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_Pillow
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torch
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torchvision
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_opencv-python
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


#### Default variations

`_cpu,_resnet50,_tensorrt`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* --**count**=value --> **CM_MLPERF_LOADGEN_QUERY_COUNT**=value
* --**dla_batch_size**=value --> **CM_MLPERF_NVIDIA_HARNESS_DLA_BATCH_SIZE**=value
* --**dla_copy_streams**=value --> **CM_MLPERF_NVIDIA_HARNESS_DLA_COPY_STREAMS**=value
* --**dla_inference_streams**=value --> **CM_MLPERF_NVIDIA_HARNESS_DLA_INFERENCE_STREAMS**=value
* --**end_on_device**=value --> **CM_MLPERF_NVIDIA_HARNESS_END_ON_DEVICE**=value
* --**gpu_batch_size**=value --> **CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE**=value
* --**gpu_copy_streams**=value --> **CM_MLPERF_NVIDIA_HARNESS_GPU_COPY_STREAMS**=value
* --**gpu_inference_streams**=value --> **CM_MLPERF_NVIDIA_HARNESS_GPU_INFERENCE_STREAMS**=value
* --**input_format**=value --> **CM_MLPERF_NVIDIA_HARNESS_INPUT_FORMAT**=value
* --**log_dir**=value --> **CM_MLPERF_NVIDIA_HARNESS_LOG_DIR**=value
* --**make_cmd**=value --> **CM_MLPERF_NVIDIA_RUN_COMMAND**=value
* --**max_batchsize**=value --> **CM_MLPERF_LOADGEN_MAX_BATCHSIZE**=value
* --**max_dlas**=value --> **CM_MLPERF_MAX_DLAS**=value
* --**mlperf_conf**=value --> **CM_MLPERF_CONF**=value
* --**mode**=value --> **CM_MLPERF_LOADGEN_MODE**=value
* --**multistream_target_latency**=value --> **CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY**=value
* --**offline_target_qps**=value --> **CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS**=value
* --**output_dir**=value --> **CM_MLPERF_OUTPUT_DIR**=value
* --**performance_sample_count**=value --> **CM_MLPERF_LOADGEN_PERFORMANCE_SAMPLE_COUNT**=value
* --**run_infer_on_copy_streams**=value --> **CM_MLPERF_NVIDIA_HARNESS_RUN_INFER_ON_COPY_STREAMS**=value
* --**scenario**=value --> **CM_MLPERF_LOADGEN_SCENARIO**=value
* --**server_target_qps**=value --> **CM_MLPERF_LOADGEN_SERVER_TARGET_QPS**=value
* --**singlestream_target_latency**=value --> **CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY**=value
* --**skip_preprocess**=value --> **CM_SKIP_PREPROCESS_DATASET**=value
* --**start_from_device**=value --> **CM_MLPERF_NVIDIA_HARNESS_START_FROM_DEVICE**=value
* --**target_latency**=value --> **CM_MLPERF_LOADGEN_TARGET_LATENCY**=value
* --**target_qps**=value --> **CM_MLPERF_LOADGEN_TARGET_QPS**=value
* --**use_graphs**=value --> **CM_MLPERF_NVIDIA_HARNESS_USE_GRAPHS**=value
* --**use_triton**=value --> **CM_MLPERF_NVIDIA_HARNESS_USE_TRITON**=value
* --**user_conf**=value --> **CM_MLPERF_USER_CONF**=value
* --**workspace_size**=value --> **CM_MLPERF_NVIDIA_HARNESS_WORKSPACE_SIZE**=value

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "count":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.

* CM_BATCH_COUNT: **1**
* CM_BATCH_SIZE: **1**
* CM_FAST_COMPILATION: **True**
* CM_MLPERF_LOADGEN_SCENARIO: **Offline**
* CM_MLPERF_LOADGEN_MODE: **performance**
* SKIP_POLICIES: **1**
* CM_SKIP_PREPROCESS_DATASET: **False**
* CM_SKIP_MODEL_DOWNLOAD: **False**
* CM_MLPERF_NVIDIA_RUN_COMMAND: **run**
* CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: **nvidia_original**

</details>

___
### Script workflow, dependencies and native scripts

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,cuda,_cudnn
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
     * get,tensorrt
       - CM script: [get-tensorrt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tensorrt)
     * build,nvidia,inference,server
       - CM script: [build-mlperf-inference-server-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-mlperf-inference-server-nvidia)
     * get,dataset,original,imagenet,_full
       * `if (CM_MODEL  == resnet50)`
       * CM names: `--adr.['imagenet-original']...`
       - CM script: [get-dataset-imagenet-val](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val)
     * get,ml-model,nvidia-retinanet,_efficient-nms
       * `if (CM_MODEL  == retinanet)`
       * CM names: `--adr.['ml-model-retinanet']...`
       - CM script: [get-ml-model-retinanet-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet-nvidia)
     * get,dataset,original,openimages,_validation,_full
       * `if (CM_MODEL  == retinanet)`
       * CM names: `--adr.['openimages-original']...`
       - CM script: [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
     * get,dataset,original,openimages,_calibration
       * `if (CM_MODEL  == retinanet)`
       * CM names: `--adr.['openimages-calibration']...`
       - CM script: [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,nvidia,mlperf,inference,common-code,_custom
       * CM names: `--adr.['nvidia-inference-common-code']...`
       - CM script: [get-mlperf-inference-nvidia-common-code](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-common-code)
     * generate,user-conf,mlperf,inference
       * CM names: `--adr.['user-conf-generator']...`
       - CM script: [generate-mlperf-inference-user-conf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia/_cm.yaml)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-nvidia/_cm.yaml)***
     * benchmark,program
       * `if (CM_MLPERF_SKIP_RUN  != True)`
       * CM names: `--adr.['runner']...`
       - CM script: [benchmark-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program)
___
### Script output
#### New environment keys (filter)

* **CM_DATASET_***
* **CM_HW_NAME**
* **CM_MAX_EXAMPLES**
* **CM_MLPERF_***
#### New environment keys auto-detected from customize

* **CM_MLPERF_LOADGEN_MODE**
* **CM_MLPERF_NVIDIA_RUN_COMMAND**
* **CM_MLPERF_RUN_CMD**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)