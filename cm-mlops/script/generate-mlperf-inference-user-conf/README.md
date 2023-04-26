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

* Category: *Modular MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *generate,mlperf,inference,user-conf,inference-user-conf*
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

1. `cm run script --tags=generate,mlperf,inference,user-conf,inference-user-conf [--input_flags]`

2. `cm run script "generate mlperf inference user-conf inference-user-conf" [--input_flags]`

3. `cm run script 3af4475745964b93 [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'generate,mlperf,inference,user-conf,inference-user-conf'
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

```cm run script --tags=gui --script="generate,mlperf,inference,user-conf,inference-user-conf"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=generate,mlperf,inference,user-conf,inference-user-conf) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
* `--hw_name=value`  &rarr;  `CM_HW_NAME=value`
* `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
* `--multistream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY=value`
* `--num_threads=value`  &rarr;  `CM_NUM_THREADS=value`
* `--offline_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS=value`
* `--output_dir=value`  &rarr;  `OUTPUT_BASE_DIR=value`
* `--performance_sample_count=value`  &rarr;  `CM_MLPERF_PERFORMANCE_SAMPLE_COUNT=value`
* `--power=value`  &rarr;  `CM_MLPERF_POWER=value`
* `--regenerate_files=value`  &rarr;  `CM_REGENERATE_MEASURE_FILES=value`
* `--rerun=value`  &rarr;  `CM_RERUN=value`
* `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
* `--server_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_SERVER_TARGET_QPS=value`
* `--singlestream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY=value`
* `--target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_LATENCY=value`
* `--target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_QPS=value`
* `--test_query_count=value`  &rarr;  `CM_TEST_QUERY_COUNT=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "count":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MLPERF_LOADGEN_MODE: `accuracy`
* CM_MLPERF_LOADGEN_SCENARIO: `Offline`
* CM_OUTPUT_FOLDER_NAME: `test_results`
* CM_MLPERF_RUN_STYLE: `test`
* CM_TEST_QUERY_COUNT: `10`
* CM_MLPERF_QUANTIZATION: `False`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,python
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,sut,configs
       - CM script: [get-mlperf-inference-sut-configs](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf/_cm.yaml)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf/_cm.yaml)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf/_cm.yaml)
</details>

___
### Script output
#### New environment keys (filter)

* `CM_HW_*`
* `CM_MAX_EXAMPLES`
* `CM_MLPERF_*`
* `CM_SUT_*`
#### New environment keys auto-detected from customize

* `CM_MAX_EXAMPLES`
* `CM_MLPERF_CONF`
* `CM_MLPERF_INFERENCE_AUDIT_PATH`
* `CM_MLPERF_LOADGEN_LOGS_DIR`
* `CM_MLPERF_LOADGEN_MODE`
* `CM_MLPERF_LOADGEN_QUERY_COUNT`
* `CM_MLPERF_LOADGEN_SCENARIO`
* `CM_MLPERF_LOADGEN_TARGET_LATENCY`
* `CM_MLPERF_LOADGEN_TARGET_QPS`
* `CM_MLPERF_OUTPUT_DIR`
* `CM_MLPERF_POWER_LOG_DIR`
* `CM_MLPERF_RESULTS_DIR`
* `CM_MLPERF_RUN_STYLE`
* `CM_MLPERF_SKIP_RUN`
* `CM_MLPERF_USER_CONF`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)