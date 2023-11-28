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
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About

#### Summary

* Category: *MLPerf benchmark support.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-tiny-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,src,source,tiny,tiny-src,tiny-source,tinymlperf,tinymlperf-src,mlperf,mlcommons*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,src,source,tiny,tiny-src,tiny-source,tinymlperf,tinymlperf-src,mlperf,mlcommons `

2. `cmr "get src source tiny tiny-src tiny-source tinymlperf tinymlperf-src mlperf mlcommons" `

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,src,source,tiny,tiny-src,tiny-source,tinymlperf,tinymlperf-src,mlperf,mlcommons'
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

```cmr "cm gui" --script="get,src,source,tiny,tiny-src,tiny-source,tinymlperf,tinymlperf-src,mlperf,mlcommons"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,src,source,tiny,tiny-src,tiny-source,tinymlperf,tinymlperf-src,mlperf,mlcommons) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get src source tiny tiny-src tiny-source tinymlperf tinymlperf-src mlperf mlcommons" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GIT_CHECKOUT: `master`
* CM_GIT_PATCH: `no`
* CM_GIT_RECURSE_SUBMODULES: ``
* CM_GIT_URL: `https://github.com/mlcommons/tiny.git`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-tiny-src/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-tiny-src/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-tiny-src/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-tiny-src/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-tiny-src/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-tiny-src/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-tiny-src/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-tiny-src/_cm.json)
</details>

___
### Script output
`cmr "get src source tiny tiny-src tiny-source tinymlperf tinymlperf-src mlperf mlcommons"  -j`
#### New environment keys (filter)

* `+PYTHONPATH`
* `CM_MLPERF_TINY_*`
#### New environment keys auto-detected from customize

* `CM_MLPERF_TINY_BENCHMARK`
* `CM_MLPERF_TINY_DATASETS`
* `CM_MLPERF_TINY_DATASETS_AD`
* `CM_MLPERF_TINY_DATASETS_IC`
* `CM_MLPERF_TINY_DATASETS_KWS`
* `CM_MLPERF_TINY_DATASETS_KWS_OPEN`
* `CM_MLPERF_TINY_DATASETS_VWW`
* `CM_MLPERF_TINY_SRC`
* `CM_MLPERF_TINY_TRAINING`
* `CM_MLPERF_TINY_TRAINING_AD`
* `CM_MLPERF_TINY_TRAINING_IC`
* `CM_MLPERF_TINY_TRAINING_KWS`
* `CM_MLPERF_TINY_TRAINING_VWW`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)