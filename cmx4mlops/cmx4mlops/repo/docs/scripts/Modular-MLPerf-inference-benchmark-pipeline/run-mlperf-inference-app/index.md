# run-mlperf-inference-app
Automatically generated README for this automation recipe: **run-mlperf-inference-app**

Category: **[Modular MLPerf inference benchmark pipeline](..)**

License: **Apache 2.0**

Developers: [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh), [Grigori Fursin](https://cKnowledge.org/gfursin)
* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-inference-app/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-inference-app/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "run-mlperf,inference" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=run-mlperf,inference[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "run-mlperf,inference [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


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


=== "Docker"
    ##### Run this script via Docker (beta)

    ```bash
    cm docker script "run-mlperf,inference[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_all-scenarios`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_ALL_SCENARIOS: `yes`
        * `_compliance`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_COMPLIANCE: `yes`
        * `_dashboard`
               - ENV variables:
                   - CM_MLPERF_DASHBOARD: `on`

        </details>


      * Group "**benchmark-version**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_r2.1`
               - ENV variables:
                   - CM_MLPERF_INFERENCE_VERSION: `2.1`
                   - CM_RUN_MLPERF_INFERENCE_APP_DEFAULTS: `r2.1_default`
        * `_r3.0`
               - ENV variables:
                   - CM_MLPERF_INFERENCE_VERSION: `3.0`
                   - CM_RUN_MLPERF_INFERENCE_APP_DEFAULTS: `r3.0_default`
        * `_r3.1`
               - ENV variables:
                   - CM_MLPERF_INFERENCE_VERSION: `3.1`
                   - CM_RUN_MLPERF_INFERENCE_APP_DEFAULTS: `r3.1_default`
        * `_r4.0`
               - ENV variables:
                   - CM_MLPERF_INFERENCE_VERSION: `4.0`
                   - CM_RUN_MLPERF_INFERENCE_APP_DEFAULTS: `r4.0_default`
        * `_r4.1`
               - ENV variables:
                   - CM_MLPERF_INFERENCE_VERSION: `4.1`
                   - CM_RUN_MLPERF_INFERENCE_APP_DEFAULTS: `r4.1_default`

        </details>


      * Group "**mode**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_all-modes`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_ALL_MODES: `yes`

        </details>


      * Group "**submission-generation**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_accuracy-only`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_MODE: `accuracy`
                   - CM_MLPERF_SUBMISSION_RUN: `yes`
                   - CM_RUN_MLPERF_ACCURACY: `on`
                   - CM_RUN_SUBMISSION_CHECKER: `no`
        * `_find-performance`
               - ENV variables:
                   - CM_MLPERF_FIND_PERFORMANCE_MODE: `yes`
                   - CM_MLPERF_LOADGEN_ALL_MODES: `no`
                   - CM_MLPERF_LOADGEN_MODE: `performance`
                   - CM_MLPERF_RESULT_PUSH_TO_GITHUB: `False`
        * **`_performance-and-accuracy`** (default)
        * `_performance-only`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_MODE: `performance`
                   - CM_MLPERF_SUBMISSION_RUN: `yes`
                   - CM_RUN_SUBMISSION_CHECKER: `no`
        * `_populate-readme`
               - ENV variables:
                   - CM_MLPERF_README: `yes`
                   - CM_MLPERF_SUBMISSION_RUN: `yes`
                   - CM_RUN_SUBMISSION_CHECKER: `no`
        * `_submission`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_COMPLIANCE: `yes`
                   - CM_MLPERF_SUBMISSION_RUN: `yes`
                   - CM_RUN_MLPERF_ACCURACY: `on`
                   - CM_RUN_SUBMISSION_CHECKER: `yes`
                   - CM_TAR_SUBMISSION_DIR: `yes`

        </details>


      * Group "**submission-generation-style**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_full`
               - ENV variables:
                   - CM_MLPERF_SUBMISSION_GENERATION_STYLE: `full`
                   - CM_MLPERF_SKIP_SUBMISSION_GENERATION: `yes`
        * **`_short`** (default)
               - ENV variables:
                   - CM_MLPERF_SUBMISSION_GENERATION_STYLE: `short`

        </details>


    ##### Default variations

    `_performance-and-accuracy,_short`
=== "Input Flags"


    #### Input Flags

    * --**division:** MLPerf division {open,closed} (*open*)
    * --**category:** MLPerf category {edge,datacenter,network} (*edge*)
    * --**device:** MLPerf device {cpu,cuda,rocm,qaic} (*cpu*)
    * --**model:** MLPerf model {resnet50,retinanet,bert-99,bert-99.9,3d-unet-99,3d-unet-99.9,rnnt,dlrm-v2-99,dlrm-v2-99.9,gptj-99,gptj-99.9,sdxl,llama2-70b-99,llama2-70b-99.9,mobilenet,efficientnet} (*resnet50*)
    * --**precision:** MLPerf model precision {float32,float16,bfloat16,int8,uint8}
    * --**implementation:** MLPerf implementation {mlcommons-python,mlcommons-cpp,nvidia,intel,qualcomm,ctuning-cpp-tflite} (*mlcommons-python*)
    * --**backend:** MLPerf framework (backend) {onnxruntime,tf,pytorch,deepsparse,tensorrt,glow,tvm-onnx} (*onnxruntime*)
    * --**scenario:** MLPerf scenario {Offline,Server,SingleStream,MultiStream} (*Offline*)
    * --**mode:** MLPerf benchmark mode {,accuracy,performance}
    * --**execution_mode:** MLPerf execution mode {test,fast,valid} (*test*)
    * --**sut:** SUT configuration (if known)
    * --**submitter:** Submitter name (without space) (*CTuning*)
    * --**results_dir:** Folder path to store results (defaults to the current working directory)
    * --**submission_dir:** Folder path to store MLPerf submission tree
    * --**adr.compiler.tags:** Compiler for loadgen and any C/C++ part of implementation
    * --**adr.inference-src-loadgen.env.CM_GIT_URL:** Git URL for MLPerf inference sources to build LoadGen (to enable non-reference implementations)
    * --**adr.inference-src.env.CM_GIT_URL:** Git URL for MLPerf inference sources to run benchmarks (to enable non-reference implementations)
    * --**adr.mlperf-inference-implementation.max_batchsize:** Maximum batchsize to be used
    * --**adr.mlperf-inference-implementation.num_threads:** Number of threads (reference & C++ implementation only)
    * --**adr.python.name:** Python virtual environment name (optional)
    * --**adr.python.version:** Force Python version (must have all system deps)
    * --**adr.python.version_min:** Minimal Python version (*3.8*)
    * --**power:** Measure power {yes,no} (*no*)
    * --**adr.mlperf-power-client.power_server:** MLPerf Power server IP address (*192.168.0.15*)
    * --**adr.mlperf-power-client.port:** MLPerf Power server port (*4950*)
    * --**clean:** Clean run (*False*)
    * --**compliance:** Whether to run compliance tests (applicable only for closed division) {yes,no} (*no*)
    * --**dashboard_wb_project:** W&B dashboard project (*cm-mlperf-dse-testing*)
    * --**dashboard_wb_user:** W&B dashboard user (*cmind*)
    * --**hw_name:** MLPerf hardware name (for example "gcp.c3_standard_8", "nvidia_orin", "lenovo_p14s_gen_4_windows_11", "macbook_pro_m1_2", "thundercomm_rb6" ...)
    * --**multistream_target_latency:** Set MultiStream target latency
    * --**offline_target_qps:** Set LoadGen Offline target QPS
    * --**quiet:** Quiet run (select default values for all questions) (*True*)
    * --**server_target_qps:** Set Server target QPS
    * --**singlestream_target_latency:** Set SingleStream target latency
    * --**target_latency:** Set Target latency
    * --**target_qps:** Set LoadGen target QPS
    * --**j:** Print results dictionary to console at the end of the run (*False*)
    * --**repro:** Record input/output/state/info files to make it easier to reproduce results (*False*)
    * --**time:** Print script execution time at the end of the run (*True*)
    * --**debug:** Debug this script (*False*)
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--backend=value`  &rarr;  `CM_MLPERF_BACKEND=value`
    * `--batch_size=value`  &rarr;  `CM_MLPERF_LOADGEN_MAX_BATCHSIZE=value`
    * `--beam_size=value`  &rarr;  `GPTJ_BEAM_SIZE=value`
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



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_MLPERF_IMPLEMENTATION: `reference`
    * CM_MLPERF_MODEL: `resnet50`
    * CM_MLPERF_RUN_STYLE: `test`


#### Versions
* `master`
* `r2.1`

___
#### Script output
```bash
cmr "run-mlperf,inference [variations]" [--input_flags] -j
```