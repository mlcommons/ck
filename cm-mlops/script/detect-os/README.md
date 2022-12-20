*This README is automatically generated - don't edit! Use `README-extra.md` for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Default environment](#default-environment)
* [CM script workflow](#cm-script-workflow)
* [New environment export](#new-environment-export)
* [New environment detected from customize](#new-environment-detected-from-customize)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Maintainers](#maintainers)

</details>

___
### About

*TBD*
___
### Category

Platform information.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
detect-os,detect,os,info

___
### Default environment

___
### CM script workflow

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/_cm.json)***
     * get,sys-utils-min
       - CM script [get-sys-utils-min](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-min)
___
### New environment export

* **+CM_HOST_OS_***
* **+PATH**
* **CM_HOST_OS_***
* **CM_HOST_PLATFORM_***
* **CM_HOST_PYTHON_***
* **CM_HOST_SYSTEM_NAME**
___
### New environment detected from customize

* **+CM_HOST_OS_DEFAULT_LIBRARY_PATH**
* **CM_HOST_OS_MACHINE**
* **CM_HOST_OS_PACKAGE_MANAGER**
* **CM_HOST_OS_PACKAGE_MANAGER**
* **CM_HOST_OS_PACKAGE_MANAGER**
* **CM_HOST_OS_PACKAGE_MANAGER**
* **CM_HOST_OS_PACKAGE_MANAGER_INSTALL_CMD**
* **CM_HOST_OS_PACKAGE_MANAGER_INSTALL_CMD**
* **CM_HOST_OS_PACKAGE_MANAGER_INSTALL_CMD**
* **CM_HOST_OS_PACKAGE_MANAGER_INSTALL_CMD**
* **CM_HOST_OS_PACKAGE_MANAGER_UPDATE_CMD**
* **CM_HOST_OS_PACKAGE_MANAGER_UPDATE_CMD**
* **CM_HOST_OS_PACKAGE_MANAGER_UPDATE_CMD**
* **CM_HOST_OS_PACKAGE_MANAGER_UPDATE_CMD**
* **CM_HOST_SYSTEM_NAME**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="detect-os,detect,os,info"`

*or*

`cm run script "detect-os detect os info"`

*or*

`cm run script 863735b7db8c44fc`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'detect-os,detect,os,info'
                  'out':'con'})

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)