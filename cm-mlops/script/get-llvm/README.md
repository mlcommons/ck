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

LLVM compiler.

See [extra README](README-extra.md).

___
### Category

Compiler automation.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,llvm,compiler,c-compiler,cpp-compiler,get-llvm

___
### Default environment

___
### CM script workflow

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm/_cm.json)***
     * install,llvm
       * `if (CM_REQUIRE_INSTALL == ['yes'])`
       - CM script: [install-llvm-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt)
       - CM script: [install-llvm-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-src)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm/_cm.json)***
     * get,compiler-flags
       - CM script: [get-compiler-flags](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-compiler-flags)
___
### New environment export

* **+ CFLAGS**
* **+ CXXFLAGS**
* **+ FFLAGS**
* **+ LDFLAGS**
* **+CM_HOST_OS_DEFAULT_INCLUDE_PATH**
* **+PATH**
* **CM_COMPILER_***
* **CM_CXX_COMPILER_***
* **CM_C_COMPILER_***
* **CM_LINKER_***
* **CM_LLVM_***
___
### New environment detected from customize

* **CM_COMPILER_CACHE_TAGS**
* **CM_COMPILER_FAMILY**
* **CM_COMPILER_FLAGS_DEBUG**
* **CM_COMPILER_FLAGS_DEFAULT**
* **CM_COMPILER_FLAGS_FAST**
* **CM_COMPILER_VERSION**
* **CM_CXX_COMPILER_BIN**
* **CM_CXX_COMPILER_FLAG_OUTPUT**
* **CM_CXX_COMPILER_FLAG_VERSION**
* **CM_CXX_COMPILER_WITH_PATH**
* **CM_C_COMPILER_BIN**
* **CM_C_COMPILER_FLAG_OUTPUT**
* **CM_C_COMPILER_FLAG_VERSION**
* **CM_C_COMPILER_WITH_PATH**
* **CM_LINKER_FLAGS_DEBUG**
* **CM_LINKER_FLAGS_DEFAULT**
* **CM_LINKER_FLAGS_FAST**
* **CM_LLVM_CLANG_BIN**
* **CM_LLVM_CLANG_CACHE_TAGS**
* **CM_REQUIRE_INSTALL**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="get,llvm,compiler,c-compiler,cpp-compiler,get-llvm"`

*or*

`cm run script "get llvm compiler c-compiler cpp-compiler get-llvm"`

*or*

`cm run script 99832a103ed04eb8`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,llvm,compiler,c-compiler,cpp-compiler,get-llvm'
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