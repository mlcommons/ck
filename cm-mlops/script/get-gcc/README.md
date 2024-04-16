**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-gcc).**



Automatically generated README for this automation recipe: **get-gcc**

Category: **Compiler automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-gcc,dbf4ab5cbed74372) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-gcc)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,gcc,compiler,c-compiler,cpp-compiler,get-gcc*
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

````cmr "get gcc compiler c-compiler cpp-compiler get-gcc" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,gcc,compiler,c-compiler,cpp-compiler,get-gcc`

`cm run script --tags=get,gcc,compiler,c-compiler,cpp-compiler,get-gcc `

*or*

`cmr "get gcc compiler c-compiler cpp-compiler get-gcc"`

`cmr "get gcc compiler c-compiler cpp-compiler get-gcc " `


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
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-gcc/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-gcc/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-gcc/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-gcc/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-gcc/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-gcc/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-gcc/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-gcc/_cm.json)***
     * get,compiler-flags
       - CM script: [get-compiler-flags](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-compiler-flags)

___
### Script output
`cmr "get gcc compiler c-compiler cpp-compiler get-gcc "  -j`
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