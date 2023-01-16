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
  * [ Variations](#variations)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys](#new-environment-keys)
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* Category: *Detection or installation of tools and artifacts.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,java*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=get,java(,variations from below) (flags from below)`

*or*

`cm run script "get java (variations from below)" (flags from below)`

*or*

`cm run script 9399d0e785704f8c`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,java'
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

* --**install**=value --> **CM_JAVA_PREBUILT_INSTALL**=value

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "install":"..."}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.

* CM_JAVA_PREBUILT_VERSION: **19**
* CM_JAVA_PREBUILT_BUILD: **36**
* CM_JAVA_PREBUILT_URL: **https://download.java.net/openjdk/jdk${CM_JAVA_PREBUILT_VERSION}/ri/**
* CM_JAVA_PREBUILT_FILENAME: **openjdk-${CM_JAVA_PREBUILT_VERSION}+${CM_JAVA_PREBUILT_BUILD}_${CM_JAVA_PREBUILT_HOST_OS}-x64_bin**

</details>


#### Variations

  * *No group (any variation can be selected)*
<details>
<summary>Click here to expand this section.</summary>

    * `_install`
      - Environment variables:
        - *CM_JAVA_PREBUILT_INSTALL*: `on`
      - Workflow:

</details>

___
### Script workflow, dependencies and native scripts

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java/_cm.json)
___
### Script output
#### New environment keys

* **+PATH**
* **CM_JAVA_***
* **JAVA_HOME**
#### New environment keys auto-detected from customize

* **CM_JAVA_BIN**
* **CM_JAVA_CACHE_TAGS**
* **CM_JAVA_PREBUILT_EXT**
* **CM_JAVA_PREBUILT_FILENAME**
* **CM_JAVA_PREBUILT_HOST_OS**
* **CM_JAVA_PREBUILT_URL**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)