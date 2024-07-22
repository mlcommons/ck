**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-mlperf-octoml-tinyml-results).**



Automatically generated README for this automation recipe: **reproduce-mlperf-octoml-tinyml-results**

Category: **Reproduce MLPerf benchmarks**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=reproduce-mlperf-octoml-tinyml-results,a63803a707d04332) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *reproduce,tiny,results,mlperf,octoml,mlcommons*
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

````cmr "reproduce tiny results mlperf octoml mlcommons" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=reproduce,tiny,results,mlperf,octoml,mlcommons`

`cm run script --tags=reproduce,tiny,results,mlperf,octoml,mlcommons[,variations] [--input_flags]`

*or*

`cmr "reproduce tiny results mlperf octoml mlcommons"`

`cmr "reproduce tiny results mlperf octoml mlcommons [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

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

</details>


#### Run this script via GUI

```cmr "cm gui" --script="reproduce,tiny,results,mlperf,octoml,mlcommons"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=reproduce,tiny,results,mlperf,octoml,mlcommons) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "reproduce tiny results mlperf octoml mlcommons[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_NRF`
      - Environment variables:
        - *CM_TINY_BOARD*: `NRF5340DK`
      - Workflow:
    * `_NUCLEO`
      - Environment variables:
        - *CM_TINY_BOARD*: `NUCLEO_L4R5ZI`
      - Workflow:
    * `_ad`
      - Environment variables:
        - *CM_TINY_MODEL*: `ad`
      - Workflow:
    * `_cmsis_nn`
      - Environment variables:
        - *CM_MICROTVM_VARIANT*: `microtvm_cmsis_nn`
      - Workflow:
    * `_ic`
      - Environment variables:
        - *CM_TINY_MODEL*: `ic`
      - Workflow:
    * `_kws`
      - Environment variables:
        - *CM_TINY_MODEL*: `kws`
      - Workflow:
    * `_native`
      - Environment variables:
        - *CM_MICROTVM_VARIANT*: `microtvm_native`
      - Workflow:
    * `_vww`
      - Environment variables:
        - *CM_TINY_MODEL*: `vww`
      - Workflow:

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--flash=value`  &rarr;  `CM_FLASH_BOARD=value`
* `--recreate_binary=value`  &rarr;  `CM_RECREATE_BINARY=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "flash":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `r1.0`

* `r1.0`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/_cm.json)***
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
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/_cm.json)***
     * flash,tiny,mlperf
       * `if (CM_FLASH_BOARD  == True)`
       - CM script: [flash-tinyml-binary](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary)

___
### Script output
`cmr "reproduce tiny results mlperf octoml mlcommons [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_TINY_*`
#### New environment keys auto-detected from customize

* `CM_TINY_MODEL`