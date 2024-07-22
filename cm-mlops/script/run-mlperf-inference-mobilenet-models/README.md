**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-inference-mobilenet-models).**



Automatically generated README for this automation recipe: **run-mlperf-inference-mobilenet-models**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=run-mlperf-inference-mobilenet-models,f21cc993a8b14a58) ]*

---

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

Since the runs can take many hours, in case you are running remotely you can install screen as follows. You may omit "screen" from all commands if you are running on a host system.
```
cmr "get generic-sys-util _screen"
```
### Default tflite


#### Do a full accuracy run for all the models (can take almost a day)

```
screen cmr "run mobilenet-models _tflite _accuracy-only" \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results
```

#### Do a full performance run for all the models (can take almost a day)
```
screen cmr "run mobilenet-models _tflite _performance-only" \
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
* Use `--hw_name="My system name"` to give a meaningful system name. Examples can be seen [here](https://github.com/mlcommons/inference_results_v3.0/tree/main/open/cTuning/systems)

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


---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-mobilenet-models)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *run,mobilenet,models,image-classification,mobilenet-models,mlperf,inference*
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

````cmr "run mobilenet models image-classification mobilenet-models mlperf inference" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=run,mobilenet,models,image-classification,mobilenet-models,mlperf,inference`

`cm run script --tags=run,mobilenet,models,image-classification,mobilenet-models,mlperf,inference[,variations] [--input_flags]`

*or*

`cmr "run mobilenet models image-classification mobilenet-models mlperf inference"`

`cmr "run mobilenet models image-classification mobilenet-models mlperf inference [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

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


#### Run this script via GUI

```cmr "cm gui" --script="run,mobilenet,models,image-classification,mobilenet-models,mlperf,inference"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,mobilenet,models,image-classification,mobilenet-models,mlperf,inference) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "run mobilenet models image-classification mobilenet-models mlperf inference[variations]" [--input_flags]`

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
      - Aliases: `_use-neon`
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
* `--results_dir=value`  &rarr;  `CM_MLPERF_INFERENCE_RESULTS_DIR=value`
* `--submission=value`  &rarr;  `CM_MLPERF_SUBMISSION_MODE=value`
* `--submission_dir=value`  &rarr;  `CM_MLPERF_INFERENCE_SUBMISSION_DIR=value`

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
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-mobilenet-models/_cm.json)***
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-mobilenet-models/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-mobilenet-models/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-mobilenet-models/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-mobilenet-models/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-mobilenet-models/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-mobilenet-models/_cm.json)

___
### Script output
`cmr "run mobilenet models image-classification mobilenet-models mlperf inference [,variations]" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
