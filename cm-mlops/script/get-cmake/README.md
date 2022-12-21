*This README is automatically generated - don't edit! Use `README-extra.md` for extra notes!*

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
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,cmake,get-cmake

___
### Default environment

___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake/_cm.json)***
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake/_cm.json)***
     * install,cmake,prebuilt
       * `if (CM_REQUIRE_INSTALL == ['yes'])`
       - CM script: [install-cmake-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cmake-prebuilt)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake/_cm.json)
___
### New environment export

* **+PATH**
* **CM_CMAKE_***
* **CM_MAKE_CORES**
___
### New environment detected from customize

* **CM_CMAKE_CACHE_TAGS**
* **CM_MAKE_CORES**
* **CM_REQUIRE_INSTALL**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="get,cmake,get-cmake"`

*or*

`cm run script "get cmake get-cmake"`

*or*

`cm run script 52bf974d791b4fc8`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,cmake,get-cmake'
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