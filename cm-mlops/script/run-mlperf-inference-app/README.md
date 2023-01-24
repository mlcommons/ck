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
being developed by the open [MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md).

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

#### CM script automation help

```cm run script --help```

#### CM CLI

`cm run script --tags=run,generate-run-cmds,run-mlperf,vision,mlcommons,mlperf,inference,reference(,variations from below) (flags from below)`

*or*

`cm run script "run generate-run-cmds run-mlperf vision mlcommons mlperf inference reference (variations from below)" (flags from below)`

*or*

`cm run script 4a5d5b13fd7e4ac8`

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

    * `_all-modes`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_ALL_MODES*: `yes`
      - Workflow:
    * `_all-scenarios`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_ALL_SCENARIOS*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,sut,description
             - CM script: [get-mlperf-inference-sut-description](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description)
    * `_compliance`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_COMPLIANCE*: `yes`
      - Workflow:
    * `_dashboard`
      - Environment variables:
        - *CM_MLPERF_DASHBOARD*: `on`
      - Workflow:
    * `_fast`
      - Environment variables:
        - *CM_FAST_FACTOR*: `5`
        - *CM_OUTPUT_FOLDER_NAME*: `fast_results`
        - *CM_MLPERF_RUN_STYLE*: `fast`
      - Workflow:
    * `_short`
      - Workflow:
    * `_submission`
      - Environment variables:
        - *CM_MLPERF_SUBMISSION_RUN*: `yes`
        - *CM_RUN_SUBMISSION_CHECKER*: `yes`
        - *CM_TAR_SUBMISSION_DIR*: `yes`
        - *CM_RUN_MLPERF_ACCURACY*: `on`
      - Workflow:
        1. ***Read "post_deps" on other CM scripts***
           * get,sut,description
             - CM script: [get-mlperf-inference-sut-description](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description)
           * generate,mlperf,inference,submission
             * CM names: `--adr.['submission-generator']...`
             - CM script: [generate-mlperf-inference-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission)
    * `_valid`
      - Environment variables:
        - *CM_OUTPUT_FOLDER_NAME*: `valid_results`
        - *CM_MLPERF_RUN_STYLE*: `valid`
        - *CM_RUN_MLPERF_ACCURACY*: `on`
      - Workflow:

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* --**backend**=value --> **CM_MLPERF_BACKEND**=value
* --**clean**=value --> **CM_MLPERF_CLEAN_ALL**=value
* --**device**=value --> **CM_MLPERF_DEVICE**=value
* --**execution_mode**=value --> **CM_MLPERF_EXECUTION_MODE**=value
* --**hw_name**=value --> **CM_HW_NAME**=value
* --**imagenet_path**=value --> **IMAGENET_PATH**=value
* --**implementation**=value --> **CM_MLPERF_IMPLEMENTATION**=value
* --**lang**=value --> **CM_MLPERF_IMPLEMENTATION**=value
* --**max_batchsize**=value --> **CM_MLPERF_LOADGEN_MAX_BATCHSIZE**=value
* --**mode**=value --> **CM_MLPERF_LOADGEN_MODE**=value
* --**model**=value --> **CM_MLPERF_MODEL**=value
* --**multistream_target_latency**=value --> **CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY**=value
* --**new_tvm_model**=value --> **CM_MLPERF_DELETE_COMPILED_MODEL**=value
* --**num_threads**=value --> **CM_NUM_THREADS**=value
* --**offline_target_qps**=value --> **CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS**=value
* --**output_dir**=value --> **OUTPUT_BASE_DIR**=value
* --**power**=value --> **CM_SYSTEM_POWER**=value
* --**precision**=value --> **CM_MLPERF_MODEL_PRECISION**=value
* --**regenerate_files**=value --> **CM_REGENERATE_MEASURE_FILES**=value
* --**rerun**=value --> **CM_RERUN**=value
* --**results_dir**=value --> **OUTPUT_BASE_DIR**=value
* --**run_checker**=value --> **CM_RUN_SUBMISSION_CHECKER**=value
* --**run_style**=value --> **CM_MLPERF_EXECUTION_MODE**=value
* --**scenario**=value --> **CM_MLPERF_LOADGEN_SCENARIO**=value
* --**server_target_qps**=value --> **CM_MLPERF_LOADGEN_SERVER_TARGET_QPS**=value
* --**singlestream_target_latency**=value --> **CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY**=value
* --**skip_truncation**=value --> **CM_SKIP_TRUNCATE_ACCURACY**=value
* --**submission_dir**=value --> **CM_MLPERF_SUBMISSION_DIR**=value
* --**submitter**=value --> **CM_MLPERF_SUBMITTER**=value
* --**target_latency**=value --> **CM_MLPERF_LOADGEN_TARGET_LATENCY**=value
* --**target_qps**=value --> **CM_MLPERF_LOADGEN_TARGET_QPS**=value
* --**test_query_count**=value --> **CM_TEST_QUERY_COUNT**=value

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "backend":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.

* CM_BATCH_COUNT: **1**
* CM_BATCH_SIZE: **1**
* CM_OUTPUT_FOLDER_NAME: **test_results**
* CM_MLPERF_RUN_STYLE: **test**
* CM_TEST_QUERY_COUNT: **5**

</details>

#### Versions
* master
* r2.1
___
### Script workflow, dependencies and native scripts

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
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app/_cm.json)
___
### Script output
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)