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
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! Use `README-extra.md` to add more info.*

### Description

#### Information

* Category: *Detection or installation of tools and artifacts.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,sys-util,generic,generic-sys-util*
* Output cached?: *True*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

##### CM pull repository

```cm pull repo mlcommons@ck```

##### CM script automation help

```cm run script --help```

#### CM CLI

1. `cm run script --tags=get,sys-util,generic,generic-sys-util[,variations] `

2. `cm run script "get sys-util generic generic-sys-util[,variations]" `

3. `cm run script bb0393afa8404a11 `

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,sys-util,generic,generic-sys-util'
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

```cm run script --tags=gui --script="get,sys-util,generic,generic-sys-util"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,sys-util,generic,generic-sys-util) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_gflags-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `gflags-dev`
      - Workflow:
    * `_glog-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `glog-dev`
      - Workflow:
    * `_libboost-all-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libboost-all-dev`
      - Workflow:
    * `_libgmock-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libgmock-dev`
      - Workflow:
    * `_libmpfr-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libmpfr-dev`
      - Workflow:
    * `_libnuma-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libnuma-dev`
      - Workflow:
    * `_libpci-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libpci-dev`
      - Workflow:
    * `_libre2-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libre2-dev`
      - Workflow:
    * `_libudev-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libudev-dev`
      - Workflow:
    * `_ntpdate`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `ntpdate`
      - Workflow:
    * `_nvidia-cuda-toolkit`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `nvidia-cuda-toolkit`
      - Workflow:
    * `_rapidjson-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `rapidjson-dev`
      - Workflow:
    * `_rsync`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `rsync`
      - Workflow:
    * `_screen`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `screen`
      - Workflow:
    * `_sox`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `sox`
      - Workflow:
    * `_transmission`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `transmission`
      - Workflow:
    * `_zlib`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `zlib`
      - Workflow:

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_CLEAN_DIRS: `bin`
* CM_SUDO: `sudo`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util/_cm.json)
</details>

___
### Script output
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)