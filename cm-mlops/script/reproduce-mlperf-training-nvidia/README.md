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
  * [ Variations](#variations)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Versions](#versions)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About

#### Summary

* Category: *Reproduce MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-training-nvidia)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *reproduce,mlcommons,mlperf,train,training,nvidia-training,nvidia*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=reproduce,mlcommons,mlperf,train,training,nvidia-training,nvidia[,variations] [--input_flags]`

2. `cmr "reproduce mlcommons mlperf train training nvidia-training nvidia[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,mlcommons,mlperf,train,training,nvidia-training,nvidia'
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

```cmr "cm gui" --script="reproduce,mlcommons,mlperf,train,training,nvidia-training,nvidia"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=reproduce,mlcommons,mlperf,train,training,nvidia-training,nvidia) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "reproduce mlcommons mlperf train training nvidia-training nvidia[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * Group "**benchmark**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_resnet`
      - Environment variables:
        - *CM_MLPERF_TRAINING_BENCHMARK*: `resnet`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * prepare,mlperf,training,resnet,_nvidia
             * CM names: `--adr.['prepare-training-data', 'nvidia-training-data']...`
             - CM script: [prepare-training-data-resnet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prepare-training-data-resnet)
           * get,nvidia,training,code
             * CM names: `--adr.['nvidia-training-code']...`
             - CM script: [get-mlperf-training-nvidia-code](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-nvidia-code)

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--results_dir=value`  &rarr;  `CM_MLPERF_RESULTS_DIR=value`
* `--system_conf_name=value`  &rarr;  `CM_MLPERF_NVIDIA_TRAINING_SYSTEM_CONF_NAME=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "results_dir":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
* `r2.1`
* `r3.0`
___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-training-nvidia/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,nvidia-docker
       - CM script: [get-nvidia-docker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-nvidia-docker)
     * get,cuda
       * CM names: `--adr.['cuda']...`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-training-nvidia/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-training-nvidia/_cm.yaml)
  1. ***Run native script if exists***
     * [run-resnet.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-training-nvidia/run-resnet.sh)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-training-nvidia/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-training-nvidia/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-training-nvidia/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-training-nvidia/_cm.yaml)
</details>

___
### Script output
`cmr "reproduce mlcommons mlperf train training nvidia-training nvidia[,variations]" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)