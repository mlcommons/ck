**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-android-sdk).**



Automatically generated README for this automation recipe: **get-android-sdk**

Category: **Detection or installation of tools and artifacts**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-android-sdk,8c5b4b83d49c441a) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-android-sdk)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,android,sdk,android-sdk*
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

````cmr "get android sdk android-sdk" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,android,sdk,android-sdk`

`cm run script --tags=get,android,sdk,android-sdk [--input_flags]`

*or*

`cmr "get android sdk android-sdk"`

`cmr "get android sdk android-sdk " [--input_flags]`


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
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-android-sdk/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,java
       - CM script: [get-java](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-android-sdk/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-android-sdk/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-android-sdk/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-android-sdk/_cm.json)

___
### Script output
`cmr "get android sdk android-sdk " [--input_flags] -j`
#### New environment keys (filter)

* `+PATH`
* `ANDROID_HOME`
* `ANDROID_NDK_HOME`
* `CM_ANDROID_HOME`
#### New environment keys auto-detected from customize

* `CM_ANDROID_HOME`