*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

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

Microsoft C compiler.

See [extra README](README-extra.md).

___
### Category

Compiler automation.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,cl,compiler,c-compiler,cpp-compiler,get-cl

___
### Default environment

___
### CM script workflow

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl/run.bat)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl/_cm.json)
___
### New environment export

* **+PATH**
* **CM_CL_***
* **CM_COMPILER_***
* **CM_CXX_COMPILER_***
* **CM_C_COMPILER_***
* **CM_LINKER_***
___
### New environment detected from customize

* **CM_CL_BIN**
* **CM_CL_BIN_WITH_PATH**
* **CM_CL_CACHE_TAGS**
* **CM_COMPILER_CACHE_TAGS**
* **CM_COMPILER_FAMILY**
* **CM_COMPILER_VERSION**
* **CM_CXX_COMPILER_BIN**
* **CM_CXX_COMPILER_FLAG_OUTPUT**
* **CM_CXX_COMPILER_FLAG_VERSION**
* **CM_CXX_COMPILER_WITH_PATH**
* **CM_C_COMPILER_BIN**
* **CM_C_COMPILER_FLAG_OUTPUT**
* **CM_C_COMPILER_FLAG_VERSION**
* **CM_C_COMPILER_WITH_PATH**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="get,cl,compiler,c-compiler,cpp-compiler,get-cl"`

*or*

`cm run script "get cl compiler c-compiler cpp-compiler get-cl"`

*or*

`cm run script 7dbb770faff947c0`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,cl,compiler,c-compiler,cpp-compiler,get-cl'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)