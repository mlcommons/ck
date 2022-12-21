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

*TBD*
___
### Category

Application automation.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
compile,program,c-program,cpp-program,compile-program,compile-c-program,compile-cpp-program

___
### Default environment

___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program/_cm.json)***
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,compiler
       * CM names: `--adr.['compiler']...`
       - CM script: [get-cl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl)
       - CM script: [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)
       - CM script: [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program/_cm.json)
___
### New environment export

___
### New environment detected from customize

* **CM_CPLUS_INCLUDE_PATH**
* **CM_CXX_COMPILER_FLAGS**
* **CM_CXX_LINKER_FLAGS**
* **CM_C_COMPILER_FLAGS**
* **CM_C_INCLUDE_PATH**
* **CM_C_LINKER_FLAGS**
* **CM_F_COMPILER_FLAGS**
* **CM_F_INCLUDE_PATH**
* **CM_F_LINKER_FLAGS**
* **CM_LD_LIBRARY_PATH**
* **CM_LINKER_BIN**
* **CM_LINKER_COMPILE_FLAGS**
* **CM_LINKER_FLAGS**
* **CM_LINKER_WITH_PATH**
* **CM_SOURCE_FOLDER_PATH**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="compile,program,c-program,cpp-program,compile-program,compile-c-program,compile-cpp-program"`

*or*

`cm run script "compile program c-program cpp-program compile-program compile-c-program compile-cpp-program"`

*or*

`cm run script c05042ba005a4bfa`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'compile,program,c-program,cpp-program,compile-program,compile-c-program,compile-cpp-program'
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