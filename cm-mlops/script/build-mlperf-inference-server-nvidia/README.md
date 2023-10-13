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
* [Versions](#versions)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* Category: *Modular MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-mlperf-inference-server-nvidia)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *build,mlcommons,mlperf,inference,inference-server,server,nvidia-harness,nvidia*
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

1. `cm run script --tags=build,mlcommons,mlperf,inference,inference-server,server,nvidia-harness,nvidia[,variations] [--input_flags]`

2. `cm run script "build mlcommons mlperf inference inference-server server nvidia-harness nvidia[,variations]" [--input_flags]`

3. `cm run script f37403af5e9f4541 [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'build,mlcommons,mlperf,inference,inference-server,server,nvidia-harness,nvidia'
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

```cm run script --tags=gui --script="build,mlcommons,mlperf,inference,inference-server,server,nvidia-harness,nvidia"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=build,mlcommons,mlperf,inference,inference-server,server,nvidia-harness,nvidia) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Variations

  * Group "**code**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_ctuning`** (default)
      - Workflow:
    * `_custom`
      - Workflow:
    * `_mlcommons`
      - Workflow:
    * `_nvidia-only`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_cpu`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cpu`
      - Workflow:
    * **`_cuda`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cuda`
        - *CM_MLPERF_DEVICE_LIB_NAMESPEC*: `cudart`
      - Workflow:
    * `_inferentia`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `inferentia`
      - Workflow:

    </details>


#### Default variations

`_ctuning,_cuda`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--clean=value`  &rarr;  `CM_MAKE_CLEAN=value`
* `--custom_system=value`  &rarr;  `CM_CUSTOM_SYSTEM_NVIDIA=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "clean":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MAKE_BUILD_COMMAND: `build`
* CM_MAKE_CLEAN: `no`

</details>

#### Versions
Default version: `r3.1`

* `r2.1`
* `r3.0`
* `r3.1`
___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-mlperf-inference-server-nvidia/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,cuda,_cudnn
       * `if (CM_MLPERF_DEVICE in ['cuda', 'inferentia'])`
       * CM names: `--adr.['cuda']...`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
     * get,tensorrt,_dev
       * `if (CM_MLPERF_DEVICE in ['cuda', 'inferentia']) AND (CM_TENSORRT_SYSTEM_DETECT  != True)`
       * CM names: `--adr.['tensorrt']...`
       - CM script: [get-tensorrt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tensorrt)
     * get,gcc
       - CM script: [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)
     * get,cmake
       - CM script: [get-cmake](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)
     * get,generic,sys-util,_glog-dev
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,generic,sys-util,_gflags-dev
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,generic,sys-util,_libgmock-dev
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,generic,sys-util,_libre2-dev
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,generic,sys-util,_libnuma-dev
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,generic,sys-util,_libboost-all-dev
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,generic,sys-util,_rapidjson-dev
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,nvidia,mlperf,inference,common-code
       * CM names: `--adr.['nvidia-inference-common-code']...`
       - CM script: [get-mlperf-inference-nvidia-common-code](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-common-code)
     * get,generic-python-lib,_pycuda
       * `if (CM_RUN_STATE_DOCKER not in ['yes', True, 'True'])`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_opencv-python
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_nvidia-dali
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,mlperf,inference,nvidia,scratch,space
       * CM names: `--adr.['nvidia-scratch-space']...`
       - CM script: [get-mlperf-inference-nvidia-scratch-space](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-scratch-space)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-mlperf-inference-server-nvidia/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-mlperf-inference-server-nvidia/_cm.yaml)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-mlperf-inference-server-nvidia/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-mlperf-inference-server-nvidia/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-mlperf-inference-server-nvidia/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-mlperf-inference-server-nvidia/_cm.yaml)***
     * add,custom,system,nvidia
       * `if (CM_CUSTOM_SYSTEM_NVIDIA not in ['no', False, 'False'])`
       * CM names: `--adr.['custom-system-nvidia', 'nvidia-inference-common-code']...`
       - CM script: [add-custom-nvidia-system](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/add-custom-nvidia-system)
</details>

___
### Script output
#### New environment keys (filter)

* `CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH`
#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)