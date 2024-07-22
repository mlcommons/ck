**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-loadgen).**



Automatically generated README for this automation recipe: **get-mlperf-inference-loadgen**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-mlperf-inference-loadgen,64c3d98d0ba04950) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-loadgen)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *get,loadgen,inference,inference-loadgen,mlperf,mlcommons*
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

````cmr "get loadgen inference inference-loadgen mlperf mlcommons" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,loadgen,inference,inference-loadgen,mlperf,mlcommons`

`cm run script --tags=get,loadgen,inference,inference-loadgen,mlperf,mlcommons[,variations] `

*or*

`cmr "get loadgen inference inference-loadgen mlperf mlcommons"`

`cmr "get loadgen inference inference-loadgen mlperf mlcommons [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,loadgen,inference,inference-loadgen,mlperf,mlcommons'
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

```cmr "cm gui" --script="get,loadgen,inference,inference-loadgen,mlperf,mlcommons"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,loadgen,inference,inference-loadgen,mlperf,mlcommons) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get loadgen inference inference-loadgen mlperf mlcommons[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_copy`
      - Workflow:
    * `_custom-python`
      - Environment variables:
        - *CM_TMP_USE_CUSTOM_PYTHON*: `on`
      - Workflow:
    * `_download`
      - Environment variables:
        - *CM_DOWNLOAD_CHECKSUM*: `af3f9525965b2c1acc348fb882a5bfd1`
        - *CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD*: `YES`
        - *CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD_URL*: `https://www.dropbox.com/scl/fi/36dgoiur26i2tvwgsaatf/loadgen.zip?rlkey=ab68i7uza9anvaw0hk1xvf0qk&dl=0`
        - *CM_MLPERF_INFERENCE_LOADGEN_VERSION*: `v3.1`
        - *CM_VERIFY_SSL*: `False`
      - Workflow:
    * `_download_v3.1`
      - Environment variables:
        - *CM_DOWNLOAD_CHECKSUM*: `af3f9525965b2c1acc348fb882a5bfd1`
        - *CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD*: `YES`
        - *CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD_URL*: `https://www.dropbox.com/scl/fi/36dgoiur26i2tvwgsaatf/loadgen.zip?rlkey=ab68i7uza9anvaw0hk1xvf0qk&dl=0`
        - *CM_MLPERF_INFERENCE_LOADGEN_VERSION*: `v3.1`
        - *CM_VERIFY_SSL*: `False`
      - Workflow:
    * `_download_v4.0`
      - Environment variables:
        - *CM_DOWNLOAD_CHECKSUM*: `b4d97525d9ad0539a64667f2a3ca20c5`
        - *CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD*: `YES`
        - *CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD_URL*: `https://www.dropbox.com/scl/fi/gk5e9kziju5t56umxyzyx/loadgen.zip?rlkey=vsie4xnzml1inpjplm5cg7t54&dl=0`
        - *CM_MLPERF_INFERENCE_LOADGEN_VERSION*: `v4.0`
        - *CM_VERIFY_SSL*: `False`
      - Workflow:

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_SHARED_BUILD: `no`

</details>

#### Versions
Default version: `master`

* `custom`
* `main`
* `master`
* `pybind_fix`
* `r2.1`
* `r3.0`
* `r3.1`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-loadgen/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,python3
       * CM names: `--adr.['python3', 'python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlcommons,inference,src
       * `if (CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD  != YES)`
       * CM names: `--adr.['inference-src-loadgen']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * download-and-extract,file,_wget,_extract
       * `if (CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD  == YES)`
       * CM names: `--adr.['inference-src-loadgen-download']...`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
     * get,compiler
       * `if (CM_HOST_OS_TYPE  != windows)`
       * CM names: `--adr.['compiler']...`
       - CM script: [get-cl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl)
       - CM script: [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)
       - CM script: [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)
     * get,cl
       * `if (CM_HOST_OS_TYPE  == windows)`
       * CM names: `--adr.['compiler']...`
       - CM script: [get-cl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl)
     * get,cmake
       * CM names: `--adr.['cmake']...`
       - CM script: [get-cmake](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)
     * get,generic-python-lib,_package.wheel
       * CM names: `--adr.['pip-package', 'wheel']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_pip
       * CM names: `--adr.['pip-package', 'pip']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_package.pybind11
       * CM names: `--adr.['pip-package', 'pybind11']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_package.setuptools
       * CM names: `--adr.['pip-package', 'setuputils']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-loadgen/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-loadgen/_cm.yaml)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-loadgen/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-loadgen/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-loadgen/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-loadgen/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-loadgen/_cm.yaml)

___
### Script output
`cmr "get loadgen inference inference-loadgen mlperf mlcommons [,variations]"  -j`
#### New environment keys (filter)

* `+CPLUS_INCLUDE_PATH`
* `+C_INCLUDE_PATH`
* `+DYLD_FALLBACK_LIBRARY_PATH`
* `+LD_LIBRARY_PATH`
* `+PYTHONPATH`
* `CM_MLPERF_INFERENCE_LOADGEN_*`
#### New environment keys auto-detected from customize

* `CM_MLPERF_INFERENCE_LOADGEN_INCLUDE_PATH`
* `CM_MLPERF_INFERENCE_LOADGEN_INSTALL_PATH`
* `CM_MLPERF_INFERENCE_LOADGEN_LIBRARY_PATH`
* `CM_MLPERF_INFERENCE_LOADGEN_PYTHON_PATH`