**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-ctuning-cpp-tflite).**



Automatically generated README for this automation recipe: **app-mlperf-inference-ctuning-cpp-tflite**

Category: **Modular MLPerf inference benchmark pipeline**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=app-mlperf-inference-ctuning-cpp-tflite,415904407cca404a) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-ctuning-cpp-tflite)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *app,mlperf,inference,tflite-cpp*
* Output cached? *False*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "app mlperf inference tflite-cpp" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=app,mlperf,inference,tflite-cpp`

`cm run script --tags=app,mlperf,inference,tflite-cpp[,variations] [--input_flags]`

*or*

`cmr "app mlperf inference tflite-cpp"`

`cmr "app mlperf inference tflite-cpp [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,mlperf,inference,tflite-cpp'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>


#### Run this script via GUI

```cmr "cm gui" --script="app,mlperf,inference,tflite-cpp"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=app,mlperf,inference,tflite-cpp) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "app mlperf inference tflite-cpp[variations]" [--input_flags]`

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
        - *CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX*: `tflite_armnn_cpp`
        - *CM_TMP_LINK_LIBS*: `tensorflowlite,armnn,armnnTfLiteParser`
        - *CM_TMP_SRC_FOLDER*: `armnn`
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
        - *CM_TMP_LINK_LIBS*: `tensorflowlite`
        - *CM_TMP_SRC_FOLDER*: `src`
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
        - *CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX1*: `using_neon`
        - *CM_MLPERF_TFLITE_USE_NEON*: `1`
      - Workflow:
    * `_use-opencl`
      - Environment variables:
        - *CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX1*: `using_opencl`
        - *CM_MLPERF_TFLITE_USE_OPENCL*: `1`
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
        - *CM_DATASET_COMPRESSED*: `on`
        - *CM_MLPERF_MODEL_PRECISION*: `int8`
      - Workflow:
    * `_uint8`
      - Environment variables:
        - *CM_DATASET_COMPRESSED*: `on`
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

* CM_DATASET_COMPRESSED: `off`
* CM_DATASET_INPUT_SQUARE_SIDE: `224`
* CM_FAST_COMPILATION: `yes`
* CM_LOADGEN_BUFFER_SIZE: `1024`
* CM_MLPERF_LOADGEN_MODE: `accuracy`
* CM_MLPERF_LOADGEN_SCENARIO: `SingleStream`
* CM_MLPERF_LOADGEN_TRIGGER_COLD_RUN: `0`
* CM_MLPERF_OUTPUT_DIR: `.`
* CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `tflite_cpp`
* CM_MLPERF_TFLITE_USE_NEON: `0`
* CM_MLPERF_TFLITE_USE_OPENCL: `0`
* CM_ML_MODEL_GIVEN_CHANNEL_MEANS: `123.68 116.78 103.94`
* CM_ML_MODEL_NORMALIZE_DATA: `0`
* CM_ML_MODEL_SUBTRACT_MEANS: `1`
* CM_VERBOSE: `0`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-ctuning-cpp-tflite/_cm.json)***
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
       * `if (CM_MLPERF_BACKEND in ['tflite', 'armnn_tflite'] AND CM_MODEL  == mobilenet)`
       * CM names: `--adr.['ml-model', 'tflite-model', 'mobilenet-model']...`
       - CM script: [get-ml-model-mobilenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet)
     * get,ml-model,resnet50,raw,_tflite,_no-argmax
       * `if (CM_MLPERF_BACKEND in ['tflite', 'armnn_tflite'] AND CM_MODEL  == resnet50)`
       * CM names: `--adr.['ml-model', 'tflite-model', 'resnet50-model']...`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * get,ml-model,resnet50,raw,_tf
       * `if (CM_MLPERF_BACKEND  == tf AND CM_MODEL  == resnet50)`
       * CM names: `--adr.['ml-model', 'tflite-model', 'resnet50-model']...`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * get,ml-model,efficientnet,raw,_tflite
       * `if (CM_MLPERF_BACKEND in ['tflite', 'armnn_tflite'] AND CM_MODEL  == efficientnet)`
       * CM names: `--adr.['ml-model', 'tflite-model', 'efficientnet-model']...`
       - CM script: [get-ml-model-efficientnet-lite](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-efficientnet-lite)
     * get,tensorflow,lib,_tflite
       - CM script: [install-tensorflow-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-from-src)
     * get,lib,armnn
       * `if (CM_MLPERF_TFLITE_USE_ARMNN  == yes)`
       * CM names: `--adr.['armnn', 'lib-armnn']...`
       - CM script: [get-lib-armnn](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-lib-armnn)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-ctuning-cpp-tflite/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-ctuning-cpp-tflite/_cm.json)***
     * generate,user-conf,mlperf,inference
       * CM names: `--adr.['user-conf-generator']...`
       - CM script: [generate-mlperf-inference-user-conf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf)
     * get,dataset,preprocessed,imagenet,_for.resnet50,_rgb32,_NHWC
       * `if (CM_MLPERF_SKIP_RUN  == no AND CM_MODEL  == resnet50) AND (CM_DATASET_COMPRESSED  != on)`
       * CM names: `--adr.['imagenet-preprocessed', 'preprocessed-dataset']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,dataset,preprocessed,imagenet,_for.mobilenet,_rgb32,_NHWC
       * `if (CM_MLPERF_SKIP_RUN  == no AND CM_MODEL in ['mobilenet', 'efficientnet']) AND (CM_DATASET_COMPRESSED  != on)`
       * CM names: `--adr.['imagenet-preprocessed', 'preprocessed-dataset']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,dataset,preprocessed,imagenet,_for.mobilenet,_rgb8,_NHWC
       * `if (CM_DATASET_COMPRESSED  == on AND CM_MLPERF_SKIP_RUN  == no AND CM_MODEL in ['mobilenet', 'efficientnet'])`
       * CM names: `--adr.['imagenet-preprocessed', 'preprocessed-dataset']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,dataset,preprocessed,imagenet,_for.resnet50,_rgb8,_NHWC
       * `if (CM_DATASET_COMPRESSED  == on AND CM_MLPERF_SKIP_RUN  == no AND CM_MODEL  == resnet50)`
       * CM names: `--adr.['imagenet-preprocessed', 'preprocessed-dataset']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-ctuning-cpp-tflite/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-ctuning-cpp-tflite/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-ctuning-cpp-tflite/_cm.json)***
     * compile,program
       * `if (CM_MLPERF_SKIP_RUN  != yes)`
       * CM names: `--adr.['compiler-program']...`
       - CM script: [compile-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program)
     * benchmark-mlperf
       * `if (CM_MLPERF_SKIP_RUN  != yes)`
       * CM names: `--adr.['mlperf-runner']...`
       - CM script: [benchmark-program-mlperf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program-mlperf)
     * save,mlperf,inference,state
       * CM names: `--adr.['save-mlperf-inference-state']...`
       - CM script: [save-mlperf-inference-implementation-state](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/save-mlperf-inference-implementation-state)

___
### Script output
`cmr "app mlperf inference tflite-cpp [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_HW_NAME`
* `CM_MLPERF_*`
* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize

* `CM_MLPERF_CONF`
* `CM_MLPERF_DEVICE`
* `CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX2`
* `CM_MLPERF_USER_CONF`