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

## Set up

We need to get imagenet full dataset to make image-classification submissions for MLPerf inference. Since this dataset is not publicly available via a URL please follow the instructions given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md) to download the dataset and register in CM.  

<details>
<summary>Click here to set up docker (Optional).</summary>

### Docker Setup

CM commands are expected to run natively but if you prefer not to modify the host system, you can do the below command to set up a docker container. 

```
cm docker script --tags=run,mobilenet-models,_tflite,_accuracy-only \
--adr.compiler.tags=gcc  \
--docker_cm_repo=mlcommons@ck \
--imagenet_path=$HOME/imagenet-2012-val \
--results_dir=$HOME/mobilenet_results \
--submission_dir=$HOME/inference_submission_3.1 \
--docker_skip_run_cmd
```

This command will build a docker container and give you an interactive shell from which you can execute the below CM run commands.
* `results_dir`, `submission_dir` and `imagenet_path` are mounted from the host system.
* `results_dir` and `submission_dir` are expected to be empty directories to be populated by the docker
* `imagenet_path` should point to the imagenet folder containing the 50000 validation images.

</details>

## Run Commands

### Default tflite


#### Do a full accuracy run for all the models (can take almost a day)

```
cmr "run mobilenet-models _tflite _accuracy-only" \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results
```


#### Do a full performance run for all the models (can take almost a day)
```
cmr "run mobilenet-models _tflite _performance-only" \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results 
```

#### Generate README files for all the runs
```
cmr "run mobilenet-models _tflite _populate-readme" \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results
```

#### Generate actual submission tree

We should use the master branch of MLCommons inference repo for the submission checker. You can use `--hw_note_extra` option to add your name to the notes.
```
cmr "generate inference submission" \
--results_dir=$HOME/mobilenet_results/valid_results \
--submission_dir=$HOME/mobilenet_submission_tree \
--clean \
--infer_scenario_results=yes \
--adr.compiler.tags=gcc --adr.inference-src.version=master \
--run-checker \
--submitter=cTuning \
--hw_notes_extra="Result taken by NAME" 
```

#### Push the results to GitHub repo

First, create a fork of [this repo](https://github.com/ctuning/mlperf_inference_submissions_v3.1/). Then run the following command after replacing `--repo_url` with your fork URL.
```
cmr "push github mlperf inference submission" \
--submission_dir=$HOME/mobilenet_submission_tree \
--repo_url=https://github.com/ctuning/mlperf_inference_submissions_v3.1/ \
--commit_message="Mobilenet results added"
```

Create a PR to [cTuning repo](https://github.com/ctuning/mlperf_inference_submissions_v3.1/)

### Using ARMNN with NEON

Follow the same procedure as above but for the first three experiment runs add `_armnn,_neon` to the tags. For example
```
cmr "run mobilenet-models _tflite _armnn _neon _accuracy-only" \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results
```

`results_dir` and `submission_dir` can be the same as before as results will be going to different subfolders. 

### Using ARMNN with OpenCL
Follow the same procedure as above but for the first three experiment runs add `_armnn,_opencl` to the tags. For example
```
cmr "run mobilenet-models _tflite _armnn _opencl _accuracy-only" \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results
```

`results_dir` and `submission_dir` can be the same as before as results will be going to different subfolders. 

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

##### CM pull repository

```cm pull repo mlcommons@ck```

##### CM script automation help

```cm run script --help```

#### CM CLI

1. `cm run script --tags=run,mobilenet,models,image-classification,mobilenet-models,mlperf,inference[,variations] [--input_flags]`

2. `cm run script "run mobilenet models image-classification mobilenet-models mlperf inference[,variations]" [--input_flags]`

3. `cm run script f21cc993a8b14a58 [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

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
    * `_find-performance`
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

`_all-models,_tflite,_tflite-default`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--find-performance=value`  &rarr;  `CM_MLPERF_FIND_PERFORMANCE_MODE=value`
* `--imagenet_path=value`  &rarr;  `IMAGENET_PATH=value`
* `--no-rerun=value`  &rarr;  `CM_MLPERF_NO_RERUN=value`
* `--power=value`  &rarr;  `CM_MLPERF_POWER=value`
* `--results_dir=value`  &rarr;  `CM_MLPERF_RESULTS_DIR=value`
* `--submission=value`  &rarr;  `CM_MLPERF_SUBMISSION_MODE=value`
* `--submission_dir=value`  &rarr;  `CM_MLPERF_SUBMISSION_DIR=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "find-performance":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MLPERF_RUN_MOBILENETS: `no`
* CM_MLPERF_RUN_EFFICIENTNETS: `no`
* CM_MLPERF_NO_RERUN: `no`
* CM_MLPERF_RUN_FP32: `yes`
* CM_MLPERF_RUN_INT8: `yes`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

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
</details>

___
### Script output
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
