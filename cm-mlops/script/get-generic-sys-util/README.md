**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-generic-sys-util).**



Automatically generated README for this automation recipe: **get-generic-sys-util**

Category: **Detection or installation of tools and artifacts**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-generic-sys-util,bb0393afa8404a11) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-sys-util)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,sys-util,generic,generic-sys-util*
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

````cmr "get sys-util generic generic-sys-util" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,sys-util,generic,generic-sys-util`

`cm run script --tags=get,sys-util,generic,generic-sys-util[,variations] `

*or*

`cmr "get sys-util generic generic-sys-util"`

`cmr "get sys-util generic generic-sys-util [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

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


#### Run this script via GUI

```cmr "cm gui" --script="get,sys-util,generic,generic-sys-util"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,sys-util,generic,generic-sys-util) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get sys-util generic generic-sys-util[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_g++-12`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `g++12`
      - Workflow:
    * `_gflags-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `gflags-dev`
      - Workflow:
    * `_git-lfs`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `git-lfs`
      - Workflow:
    * `_glog-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `glog-dev`
      - Workflow:
    * `_libboost-all-dev`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libboost-all-dev`
      - Workflow:
    * `_libffi7`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `libffi7`
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
    * `_ninja-build`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `ninja-build`
      - Workflow:
    * `_ntpdate`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `ntpdate`
      - Workflow:
    * `_numactl`
      - Environment variables:
        - *CM_SYS_UTIL_NAME*: `numactl`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * install,numactl,from.src
             * `if (CM_HOST_OS_FLAVOR  == rhel AND CM_HOST_OS_VERSION in ['9.1', '9.2', '9.3'])`
             - CM script: [install-numactl-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-numactl-from-src)
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
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-sys-util/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-sys-util/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-sys-util/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-sys-util/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-sys-util/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-sys-util/_cm.json)

___
### Script output
`cmr "get sys-util generic generic-sys-util [,variations]"  -j`
#### New environment keys (filter)

* `+PATH`
#### New environment keys auto-detected from customize
