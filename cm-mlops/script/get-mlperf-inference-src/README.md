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
* [Versions](#versions)
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
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,src,source,inference,inference-src,inference-source,mlperf,mlcommons

___
### Variations
#### All variations
* 3d-unet
  - *ENV CM_SUBMODULE_3D_UNET*: `yes`
* deeplearningexamples
  - *ENV CM_SUBMODULE_DEEPLEARNINGEXAMPLES*: `yes`
* **default** (default)
  - *ENV CM_GIT_PATCH*: `no`
* full-history
  - *ENV CM_GIT_DEPTH*: ``
* gn
  - *ENV CM_SUBMODULE_GN*: `yes`
* no-recurse-submodules
  - *ENV CM_GIT_RECURSE_SUBMODULES*: ``
* nvidia-pycocotools
  - *ENV CM_GIT_PATCH_FILENAME*: `coco.patch`
* octoml
  - *ENV CM_GIT_URL*: `https://github.com/octoml/inference`
* patch
  - *ENV CM_GIT_PATCH*: `yes`
* power-dev
  - *ENV CM_SUBMODULE_POWER_DEV*: `yes`
* pybind
  - *ENV CM_SUBMODULE_PYBIND*: `yes`
* recurse-submodules
  - *ENV CM_GIT_RECURSE_SUBMODULES*: ` --recurse-submodules`
* short-history
  - *ENV CM_GIT_DEPTH*: `--depth 10`
___
### Versions
Default version: *master*

* custom
* master
* r2.1
* tvm
___
### Default environment

* CM_GIT_DEPTH: **--depth 4**
* CM_GIT_PATCH: **no**
* CM_GIT_URL: **https://github.com/mlcommons/inference.git**
* CM_GIT_RECURSE_SUBMODULES: ****
* CM_GIT_CHECKOUT: **master**
___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/_cm.json)
___
### New environment export

* **+PYTHONPATH**
* **CM_MLPERF_INFERENCE_***
* **CM_MLPERF_LAST_RELEASE**
___
### New environment detected from customize

* **CM_GIT_CHECKOUT**
* **CM_GIT_DEPTH**
* **CM_GIT_RECURSE_SUBMODULES**
* **CM_GIT_SUBMODULES**
* **CM_MLPERF_INFERENCE_BERT_PATH**
* **CM_MLPERF_INFERENCE_DLRM_PATH**
* **CM_MLPERF_INFERENCE_RNNT_PATH**
* **CM_MLPERF_INFERENCE_SOURCE**
* **CM_MLPERF_INFERENCE_VISION_PATH**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="get,src,source,inference,inference-src,inference-source,mlperf,mlcommons"`

*or*

`cm run script "get src source inference inference-src inference-source mlperf mlcommons"`

*or*

`cm run script 4b57186581024797`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,src,source,inference,inference-src,inference-source,mlperf,mlcommons'
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
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)