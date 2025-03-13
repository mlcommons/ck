# app-mlperf-inference-qualcomm
Automatically generated README for this automation recipe: **app-mlperf-inference-qualcomm**

Category: **[Modular MLPerf benchmarks](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-qualcomm/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "reproduce mlcommons mlperf inference harness qualcomm-harness qualcomm kilt-harness kilt" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=reproduce,mlcommons,mlperf,inference,harness,qualcomm-harness,qualcomm,kilt-harness,kilt[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "reproduce mlcommons mlperf inference harness qualcomm-harness qualcomm kilt-harness kilt [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,mlcommons,mlperf,inference,harness,qualcomm-harness,qualcomm,kilt-harness,kilt'
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
    cm docker script "reproduce mlcommons mlperf inference harness qualcomm-harness qualcomm kilt-harness kilt[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_activation-count.#`
               - ENV variables:
                   - CM_MLPERF_QAIC_ACTIVATION_COUNT: `#`
        * `_num-devices.4`
               - ENV variables:
                   - CM_QAIC_DEVICES: `0,1,2,3`
        * `_pro`
               - ENV variables:
                   - qaic_queue_length: `10`

        </details>


      * Group "**batch-size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_bs.#`
               - ENV variables:
                   - kilt_model_batch_size: `#`
        * `_bs.0`
               - ENV variables:
                   - kilt_model_batch_size: `1`

        </details>


      * Group "**device**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_cpu`** (default)
               - ENV variables:
                   - CM_MLPERF_DEVICE: `cpu`
                   - kilt_backend_type: `cpu`
        * `_cuda`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `gpu`
                   - CM_MLPERF_DEVICE_LIB_NAMESPEC: `cudart`
                   - kilt_backend_type: `gpu`
        * `_qaic`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `qaic`
                   - CM_MLPERF_DEVICE_LIB_NAMESPEC: `QAic`
                   - kilt_backend_type: `qaic`

        </details>


      * Group "**framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_glow`
               - ENV variables:
                   - device: `qaic`
                   - CM_MLPERF_BACKEND: `glow`
                   - CM_MLPERF_BACKEND_LIB_NAMESPEC: `QAic`
        * **`_onnxruntime`** (default)
               - ENV variables:
                   - device: `onnxrt`
                   - CM_MLPERF_BACKEND: `onnxruntime`
                   - CM_MLPERF_BACKEND_LIB_NAMESPEC: `onnxruntime`
        * `_tensorrt`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tensorrt`
                   - device: `tensorrt`
                   - CM_MLPERF_BACKEND_NAME: `TensorRT`

        </details>


      * Group "**loadgen-batch-size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_loadgen-batch-size.#`
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
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://zenodo.org/record/3750364/files/bert_large_v1_1_fake_quant.onnx`
        * `_bert-99.9`
               - ENV variables:
                   - CM_MODEL: `bert-99.9`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://zenodo.org/record/3733910/files/model.onnx`
        * **`_resnet50`** (default)
               - ENV variables:
                   - CM_MODEL: `resnet50`
                   - kilt_model_name: `resnet50`
                   - kilt_input_count: `1`
                   - kilt_output_count: `1`
                   - kilt_input_format: `FLOAT32,-1,224,224,3`
                   - kilt_output_format: `INT64,-1`
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
                   - kilt_model_name: `retinanet`
                   - kilt_input_count: `1`
                   - kilt_model_max_detections: `600`
                   - kilt_output_count: `1`
                   - kilt_input_format: `FLOAT32,-1,3,800,800`
                   - kilt_output_format: `INT64,-1`
                   - dataset_imagenet_preprocessed_input_square_side: `224`
                   - ml_model_image_height: `800`
                   - ml_model_image_width: `800`
                   - loadgen_buffer_size: `64`
                   - loadgen_dataset_size: `24576`
                   - CM_BENCHMARK: `STANDALONE_OBJECT_DETECTION`

        </details>


      * Group "**nsp**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_nsp.#`
        * `_nsp.14`
        * `_nsp.16`

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

        * `_fp16`
        * `_fp32`
               - ENV variables:
                   - CM_IMAGENET_ACCURACY_DTYPE: `float32`
        * `_uint8`

        </details>


      * Group "**run-mode**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_network-client`
               - ENV variables:
                   - CM_RUN_MODE: `network-client`
        * `_network-server`
               - ENV variables:
                   - CM_RUN_MODE: `network-server`
        * **`_standalone`** (default)
               - ENV variables:
                   - CM_RUN_MODE: `standalone`

        </details>


      * Group "**sut**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_dl2q.24xlarge`
               - ENV variables:
                   - CM_QAIC_DEVICES: `0,1,2,3,4,5,6,7`
                   - qaic_queue_length: `4`
        * `_rb6`
               - ENV variables:
                   - CM_QAIC_DEVICES: `0`
                   - qaic_queue_length: `6`

        </details>


    ##### Default variations

    `_cpu,_onnxruntime,_resnet50,_standalone`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
    * `--devices=value`  &rarr;  `CM_QAIC_DEVICES=value`
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
    * CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `kilt`
    * CM_MLPERF_SKIP_RUN: `no`
    * CM_KILT_REPO_URL: `https://github.com/GATEOverflow/kilt-mlperf`
    * CM_QAIC_DEVICES: `0`
    * kilt_max_wait_abs: `10000`
    * verbosity: `0`
    * loadgen_trigger_cold_run: `0`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-qualcomm/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "reproduce mlcommons mlperf inference harness qualcomm-harness qualcomm kilt-harness kilt [variations]" [--input_flags] -j
```