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

* Category: *CUDA automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-lib)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,cuda-rt,cuda,lib,cuda-lib,lib-only,runtime,get-cuda*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=get,cuda-rt,cuda,lib,cuda-lib,lib-only,runtime,get-cuda(,variations from below) (flags from below)`

*or*

`cm run script "get cuda-rt cuda lib cuda-lib lib-only runtime get-cuda (variations from below)" (flags from below)`

*or*

`cm run script 49df6b19c3fb496e`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,cuda-rt,cuda,lib,cuda-lib,lib-only,runtime,get-cuda'
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

* CM_CUDA_PATH_LIB_CUDNN_EXISTS: **no**
* CM_REQUIRE_INSTALL: **no**

</details>


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
             - CM script: [get-cudnn](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cudnn)

</details>

___
### Script workflow, dependencies and native scripts

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-lib/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-lib/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-lib/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-lib/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-lib/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-lib/_cm.json)
___
### Script output
#### New environment keys

* **+CPLUS_INCLUDE_PATH**
* **+C_INCLUDE_PATH**
* **+DYLD_FALLBACK_LIBRARY_PATH**
* **+LD_LIBRARY_PATH**
* **+PATH**
* **CM_CUDA_***
* **CUDA_HOME**
* **CUDA_PATH**
#### New environment keys auto-detected from customize

* **CM_CUDA_INSTALLED_PATH**
* **CM_CUDA_PATH_INCLUDE**
* **CM_CUDA_PATH_LIB**
* **CM_CUDA_PATH_LIB_CUDNN**
* **CM_CUDA_PATH_LIB_CUDNN_EXISTS**
* **CM_CUDA_VERSION**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)