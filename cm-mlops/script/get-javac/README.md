*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Variations](#variations)
  * [ All variations](#all-variations)
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
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-javac)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,javac

___
### Variations
#### All variations
* install
  - *ENV CM_JAVAC_PREBUILT_INSTALL: on*
___
### Default environment

* CM_JAVAC_PREBUILT_VERSION: **19**
* CM_JAVAC_PREBUILT_BUILD: **36**
* CM_JAVAC_PREBUILT_URL: **https://download.java.net/openjdk/jdk${CM_JAVAC_PREBUILT_VERSION}/ri/**
* CM_JAVAC_PREBUILT_FILENAME: **openjdk-${CM_JAVAC_PREBUILT_VERSION}+${CM_JAVAC_PREBUILT_BUILD}_${CM_JAVAC_PREBUILT_HOST_OS}-x64_bin**
___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-javac/_cm.json)***
     * detect,os
       - CM script [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-javac/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-javac/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-javac/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-javac/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-javac/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-javac/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-javac/_cm.json)
___
### New environment export

* **+PATH**
* **CM_JAVAC_***
* **CM_JAVA_***
* **JAVA_HOME**
___
### New environment detected from customize

* **CM_JAVAC_BIN**
* **CM_JAVAC_CACHE_TAGS**
* **CM_JAVA_BIN**
* **CM_JAVA_BIN**
* **CM_JAVA_BIN_WITH_PATH**
* **JAVA_HOME**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="get,javac"`

*or*

`cm run script "get javac"`

*or*

`cm run script 509280c497b24226`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,javac'
                  'out':'con'})

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*

#### Script input flags mapped to environment

* install --> **CM_JAVAC_PREBUILT_INSTALL**

Examples:

```bash
cm run script "get javac" --install=...
```
```python
r=cm.access({... , "install":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)