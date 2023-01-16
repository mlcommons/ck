*This README is automatically generated - don't edit! Use `README-extra.md` for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Variations](#variations)
  * [ All variations](#all-variations)
  * [ Variations by groups](#variations-by-groups)
* [Default environment](#default-environment)
* [CM script workflow](#cm-script-workflow)
* [New environment export](#new-environment-export)
* [New environment detected from customize](#new-environment-detected-from-customize)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
  * [ Script input flags mapped to environment](#script-input-flags-mapped-to-environment)
* [Maintainers](#maintainers)

</details>

___
### About

*TBD*
___
### Category

Modular MLPerf benchmarks.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-image-classification-cpp)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
app,mlcommons,mlperf,inference,tflite-cpp

___
### Variations
#### All variations
* **cpu** (default)
  - *ENV CM_MLPERF_DEVICE*: `cpu`
* gpu
  - *ENV CM_MLPERF_DEVICE*: `gpu`
  - *ENV CM_MLPERF_DEVICE_LIB_NAMESPEC*: `cudart`
* mobilenet
  - *ENV CM_MODEL*: `mobilenet`
* **resnet50** (default)
  - *ENV CM_MODEL*: `resnet50`
* tf
  - *ENV CM_MLPERF_BACKEND*: `tf`
* **tflite** (default)
  - *ENV CM_MLPERF_BACKEND*: `tflite`

#### Variations by groups

  * backend
    * tf
      - *ENV CM_MLPERF_BACKEND*: `tf`
    * **tflite** (default)
      - *ENV CM_MLPERF_BACKEND*: `tflite`

  * device
    * **cpu** (default)
      - *ENV CM_MLPERF_DEVICE*: `cpu`
    * gpu
      - *ENV CM_MLPERF_DEVICE*: `gpu`
      - *ENV CM_MLPERF_DEVICE_LIB_NAMESPEC*: `cudart`

  * model
    * mobilenet
      - *ENV CM_MODEL*: `mobilenet`
    * **resnet50** (default)
      - *ENV CM_MODEL*: `resnet50`
___
### Default environment

* CM_MLPERF_OUTPUT_DIR: **.**
* CM_MLPERF_LOADGEN_SCENARIO: **SingleStream**
* CM_LOADGEN_BUFFER_SIZE: **1024**
* CM_MLPERF_LOADGEN_MODE: **accuracy**
* CM_FAST_COMPILATION: **yes**
___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-image-classification-cpp/_cm.json)***
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
     * get,dataset,preprocessed,imagenet,_for.resnet50-rgb8,_NHWC
       * `if (CM_MODEL  == resnet50)`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,ml-model,resnet50,raw,_tflite,_no-argmax
       * `if (CM_MODEL  == resnet50 AND CM_MLPERF_BACKEND  == tflite)`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * get,ml-model,resnet50,raw,_tf
       * `if (CM_MODEL  == resnet50 AND CM_MLPERF_BACKEND  == tf)`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * get,tensorflow,lib,_tflite
       - CM script: [install-tensorflow-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-from-src)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-image-classification-cpp/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-image-classification-cpp/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-image-classification-cpp/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-image-classification-cpp/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-image-classification-cpp/_cm.json)***
     * compile,program
       * CM names: `--adr.['compiler-program']...`
       - CM script: [compile-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program)
     * benchmark,program
       * CM names: `--adr.['runner']...`
       - CM script: [benchmark-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program)
___
### New environment export

___
### New environment detected from customize

* **CM_CXX_SOURCE_FILES**
* **CM_LINKER_LANG**
* **CM_MLPERF_CONF**
* **CM_MLPERF_DEVICE**
* **CM_MLPERF_USER_CONF**
* **CM_RUN_DIR**
* **CM_SOURCE_FOLDER_PATH**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="app,mlcommons,mlperf,inference,tflite-cpp"`

*or*

`cm run script "app mlcommons mlperf inference tflite-cpp"`

*or*

`cm run script 415904407cca404a`

#### CM Python API

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

#### CM modular Docker container
*TBD*

#### Script input flags mapped to environment

* count --> **CM_MLPERF_LOADGEN_QUERY_COUNT**
* mlperf_conf --> **CM_MLPERF_CONF**
* mode --> **CM_MLPERF_LOADGEN_MODE**
* output_dir --> **CM_MLPERF_OUTPUT_DIR**
* performance_sample_count --> **CM_MLPERF_LOADGEN_PERFORMANCE_SAMPLE_COUNT**
* scenario --> **CM_MLPERF_LOADGEN_SCENARIO**
* user_conf --> **CM_MLPERF_USER_CONF**

Examples:

```bash
cm run script "app mlcommons mlperf inference tflite-cpp" --count=...
```
```python
r=cm.access({... , "count":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)