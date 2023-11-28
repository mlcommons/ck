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
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About


See extra [notes](README-extra.md) from the authors and contributors.

#### Summary

* Category: *Detection or installation of tools and artifacts.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-android-sdk)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,android,sdk,android-sdk*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,android,sdk,android-sdk [--input_flags]`

2. `cmr "get android sdk android-sdk" [--input_flags]`

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

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


#### Run this script via GUI

```cmr "cm gui" --script="get,android,sdk,android-sdk"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,android,sdk,android-sdk) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get android sdk android-sdk" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--android_cmake_version=value`  &rarr;  `CM_ANDROID_CMAKE_VERSION=value`
* `--android_ndk_version=value`  &rarr;  `CM_ANDROID_NDK_VERSION=value`
* `--android_version=value`  &rarr;  `CM_ANDROID_VERSION=value`
* `--build_tools_version=value`  &rarr;  `CM_ANDROID_BUILD_TOOLS_VERSION=value`
* `--cmdline_tools_version=value`  &rarr;  `CM_ANDROID_CMDLINE_TOOLS_VERSION=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "android_cmake_version":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_ANDROID_BUILD_TOOLS_VERSION: `29.0.3`
* CM_ANDROID_CMAKE_VERSION: `3.6.4111459`
* CM_ANDROID_CMDLINE_TOOLS_URL: `https://dl.google.com/android/repository/commandlinetools-${CM_ANDROID_CMDLINE_TOOLS_OS}-${CM_ANDROID_CMDLINE_TOOLS_VERSION}_latest.zip`
* CM_ANDROID_CMDLINE_TOOLS_VERSION: `9123335`
* CM_ANDROID_NDK_VERSION: `21.3.6528147`
* CM_ANDROID_VERSION: `30`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

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
</details>

___
### Script output
`cmr "get android sdk android-sdk" [--input_flags] -j`
#### New environment keys (filter)

* `+PATH`
* `ANDROID_HOME`
* `ANDROID_NDK_HOME`
* `CM_ANDROID_HOME`
#### New environment keys auto-detected from customize

* `CM_ANDROID_HOME`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)