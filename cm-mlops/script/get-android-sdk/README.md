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
  * [ Script input flags mapped to environment](#script-input-flags-mapped-to-environment)
* [Maintainers](#maintainers)

</details>

___
### About

*TBD*
___
### Category

Detection or installation of tools and artifacts.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-android-sdk)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,android,sdk,android-sdk

___
### Default environment

* CM_ANDROID_BUILD_TOOLS_VERSION: **29.0.3**
* CM_ANDROID_CMAKE_VERSION: **3.6.4111459**
* CM_ANDROID_CMDLINE_TOOLS_URL: **https://dl.google.com/android/repository/commandlinetools-${CM_ANDROID_CMDLINE_TOOLS_OS}-${CM_ANDROID_CMDLINE_TOOLS_VERSION}_latest.zip**
* CM_ANDROID_CMDLINE_TOOLS_VERSION: **9123335**
* CM_ANDROID_NDK_VERSION: **21.3.6528147**
* CM_ANDROID_VERSION: **30**
___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-android-sdk/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,java
       - CM script: [get-java](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-android-sdk/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-android-sdk/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-android-sdk/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-android-sdk/_cm.json)
___
### New environment export

* **+PATH**
* **ANDROID_HOME**
* **ANDROID_NDK_HOME**
* **CM_ANDROID_HOME**
___
### New environment detected from customize

* **CM_ANDROID_BUILD_TOOLS_PATH**
* **CM_ANDROID_CMAKE_PATH**
* **CM_ANDROID_CMDLINE_TOOLS_URL**
* **CM_ANDROID_CMDLINE_TOOLS_VERSION**
* **CM_ANDROID_EMULATOR_PATH**
* **CM_ANDROID_HOME**
* **CM_ANDROID_LLVM_CLANG_BIN_WITH_PATH**
* **CM_ANDROID_LLVM_PATH**
* **CM_ANDROID_NDK_PATH**
* **CM_ANDROID_PLATFORMS_PATH**
* **CM_ANDROID_PLATFORM_TOOLS_PATH**
* **CM_ANDROID_SDK_MANAGER_BIN**
* **CM_ANDROID_SDK_MANAGER_BIN_WITH_PATH**
* **CM_ANDROID_TOOLS_PATH**
* **CM_GET_DEPENDENT_CACHED_PATH**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="get,android,sdk,android-sdk"`

*or*

`cm run script "get android sdk android-sdk"`

*or*

`cm run script 8c5b4b83d49c441a`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,android,sdk,android-sdk'
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

#### Script input flags mapped to environment

* android_cmake_version --> **CM_ANDROID_CMAKE_VERSION**
* android_ndk_version --> **CM_ANDROID_NDK_VERSION**
* android_version --> **CM_ANDROID_VERSION**
* build_tools_version --> **CM_ANDROID_BUILD_TOOLS_VERSION**
* cmdline_tools_version --> **CM_ANDROID_CMDLINE_TOOLS_VERSION**

Examples:

```bash
cm run script "get android sdk android-sdk" --android_cmake_version=...
```
```python
r=cm.access({... , "android_cmake_version":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)