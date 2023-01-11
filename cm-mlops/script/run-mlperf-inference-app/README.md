*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Variations](#variations)
  * [ All variations](#all-variations)
* [Versions](#versions)
* [Default environment](#default-environment)
* [CM script workflow](#cm-script-workflow)
* [New environment export](#new-environment-export)
* [New environment detected from customize](#new-environment-detected-from-customize)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
  * [ Script input flags mapped to environment](#script-input-flags-mapped-to-environment)
* [Maintainers](#maintainers)

</details>

___
### About

*TBD*
___
### Category

Modular MLPerf benchmarks.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
run,generate-run-cmds,run-mlperf,vision,mlcommons,mlperf,inference,reference

___
### Variations
#### All variations
* all-modes
  - *ENV CM_MLPERF_LOADGEN_ALL_MODES*: `yes`
* all-scenarios
  - *ENV CM_MLPERF_LOADGEN_ALL_SCENARIOS*: `yes`
* compliance
  - *ENV CM_MLPERF_LOADGEN_COMPLIANCE*: `yes`
* dashboard
  - *ENV CM_MLPERF_DASHBOARD*: `on`
* fast
  - *ENV CM_FAST_FACTOR*: `5`
  - *ENV CM_OUTPUT_FOLDER_NAME*: `fast_results`
  - *ENV CM_MLPERF_RUN_STYLE*: `fast`
* short
* submission
  - *ENV CM_MLPERF_SUBMISSION_RUN*: `yes`
  - *ENV CM_RUN_SUBMISSION_CHECKER*: `yes`
  - *ENV CM_TAR_SUBMISSION_DIR*: `yes`
  - *ENV CM_RUN_MLPERF_ACCURACY*: `on`
* valid
  - *ENV CM_OUTPUT_FOLDER_NAME*: `valid_results`
  - *ENV CM_MLPERF_RUN_STYLE*: `valid`
  - *ENV CM_RUN_MLPERF_ACCURACY*: `on`
___
### Versions
* master
* r2.1
___
### Default environment

* CM_BATCH_COUNT: **1**
* CM_BATCH_SIZE: **1**
* CM_OUTPUT_FOLDER_NAME: **test_results**
* CM_MLPERF_RUN_STYLE: **test**
* CM_TEST_QUERY_COUNT: **5**
___
### CM script workflow

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
### New environment export

___
### New environment detected from customize

* **CM_MLPERF_BACKEND_VERSION**
* **CM_MLPERF_CLEAN_SUBMISSION_DIR**
* **CM_MLPERF_DEVICE**
* **CM_MLPERF_LOADGEN_COMPLIANCE**
* **CM_MLPERF_LOADGEN_COMPLIANCE_TEST**
* **CM_MLPERF_LOADGEN_EXTRA_OPTIONS**
* **CM_MLPERF_LOADGEN_MODE**
* **CM_MLPERF_LOADGEN_MODES**
* **CM_MLPERF_LOADGEN_SCENARIO**
* **CM_MLPERF_LOADGEN_SCENARIOS**
* **CM_MLPERF_RESULTS_DIR**
* **CM_MODEL**
* **CM_RERUN**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="run,generate-run-cmds,run-mlperf,vision,mlcommons,mlperf,inference,reference"`

*or*

`cm run script "run generate-run-cmds run-mlperf vision mlcommons mlperf inference reference"`

*or*

`cm run script 4a5d5b13fd7e4ac8`

#### CM Python API

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

#### CM modular Docker container
*TBD*

#### Script input flags mapped to environment

* lang --> **CM_MLPERF_LANG**
* device --> **CM_MLPERF_DEVICE**
* submitter --> **CM_MLPERF_SUBMITTER**
* backend --> **CM_MLPERF_BACKEND**
* model --> **CM_MLPERF_MODEL**
* run_style --> **CM_MLPERF_RUN_STYLE**
* rerun --> **CM_RERUN**
* hw_name --> **CM_HW_NAME**
* imagenet_path --> **IMAGENET_PATH**
* max_batchsize --> **CM_MLPERF_LOADGEN_MAX_BATCHSIZE**
* mode --> **CM_MLPERF_LOADGEN_MODE**
* num_threads --> **CM_NUM_THREADS**
* output_dir --> **OUTPUT_BASE_DIR**
* results_dir --> **OUTPUT_BASE_DIR**
* submission_dir --> **CM_MLPERF_SUBMISSION_DIR**
* power --> **CM_SYSTEM_POWER**
* regenerate_files --> **CM_REGENERATE_MEASURE_FILES**
* scenario --> **CM_MLPERF_LOADGEN_SCENARIO**
* quantized --> **CM_MLPERF_QUANTIZATION**
* test_query_count --> **CM_TEST_QUERY_COUNT**
* run_checker --> **CM_RUN_SUBMISSION_CHECKER**
* skip_truncation --> **CM_SKIP_TRUNCATE_ACCURACY**
* clean --> **CM_MLPERF_CLEAN_ALL**
* new_tvm_model --> **CM_MLPERF_DELETE_COMPILED_MODEL**

Examples:

```bash
cm run script "run generate-run-cmds run-mlperf vision mlcommons mlperf inference reference" --lang=...
```
```python
r=cm.access({... , "lang":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)