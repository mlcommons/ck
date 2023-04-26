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

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description

This portable CM script is being developed by the [MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)
to modularize the *python reference implementations* of the [MLPerf inference benchmark](https://github.com/mlcommons/inference) 
using the [MLCommons CM automation meta-framework](https://github.com/mlcommons/ck).
The goal is to make it easier to run, optimize and reproduce MLPerf benchmarks 
across diverse platforms with continuously changing software and hardware.

See the current coverage of different models, devices and backends [here](README-extra.md#current-coverage).


See [more info](README-extra.md).

#### Information

* Category: *Modular MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *app,vision,language,mlcommons,mlperf,inference,reference,ref*
* Output cached?: *False*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

##### CM pull repository

```cm pull repo mlcommons@ck```

##### CM script automation help

```cm run script --help```

#### CM CLI

1. `cm run script --tags=app,vision,language,mlcommons,mlperf,inference,reference,ref[,variations] [--input_flags]`

2. `cm run script "app vision language mlcommons mlperf inference reference ref[,variations]" [--input_flags]`

3. `cm run script ff149e9781fc4b65 [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,vision,language,mlcommons,mlperf,inference,reference,ref'
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

```cm run script --tags=gui --script="app,vision,language,mlcommons,mlperf,inference,reference,ref"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=app,vision,language,mlcommons,mlperf,inference,reference,ref) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_3d-unet`
      - Environment variables:
        - *CM_TMP_IGNORE_MLPERF_QUERY_COUNT*: `True`
        - *CM_MLPERF_MODEL_SKIP_BATCHING*: `True`
      - Workflow:
    * `_batch_size.#`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_MAX_BATCHSIZE*: `#`
      - Workflow:
    * `_bert`
      - Environment variables:
        - *CM_MLPERF_MODEL_SKIP_BATCHING*: `True`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_tokenization
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_six
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_protobuf
             * `if (CM_MLPERF_BACKEND in ['tf', 'tflite'])`
             * CM names: `--adr.['protobuf']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_boto3
             * `if (CM_MLPERF_BACKEND  == pytorch)`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torch
             * CM names: `--adr.['ml-engine-pytorch']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_dlrm`
      - Environment variables:
        - *CM_MLPERF_MODEL_SKIP_BATCHING*: `True`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,dlrm,src
             * CM names: `--adr.['dlrm-src']...`
             - CM script: [get-dlrm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dlrm)
           * get,generic-python-lib,_mlperf_logging
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_opencv-python
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_tensorboard
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_protobuf
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_scikit-learn
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_tqdm
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_onnx
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,python3
             - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
    * `_onnxruntime,cpu`
      - Environment variables:
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_ONNXRUNTIME_VERSION>>>`
      - Workflow:
    * `_onnxruntime,cuda`
      - Environment variables:
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_ONNXRUNTIME_GPU_VERSION>>>`
      - Workflow:
    * `_r2.1_default`
      - Environment variables:
        - *CM_RERUN*: `yes`
        - *CM_SKIP_SYS_UTILS*: `yes`
        - *CM_TEST_QUERY_COUNT*: `100`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cpu`
        - *CUDA_VISIBLE_DEVICES*: ``
        - *USE_CUDA*: `False`
        - *USE_GPU*: `False`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `gpu`
        - *USE_CUDA*: `True`
        - *USE_GPU*: `True`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_deepsparse`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `deepsparse`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_DEEPSPARSE_VERSION>>>`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_deepsparse
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * **`_onnxruntime`** (default)
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `onnxruntime`
      - Workflow:
    * `_pytorch`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `pytorch`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TORCH_VERSION>>>`
      - Workflow:
    * `_tf`
      - Aliases: `_tensorflow`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tf`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TENSORFLOW_VERSION>>>`
      - Workflow:
    * `_tvm-onnx`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tvm-onnx`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_ONNXRUNTIME_VERSION>>>`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_onnx
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,tvm
             * CM names: `--adr.tvm...`
             - CM script: [get-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm)
    * `_tvm-pytorch`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tvm-pytorch`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TORCH_VERSION>>>`
        - *MLPERF_TVM_TORCH_QUANTIZED_ENGINE*: `qnnpack`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,tvm
             * CM names: `--adr.tvm...`
             - CM script: [get-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm)
    * `_tvm-tflite`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tvm-tflite`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TVM-TFLITE_VERSION>>>`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,tvm
             * CM names: `--adr.tvm...`
             - CM script: [get-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm)

    </details>


  * Group "**implementation**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_python`** (default)
      - Environment variables:
        - *CM_MLPERF_PYTHON*: `yes`
        - *CM_MLPERF_IMPLEMENTATION*: `reference`
      - Workflow:

    </details>


  * Group "**models**"
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
    * `_dlrm-99`
      - Environment variables:
        - *CM_MODEL*: `dlrm-99`
      - Workflow:
    * `_dlrm-99.9`
      - Environment variables:
        - *CM_MODEL*: `dlrm-99.9`
      - Workflow:
    * **`_resnet50`** (default)
      - Environment variables:
        - *CM_MODEL*: `resnet50`
        - *CM_MLPERF_USE_MLCOMMONS_RUN_SCRIPT*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_opencv-python
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_pycocotools
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_retinanet`
      - Environment variables:
        - *CM_MODEL*: `retinanet`
        - *CM_MLPERF_USE_MLCOMMONS_RUN_SCRIPT*: `yes`
        - *CM_MLPERF_LOADGEN_MAX_BATCHSIZE*: `1`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_opencv-python
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_pycocotools
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_rnnt`
      - Environment variables:
        - *CM_MODEL*: `rnnt`
        - *CM_MLPERF_MODEL_SKIP_BATCHING*: `True`
        - *CM_TMP_IGNORE_MLPERF_QUERY_COUNT*: `True`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_librosa
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_inflect
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_unidecode
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_toml
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_fp32`** (default)
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


#### Default variations

`_cpu,_fp32,_onnxruntime,_python,_resnet50`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--clean=value`  &rarr;  `CM_MLPERF_CLEAN_SUBMISSION_DIR=value`
* `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
* `--dataset=value`  &rarr;  `CM_MLPERF_VISION_DATASET_OPTION=value`
* `--dataset_args=value`  &rarr;  `CM_MLPERF_EXTRA_DATASET_ARGS=value`
* `--docker=value`  &rarr;  `CM_RUN_DOCKER_CONTAINER=value`
* `--hw_name=value`  &rarr;  `CM_HW_NAME=value`
* `--imagenet_path=value`  &rarr;  `IMAGENET_PATH=value`
* `--max_amps=value`  &rarr;  `CM_MLPERF_POWER_MAX_AMPS=value`
* `--max_batchsize=value`  &rarr;  `CM_MLPERF_LOADGEN_MAX_BATCHSIZE=value`
* `--max_volts=value`  &rarr;  `CM_MLPERF_POWER_MAX_VOLTS=value`
* `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
* `--model=value`  &rarr;  `CM_MLPERF_CUSTOM_MODEL_PATH=value`
* `--ntp_server=value`  &rarr;  `CM_MLPERF_POWER_NTP_SERVER=value`
* `--num_threads=value`  &rarr;  `CM_NUM_THREADS=value`
* `--output_dir=value`  &rarr;  `OUTPUT_BASE_DIR=value`
* `--power=value`  &rarr;  `CM_MLPERF_POWER=value`
* `--power_server=value`  &rarr;  `CM_MLPERF_POWER_SERVER_ADDRESS=value`
* `--regenerate_files=value`  &rarr;  `CM_REGENERATE_MEASURE_FILES=value`
* `--rerun=value`  &rarr;  `CM_RERUN=value`
* `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
* `--test_query_count=value`  &rarr;  `CM_TEST_QUERY_COUNT=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "clean":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MLPERF_LOADGEN_MODE: `accuracy`
* CM_MLPERF_LOADGEN_SCENARIO: `Offline`
* CM_OUTPUT_FOLDER_NAME: `test_results`
* CM_MLPERF_RUN_STYLE: `test`
* CM_TEST_QUERY_COUNT: `10`
* CM_MLPERF_QUANTIZATION: `False`
* CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `reference`
* CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX: ``

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,python
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,cuda,_cudnn
       * `if (CM_MLPERF_DEVICE  == gpu)`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
     * get,nvidia,tensorrt
       * `if (CM_MLPERF_BACKEND  == tensorrt)`
       - CM script: [get-tensorrt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tensorrt)
     * get,generic-python-lib,_onnxruntime
       * `if (CM_MLPERF_BACKEND in ['onnxruntime', 'tvm-onnx'] AND CM_MLPERF_DEVICE  == cpu)`
       * CM names: `--adr.['ml-engine-onnxruntime']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_onnxruntime_gpu
       * `if (CM_MLPERF_BACKEND in ['onnxruntime', 'tvm-onnx'] AND CM_MLPERF_DEVICE  == gpu) AND (CM_MODEL not in ['3d-unet-99', '3d-unet-99.9', 'resnet50'])`
       * CM names: `--adr.['ml-engine-onnxruntime-cuda']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_onnxruntime
       * `if (CM_MLPERF_BACKEND  == onnxruntime AND CM_MLPERF_DEVICE  == gpu AND CM_MODEL in ['3d-unet-99', '3d-unet-99.9', 'resnet50'])`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_onnxruntime_gpu
       * `if (CM_MLPERF_BACKEND  == onnxruntime AND CM_MLPERF_DEVICE  == gpu AND CM_MODEL in ['3d-unet-99', '3d-unet-99.9', 'resnet50'])`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torch
       * `if (CM_MLPERF_BACKEND in ['pytorch', 'tvm-pytorch'] AND CM_MLPERF_DEVICE  == cpu)`
       * CM names: `--adr.['ml-engine-pytorch']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torch_cuda
       * `if (CM_MLPERF_BACKEND in ['pytorch', 'tvm-pytorch'] AND CM_MLPERF_DEVICE  == gpu)`
       * CM names: `--adr.['ml-engine-pytorch']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torchvision
       * `if (CM_MLPERF_BACKEND in ['pytorch', 'tvm-pytorch'] AND CM_MLPERF_DEVICE  == cpu)`
       * CM names: `--adr.['ml-engine-torchvision']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torchvision_cuda
       * `if (CM_MLPERF_BACKEND in ['pytorch', 'tvm-pytorch'] AND CM_MLPERF_DEVICE  == gpu)`
       * CM names: `--adr.['ml-engine-torchvision']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_transformers
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       * CM names: `--adr.['ml-engine-transformers']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_tensorflow
       * `if (CM_MLPERF_BACKEND in ['tf', 'tflite'])`
       * CM names: `--adr.['ml-engine-tensorflow']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,ml-model,image-classification,resnet50
       * `if (CM_MODEL  == resnet50) AND (CM_MLPERF_CUSTOM_MODEL_PATH  != on)`
       * CM names: `--adr.['ml-model', 'resnet50-model']...`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
       - CM script: [get-ml-model-resnet50-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm)
     * get,ml-model,object-detection,retinanet
       * `if (CM_MODEL  == retinanet)`
       * CM names: `--adr.['ml-model', 'retinanet-model']...`
       - CM script: [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
     * get,ml-model,object-detection,resnext50,fp32,_pytorch-weights
       * `if (CM_MLPERF_BACKEND  == pytorch AND CM_MLPERF_IMPLEMENTATION  == nvidia AND CM_MODEL  == retinanet)`
       * CM names: `--adr.['ml-model', 'retinanet-model']...`
       - *Warning: no scripts found*
     * get,ml-model,language-processing,bert-large
       * `if (CM_MODEL in ['bert-99', 'bert-99.9']) AND (CM_MLPERF_CUSTOM_MODEL_PATH  != on)`
       * CM names: `--adr.['ml-model', 'bert-model']...`
       - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
     * get,ml-model,medical-imaging,3d-unet
       * `if (CM_MODEL in ['3d-unet-99', '3d-unet-99.9'])`
       * CM names: `--adr.['ml-model', '3d-unet-model']...`
       - CM script: [get-ml-model-3d-unet-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-3d-unet-kits19)
     * get,ml-model,speech-recognition,rnnt
       * `if (CM_MODEL  == rnnt)`
       * CM names: `--adr.['ml-model', 'rnnt-model']...`
       - CM script: [get-ml-model-rnnt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt)
     * get,ml-model,recommendation,dlrm
       * `if (CM_MODEL in ['dlrm-99', 'dlrm-99.9'])`
       * CM names: `--adr.['ml-model', 'dlrm-model']...`
       - CM script: [get-ml-model-dlrm-terabyte](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte)
     * get,dataset,image-classification,imagenet,preprocessed,_default
       * `if (CM_MODEL  == resnet50) AND (CM_MLPERF_VISION_DATASET_OPTION  != True)`
       * CM names: `--adr.['imagenet-preprocessed']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,dataset,image-classification,imagenet,preprocessed,_pytorch
       * `if (CM_MODEL  == resnet50 AND CM_MLPERF_VISION_DATASET_OPTION  == imagenet_pytorch)`
       * CM names: `--adr.['imagenet-preprocessed']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,dataset-aux,image-classification,imagenet-aux
       * `if (CM_MODEL  == resnet50)`
       - CM script: [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)
     * get,dataset,object-detection,open-images,openimages,preprocessed,_validation
       * `if (CM_MODEL  == retinanet)`
       * CM names: `--adr.['openimages-preprocessed']...`
       - CM script: [get-preprocessed-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages)
     * get,dataset,squad,original
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       - CM script: [get-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad)
     * get,dataset-aux,squad-vocab
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       - CM script: [get-dataset-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad-vocab)
     * get,dataset,kits19,preprocessed
       * `if (CM_MODEL in ['3d-unet-99', '3d-unet-99.9'])`
       - CM script: [get-preprocessed-dataset-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-kits19)
     * get,dataset,librispeech,preprocessed
       * `if (CM_MODEL  == rnnt)`
       - CM script: [get-preprocessed-dataset-librispeech](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-librispeech)
     * get,dataset,criteo,preprocessed
       * `if (CM_MODEL in ['dlrm-99', 'dlrm-99.9'])`
       * CM names: `--adr.['criteo-preprocessed']...`
       - CM script: [get-preprocessed-dataset-criteo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-criteo)
     * generate,user-conf,mlperf,inference
       * CM names: `--adr.['user-conf-generator']...`
       - CM script: [generate-mlperf-inference-user-conf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf)
     * get,loadgen
       * CM names: `--adr.['loadgen', 'mlperf-inference-loadgen']...`
       - CM script: [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference/_cm.yaml)
  1. ***Run native script if exists***
  1. ***Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference/_cm.yaml)***
     * benchmark,program
       * `if (CM_MLPERF_SKIP_RUN  != True)`
       * CM names: `--adr.['runner']...`
       - CM script: [benchmark-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference/_cm.yaml)
</details>

___
### Script output
#### New environment keys (filter)

* `CM_DATASET_*`
* `CM_HW_NAME`
* `CM_MAX_EXAMPLES`
* `CM_MLPERF_*`
* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize

* `CM_MLPERF_BACKEND`
* `CM_MLPERF_CONF`
* `CM_MLPERF_DEVICE`
* `CM_MLPERF_LOADGEN_EXTRA_OPTIONS`
* `CM_MLPERF_LOADGEN_MODE`
* `CM_MLPERF_LOADGEN_QPS_OPT`
* `CM_MLPERF_LOADGEN_SCENARIO`
* `CM_MLPERF_OUTPUT_DIR`
* `CM_MLPERF_RUN_CMD`
* `CM_ML_MODEL_FILE_WITH_PATH`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)