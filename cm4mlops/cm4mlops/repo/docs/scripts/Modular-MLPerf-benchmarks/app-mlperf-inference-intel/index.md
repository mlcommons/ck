# app-mlperf-inference-intel
Automatically generated README for this automation recipe: **app-mlperf-inference-intel**

Category: **[Modular MLPerf benchmarks](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-intel/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "reproduce mlcommons mlperf inference harness intel-harness intel intel-harness intel" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=reproduce,mlcommons,mlperf,inference,harness,intel-harness,intel,intel-harness,intel[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "reproduce mlcommons mlperf inference harness intel-harness intel intel-harness intel [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,mlcommons,mlperf,inference,harness,intel-harness,intel,intel-harness,intel'
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
    cm docker script "reproduce mlcommons mlperf inference harness intel-harness intel intel-harness intel[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_bs.#`
               - ENV variables:
                   - ML_MLPERF_MODEL_BATCH_SIZE: `#`
        * `_v3.1`
               - ENV variables:
                   - CM_MLPERF_INFERENCE_CODE_VERSION: `v3.1`

        </details>


      * Group "**device**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_cpu`** (default)
               - ENV variables:
                   - CM_MLPERF_DEVICE: `cpu`

        </details>


      * Group "**framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_pytorch`** (default)
               - ENV variables:
                   - CM_MLPERF_BACKEND: `pytorch`
                   - CM_MLPERF_BACKEND_LIB_NAMESPEC: `pytorch`

        </details>


      * Group "**loadgen-batchsize**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_batch_size.#`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_BATCH_SIZE: `#`

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
                   - CM_NOT_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://zenodo.org/record/3750364/files/bert_large_v1_1_fake_quant.onnx`
        * `_bert-99.9`
               - ENV variables:
                   - CM_MODEL: `bert-99.9`
                   - CM_NOT_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://zenodo.org/record/3733910/files/model.onnx`
        * `_gptj-99`
               - ENV variables:
                   - CM_MODEL: `gptj-99`
                   - CM_NOT_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://zenodo.org/record/3733910/files/model.onnx`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `int8`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int8`
        * `_gptj-99.9`
               - ENV variables:
                   - CM_MODEL: `gptj-99.9`
                   - CM_NOT_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://zenodo.org/record/3733910/files/model.onnx`
        * **`_resnet50`** (default)
               - ENV variables:
                   - CM_MODEL: `resnet50`
                   - dataset_imagenet_preprocessed_input_square_side: `224`
                   - ml_model_has_background_class: `YES`
                   - ml_model_image_height: `224`
                   - loadgen_buffer_size: `1024`
                   - loadgen_dataset_size: `50000`
                   - CM_BENCHMARK: `STANDALONE_CLASSIFICATION`
        * `_retinanet`
               - ENV variables:
                   - CM_MODEL: `retinanet`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://zenodo.org/record/6617981/files/resnext50_32x4d_fpn.pth`
                   - dataset_imagenet_preprocessed_input_square_side: `224`
                   - ml_model_image_height: `800`
                   - ml_model_image_width: `800`
                   - loadgen_buffer_size: `64`
                   - loadgen_dataset_size: `24576`
                   - CM_BENCHMARK: `STANDALONE_OBJECT_DETECTION`

        </details>


      * Group "**network-mode**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_network-server`
               - ENV variables:
                   - CM_MLPERF_NETWORK_RUN_MODE: `network-server`
        * **`_standalone`** (default)
               - ENV variables:
                   - CM_MLPERF_NETWORK_RUN_MODE: `standalone`

        </details>


      * Group "**network-run-mode**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_network-client`
               - ENV variables:
                   - CM_MLPERF_NETWORK_RUN_MODE: `network-client`

        </details>


      * Group "**power-mode**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_maxn`
               - ENV variables:
                   - CM_MLPERF_NVIDIA_HARNESS_MAXN: `True`
        * `_maxq`
               - ENV variables:
                   - CM_MLPERF_NVIDIA_HARNESS_MAXQ: `True`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_fp32`
               - ENV variables:
                   - CM_IMAGENET_ACCURACY_DTYPE: `float32`
        * `_int4`
        * `_uint8`

        </details>


      * Group "**run-mode**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_build-harness`
               - ENV variables:
                   - CM_LOCAL_MLPERF_INFERENCE_INTEL_RUN_MODE: `build_harness`
        * `_calibration`
               - ENV variables:
                   - CM_LOCAL_MLPERF_INFERENCE_INTEL_RUN_MODE: `calibration`
        * **`_run-harness`** (default)
               - ENV variables:
                   - CM_LOCAL_MLPERF_INFERENCE_INTEL_RUN_MODE: `run_harness`

        </details>


      * Group "**sut**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_sapphire-rapids.112c`
               - ENV variables:
                   - WARMUP: ` --warmup`
        * `_sapphire-rapids.24c`

        </details>


      * Group "**version**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_v4.0`** (default)
               - ENV variables:
                   - CM_MLPERF_INFERENCE_CODE_VERSION: `v4.0`

        </details>


    ##### Default variations

    `_cpu,_pytorch,_resnet50,_run-harness,_standalone,_v4.0`
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

    * CM_BATCH_COUNT: `1`
    * CM_BATCH_SIZE: `1`
    * CM_FAST_COMPILATION: `yes`
    * CM_MLPERF_LOADGEN_SCENARIO: `Offline`
    * CM_MLPERF_LOADGEN_MODE: `performance`
    * CM_SKIP_PREPROCESS_DATASET: `no`
    * CM_SKIP_MODEL_DOWNLOAD: `no`
    * CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `intel`
    * CM_MLPERF_SKIP_RUN: `no`
    * verbosity: `1`
    * loadgen_trigger_cold_run: `0`



#### Native script being run
=== "Linux/macOS"
     * [run_bert_harness.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-intel/run_bert_harness.sh)
     * [run_gptj_harness_v3_1.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-intel/run_gptj_harness_v3_1.sh)
     * [run_gptj_harness_v4_0.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-intel/run_gptj_harness_v4_0.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "reproduce mlcommons mlperf inference harness intel-harness intel intel-harness intel [variations]" [--input_flags] -j
```