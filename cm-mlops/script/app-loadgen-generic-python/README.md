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
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-loadgen-generic-python)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.yaml](_cm.yaml)

___
### Tags
app,loadgen,generic,loadgen-generic,python

___
### Variations
#### All variations
* **cpu** (default)
  - *ENV CM_MLPERF_DEVICE*: `cpu`
* cuda
  - *ENV CM_MLPERF_DEVICE*: `gpu`
* **onnxruntime** (default)
  - *ENV CM_MLPERF_BACKEND*: `onnxruntime`
* resnet50
  - *ENV CM_MODEL*: `resnet50`
* retinanet
  - *ENV CM_MODEL*: `retinanet`

#### Variations by groups

  * backend
    * **onnxruntime** (default)
      - *ENV CM_MLPERF_BACKEND*: `onnxruntime`

  * device
    * **cpu** (default)
      - *ENV CM_MLPERF_DEVICE*: `cpu`
    * cuda
      - *ENV CM_MLPERF_DEVICE*: `gpu`

  * models
    * resnet50
      - *ENV CM_MODEL*: `resnet50`
    * retinanet
      - *ENV CM_MODEL*: `retinanet`
___
### Default environment

* CM_MLPERF_EXECUTION_MODE: **parallel**
* CM_MLPERF_BACKEND: **onnxruntime**
___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-loadgen-generic-python/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-python-lib,_psutil
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,cuda
       * `if (CM_MLPERF_DEVICE == ['gpu'])`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
     * get,loadgen
       * CM names: `--adr.['loadgen']...`
       - CM script: [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)
     * get,generic-python-lib,_onnxruntime
       * `if (CM_MLPERF_BACKEND == ['onnxruntime'] AND CM_MLPERF_DEVICE == ['cpu'])`
       * CM names: `--adr.['onnxruntime']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_onnxruntime_gpu
       * `if (CM_MLPERF_BACKEND == ['onnxruntime'] AND CM_MLPERF_DEVICE == ['gpu'])`
       * CM names: `--adr.['onnxruntime']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_onnx
       * `if (CM_MLPERF_BACKEND == ['onnxruntime'])`
       * CM names: `--adr.['onnx']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,ml-model,resnet50,_onnx
       * `if (CM_MODEL == ['resnet50'])`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
       - CM script: [get-ml-model-resnet50-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm)
     * get,ml-model,retinanet,_onnx,_fp32
       * `if (CM_MODEL == ['retinanet'])`
       - CM script: [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-loadgen-generic-python/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-loadgen-generic-python/_cm.yaml)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-loadgen-generic-python/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-loadgen-generic-python/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-loadgen-generic-python/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-loadgen-generic-python/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-loadgen-generic-python/_cm.yaml)
___
### New environment export

* **CM_MLPERF_***
___
### New environment detected from customize

* **CM_RUN_OPTS**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="app,loadgen,generic,loadgen-generic,python"`

*or*

`cm run script "app loadgen generic loadgen-generic python"`

*or*

`cm run script d3d949cc361747a6`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,loadgen,generic,loadgen-generic,python'
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

* output_dir --> **CM_MLPERF_OUTPUT_DIR**
* scenario --> **CM_MLPERF_LOADGEN_SCENARIO**
* runner --> **CM_MLPERF_RUNNER**
* concurrency --> **CM_MLPERF_CONCURRENCY**
* ep --> **CM_MLPERF_EXECUTION_PROVIDER**
* intraop --> **CM_MLPERF_INTRAOP**
* interop --> **CM_MLPERF_INTEROP**
* execmode --> **CM_MLPERF_EXEC_MODE**
* modelpath --> **CM_ML_MODEL_FILE_WITH_PATH**

Examples:

```bash
cm run script "app loadgen generic loadgen-generic python" --output_dir=...
```
```python
r=cm.access({... , "output_dir":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)