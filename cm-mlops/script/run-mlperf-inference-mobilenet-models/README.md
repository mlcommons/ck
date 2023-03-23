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

## Run Commands

We need to get imagenet full dataset to make image-classification submissions for MLPerf inference. Since this dataset is not publicly available via a URL please follow the instructions given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md) to download the dataset and register in CM.  

### Default tflite

#### Do a test run to detect and record the system performance for each model (about an hour runtime)

```
cm run script --tags=run,mobilenet-models,_tflite,_find-performance
```

During the run, tflite library will be installed and you can give the following answers for the prompt questions

```
Please input the desired Python library path to use.  Default is [/home/ubuntu/CM/repos/local/cache/3795df3c20b44647/inference/tools/submission]

Do you wish to build TensorFlow with ROCm support? [y/N]: N
No ROCm support will be enabled for TensorFlow.

Do you wish to build TensorFlow with CUDA support? [y/N]: N
No CUDA support will be enabled for TensorFlow.

Do you wish to download a fresh release of clang? (Experimental) [y/N]: N
Clang will not be downloaded.

Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is -Wno-sign-compare]:


Would you like to interactively configure ./WORKSPACE for Android builds? [y/N]: N
```
#### Do a full accuracy run for all the models (can take almost a day)

```
cm run script --tags=run,mobilenet-models,_tflite,_accuracy-only --results_dir=$HOME/mobilenet_results
```
#### Do a full performance run for all the models (can take almost a day)
```
cm run script --tags=run,mobilenet-models,_tflite,_performance-only --results_dir=$HOME/mobilenet_results
```

#### Generate README files for all the runs
```
cm run script --tags=run,mobilenet-models,_tflite,_populate-readme --results_dir=$HOME/mobilenet_results
```

#### Generate actual submission tree

We should use the master branch of MLCommons inference repo for the submission checker. You can use `--hw_note_extra` option to add your name to the notes.
```
cm run script --tags=generate,inference,submission --results_dir=$HOME/mobilenet_results/valid_results \
--submission_dir=$HOME/mobilenet_submission_tree --clean --infer_scenario_results=yes \
--run-checker --submitter=cTuning --adr.inference-src.version=master --hw_notes_extra="Result taken by NAME"
```

#### Push the results to GitHub repo

First create a fork of [this repo](https://github.com/ctuning/mlperf_inference_submissions_v3.0/). Then run the following command after replacing `--repo_url` with your fork URL.
```
cm run script --tags=push,github,mlperf,inference,submission --submission_dir=$HOME/mobilenet_submission_tree \
--repo_url=https://github.com/ctuning/mlperf_inference_submissions_v3.0/ \
--commit_message="Mobilenet results added"
```

Create a PR to [cTuning repo](https://github.com/ctuning/mlperf_inference_submissions_v3.0/)

### Using ARMNN with NEON

Follow the same procedure as above but for the first 3 experiment runs add `_armnn,_neon` to the tags. For example
```
cm run script --tags=run,mobilenet-models,_tflite,_armnn,_neon,_find-performance
```

`results_dir` and `submission_dir` can be the same as before as results will be going to different sub folders. 

### Using ARMNN with OpenCL
Follow the same procedure as above but for the first 3 experiment runs add `_armnn,_opencl` to the tags. For example
```
cm run script --tags=run,mobilenet-models,_tflite,_armnn,_opencl,_find-performance
```

`results_dir` and `submission_dir` can be the same as before as results will be going to different sub folders. 

#### Information

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-mobilenet-models)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *run,mobilenet,models,image-classification,mobilenet-models,mlperf,inference*
* Output cached?: *False*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help

```cm run script --help```

#### CM CLI

`cm run script --tags=run,mobilenet,models,image-classification,mobilenet-models,mlperf,inference(,variations from below) (flags from below)`

*or*

`cm run script "run mobilenet models image-classification mobilenet-models mlperf inference (variations from below)" (flags from below)`

*or*

`cm run script f21cc993a8b14a58`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,mobilenet,models,image-classification,mobilenet-models,mlperf,inference'
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

```cm run script --tags=gui --script="run,mobilenet,models,image-classification,mobilenet-models,mlperf,inference"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,mobilenet,models,image-classification,mobilenet-models,mlperf,inference) to generate CM CMD.

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


  * Group "**base-framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_tflite`** (default)
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

    * `_accuracy-only`
      - Environment variables:
        - *CM_MLPERF_FIND_PERFORMANCE_MODE*: `no`
        - *CM_MLPERF_ACCURACY_MODE*: `yes`
        - *CM_MLPERF_SUBMISSION_MODE*: `no`
      - Workflow:
    * **`_find-performance`** (default)
      - Environment variables:
        - *CM_MLPERF_FIND_PERFORMANCE_MODE*: `yes`
        - *CM_MLPERF_SUBMISSION_MODE*: `no`
      - Workflow:
    * `_performance-only`
      - Environment variables:
        - *CM_MLPERF_FIND_PERFORMANCE_MODE*: `no`
        - *CM_MLPERF_PERFORMANCE_MODE*: `yes`
        - *CM_MLPERF_SUBMISSION_MODE*: `no`
      - Workflow:
    * `_populate-readme`
      - Environment variables:
        - *CM_MLPERF_FIND_PERFORMANCE_MODE*: `no`
        - *CM_MLPERF_POPULATE_README*: `yes`
      - Workflow:
    * `_submission`
      - Environment variables:
        - *CM_MLPERF_FIND_PERFORMANCE_MODE*: `no`
        - *CM_MLPERF_SUBMISSION_MODE*: `yes`
      - Workflow:

    </details>


#### Default variations

`_all-models,_find-performance,_tflite,_tflite-default`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* --**find-performance**=value --> **CM_MLPERF_FIND_PERFORMANCE_MODE**=value
* --**no-rerun**=value --> **CM_MLPERF_NO_RERUN**=value
* --**power**=value --> **CM_MLPERF_POWER**=value
* --**results_dir**=value --> **CM_MLPERF_RESULTS_DIR**=value
* --**submission**=value --> **CM_MLPERF_SUBMISSION_MODE**=value
* --**submission_dir**=value --> **CM_MLPERF_SUBMISSION_DIR**=value

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
* CM_MLPERF_NO_RERUN: **no**
* CM_MLPERF_RUN_FP32: **yes**
* CM_MLPERF_RUN_INT8: **yes**

</details>

___
### Script workflow, dependencies and native scripts

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-mobilenet-models/_cm.json)***
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-mobilenet-models/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-mobilenet-models/_cm.json)
  1. ***Run native script if exists***
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