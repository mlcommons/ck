# app-mlperf-inference-dummy
Automatically generated README for this automation recipe: **app-mlperf-inference-dummy**

Category: **[Modular MLPerf benchmarks](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-dummy/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "reproduce mlcommons mlperf inference harness dummy-harness dummy" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=reproduce,mlcommons,mlperf,inference,harness,dummy-harness,dummy[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "reproduce mlcommons mlperf inference harness dummy-harness dummy [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,mlcommons,mlperf,inference,harness,dummy-harness,dummy'
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
    cm docker script "reproduce mlcommons mlperf inference harness dummy-harness dummy[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * Group "**backend**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_pytorch`** (default)
               - ENV variables:
                   - CM_MLPERF_BACKEND: `pytorch`

        </details>


      * Group "**batch-size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_bs.#`

        </details>


      * Group "**device**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_cpu`** (default)
               - ENV variables:
                   - CM_MLPERF_DEVICE: `cpu`
        * `_cuda`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `gpu`
                   - CM_MLPERF_DEVICE_LIB_NAMESPEC: `cudart`

        </details>


      * Group "**loadgen-scenario**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_multistream`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `MultiStream`
        * `_offline`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `Offline`
        * `_server`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `Server`
        * `_singlestream`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `SingleStream`

        </details>


      * Group "**model**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_bert-99`
               - ENV variables:
                   - CM_MODEL: `bert-99`
                   - CM_SQUAD_ACCURACY_DTYPE: `float32`
        * `_bert-99.9`
               - ENV variables:
                   - CM_MODEL: `bert-99.9`
        * `_gptj-99`
               - ENV variables:
                   - CM_MODEL: `gptj-99`
                   - CM_SQUAD_ACCURACY_DTYPE: `float32`
        * `_gptj-99.9`
               - ENV variables:
                   - CM_MODEL: `gptj-99.9`
        * `_llama2-70b-99`
               - ENV variables:
                   - CM_MODEL: `llama2-70b-99`
        * `_llama2-70b-99.9`
               - ENV variables:
                   - CM_MODEL: `llama2-70b-99.9`
        * **`_resnet50`** (default)
               - ENV variables:
                   - CM_MODEL: `resnet50`
        * `_retinanet`
               - ENV variables:
                   - CM_MODEL: `retinanet`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_fp16`
        * `_fp32`
        * `_uint8`

        </details>


    ##### Default variations

    `_cpu,_pytorch,_resnet50`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
    * `--max_batchsize=value`  &rarr;  `CM_MLPERF_LOADGEN_MAX_BATCHSIZE=value`
    * `--mlperf_conf=value`  &rarr;  `CM_MLPERF_CONF=value`
    * `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
    * `--multistream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY=value`
    * `--offline_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS=value`
    * `--output_dir=value`  &rarr;  `CM_MLPERF_OUTPUT_DIR=value`
    * `--performance_sample_count=value`  &rarr;  `CM_MLPERF_LOADGEN_PERFORMANCE_SAMPLE_COUNT=value`
    * `--rerun=value`  &rarr;  `CM_RERUN=value`
    * `--results_repo=value`  &rarr;  `CM_MLPERF_INFERENCE_RESULTS_REPO=value`
    * `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
    * `--server_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_SERVER_TARGET_QPS=value`
    * `--singlestream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY=value`
    * `--skip_preprocess=value`  &rarr;  `CM_SKIP_PREPROCESS_DATASET=value`
    * `--skip_preprocessing=value`  &rarr;  `CM_SKIP_PREPROCESS_DATASET=value`
    * `--target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_LATENCY=value`
    * `--target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_QPS=value`
    * `--user_conf=value`  &rarr;  `CM_MLPERF_USER_CONF=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_MLPERF_LOADGEN_SCENARIO: `Offline`
    * CM_MLPERF_LOADGEN_MODE: `performance`
    * CM_SKIP_PREPROCESS_DATASET: `no`
    * CM_SKIP_MODEL_DOWNLOAD: `no`
    * CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `dummy_harness`
    * CM_MLPERF_SKIP_RUN: `no`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-dummy/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "reproduce mlcommons mlperf inference harness dummy-harness dummy [variations]" [--input_flags] -j
```