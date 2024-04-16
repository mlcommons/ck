**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/generate-mlperf-inference-user-conf).**



Automatically generated README for this automation recipe: **generate-mlperf-inference-user-conf**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Developers: [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh), [Thomas Zhu](https://www.linkedin.com/in/hanwen-zhu-483614189), [Grigori Fursin](https://cKnowledge.org/gfursin)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=generate-mlperf-inference-user-conf,3af4475745964b93) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-user-conf)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *generate,mlperf,inference,user-conf,inference-user-conf*
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

````cmr "generate mlperf inference user-conf inference-user-conf" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=generate,mlperf,inference,user-conf,inference-user-conf`

`cm run script --tags=generate,mlperf,inference,user-conf,inference-user-conf [--input_flags]`

*or*

`cmr "generate mlperf inference user-conf inference-user-conf"`

`cmr "generate mlperf inference user-conf inference-user-conf " [--input_flags]`


#### Run this script from Python

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


#### Run this script via GUI

```cmr "cm gui" --script="generate,mlperf,inference,user-conf,inference-user-conf"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=generate,mlperf,inference,user-conf,inference-user-conf) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "generate mlperf inference user-conf inference-user-conf" [--input_flags]`

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
* CM_FAST_FACTOR: `5`
* CM_MLPERF_QUANTIZATION: `False`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-user-conf/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,python
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlperf,results,dir
       * `if (OUTPUT_BASE_DIR  != on)`
       * CM names: `--adr.['get-mlperf-results-dir']...`
       - CM script: [get-mlperf-inference-results-dir](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-results-dir)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,sut,configs
       - CM script: [get-mlperf-inference-sut-configs](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-user-conf/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-user-conf/_cm.yaml)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-user-conf/_cm.yaml)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-user-conf/_cm.yaml)

___
### Script output
`cmr "generate mlperf inference user-conf inference-user-conf " [--input_flags] -j`
#### New environment keys (filter)

* `CM_HW_*`
* `CM_LOGS_DIR`
* `CM_MAX_EXAMPLES`
* `CM_MLPERF_*`
* `CM_SUT_*`
#### New environment keys auto-detected from customize

* `CM_LOGS_DIR`
* `CM_MAX_EXAMPLES`
* `CM_MLPERF_ACCURACY_RESULTS_DIR`
* `CM_MLPERF_COMPLIANCE_RUN_POSTPONED`
* `CM_MLPERF_CONF`
* `CM_MLPERF_INFERENCE_AUDIT_PATH`
* `CM_MLPERF_INFERENCE_FINAL_RESULTS_DIR`
* `CM_MLPERF_INFERENCE_MIN_DURATION`
* `CM_MLPERF_LOADGEN_LOGS_DIR`
* `CM_MLPERF_LOADGEN_MODE`
* `CM_MLPERF_LOADGEN_QUERY_COUNT`
* `CM_MLPERF_LOADGEN_SCENARIO`
* `CM_MLPERF_LOADGEN_TARGET_LATENCY`
* `CM_MLPERF_LOADGEN_TARGET_QPS`
* `CM_MLPERF_OUTPUT_DIR`
* `CM_MLPERF_POWER_LOG_DIR`
* `CM_MLPERF_RANGING_USER_CONF`
* `CM_MLPERF_RUN_STYLE`
* `CM_MLPERF_SKIP_RUN`
* `CM_MLPERF_TESTING_USER_CONF`
* `CM_MLPERF_USER_CONF`
* `CM_MLPERF_USE_MAX_DURATION`