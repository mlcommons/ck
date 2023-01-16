<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Default environment](#default-environment)
  * [ Variations](#variations)
* [Versions](#versions)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys](#new-environment-keys)
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* Category: *ML/AI frameworks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,tvm,get-tvm*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=get,tvm,get-tvm(,variations from below) (flags from below)`

*or*

`cm run script "get tvm get-tvm (variations from below)" (flags from below)`

*or*

`cm run script 93c89140e6224f4b`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,tvm,get-tvm'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>

#### CM modular Docker container
*TBD*
___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.

* CM_GIT_CHECKOUT: **main**
* CM_GIT_URL: **https://github.com/apache/tvm**
* CM_TVM_PIP_INSTALL: **no**

</details>


#### Variations

  * *No group (any variation can be selected)*
<details>
<summary>Click here to expand this section.</summary>

    * `_cuda`
      - Environment variables:
        - *CM_TVM_USE_CUDA*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda
             - CM script: [get-cuda-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-lib)
             - CM script: [get-cuda-toolkit](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-toolkit)
    * `_llvm`
      - Environment variables:
        - *CM_TVM_USE_LLVM*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,llvm
             * CM names: `--adr.['llvm']...`
             - CM script: [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)
    * `_openmp`
      - Environment variables:
        - *CM_TVM_USE_OPENMP*: `yes`
      - Workflow:
    * `_pip-install`
      - Environment variables:
        - *CM_TVM_PIP_INSTALL*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_apache-tvm
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

</details>

___
### Versions
* main
* v0.10.0
* v0.7.0
* v0.8.0
* v0.9.0
___
### Script workflow, dependencies and native scripts

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm/_cm.json)***
     * cmake,get-cmake
       - CM script: [get-cmake](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,generic-python-lib,_decorator
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_scipy
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_attrs
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_psutil
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm/_cm.json)
___
### Script output
#### New environment keys

* **+DYLD_FALLBACK_LIBRARY_PATH**
* **+LD_LIBRARY_PATH**
* **+PYTHONPATH**
* **CM_TVM_***
* **TVM_HOME**
#### New environment keys auto-detected from customize

* **CM_TVM_PATH_INCLUDE**
* **CM_TVM_PATH_LIB**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)