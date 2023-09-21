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
  * [ Input description](#input-description)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Versions](#versions)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description

This portable CM (CK2) script provides a unified and portable interface to the MLPerf inference benchmark 
modularized by other [portable CM scripts](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md)
being developed by the open [MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md).

It is a higher-level wrapper that automatically generates the command line for the [universal MLPerf inference script](../app-mlperf-inference)
to run MLPerf scenarios for a given ML task, model, runtime and device, and prepare and validate submissions.

Check these [tutorials](https://github.com/mlcommons/ck/blob/master/docs/tutorials/sc22-scc-mlperf.md) from the Student Cluster Competition
at Supercomputing'22 to understand how to use this script to run the MLPerf inference benchmark and automate submissions.

See the development roadmap [here](https://github.com/mlcommons/ck/issues/536).

See extension projects to enable collaborative benchmarking, design space exploration and optimization of ML and AI Systems [here](https://github.com/mlcommons/ck/issues/627).


See [more info](README-extra.md).

#### Information

* Category: *Modular MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *run,generate-run-cmds,run-mlperf,vision,mlcommons,mlperf,inference,reference*
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

1. `cm run script --tags=run,generate-run-cmds,run-mlperf,vision,mlcommons,mlperf,inference,reference[,variations] [--input_flags]`

2. `cm run script "run generate-run-cmds run-mlperf vision mlcommons mlperf inference reference[,variations]" [--input_flags]`

3. `cm run script 4a5d5b13fd7e4ac8 [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,generate-run-cmds,run-mlperf,vision,mlcommons,mlperf,inference,reference'
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

```cm run script --tags=gui --script="run,generate-run-cmds,run-mlperf,vision,mlcommons,mlperf,inference,reference"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,generate-run-cmds,run-mlperf,vision,mlcommons,mlperf,inference,reference) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_all-scenarios`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_ALL_SCENARIOS*: `yes`
      - Workflow:
    * `_compliance`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_COMPLIANCE*: `yes`
      - Workflow:
    * `_dashboard`
      - Environment variables:
        - *CM_MLPERF_DASHBOARD*: `on`
      - Workflow:

    </details>


  * Group "**mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_all-modes`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_ALL_MODES*: `yes`
      - Workflow:

    </details>


  * Group "**reproducibility**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_r2.1`
      - Environment variables:
        - *CM_MLPERF_INFERENCE_APP_DEFAULTS*: `r2.1_default`
      - Workflow:
    * `_r3.0`
      - Environment variables:
        - *CM_MLPERF_INFERENCE_APP_DEFAULTS*: `r3.0_default`
      - Workflow:
    * **`_r3.1`** (default)
      - Environment variables:
        - *CM_MLPERF_INFERENCE_APP_DEFAULTS*: `r3.1_default`
      - Workflow:
    * `_r4.0`
      - Environment variables:
        - *CM_MLPERF_INFERENCE_APP_DEFAULTS*: `r4.0_default`
      - Workflow:

    </details>


  * Group "**submission-generation**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_accuracy-only`
      - Environment variables:
        - *CM_MLPERF_SUBMISSION_RUN*: `yes`
        - *CM_MLPERF_LOADGEN_MODE*: `accuracy`
        - *CM_RUN_SUBMISSION_CHECKER*: `no`
        - *CM_RUN_MLPERF_ACCURACY*: `on`
      - Workflow:
    * **`_find-performance`** (default)
      - Environment variables:
        - *CM_MLPERF_LOADGEN_ALL_MODES*: `no`
        - *CM_MLPERF_LOADGEN_MODE*: `performance`
        - *CM_MLPERF_FIND_PERFORMANCE_MODE*: `yes`
        - *CM_MLPERF_RESULT_PUSH_TO_GITHUB*: `False`
      - Workflow:
    * `_performance-only`
      - Environment variables:
        - *CM_MLPERF_SUBMISSION_RUN*: `yes`
        - *CM_MLPERF_LOADGEN_MODE*: `performance`
        - *CM_RUN_SUBMISSION_CHECKER*: `no`
      - Workflow:
    * `_populate-readme`
      - Environment variables:
        - *CM_MLPERF_SUBMISSION_RUN*: `yes`
        - *CM_MLPERF_README*: `yes`
        - *CM_RUN_SUBMISSION_CHECKER*: `no`
      - Workflow:
    * `_submission`
      - Environment variables:
        - *CM_MLPERF_SUBMISSION_RUN*: `yes`
        - *CM_RUN_SUBMISSION_CHECKER*: `yes`
        - *CM_MLPERF_LOADGEN_COMPLIANCE*: `yes`
        - *CM_TAR_SUBMISSION_DIR*: `yes`
        - *CM_RUN_MLPERF_ACCURACY*: `on`
      - Workflow:
        1. ***Read "post_deps" on other CM scripts***
           * generate,mlperf,inference,submission
             * `if (CM_MLPERF_SKIP_SUBMISSION_GENERATION not in ['yes', 'True'])`
             * CM names: `--adr.['submission-generator']...`
             - CM script: [generate-mlperf-inference-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission)

    </details>


  * Group "**submission-generation-style**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_full`
      - Environment variables:
        - *CM_MLPERF_SUBMISSION_GENERATION_STYLE*: `full`
      - Workflow:
    * **`_short`** (default)
      - Environment variables:
        - *CM_MLPERF_SUBMISSION_GENERATION_STYLE*: `short`
      - Workflow:

    </details>


#### Default variations

`_find-performance,_r3.1,_short`

#### Input description

* --**adr.python.name** Python virtual environment name (optional) (*mlperf*)
* --**adr.python.version_min** Minimal Python version (*3.8*)
* --**adr.python.version** Force Python version (must have all system deps)
* --**adr.compiler.tags** Compiler for loadgen and any C/C++ part of implementation (*gcc*)
* --**adr.inference-src-loadgen.env.CM_GIT_URL** Git URL for MLPerf inference sources to build LoadGen (to enable non-reference implementations)
* --**adr.inference-src.env.CM_GIT_URL** Git URL for MLPerf inference sources to run benchmarks (to enable non-reference implementations)
* --**submitter** Submitter name (without space) (*TheCommunity*)
* --**implementation** MLPerf implementation {reference,cpp,nvidia-original,tflite-cpp} (*reference*)
* --**compliance** Whether to run compliance tests (applicable only for closed division) {yes,no} (*yes*)
* --**model** MLPerf model {resnet50,retinanet,bert-99,bert-99.9,3d-unet,rnnt} (*resnet50*)
* --**precision** MLPerf model precision {fp32,int8}
* --**backend** MLPerf backend {onnxruntime,tf,pytorch,deepsparse,tensorrt,tvm-onnx} (*onnxruntime*)
* --**hw_name** MLPerf hardware name (from [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description/hardware)) (*default*)
* --**device** MLPerf device {cpu,cuda} (*cpu*)
* --**scenario** MLPerf scenario {Offline,Server,SingleStream,MultiStream} (*Offline*)
* --**mode** MLPerf mode {,accuracy,performance}
* --**execution_mode** Execution mode {test,fast,valid} (*test*)
* --**adr.mlperf-inference-implementation.max_batchsize** Maximum batchsize to be used
* --**adr.mlperf-inference-implementation.num_threads** Number of threads (reference&C++ implementation only)
* --**target_qps** Set LoadGen target QPS
* --**offline_target_qps** Set LoadGen Offline target QPS
* --**server_target_qps** Set Server target QPS
* --**target_latency** Set Target latency
* --**singlestream_target_latency** Set SingleStream target latency
* --**multistream_target_latency** Set MultiStream target latency
* --**results_dir** Folder path where run results should be stored (defaults to the current working directory)
* --**submission_dir** Folder path where submission tree (to be submitted) must be stored
* --**dashboard_wb_user** W&B dashboard user (*cmind*)
* --**dashboard_wb_project** W&B dashboard project (*cm-mlperf-dse-testing*)
* --**clean** Clean run (*True*)
* --**quiet** Quiet run (select default values for all questions) (*False*)

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "adr.python.name":...}
```

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--backend=value`  &rarr;  `CM_MLPERF_BACKEND=value`
* `--category=value`  &rarr;  `CM_MLPERF_SUBMISSION_SYSTEM_TYPE=value`
* `--clean=value`  &rarr;  `CM_MLPERF_CLEAN_ALL=value`
* `--compliance=value`  &rarr;  `CM_MLPERF_LOADGEN_COMPLIANCE=value`
* `--dashboard_wb_project=value`  &rarr;  `CM_MLPERF_DASHBOARD_WANDB_PROJECT=value`
* `--dashboard_wb_user=value`  &rarr;  `CM_MLPERF_DASHBOARD_WANDB_USER=value`
* `--debug=value`  &rarr;  `CM_DEBUG_SCRIPT_BENCHMARK_PROGRAM=value`
* `--device=value`  &rarr;  `CM_MLPERF_DEVICE=value`
* `--division=value`  &rarr;  `CM_MLPERF_SUBMISSION_DIVISION=value`
* `--execution_mode=value`  &rarr;  `CM_MLPERF_EXECUTION_MODE=value`
* `--find_performance=value`  &rarr;  `CM_MLPERF_FIND_PERFORMANCE_MODE=value`
* `--gpu_name=value`  &rarr;  `CM_NVIDIA_GPU_NAME=value`
* `--hw_name=value`  &rarr;  `CM_HW_NAME=value`
* `--hw_notes_extra=value`  &rarr;  `CM_MLPERF_SUT_SW_NOTES_EXTRA=value`
* `--implementation=value`  &rarr;  `CM_MLPERF_IMPLEMENTATION=value`
* `--lang=value`  &rarr;  `CM_MLPERF_IMPLEMENTATION=value`
* `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
* `--model=value`  &rarr;  `CM_MLPERF_MODEL=value`
* `--multistream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY=value`
* `--offline_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS=value`
* `--output_dir=value`  &rarr;  `OUTPUT_BASE_DIR=value`
* `--power=value`  &rarr;  `CM_SYSTEM_POWER=value`
* `--precision=value`  &rarr;  `CM_MLPERF_MODEL_PRECISION=value`
* `--preprocess_submission=value`  &rarr;  `CM_RUN_MLPERF_SUBMISSION_PREPROCESSOR=value`
* `--push_to_github=value`  &rarr;  `CM_MLPERF_RESULT_PUSH_TO_GITHUB=value`
* `--readme=value`  &rarr;  `CM_MLPERF_README=value`
* `--regenerate_files=value`  &rarr;  `CM_REGENERATE_MEASURE_FILES=value`
* `--rerun=value`  &rarr;  `CM_RERUN=value`
* `--results_dir=value`  &rarr;  `OUTPUT_BASE_DIR=value`
* `--results_git_url=value`  &rarr;  `CM_MLPERF_RESULTS_GIT_REPO_URL=value`
* `--run_checker=value`  &rarr;  `CM_RUN_SUBMISSION_CHECKER=value`
* `--run_style=value`  &rarr;  `CM_MLPERF_EXECUTION_MODE=value`
* `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
* `--server_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_SERVER_TARGET_QPS=value`
* `--singlestream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY=value`
* `--skip_submission_generation=value`  &rarr;  `CM_MLPERF_SKIP_SUBMISSION_GENERATION=value`
* `--skip_truncation=value`  &rarr;  `CM_SKIP_TRUNCATE_ACCURACY=value`
* `--submission_dir=value`  &rarr;  `CM_MLPERF_SUBMISSION_DIR=value`
* `--submitter=value`  &rarr;  `CM_MLPERF_SUBMITTER=value`
* `--sw_notes_extra=value`  &rarr;  `CM_MLPERF_SUT_SW_NOTES_EXTRA=value`
* `--system_type=value`  &rarr;  `CM_MLPERF_SUBMISSION_SYSTEM_TYPE=value`
* `--target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_LATENCY=value`
* `--target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_QPS=value`
* `--test_query_count=value`  &rarr;  `CM_TEST_QUERY_COUNT=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "backend":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_OUTPUT_FOLDER_NAME: `test_results`
* CM_MLPERF_RUN_STYLE: `test`
* CM_MLPERF_IMPLEMENTATION: `reference`
* CM_MLPERF_MODEL: `resnet50`

</details>

#### Versions
* `master`
* `r2.1`
___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,sut,description
       - CM script: [get-mlperf-inference-sut-description](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app/_cm.json)
</details>

___
### Script output
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)