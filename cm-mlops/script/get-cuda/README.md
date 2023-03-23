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

# System dependencies

* Download [CUDA toolkit](https://developer.nvidia.com/cuda-toolkit).
* Download [cuDNN](https://developer.nvidia.com/rdp/cudnn-download).
* Download [TensorRT](https://developer.nvidia.com/nvidia-tensorrt-8x-download).



See [more info](README-extra.md).

#### Information

* Category: *CUDA automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda*
* Output cached?: *True*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help

```cm run script --help```

#### CM CLI

`cm run script --tags=get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda(,variations from below) (flags from below)`

*or*

`cm run script "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda (variations from below)" (flags from below)`

*or*

`cm run script 46d133d9ef92422d`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda'
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

```cm run script --tags=gui --script="get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_cudnn`
      - Environment variables:
        - *CM_CUDA_NEEDS_CUDNN*: `yes`
      - Workflow:
        1. ***Read "post_deps" on other CM scripts***
           * get,nvidia,cudnn
             * CM names: `--adr.['cudnn']...`
             - CM script: [get-cudnn](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cudnn)

    </details>


  * Group "**installation-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_lib-only`
      - Environment variables:
        - *CM_CUDA_FULL_TOOLKIT_INSTALL*: `no`
        - *CM_TMP_FILE_TO_CHECK_UNIX*: `libcudart.so`
        - *CM_TMP_FILE_TO_CHECK_WINDOWS*: `libcudart.dll`
      - Workflow:
    * **`_toolkit`** (default)
      - Environment variables:
        - *CM_CUDA_FULL_TOOLKIT_INSTALL*: `yes`
        - *CM_TMP_FILE_TO_CHECK_UNIX*: `nvcc`
        - *CM_TMP_FILE_TO_CHECK_WINDOWS*: `nvcc.exe`
      - Workflow:

    </details>


#### Default variations

`_toolkit`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* --**cudnn_tar_path**=value --> **CM_CUDNN_TAR_FILE_PATH**=value

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "cudnn_tar_path":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.

* CM_CUDA_PATH_LIB_CUDNN_EXISTS: **no**
* CM_REQUIRE_INSTALL: **no**

</details>

___
### Script workflow, dependencies and native scripts

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/_cm.json)***
     * install,cuda,prebuilt
       * `if (CM_REQUIRE_INSTALL  == yes)`
       - CM script: [install-cuda-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/_cm.json)
___
### Script output
#### New environment keys (filter)

* **+ LDFLAGS**
* **+CPLUS_INCLUDE_PATH**
* **+C_INCLUDE_PATH**
* **+DYLD_FALLBACK_LIBRARY_PATH**
* **+LD_LIBRARY_PATH**
* **+PATH**
* **CM_CUDA_***
* **CM_NVCC_***
* **CUDA_HOME**
* **CUDA_PATH**
#### New environment keys auto-detected from customize

* **CM_CUDA_CACHE_TAGS**
* **CM_CUDA_FULL_TOOLKIT_INSTALL**
* **CM_CUDA_INSTALLED_PATH**
* **CM_CUDA_PATH_BIN**
* **CM_CUDA_PATH_INCLUDE**
* **CM_CUDA_PATH_LIB**
* **CM_CUDA_VERSION**
* **CM_NVCC_BIN**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)