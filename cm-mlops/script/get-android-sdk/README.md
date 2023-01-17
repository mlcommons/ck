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
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* Category: *Detection or installation of tools and artifacts.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-android-sdk)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,android,sdk,android-sdk*
* Output cached?: *True*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=get,android,sdk,android-sdk(,variations from below) (flags from below)`

*or*

`cm run script "get android sdk android-sdk (variations from below)" (flags from below)`

*or*

`cm run script 8c5b4b83d49c441a`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

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

</details>

#### CM modular Docker container
*TBD*
___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* --**android_cmake_version**=value --> **CM_ANDROID_CMAKE_VERSION**=value
* --**android_ndk_version**=value --> **CM_ANDROID_NDK_VERSION**=value
* --**android_version**=value --> **CM_ANDROID_VERSION**=value
* --**build_tools_version**=value --> **CM_ANDROID_BUILD_TOOLS_VERSION**=value
* --**cmdline_tools_version**=value --> **CM_ANDROID_CMDLINE_TOOLS_VERSION**=value

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "android_cmake_version":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.

* CM_ANDROID_BUILD_TOOLS_VERSION: **29.0.3**
* CM_ANDROID_CMAKE_VERSION: **3.6.4111459**
* CM_ANDROID_CMDLINE_TOOLS_URL: **https://dl.google.com/android/repository/commandlinetools-${CM_ANDROID_CMDLINE_TOOLS_OS}-${CM_ANDROID_CMDLINE_TOOLS_VERSION}_latest.zip**
* CM_ANDROID_CMDLINE_TOOLS_VERSION: **9123335**
* CM_ANDROID_NDK_VERSION: **21.3.6528147**
* CM_ANDROID_VERSION: **30**

</details>

___
### Script workflow, dependencies and native scripts

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
### Script output
#### New environment keys (filter)

* **+PATH**
* **ANDROID_HOME**
* **ANDROID_NDK_HOME**
* **CM_ANDROID_HOME**
#### New environment keys auto-detected from customize

* **CM_ANDROID_HOME**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)