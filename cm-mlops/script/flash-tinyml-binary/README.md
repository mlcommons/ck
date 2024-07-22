**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/flash-tinyml-binary).**



Automatically generated README for this automation recipe: **flash-tinyml-binary**

Category: **TinyML automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=flash-tinyml-binary,98913babb43f4fcb) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/flash-tinyml-binary)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *flash,tiny,mlperf,mlcommons*
* Output cached? *False*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "flash tiny mlperf mlcommons" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=flash,tiny,mlperf,mlcommons`

`cm run script --tags=flash,tiny,mlperf,mlcommons[,variations] [--input_flags]`

*or*

`cmr "flash tiny mlperf mlcommons"`

`cmr "flash tiny mlperf mlcommons [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'flash,tiny,mlperf,mlcommons'
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

```cmr "cm gui" --script="flash,tiny,mlperf,mlcommons"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=flash,tiny,mlperf,mlcommons) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "flash tiny mlperf mlcommons[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_NRF`
      - Workflow:
    * `_NUCLEO`
      - Workflow:
    * `_ad`
      - Workflow:
    * `_cmsis_nn`
      - Workflow:
    * `_ic`
      - Workflow:
    * `_kws`
      - Workflow:
    * `_native`
      - Workflow:
    * `_vww`
      - Workflow:

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--build_dir=value`  &rarr;  `CM_TINY_BUILD_DIR=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "build_dir":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `r1.0`

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/flash-tinyml-binary/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,zephyr
       * CM names: `--adr.['zephyr']...`
       - CM script: [get-zephyr](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr)
     * get,zephyr-sdk
       * CM names: `--adr.['zephyr-sdk']...`
       - CM script: [get-zephyr-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr-sdk)
     * reproduce,tiny,mlperf
       * `if (CM_TINY_BUILD_DIR  != on)`
       - CM script: [reproduce-mlperf-octoml-tinyml-results](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/flash-tinyml-binary/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/flash-tinyml-binary/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/flash-tinyml-binary/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/flash-tinyml-binary/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/flash-tinyml-binary/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/flash-tinyml-binary/_cm.json)

___
### Script output
`cmr "flash tiny mlperf mlcommons [,variations]" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
