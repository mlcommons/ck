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

#### Information

* Category: *Modular MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-tflite-cpp)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *app,mlcommons,mlperf,inference,tflite-cpp*
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

1. `cm run script --tags=app,mlcommons,mlperf,inference,tflite-cpp[,variations] [--input_flags]`

2. `cm run script "app mlcommons mlperf inference tflite-cpp[,variations]" [--input_flags]`

3. `cm run script 415904407cca404a [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,mlcommons,mlperf,inference,tflite-cpp'
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

```cm run script --tags=gui --script="app,mlcommons,mlperf,inference,tflite-cpp"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=app,mlcommons,mlperf,inference,tflite-cpp) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_armnn`
      - Environment variables:
        - *CM_MLPERF_TFLITE_USE_ARMNN*: `yes`
        - *CM_TMP_LINK_LIBS*: `tensorflowlite,armnn`
      - Workflow:
    * `_armnn,tflite`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `armnn_tflite`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_LIB_ARMNN_VERSION>>>`
        - *CM_TMP_SRC_FOLDER*: `armnn`
        - *CM_TMP_LINK_LIBS*: `tensorflowlite,armnn,armnnTfLiteParser`
        - *CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX*: `tflite_armnn_cpp`
      - Workflow:

    </details>


  * Group "**backend**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_tf`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tf`
      - Workflow:
    * **`_tflite`** (default)
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tflite`
        - *CM_MLPERF_BACKEND_VERSION*: `master`
        - *CM_TMP_SRC_FOLDER*: `src`
        - *CM_TMP_LINK_LIBS*: `tensorflowlite`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cpu`
      - Workflow:
    * `_gpu`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `gpu`
        - *CM_MLPERF_DEVICE_LIB_NAMESPEC*: `cudart`
      - Workflow:

    </details>


  * Group "**loadgen-scenario**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_singlestream`** (default)
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `SingleStream`
      - Workflow:

    </details>


  * Group "**model**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_efficientnet`
      - Environment variables:
        - *CM_MODEL*: `efficientnet`
      - Workflow:
    * `_mobilenet`
      - Environment variables:
        - *CM_MODEL*: `mobilenet`
      - Workflow:
    * **`_resnet50`** (default)
      - Environment variables:
        - *CM_MODEL*: `resnet50`
      - Workflow:

    </details>


  * Group "**optimization-target**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_use-neon`
      - Environment variables:
        - *CM_MLPERF_TFLITE_USE_NEON*: `1`
        - *CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX1*: `using_neon`
      - Workflow:
    * `_use-opencl`
      - Environment variables:
        - *CM_MLPERF_TFLITE_USE_OPENCL*: `1`
        - *CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX1*: `using_opencl`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_fp32`** (default)
      - Environment variables:
        - *CM_MLPERF_MODEL_PRECISION*: `float32`
      - Workflow:
    * `_int8`
      - Environment variables:
        - *CM_MLPERF_MODEL_PRECISION*: `int8`
      - Workflow:
    * `_uint8`
      - Environment variables:
        - *CM_MLPERF_MODEL_PRECISION*: `uint8`
      - Workflow:

    </details>


#### Default variations

`_cpu,_fp32,_resnet50,_singlestream,_tflite`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--compressed_dataset=value`  &rarr;  `CM_DATASET_COMPRESSED=value`
* `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
* `--mlperf_conf=value`  &rarr;  `CM_MLPERF_CONF=value`
* `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
* `--output_dir=value`  &rarr;  `CM_MLPERF_OUTPUT_DIR=value`
* `--performance_sample_count=value`  &rarr;  `CM_MLPERF_LOADGEN_PERFORMANCE_SAMPLE_COUNT=value`
* `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
* `--user_conf=value`  &rarr;  `CM_MLPERF_USER_CONF=value`
* `--verbose=value`  &rarr;  `CM_VERBOSE=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "compressed_dataset":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MLPERF_OUTPUT_DIR: `.`
* CM_MLPERF_LOADGEN_SCENARIO: `SingleStream`
* CM_LOADGEN_BUFFER_SIZE: `1024`
* CM_MLPERF_LOADGEN_MODE: `accuracy`
* CM_FAST_COMPILATION: `yes`
* CM_DATASET_INPUT_SQUARE_SIDE: `224`
* CM_DATASET_COMPRESSED: `off`
* CM_ML_MODEL_NORMALIZE_DATA: `0`
* CM_ML_MODEL_SUBTRACT_MEANS: `1`
* CM_ML_MODEL_GIVEN_CHANNEL_MEANS: `123.68 116.78 103.94`
* CM_MLPERF_LOADGEN_TRIGGER_COLD_RUN: `0`
* CM_VERBOSE: `0`
* CM_MLPERF_TFLITE_USE_NEON: `0`
* CM_MLPERF_TFLITE_USE_OPENCL: `0`
* CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `tflite_cpp`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-tflite-cpp/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,cuda
       * `if (CM_MLPERF_DEVICE  == gpu)`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
     * get,loadgen
       * CM names: `--adr.['loadgen']...`
       - CM script: [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,ml-model,mobilenet,raw,_tflite
       * `if (CM_MODEL  == mobilenet AND CM_MLPERF_BACKEND in ['tflite', 'armnn_tflite'])`
       * CM names: `--adr.['ml-model', 'tflite-model', 'mobilenet-model']...`
       - CM script: [get-ml-model-mobilenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet)
     * get,ml-model,resnet50,raw,_tflite,_no-argmax
       * `if (CM_MODEL  == resnet50 AND CM_MLPERF_BACKEND in ['tflite', 'armnn_tflite'])`
       * CM names: `--adr.['ml-model', 'tflite-model', 'resnet50-model']...`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * get,ml-model,resnet50,raw,_tf
       * `if (CM_MODEL  == resnet50 AND CM_MLPERF_BACKEND  == tf)`
       * CM names: `--adr.['ml-model', 'tflite-model', 'resnet50-model']...`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * get,ml-model,efficientnet,raw,_tflite
       * `if (CM_MODEL  == efficientnet AND CM_MLPERF_BACKEND in ['tflite', 'armnn_tflite'])`
       * CM names: `--adr.['ml-model', 'tflite-model', 'efficientnet-model']...`
       - CM script: [get-ml-model-efficientnet-lite](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-efficientnet-lite)
     * get,dataset,preprocessed,imagenet,_for.resnet50,_rgb32,_NHWC
       * `if (CM_MODEL  == resnet50) AND (CM_DATASET_COMPRESSED  != on)`
       * CM names: `--adr.['imagenet-preprocessed']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,dataset,preprocessed,imagenet,_for.mobilenet,_rgb32,_NHWC
       * `if (CM_MODEL in ['mobilenet', 'efficientnet'])`
       * CM names: `--adr.['imagenet-preprocessed']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,dataset,preprocessed,imagenet,_for.resnet50,_rgb8,_NHWC
       * `if (CM_MODEL  == resnet50 AND CM_DATASET_COMPRESSED  == on)`
       * CM names: `--adr.['imagenet-preprocessed']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,tensorflow,lib,_tflite
       - CM script: [install-tensorflow-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-from-src)
     * get,lib,armnn
       * `if (CM_MLPERF_TFLITE_USE_ARMNN  == yes)`
       * CM names: `--adr.['armnn', 'lib-armnn']...`
       - CM script: [get-lib-armnn](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-lib-armnn)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-tflite-cpp/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-tflite-cpp/_cm.json)***
     * generate,user-conf,mlperf,inference
       * CM names: `--adr.['user-conf-generator']...`
       - CM script: [generate-mlperf-inference-user-conf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-tflite-cpp/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-tflite-cpp/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-tflite-cpp/_cm.json)***
     * compile,program
       * `if (CM_MLPERF_SKIP_RUN  != yes)`
       * CM names: `--adr.['compiler-program']...`
       - CM script: [compile-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program)
     * benchmark-mlperf
       * `if (CM_MLPERF_SKIP_RUN  != yes)`
       * CM names: `--adr.['mlperf-runner']...`
       - CM script: [benchmark-program-mlperf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program-mlperf)
</details>

___
### Script output
#### New environment keys (filter)

* `CM_HW_NAME`
* `CM_MLPERF_*`
* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize

* `CM_MLPERF_CONF`
* `CM_MLPERF_DEVICE`
* `CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX2`
* `CM_MLPERF_USER_CONF`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)