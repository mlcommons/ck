**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-inference-app).**



Automatically generated README for this automation recipe: **run-mlperf-inference-app**

Category: **Modular MLPerf inference benchmark pipeline**

License: **Apache 2.0**

Developers: [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh), [Grigori Fursin](https://cKnowledge.org/gfursin)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=run-mlperf-inference-app,4a5d5b13fd7e4ac8) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-app)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *run-mlperf,inference*
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

````cmr "run-mlperf,inference" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=run-mlperf,inference`

`cm run script --tags=run-mlperf,inference[,variations] [--input_flags]`

*or*

`cmr "run-mlperf,inference"`

`cmr "run-mlperf,inference [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*


#### Input Flags

* --**division**=MLPerf division {open,closed} (*open*)
* --**category**=MLPerf category {edge,datacenter,network} (*edge*)
* --**device**=MLPerf device {cpu,cuda,rocm,qaic} (*cpu*)
* --**model**=MLPerf model {resnet50,retinanet,bert-99,bert-99.9,3d-unet-99,3d-unet-99.9,rnnt,dlrm-v2-99,dlrm-v2-99.9,gptj-99,gptj-99.9,sdxl,llama2-70b-99,llama2-70b-99.9,mobilenet,efficientnet} (*resnet50*)
* --**precision**=MLPerf model precision {float32,float16,bfloat16,int8,uint8}
* --**implementation**=MLPerf implementation {mlcommons-python,mlcommons-cpp,nvidia,intel,qualcomm,ctuning-cpp-tflite} (*mlcommons-python*)
* --**backend**=MLPerf framework (backend) {onnxruntime,tf,pytorch,deepsparse,tensorrt,glow,tvm-onnx} (*onnxruntime*)
* --**scenario**=MLPerf scenario {Offline,Server,SingleStream,MultiStream} (*Offline*)
* --**mode**=MLPerf benchmark mode {,accuracy,performance}
* --**execution_mode**=MLPerf execution mode {test,fast,valid} (*test*)
* --**sut**=SUT configuration (if known)
* --**submitter**=Submitter name (without space) (*CTuning*)
* --**results_dir**=Folder path to store results (defaults to the current working directory)
* --**submission_dir**=Folder path to store MLPerf submission tree
* --**adr.compiler.tags**=Compiler for loadgen and any C/C++ part of implementation
* --**adr.inference-src-loadgen.env.CM_GIT_URL**=Git URL for MLPerf inference sources to build LoadGen (to enable non-reference implementations)
* --**adr.inference-src.env.CM_GIT_URL**=Git URL for MLPerf inference sources to run benchmarks (to enable non-reference implementations)
* --**adr.mlperf-inference-implementation.max_batchsize**=Maximum batchsize to be used
* --**adr.mlperf-inference-implementation.num_threads**=Number of threads (reference & C++ implementation only)
* --**adr.python.name**=Python virtual environment name (optional)
* --**adr.python.version**=Force Python version (must have all system deps)
* --**adr.python.version_min**=Minimal Python version (*3.8*)
* --**power**=Measure power {yes,no} (*no*)
* --**adr.mlperf-power-client.power_server**=MLPerf Power server IP address (*192.168.0.15*)
* --**adr.mlperf-power-client.port**=MLPerf Power server port (*4950*)
* --**clean**=Clean run (*False*)
* --**compliance**=Whether to run compliance tests (applicable only for closed division) {yes,no} (*no*)
* --**dashboard_wb_project**=W&B dashboard project (*cm-mlperf-dse-testing*)
* --**dashboard_wb_user**=W&B dashboard user (*cmind*)
* --**hw_name**=MLPerf hardware name (for example "gcp.c3_standard_8", "nvidia_orin", "lenovo_p14s_gen_4_windows_11", "macbook_pro_m1_2", "thundercomm_rb6" ...)
* --**multistream_target_latency**=Set MultiStream target latency
* --**offline_target_qps**=Set LoadGen Offline target QPS
* --**quiet**=Quiet run (select default values for all questions) (*True*)
* --**server_target_qps**=Set Server target QPS
* --**singlestream_target_latency**=Set SingleStream target latency
* --**target_latency**=Set Target latency
* --**target_qps**=Set LoadGen target QPS
* --**j**=Print results dictionary to console at the end of the run (*False*)
* --**repro**=Record input/output/state/info files to make it easier to reproduce results (*False*)
* --**time**=Print script execution time at the end of the run (*True*)
* --**debug**=Debug this script (*False*)

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "division":...}
```
#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run-mlperf,inference'
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

```cmr "cm gui" --script="run-mlperf,inference"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run-mlperf,inference) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "run-mlperf,inference[variations]" [--input_flags]`

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


  * Group "**benchmark-version**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_r2.1`
      - Environment variables:
        - *CM_MLPERF_INFERENCE_VERSION*: `2.1`
        - *CM_RUN_MLPERF_INFERENCE_APP_DEFAULTS*: `r2.1_default`
      - Workflow:
    * `_r3.0`
      - Environment variables:
        - *CM_MLPERF_INFERENCE_VERSION*: `3.0`
        - *CM_RUN_MLPERF_INFERENCE_APP_DEFAULTS*: `r3.0_default`
      - Workflow:
    * `_r3.1`
      - Environment variables:
        - *CM_MLPERF_INFERENCE_VERSION*: `3.1`
        - *CM_RUN_MLPERF_INFERENCE_APP_DEFAULTS*: `r3.1_default`
      - Workflow:
    * `_r4.0`
      - Environment variables:
        - *CM_MLPERF_INFERENCE_VERSION*: `4.0`
        - *CM_RUN_MLPERF_INFERENCE_APP_DEFAULTS*: `r4.0_default`
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


  * Group "**submission-generation**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_accuracy-only`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_MODE*: `accuracy`
        - *CM_MLPERF_SUBMISSION_RUN*: `yes`
        - *CM_RUN_MLPERF_ACCURACY*: `on`
        - *CM_RUN_SUBMISSION_CHECKER*: `no`
      - Workflow:
    * **`_find-performance`** (default)
      - Environment variables:
        - *CM_MLPERF_FIND_PERFORMANCE_MODE*: `yes`
        - *CM_MLPERF_LOADGEN_ALL_MODES*: `no`
        - *CM_MLPERF_LOADGEN_MODE*: `performance`
        - *CM_MLPERF_RESULT_PUSH_TO_GITHUB*: `False`
      - Workflow:
    * `_performance-only`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_MODE*: `performance`
        - *CM_MLPERF_SUBMISSION_RUN*: `yes`
        - *CM_RUN_SUBMISSION_CHECKER*: `no`
      - Workflow:
    * `_populate-readme`
      - Environment variables:
        - *CM_MLPERF_README*: `yes`
        - *CM_MLPERF_SUBMISSION_RUN*: `yes`
        - *CM_RUN_SUBMISSION_CHECKER*: `no`
      - Workflow:
    * `_submission`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_COMPLIANCE*: `yes`
        - *CM_MLPERF_SUBMISSION_RUN*: `yes`
        - *CM_RUN_MLPERF_ACCURACY*: `on`
        - *CM_RUN_SUBMISSION_CHECKER*: `yes`
        - *CM_TAR_SUBMISSION_DIR*: `yes`
      - Workflow:
        1. ***Read "post_deps" on other CM scripts***
           * generate,mlperf,inference,submission
             * `if (CM_MLPERF_SKIP_SUBMISSION_GENERATION in ['no', 'false', 'False', '0'])`
             * CM names: `--adr.['submission-generator']...`
             - CM script: [generate-mlperf-inference-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission)

    </details>


  * Group "**submission-generation-style**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_full`
      - Environment variables:
        - *CM_MLPERF_SUBMISSION_GENERATION_STYLE*: `full`
        - *CM_MLPERF_SKIP_SUBMISSION_GENERATION*: `yes`
      - Workflow:
    * **`_short`** (default)
      - Environment variables:
        - *CM_MLPERF_SUBMISSION_GENERATION_STYLE*: `short`
      - Workflow:

    </details>


#### Default variations

`_find-performance,_short`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--backend=value`  &rarr;  `CM_MLPERF_BACKEND=value`
* `--batch_size=value`  &rarr;  `CM_MLPERF_LOADGEN_MAX_BATCHSIZE=value`
* `--category=value`  &rarr;  `CM_MLPERF_SUBMISSION_SYSTEM_TYPE=value`
* `--clean=value`  &rarr;  `CM_MLPERF_CLEAN_ALL=value`
* `--compliance=value`  &rarr;  `CM_MLPERF_LOADGEN_COMPLIANCE=value`
* `--dashboard_wb_project=value`  &rarr;  `CM_MLPERF_DASHBOARD_WANDB_PROJECT=value`
* `--dashboard_wb_user=value`  &rarr;  `CM_MLPERF_DASHBOARD_WANDB_USER=value`
* `--debug=value`  &rarr;  `CM_DEBUG_SCRIPT_BENCHMARK_PROGRAM=value`
* `--device=value`  &rarr;  `CM_MLPERF_DEVICE=value`
* `--division=value`  &rarr;  `CM_MLPERF_SUBMISSION_DIVISION=value`
* `--docker=value`  &rarr;  `CM_MLPERF_USE_DOCKER=value`
* `--dump_version_info=value`  &rarr;  `CM_DUMP_VERSION_INFO=value`
* `--execution_mode=value`  &rarr;  `CM_MLPERF_RUN_STYLE=value`
* `--find_performance=value`  &rarr;  `CM_MLPERF_FIND_PERFORMANCE_MODE=value`
* `--gpu_name=value`  &rarr;  `CM_NVIDIA_GPU_NAME=value`
* `--hw_name=value`  &rarr;  `CM_HW_NAME=value`
* `--hw_notes_extra=value`  &rarr;  `CM_MLPERF_SUT_SW_NOTES_EXTRA=value`
* `--imagenet_path=value`  &rarr;  `IMAGENET_PATH=value`
* `--implementation=value`  &rarr;  `CM_MLPERF_IMPLEMENTATION=value`
* `--lang=value`  &rarr;  `CM_MLPERF_IMPLEMENTATION=value`
* `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
* `--model=value`  &rarr;  `CM_MLPERF_MODEL=value`
* `--multistream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY=value`
* `--network=value`  &rarr;  `CM_NETWORK_LOADGEN=value`
* `--offline_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS=value`
* `--output_dir=value`  &rarr;  `OUTPUT_BASE_DIR=value`
* `--output_summary=value`  &rarr;  `MLPERF_INFERENCE_SUBMISSION_SUMMARY=value`
* `--output_tar=value`  &rarr;  `MLPERF_INFERENCE_SUBMISSION_TAR_FILE=value`
* `--performance_sample_count=value`  &rarr;  `CM_MLPERF_LOADGEN_PERFORMANCE_SAMPLE_COUNT=value`
* `--power=value`  &rarr;  `CM_SYSTEM_POWER=value`
* `--precision=value`  &rarr;  `CM_MLPERF_MODEL_PRECISION=value`
* `--preprocess_submission=value`  &rarr;  `CM_RUN_MLPERF_SUBMISSION_PREPROCESSOR=value`
* `--push_to_github=value`  &rarr;  `CM_MLPERF_RESULT_PUSH_TO_GITHUB=value`
* `--readme=value`  &rarr;  `CM_MLPERF_README=value`
* `--regenerate_accuracy_file=value`  &rarr;  `CM_MLPERF_REGENERATE_ACCURACY_FILE=value`
* `--regenerate_files=value`  &rarr;  `CM_REGENERATE_MEASURE_FILES=value`
* `--rerun=value`  &rarr;  `CM_RERUN=value`
* `--results_dir=value`  &rarr;  `OUTPUT_BASE_DIR=value`
* `--results_git_url=value`  &rarr;  `CM_MLPERF_RESULTS_GIT_REPO_URL=value`
* `--run_checker=value`  &rarr;  `CM_RUN_SUBMISSION_CHECKER=value`
* `--run_style=value`  &rarr;  `CM_MLPERF_RUN_STYLE=value`
* `--save_console_log=value`  &rarr;  `CM_SAVE_CONSOLE_LOG=value`
* `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
* `--server_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_SERVER_TARGET_QPS=value`
* `--singlestream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY=value`
* `--skip_submission_generation=value`  &rarr;  `CM_MLPERF_SKIP_SUBMISSION_GENERATION=value`
* `--skip_truncation=value`  &rarr;  `CM_SKIP_TRUNCATE_ACCURACY=value`
* `--submission_dir=value`  &rarr;  `CM_MLPERF_INFERENCE_SUBMISSION_DIR=value`
* `--submitter=value`  &rarr;  `CM_MLPERF_SUBMITTER=value`
* `--sut=value`  &rarr;  `CM_MLPERF_INFERENCE_SUT_VARIATION=value`
* `--sut_servers=value`  &rarr;  `CM_NETWORK_LOADGEN_SUT_SERVERS=value`
* `--sw_notes_extra=value`  &rarr;  `CM_MLPERF_SUT_SW_NOTES_EXTRA=value`
* `--system_type=value`  &rarr;  `CM_MLPERF_SUBMISSION_SYSTEM_TYPE=value`
* `--target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_LATENCY=value`
* `--target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_QPS=value`
* `--test_query_count=value`  &rarr;  `CM_TEST_QUERY_COUNT=value`
* `--threads=value`  &rarr;  `CM_NUM_THREADS=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "backend":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MLPERF_IMPLEMENTATION: `reference`
* CM_MLPERF_MODEL: `resnet50`
* CM_MLPERF_RUN_STYLE: `test`

</details>

#### Versions
* `master`
* `r2.1`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-app/_cm.yaml)***
     * detect,os
       * `if (CM_MLPERF_USE_DOCKER  != True)`
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       * `if (CM_MLPERF_USE_DOCKER  != True)`
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,python3
       * `if (CM_MLPERF_USE_DOCKER  != True)`
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,sut,description
       - CM script: [get-mlperf-inference-sut-description](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description)
     * get,mlperf,inference,results,dir
       * `if (CM_MLPERF_USE_DOCKER  == False) AND (OUTPUT_BASE_DIR  != True)`
       * CM names: `--adr.['get-mlperf-inference-results-dir']...`
       - CM script: [get-mlperf-inference-results-dir](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-results-dir)
     * install,pip-package,for-cmind-python,_package.tabulate
       - CM script: [install-pip-package-for-cmind-python](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pip-package-for-cmind-python)
     * get,mlperf,inference,utils
       - CM script: [get-mlperf-inference-utils](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-utils)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-app/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-app/_cm.yaml)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-app/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-app/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-app/_cm.yaml)

___
### Script output
`cmr "run-mlperf,inference [,variations]" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
