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
  * [ Default environment](#default-environment)
* [Versions](#versions)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About


See extra [notes](README-extra.md) from the authors and contributors.

#### Summary

* Category: *MLPerf benchmark support.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,loadgen,inference,inference-loadgen,mlperf,mlcommons*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,loadgen,inference,inference-loadgen,mlperf,mlcommons[,variations] `

2. `cmr "get loadgen inference inference-loadgen mlperf mlcommons[ variations]" `

* `variations` can be seen [here](#variations)

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

`cm docker script "get loadgen inference inference-loadgen mlperf mlcommons[ variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_custom-python`
      - Environment variables:
        - *CM_TMP_USE_CUSTOM_PYTHON*: `on`
      - Workflow:
    * `_download`
      - Environment variables:
        - *CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD_URL*: `https://www.dropbox.com/scl/fi/36dgoiur26i2tvwgsaatf/loadgen.zip?rlkey=ab68i7uza9anvaw0hk1xvf0qk&dl=0`
        - *CM_MLPERF_INFERENCE_LOADGEN_VERSION*: `v3.1`
        - *CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD*: `YES`
        - *CM_DOWNLOAD_CHECKSUM*: `af3f9525965b2c1acc348fb882a5bfd1`
        - *CM_VERIFY_SSL*: `False`
      - Workflow:
    * `_download_v3.1`
      - Environment variables:
        - *CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD_URL*: `https://www.dropbox.com/scl/fi/36dgoiur26i2tvwgsaatf/loadgen.zip?rlkey=ab68i7uza9anvaw0hk1xvf0qk&dl=0`
        - *CM_MLPERF_INFERENCE_LOADGEN_VERSION*: `v3.1`
        - *CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD*: `YES`
        - *CM_DOWNLOAD_CHECKSUM*: `af3f9525965b2c1acc348fb882a5bfd1`
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
* `master`
* `pybind_fix`
* `r2.1`
* `r3.0`
* `r3.1`
___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen/_cm.json)***
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
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen/_cm.json)
</details>

___
### Script output
`cmr "get loadgen inference inference-loadgen mlperf mlcommons[,variations]"  -j`
#### New environment keys (filter)

* `+CPLUS_INCLUDE_PATH`
* `+C_INCLUDE_PATH`
* `+DYLD_FALLBACK_LIBRARY_PATH`
* `+LD_LIBRARY_PATH`
* `+PYTHONPATH`
* `CM_MLPERF_INFERENCE_LOADGEN_VERSION`
#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)