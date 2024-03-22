Automatically generated README for this automation recipe: **get-target-device**

Category: **Hardware automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-target-device,3709c39c71b84492) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-target-device)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *get,target,device,target-device*
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

````cmr "get target device target-device" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,target,device,target-device`

`cm run script --tags=get,target,device,target-device[,variations] `

*or*

`cmr "get target device target-device"`

`cmr "get target device target-device [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,target,device,target-device'
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

```cmr "cm gui" --script="get,target,device,target-device"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,target,device,target-device) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get target device target-device[variations]" `

___
### Customization


#### Variations

  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_TARGET_DEVICE_ENV_TYPE*: `cpu`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *CM_TARGET_DEVICE_ENV_TYPE*: `cuda`
      - Workflow:

    </details>


#### Default variations

`_cpu`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-target-device/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,cuda,_toolkit
       * `if (CM_TARGET_DEVICE_ENV_TYPE  == cuda)`
       * CM names: `--adr.['get-cuda', '46d133d9ef92422d']...`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
     * get,cuda-devices
       * `if (CM_TARGET_DEVICE_ENV_TYPE  == cuda)`
       * CM names: `--adr.['get-cuda-devices', '46d133d9ef92422d']...`
       - CM script: [get-cuda-devices](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-devices)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-target-device/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-target-device/_cm.yaml)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-target-device/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-target-device/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-target-device/_cm.yaml)

___
### Script output
`cmr "get target device target-device [,variations]"  -j`
#### New environment keys (filter)

* `+ LDFLAGS`
* `+CPLUS_INCLUDE_PATH`
* `+C_INCLUDE_PATH`
* `+DYLD_FALLBACK_LIBRARY_PATH`
* `+LD_LIBRARY_PATH`
* `+PATH`
* `CM_CUDA_*`
* `CM_HOST_*`
* `CM_NVCC_*`
* `CM_TARGET_*`
* `CUDA_HOME*`
#### New environment keys auto-detected from customize

* `CM_TARGET_DEVICE_PATH`