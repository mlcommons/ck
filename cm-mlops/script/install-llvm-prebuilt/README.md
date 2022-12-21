*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Versions](#versions)
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

Install prebuilt LLVM compiler.

See [extra README](README-extra.md).

___
### Category

Compiler automation.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
install,prebuilt,llvm,prebuilt-llvm,install-prebuilt-llvm

___
### Versions
Default version: *14.0.0*

___
### Default environment

___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt/_cm.json)
  1. Run "postrocess" function from customize.py
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt/_cm.json)***
     * get,llvm
       * `if (CM_REQUIRE_INSTALL != ['yes'])`
       - CM script: [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)
___
### New environment export

* **+C_INCLUDE_PATH**
* **+LD_LIBRARY_PATH**
* **+PATH**
* **CM_GET_DEPENDENT_CACHED_PATH**
* **CM_LLVM_***
___
### New environment detected from customize

* **CM_GET_DEPENDENT_CACHED_PATH**
* **CM_LLVM_CLANG_BIN_WITH_PATH**
* **CM_LLVM_INSTALLED_PATH**
* **CM_LLVM_PACKAGE**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="install,prebuilt,llvm,prebuilt-llvm,install-prebuilt-llvm"`

*or*

`cm run script "install prebuilt llvm prebuilt-llvm install-prebuilt-llvm"`

*or*

`cm run script cda9094971724a0a`

#### CM Python API

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

#### CM modular Docker container
*TBD*
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)