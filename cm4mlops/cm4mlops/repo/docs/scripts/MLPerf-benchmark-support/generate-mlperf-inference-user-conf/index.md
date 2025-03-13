# generate-mlperf-inference-user-conf
Automatically generated README for this automation recipe: **generate-mlperf-inference-user-conf**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

Developers: [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh), [Thomas Zhu](https://www.linkedin.com/in/hanwen-zhu-483614189), [Grigori Fursin](https://cKnowledge.org/gfursin)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/generate-mlperf-inference-user-conf/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "generate mlperf inference user-conf inference-user-conf" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=generate,mlperf,inference,user-conf,inference-user-conf [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "generate mlperf inference user-conf inference-user-conf " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


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


=== "Docker"
    ##### Run this script via Docker (beta)

    ```bash
    cm docker script "generate mlperf inference user-conf inference-user-conf" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

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



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_MLPERF_LOADGEN_MODE: `accuracy`
    * CM_MLPERF_LOADGEN_SCENARIO: `Offline`
    * CM_OUTPUT_FOLDER_NAME: `test_results`
    * CM_MLPERF_RUN_STYLE: `test`
    * CM_TEST_QUERY_COUNT: `10`
    * CM_FAST_FACTOR: `5`
    * CM_MLPERF_QUANTIZATION: `False`



___
#### Script output
```bash
cmr "generate mlperf inference user-conf inference-user-conf " [--input_flags] -j
```