<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Summary](#summary)
* [Reuse this script in your project](#reuse-this-script-in-your-project)
  * [ Install CM automation language](#install-cm-automation-language)
  * [ Check CM script flags](#check-cm-script-flags)
  * [ Run this script from command line](#run-this-script-from-command-line)
  * [ Run this script from Python](#run-this-script-from-python)
  * [ Run this script via GUI](#run-this-script-via-gui)
  * [ Run this script via Docker (beta)](#run-this-script-via-docker-(beta))
* [Customization](#customization)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About

*Detect or install GCC compiler.*


See extra [notes](README-extra.md) from the authors and contributors.

#### Summary

* Category: *Compiler automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,gcc,compiler,c-compiler,cpp-compiler,get-gcc*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,gcc,compiler,c-compiler,cpp-compiler,get-gcc `

2. `cmr "get gcc compiler c-compiler cpp-compiler get-gcc" `

#### Run this script from Python

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


#### Run this script via GUI

```cmr "cm gui" --script="get,gcc,compiler,c-compiler,cpp-compiler,get-gcc"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,gcc,compiler,c-compiler,cpp-compiler,get-gcc) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get gcc compiler c-compiler cpp-compiler get-gcc" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

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
</details>

___
### Script output
`cmr "get gcc compiler c-compiler cpp-compiler get-gcc"  -j`
#### New environment keys (filter)

* `+ CFLAGS`
* `+ CXXFLAGS`
* `+ FFLAGS`
* `+ LDFLAGS`
* `+CM_HOST_OS_DEFAULT_INCLUDE_PATH`
* `+PATH`
* `CM_COMPILER_*`
* `CM_CXX_COMPILER_*`
* `CM_C_COMPILER_*`
* `CM_GCC_*`
* `CM_LINKER_*`
#### New environment keys auto-detected from customize

* `CM_COMPILER_CACHE_TAGS`
* `CM_COMPILER_FAMILY`
* `CM_COMPILER_FLAGS_DEBUG`
* `CM_COMPILER_FLAGS_DEFAULT`
* `CM_COMPILER_FLAGS_FAST`
* `CM_COMPILER_VERSION`
* `CM_CXX_COMPILER_BIN`
* `CM_CXX_COMPILER_FLAG_OUTPUT`
* `CM_CXX_COMPILER_FLAG_VERSION`
* `CM_CXX_COMPILER_WITH_PATH`
* `CM_C_COMPILER_BIN`
* `CM_C_COMPILER_FLAG_OUTPUT`
* `CM_C_COMPILER_FLAG_VERSION`
* `CM_C_COMPILER_WITH_PATH`
* `CM_GCC_BIN`
* `CM_GCC_CACHE_TAGS`
* `CM_GCC_INSTALLED_PATH`
* `CM_LINKER_FLAGS_DEBUG`
* `CM_LINKER_FLAGS_DEFAULT`
* `CM_LINKER_FLAGS_FAST`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)