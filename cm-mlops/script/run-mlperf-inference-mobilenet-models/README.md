<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM GUI](#cm-gui)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! Use `README-extra.md` to add more info.*

### Description

#### Information

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-mobilenet-models)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *run,mobilenet,image-classification,mobilenet-models,mlperf,inference*
* Output cached?: *False*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help

```cm run script --help```

#### CM CLI

`cm run script --tags=run,mobilenet,image-classification,mobilenet-models,mlperf,inference(,variations from below) (flags from below)`

*or*

`cm run script "run mobilenet image-classification mobilenet-models mlperf inference (variations from below)" (flags from below)`

*or*

`cm run script f21cc993a8b14a58`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,mobilenet,image-classification,mobilenet-models,mlperf,inference'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>


#### CM GUI

```cm run script --tags=gui --script="run,mobilenet,image-classification,mobilenet-models,mlperf,inference"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,mobilenet,image-classification,mobilenet-models,mlperf,inference) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_armnn`
      - Environment variables:
        - *CM_MLPERF_USE_ARMNN_LIBRARY*: `yes`
      - Workflow:
    * `_neon`
      - Environment variables:
        - *CM_MLPERF_USE_NEON*: `yes`
      - Workflow:
    * `_only-fp32`
      - Environment variables:
        - *CM_MLPERF_RUN_INT8*: `no`
      - Workflow:
    * `_only-int8`
      - Environment variables:
        - *CM_MLPERF_RUN_FP32*: `no`
      - Workflow:
    * `_opencl`
      - Environment variables:
        - *CM_MLPERF_USE_OPENCL*: `yes`
      - Workflow:
    * `_tflite,armnn`
      - Environment variables:
        - *CM_MLPERF_TFLITE_ARMNN*: `yes`
      - Workflow:
    * `_tflite,armnn,neon`
      - Environment variables:
        - *CM_MLPERF_TFLITE_ARMNN_NEON*: `yes`
      - Workflow:
    * `_tflite,armnn,opencl`
      - Environment variables:
        - *CM_MLPERF_TFLITE_ARMNN_OPENCL*: `yes`
      - Workflow:

    </details>


  * Group "**model-selection**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_all-models`** (default)
      - Environment variables:
        - *CM_MLPERF_RUN_MOBILENETS*: `yes`
        - *CM_MLPERF_RUN_EFFICIENTNETS*: `yes`
      - Workflow:
    * `_efficientnet`
      - Environment variables:
        - *CM_MLPERF_RUN_EFFICIENTNETS*: `yes`
      - Workflow:
    * `_mobilenet`
      - Environment variables:
        - *CM_MLPERF_RUN_MOBILENETS*: `yes`
      - Workflow:

    </details>


  * Group "**optimization**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_tflite-default`** (default)
      - Environment variables:
        - *CM_MLPERF_TFLITE_DEFAULT_MODE*: `yes`
      - Workflow:

    </details>


  * Group "**run-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_find-performance`** (default)
      - Environment variables:
        - *CM_MLPERF_FIND_PERFORMANCE_MODE*: `yes`
        - *CM_MLPERF_SUBMISSION_MODE*: `no`
      - Workflow:
    * `_submission`
      - Environment variables:
        - *CM_MLPERF_FIND_PERFORMANCE_MODE*: `no`
        - *CM_MLPERF_SUBMISSION_MODE*: `yes`
      - Workflow:

    </details>


#### Default variations

`_all-models,_find-performance,_tflite-default`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* --**find-performance**=value --> **CM_MLPERF_FIND_PERFORMANCE_MODE**=value
* --**results_dir**=value --> **CM_MLPERF_RESULTS_DIR**=value
* --**submission**=value --> **CM_MLPERF_SUBMISSION_MODE**=value

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "find-performance":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.

* CM_MLPERF_RUN_MOBILENETS: **no**
* CM_MLPERF_RUN_EFFICIENTNETS: **no**
* CM_MLPERF_RUN_FP32: **yes**
* CM_MLPERF_RUN_INT8: **yes**
* CM_MLPERF_FIND_PERFORMANCE_MODE: **yes**

</details>

___
### Script workflow, dependencies and native scripts

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-mobilenet-models/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-mobilenet-models/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-mobilenet-models/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-mobilenet-models/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-mobilenet-models/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-mobilenet-models/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-mobilenet-models/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-mobilenet-models/_cm.json)
___
### Script output
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)