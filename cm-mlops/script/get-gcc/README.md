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
* [New environment keys](#new-environment-keys)
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description

*Detect or install GCC compiler.*


See [more info](README-extra.md).

#### Information

* Category: *Compiler automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,gcc,compiler,c-compiler,cpp-compiler,get-gcc*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=get,gcc,compiler,c-compiler,cpp-compiler,get-gcc(,variations from below) (flags from below)`

*or*

`cm run script "get gcc compiler c-compiler cpp-compiler get-gcc (variations from below)" (flags from below)`

*or*

`cm run script dbf4ab5cbed74372`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,gcc,compiler,c-compiler,cpp-compiler,get-gcc'
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

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc/_cm.json)***
     * get,compiler-flags
       - CM script: [get-compiler-flags](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-compiler-flags)
___
### Script output
#### New environment keys

* **+ CFLAGS**
* **+ CXXFLAGS**
* **+ FFLAGS**
* **+ LDFLAGS**
* **+CM_HOST_OS_DEFAULT_INCLUDE_PATH**
* **+PATH**
* **CM_COMPILER_***
* **CM_CXX_COMPILER_***
* **CM_C_COMPILER_***
* **CM_GCC_***
* **CM_LINKER_***
#### New environment keys auto-detected from customize

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
* **CM_GCC_BIN**
* **CM_GCC_CACHE_TAGS**
* **CM_GCC_INSTALLED_PATH**
* **CM_LINKER_FLAGS_DEBUG**
* **CM_LINKER_FLAGS_DEFAULT**
* **CM_LINKER_FLAGS_FAST**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)