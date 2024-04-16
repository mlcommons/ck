**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/install-llvm-prebuilt).**



Automatically generated README for this automation recipe: **install-llvm-prebuilt**

Category: **Compiler automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=install-llvm-prebuilt,cda9094971724a0a) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-prebuilt)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *install,prebuilt,llvm,prebuilt-llvm,install-prebuilt-llvm*
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

````cmr "install prebuilt llvm prebuilt-llvm install-prebuilt-llvm" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=install,prebuilt,llvm,prebuilt-llvm,install-prebuilt-llvm`

`cm run script --tags=install,prebuilt,llvm,prebuilt-llvm,install-prebuilt-llvm `

*or*

`cmr "install prebuilt llvm prebuilt-llvm install-prebuilt-llvm"`

`cmr "install prebuilt llvm prebuilt-llvm install-prebuilt-llvm " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,prebuilt,llvm,prebuilt-llvm,install-prebuilt-llvm'
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

```cmr "cm gui" --script="install,prebuilt,llvm,prebuilt-llvm,install-prebuilt-llvm"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=install,prebuilt,llvm,prebuilt-llvm,install-prebuilt-llvm) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "install prebuilt llvm prebuilt-llvm install-prebuilt-llvm" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `15.0.6`

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-prebuilt/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-prebuilt/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-prebuilt/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-prebuilt/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-prebuilt/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-prebuilt/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-prebuilt/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-prebuilt/_cm.json)***
     * get,llvm
       * `if (CM_REQUIRE_INSTALL  != yes)`
       - CM script: [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)

___
### Script output
`cmr "install prebuilt llvm prebuilt-llvm install-prebuilt-llvm "  -j`
#### New environment keys (filter)

* `+CPLUS_INCLUDE_PATH`
* `+C_INCLUDE_PATH`
* `+LD_LIBRARY_PATH`
* `+PATH`
* `CM_COMPILER_NAME`
* `CM_LLVM_*`
#### New environment keys auto-detected from customize

* `CM_LLVM_CLANG_BIN_WITH_PATH`
* `CM_LLVM_INSTALLED_PATH`
* `CM_LLVM_PACKAGE`