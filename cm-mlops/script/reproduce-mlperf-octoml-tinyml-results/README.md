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
  * [ Script input flags mapped to environment](#script-input-flags-mapped-to-environment)
* [Maintainers](#maintainers)

</details>

___
### About

*TBD*
___
### Category

Modular MLPerf benchmarks.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
reproduce,tiny,results,mlperf,octoml,mlcommons

___
### Variations
#### All variations
* NRF
  - *ENV CM_TINY_BOARD*: `NRF5340DK`
* NUCLEO
  - *ENV CM_TINY_BOARD*: `NUCLEO_L4R5ZI`
* ad
  - *ENV CM_TINY_MODEL*: `ad`
* cmsis_nn
  - *ENV CM_MICROTVM_VARIANT*: `microtvm_cmsis_nn`
* ic
  - *ENV CM_TINY_MODEL*: `ic`
* kws
  - *ENV CM_TINY_MODEL*: `kws`
* native
  - *ENV CM_MICROTVM_VARIANT*: `microtvm_native`
* vww
  - *ENV CM_TINY_MODEL*: `vww`
___
### Versions
Default version: *r1.0*

* r1.0
___
### Default environment

___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,python3
       * CM names: `--adr.['python3', 'python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,zephyr
       * CM names: `--adr.['zephyr']...`
       - CM script: [get-zephyr](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr)
     * get,zephyr-sdk
       * CM names: `--adr.['zephyr-sdk']...`
       - CM script: [get-zephyr-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr-sdk)
     * get,cmsis
       * CM names: `--adr.['cmsis']...`
       - CM script: [get-cmsis_5](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmsis_5)
     * get,microtvm
       * CM names: `--adr.['microtvm']...`
       - CM script: [get-microtvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-microtvm)
     * get,cmake
       * CM names: `--adr.['cmake']...`
       - CM script: [get-cmake](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)
     * get,gcc
       - CM script: [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/_cm.json)***
     * flash,tiny,mlperf
       * `if (CM_FLASH_BOARD == ['True'])`
       - CM script: [flash-tinyml-binary](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary)
___
### New environment export

* **CM_TINY_***
___
### New environment detected from customize

* **CM_MICROTVM_VARIANT**
* **CM_TINY_MODEL**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="reproduce,tiny,results,mlperf,octoml,mlcommons"`

*or*

`cm run script "reproduce tiny results mlperf octoml mlcommons"`

*or*

`cm run script a63803a707d04332`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,tiny,results,mlperf,octoml,mlcommons'
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

* flash --> **CM_FLASH_BOARD**
* recreate_binary --> **CM_RECREATE_BINARY**

Examples:

```bash
cm run script "reproduce tiny results mlperf octoml mlcommons" --flash=...
```
```python
r=cm.access({... , "flash":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)