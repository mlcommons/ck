*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

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
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.yaml](_cm.yaml)

___
### Tags
app,vision,language,mlcommons,mlperf,inference,generic

___
### Variations
#### All variations
* 3dunet
  - *ENV CM_MODEL*: `3dunet`
* bert-99
  - *ENV CM_MODEL*: `bert-99`
* bert-99.9
  - *ENV CM_MODEL*: `bert-99.9`
* bert_
* cpp
  - *ENV CM_MLPERF_CPP*: `yes`
  - *ENV CM_MLPERF_IMPLEMENTATION*: `cpp`
* **cpu** (default)
  - *ENV CM_MLPERF_DEVICE*: `cpu`
* cuda
  - *ENV CM_MLPERF_DEVICE*: `gpu`
* fast
  - *ENV CM_FAST_FACTOR*: `5`
  - *ENV CM_OUTPUT_FOLDER_NAME*: `fast_results`
  - *ENV CM_MLPERF_RUN_STYLE*: `fast`
* nvidia
  - *ENV CM_MLPERF_IMPLEMENTATION*: `nvidia`
* **onnxruntime** (default)
  - *ENV CM_MLPERF_BACKEND*: `onnxruntime`
* power
  - *ENV CM_MLPERF_POWER*: `True`
  - *ENV CM_SYSTEM_POWER*: `True`
* python
* pytorch
  - *ENV CM_MLPERF_BACKEND*: `pytorch`
* quantized
  - *ENV CM_MLPERF_QUANTIZATION*: `True`
* r2.1_default
  - *ENV CM_RERUN*: `yes`
  - *ENV CM_SKIP_SYS_UTILS*: `yes`
  - *ENV CM_TEST_QUERY_COUNT*: `100`
* reference
  - *ENV CM_MLPERF_PYTHON*: `yes`
  - *ENV CM_MLPERF_IMPLEMENTATION*: `reference`
* **resnet50** (default)
  - *ENV CM_MODEL*: `resnet50`
* retinanet
  - *ENV CM_MODEL*: `retinanet`
* rnnt
  - *ENV CM_MODEL*: `rnnt`
* **test** (default)
  - *ENV CM_OUTPUT_FOLDER_NAME*: `test_results`
  - *ENV CM_MLPERF_RUN_STYLE*: `test`
* tf
  - *ENV CM_MLPERF_BACKEND*: `tf`
* tflite
  - *ENV CM_MLPERF_BACKEND*: `tflite`
* tflite-cpp
  - *ENV CM_MLPERF_TFLITE_CPP*: `yes`
  - *ENV CM_MLPERF_CPP*: `yes`
  - *ENV CM_MLPERF_IMPLEMENTATION*: `tflite-cpp`
* tvm-onnx
  - *ENV CM_MLPERF_BACKEND*: `tvm-onnx`
* tvm-pytorch
  - *ENV CM_MLPERF_BACKEND*: `tvm-pytorch`
* valid
  - *ENV CM_OUTPUT_FOLDER_NAME*: `valid_results`
  - *ENV CM_MLPERF_RUN_STYLE*: `valid`

#### Variations by groups

  * backend
    * **onnxruntime** (default)
      - *ENV CM_MLPERF_BACKEND*: `onnxruntime`
    * pytorch
      - *ENV CM_MLPERF_BACKEND*: `pytorch`
    * tf
      - *ENV CM_MLPERF_BACKEND*: `tf`
    * tflite
      - *ENV CM_MLPERF_BACKEND*: `tflite`
    * tvm-onnx
      - *ENV CM_MLPERF_BACKEND*: `tvm-onnx`
    * tvm-pytorch
      - *ENV CM_MLPERF_BACKEND*: `tvm-pytorch`

  * device
    * **cpu** (default)
      - *ENV CM_MLPERF_DEVICE*: `cpu`
    * cuda
      - *ENV CM_MLPERF_DEVICE*: `gpu`

  * execution-mode
    * fast
      - *ENV CM_FAST_FACTOR*: `5`
      - *ENV CM_OUTPUT_FOLDER_NAME*: `fast_results`
      - *ENV CM_MLPERF_RUN_STYLE*: `fast`
    * **test** (default)
      - *ENV CM_OUTPUT_FOLDER_NAME*: `test_results`
      - *ENV CM_MLPERF_RUN_STYLE*: `test`
    * valid
      - *ENV CM_OUTPUT_FOLDER_NAME*: `valid_results`
      - *ENV CM_MLPERF_RUN_STYLE*: `valid`

  * models
    * 3dunet
      - *ENV CM_MODEL*: `3dunet`
    * bert-99
      - *ENV CM_MODEL*: `bert-99`
    * bert-99.9
      - *ENV CM_MODEL*: `bert-99.9`
    * **resnet50** (default)
      - *ENV CM_MODEL*: `resnet50`
    * retinanet
      - *ENV CM_MODEL*: `retinanet`
    * rnnt
      - *ENV CM_MODEL*: `rnnt`
___
### Default environment

* CM_BATCH_COUNT: **1**
* CM_BATCH_SIZE: **1**
* CM_MLPERF_LOADGEN_MODE: **accuracy**
* CM_MLPERF_LOADGEN_SCENARIO: **Offline**
* CM_OUTPUT_FOLDER_NAME: **test_results**
* CM_MLPERF_RUN_STYLE: **test**
* CM_TEST_QUERY_COUNT: **10**
* CM_MLPERF_QUANTIZATION: **False**
___
### CM script workflow

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
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
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
### New environment export

* **CM_MLPERF_***
___
### New environment detected from customize

* **CM_MAX_EXAMPLES**
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
* **CM_NUM_THREADS**
* **CM_SKIP_RUN**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="app,vision,language,mlcommons,mlperf,inference,generic"`

*or*

`cm run script "app vision language mlcommons mlperf inference generic"`

*or*

`cm run script d775cac873ee4231`

#### CM Python API

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

#### CM modular Docker container
*TBD*

#### Script input flags mapped to environment

* count --> **CM_MLPERF_LOADGEN_QUERY_COUNT**
* docker --> **CM_RUN_DOCKER_CONTAINER**
* hw_name --> **CM_HW_NAME**
* imagenet_path --> **IMAGENET_PATH**
* max_batchsize --> **CM_MLPERF_LOADGEN_MAX_BATCHSIZE**
* mode --> **CM_MLPERF_LOADGEN_MODE**
* num_threads --> **CM_NUM_THREADS**
* output_dir --> **OUTPUT_BASE_DIR**
* power --> **CM_SYSTEM_POWER**
* power_server --> **CM_MLPERF_POWER_SERVER_ADDRESS**
* ntp_server --> **CM_MLPERF_POWER_NTP_SERVER**
* max_amps --> **CM_MLPERF_POWER_MAX_AMPS**
* max_volts --> **CM_MLPERF_POWER_MAX_VOLTS**
* regenerate_files --> **CM_REGENERATE_MEASURE_FILES**
* rerun --> **CM_RERUN**
* scenario --> **CM_MLPERF_LOADGEN_SCENARIO**
* test_query_count --> **CM_TEST_QUERY_COUNT**
* new_tvm_model --> **CM_MLPERF_DELETE_COMPILED_MODEL**
* clean --> **CM_MLPERF_CLEAN_SUBMISSION_DIR**

Examples:

```bash
cm run script "app vision language mlcommons mlperf inference generic" --count=...
```
```python
r=cm.access({... , "count":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)