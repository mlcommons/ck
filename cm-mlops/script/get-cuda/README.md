**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-cuda).**



Automatically generated README for this automation recipe: **get-cuda**

Category: **CUDA automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-cuda,46d133d9ef92422d) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---

# System dependencies

* Download [CUDA toolkit](https://developer.nvidia.com/cuda-toolkit).
* Download [cuDNN](https://developer.nvidia.com/rdp/cudnn-download).
* Download [TensorRT](https://developer.nvidia.com/nvidia-tensorrt-8x-download).



---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cuda)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda*
* Output cached? *True*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda`

`cm run script --tags=get,cuda,cuda-compiler,cuda-lib,toolkit,lib,nvcc,get-nvcc,get-cuda[,variations] [--input_flags]`

*or*

`cmr "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda"`

`cmr "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

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

`cm docker script "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda[variations]" [--input_flags]`

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

* `--cudnn_tar_file=value`  &rarr;  `CM_CUDNN_TAR_FILE_PATH=value`
* `--cudnn_tar_path=value`  &rarr;  `CM_CUDNN_TAR_FILE_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "cudnn_tar_file":...}
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
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cuda/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,cl
       * `if (CM_CUDA_FULL_TOOLKIT_INSTALL  == yes AND CM_HOST_OS_TYPE  == windows)`
       * CM names: `--adr.['compiler']...`
       - CM script: [get-cl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cuda/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cuda/_cm.json)***
     * install,cuda,prebuilt
       * `if (CM_REQUIRE_INSTALL  == yes)`
       * CM names: `--adr.['install-cuda-prebuilt']...`
       - CM script: [install-cuda-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt)
     * get,generic-sys-util,_nvidia-cuda-toolkit
       * `if (CM_CUDA_PACKAGE_MANAGER_INSTALL  == yes)`
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cuda/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cuda/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cuda/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cuda/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cuda/_cm.json)

___
### Script output
`cmr "get cuda cuda-compiler cuda-lib toolkit lib nvcc get-nvcc get-cuda [,variations]" [--input_flags] -j`
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