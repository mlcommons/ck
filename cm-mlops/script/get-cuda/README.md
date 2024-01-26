<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Summary](#summary)
* [Reuse this script in your project](#reuse-this-script-in-your-project)
  * [ Install CM automation language](#install-cm-automation-language)
  * [ Check CM script flags](#check-cm-script-flags)
  * [ Run this script from command line](#run-this-script-from-command-line)
  * [ Run this script from Python](#run-this-script-from-python)
  * [ Run this script via GUI](#run-this-script-via-gui)
  * [ Run this script via Docker (beta)](#run-this-script-via-docker-(beta))
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

*Note that this README is automatically generated - don't edit!*

### About

# System dependencies

* Download [CUDA toolkit](https://developer.nvidia.com/cuda-toolkit).
* Download [cuDNN](https://developer.nvidia.com/rdp/cudnn-download).
* Download [TensorRT](https://developer.nvidia.com/nvidia-tensorrt-8x-download).



See extra [notes](README-extra.md) from the authors and contributors.

#### Summary

* Category: *CUDA automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda[,variations] [--input_flags]`

2. `cmr "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

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


#### Run this script via GUI

```cmr "cm gui" --script="get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda[ variations]" [--input_flags]`

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
    * `_package-manager`
      - Environment variables:
        - *CM_CUDA_PACKAGE_MANAGER_INSTALL*: `yes`
      - Workflow:

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

* `--cudnn_tar_path=value`  &rarr;  `CM_CUDNN_TAR_FILE_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "cudnn_tar_path":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_CUDA_PATH_LIB_CUDNN_EXISTS: `no`
* CM_REQUIRE_INSTALL: `no`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,cl
       * `if (CM_CUDA_FULL_TOOLKIT_INSTALL  == yes AND CM_HOST_OS_TYPE  == windows)`
       * CM names: `--adr.['compiler']...`
       - CM script: [get-cl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/_cm.json)***
     * install,cuda,prebuilt
       * `if (CM_REQUIRE_INSTALL  == yes)`
       * CM names: `--adr.['install-cuda-prebuilt']...`
       - CM script: [install-cuda-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt)
     * get,generic-sys-util,_nvidia-cuda-toolkit
       * `if (CM_CUDA_PACKAGE_MANAGER_INSTALL  == yes)`
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/_cm.json)
</details>

___
### Script output
`cmr "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda[,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `+ LDFLAGS`
* `+CPLUS_INCLUDE_PATH`
* `+C_INCLUDE_PATH`
* `+DYLD_FALLBACK_LIBRARY_PATH`
* `+LD_LIBRARY_PATH`
* `+PATH`
* `CM_CUDA_*`
* `CM_NVCC_*`
* `CUDA_HOME`
* `CUDA_PATH`
#### New environment keys auto-detected from customize

* `CM_CUDA_CACHE_TAGS`
* `CM_CUDA_FULL_TOOLKIT_INSTALL`
* `CM_CUDA_INSTALLED_PATH`
* `CM_CUDA_PATH_BIN`
* `CM_CUDA_PATH_INCLUDE`
* `CM_CUDA_PATH_LIB`
* `CM_CUDA_VERSION`
* `CM_CUDA_VERSION_STRING`
* `CM_NVCC_BIN`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)