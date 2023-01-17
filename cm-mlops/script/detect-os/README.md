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
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! Use `README-extra.md` to add more info.*

### Description

#### Information

* Category: *Platform information.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *detect-os,detect,os,info*
* Output cached?: *False*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=detect-os,detect,os,info(,variations from below) (flags from below)`

*or*

`cm run script "detect-os detect os info (variations from below)" (flags from below)`

*or*

`cm run script 863735b7db8c44fc`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'detect-os,detect,os,info'
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


</details>

___
### Script workflow, dependencies and native scripts

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
       * `if (CM_HOST_OS_TYPE  == windows)`
       - CM script: [get-sys-utils-min](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-min)
___
### Script output
#### New environment keys (filter)

* **+CM_HOST_OS_***
* **+PATH**
* **CM_HOST_OS_***
* **CM_HOST_PLATFORM_***
* **CM_HOST_PYTHON_***
* **CM_HOST_SYSTEM_NAME**
#### New environment keys auto-detected from customize

* **CM_HOST_OS_BITS**
* **CM_HOST_OS_MACHINE**
* **CM_HOST_OS_PACKAGE_MANAGER**
* **CM_HOST_OS_PACKAGE_MANAGER_INSTALL_CMD**
* **CM_HOST_OS_PACKAGE_MANAGER_UPDATE_CMD**
* **CM_HOST_OS_TYPE**
* **CM_HOST_PYTHON_BITS**
* **CM_HOST_SYSTEM_NAME**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)