**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/build-mlperf-inference-server-nvidia).**



Automatically generated README for this automation recipe: **build-mlperf-inference-server-nvidia**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=build-mlperf-inference-server-nvidia,f37403af5e9f4541) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-mlperf-inference-server-nvidia)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *build,mlcommons,mlperf,inference,inference-server,server,nvidia-harness,nvidia*
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

````cmr "build mlcommons mlperf inference inference-server server nvidia-harness nvidia" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=build,mlcommons,mlperf,inference,inference-server,server,nvidia-harness,nvidia`

`cm run script --tags=build,mlcommons,mlperf,inference,inference-server,server,nvidia-harness,nvidia[,variations] [--input_flags]`

*or*

`cmr "build mlcommons mlperf inference inference-server server nvidia-harness nvidia"`

`cmr "build mlcommons mlperf inference inference-server server nvidia-harness nvidia [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

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


#### Run this script via GUI

```cmr "cm gui" --script="build,mlcommons,mlperf,inference,inference-server,server,nvidia-harness,nvidia"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=build,mlcommons,mlperf,inference,inference-server,server,nvidia-harness,nvidia) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "build mlcommons mlperf inference inference-server server nvidia-harness nvidia[variations]" [--input_flags]`

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
* CM_CUSTOM_SYSTEM_NVIDIA: `yes`

</details>

#### Versions
Default version: `r3.1`

* `r2.1`
* `r3.0`
* `r3.1`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-mlperf-inference-server-nvidia/_cm.yaml)***
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
     * get,generic-python-lib,_package.pybind11
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
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
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-mlperf-inference-server-nvidia/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-mlperf-inference-server-nvidia/_cm.yaml)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-mlperf-inference-server-nvidia/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-mlperf-inference-server-nvidia/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-mlperf-inference-server-nvidia/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-mlperf-inference-server-nvidia/_cm.yaml)***
     * add,custom,system,nvidia
       * `if (CM_CUSTOM_SYSTEM_NVIDIA not in ['no', False, 'False'])`
       * CM names: `--adr.['custom-system-nvidia', 'nvidia-inference-common-code']...`
       - CM script: [add-custom-nvidia-system](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/add-custom-nvidia-system)

___
### Script output
`cmr "build mlcommons mlperf inference inference-server server nvidia-harness nvidia [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH`
#### New environment keys auto-detected from customize
