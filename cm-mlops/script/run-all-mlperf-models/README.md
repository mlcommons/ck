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
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *run,natively,all,mlperf-models*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=run,natively,all,mlperf-models[,variations] `

2. `cmr "run natively all mlperf-models[ variations]" `

* `variations` can be seen [here](#variations)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,natively,all,mlperf-models'
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

```cmr "cm gui" --script="run,natively,all,mlperf-models"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,natively,all,mlperf-models) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "run natively all mlperf-models[ variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_phoenix,reference`
      - Workflow:

    </details>


  * Group "**implementation**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_deepsparse`
      - Environment variables:
        - *DIVISION*: `open`
        - *IMPLEMENTATION*: `deepsparse`
      - Workflow:
    * `_intel`
      - Environment variables:
        - *IMPLEMENTATION*: `intel`
      - Workflow:
    * `_mil`
      - Environment variables:
        - *IMPLEMENTATION*: `mil`
      - Workflow:
    * `_nvidia`
      - Environment variables:
        - *IMPLEMENTATION*: `nvidia`
      - Workflow:
    * `_qualcomm`
      - Environment variables:
        - *IMPLEMENTATION*: `qualcomm`
      - Workflow:
    * `_reference`
      - Environment variables:
        - *IMPLEMENTATION*: `reference`
      - Workflow:
    * `_tflite-cpp`
      - Environment variables:
        - *IMPLEMENTATION*: `tflite_cpp`
      - Workflow:

    </details>


  * Group "**power**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_performance-only`** (default)
      - Workflow:
    * `_power`
      - Environment variables:
        - *POWER*: `True`
      - Workflow:

    </details>


  * Group "**sut**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_macbookpro-m1`
      - Environment variables:
        - *CATEGORY*: `edge`
        - *DIVISION*: `closed`
      - Workflow:
    * `_orin.32g`
      - Environment variables:
        - *CATEGORY*: `edge`
        - *DIVISION*: `closed`
      - Workflow:
    * `_phoenix`
      - Environment variables:
        - *CATEGORY*: `edge,datacenter`
        - *DIVISION*: `closed`
      - Workflow:
    * `_sapphire-rapids.24c`
      - Environment variables:
        - *CATEGORY*: `edge,datacenter`
        - *DIVISION*: `closed`
      - Workflow:

    </details>


#### Default variations

`_performance-only`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/_cm.yaml)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/_cm.yaml)
  1. ***Run native script if exists***
     * [run-bert-macos.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/run-bert-macos.sh)
     * [run-bert.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/run-bert.sh)
     * [run-cpp-implementation.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/run-cpp-implementation.sh)
     * [run-mobilenet-models.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/run-mobilenet-models.sh)
     * [run-nvidia-4090.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/run-nvidia-4090.sh)
     * [run-nvidia-a100.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/run-nvidia-a100.sh)
     * [run-nvidia-t4.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/run-nvidia-t4.sh)
     * [run-pruned-bert.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/run-pruned-bert.sh)
     * [run-reference-models.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/run-reference-models.sh)
     * [run-resnet50-macos.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/run-resnet50-macos.sh)
     * [run-resnet50.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/run-resnet50.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-all-mlperf-models/_cm.yaml)
</details>

___
### Script output
`cmr "run natively all mlperf-models[,variations]"  -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)