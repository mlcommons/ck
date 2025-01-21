# app-mlperf-inference-mlcommons-python
Automatically generated README for this automation recipe: **app-mlperf-inference-mlcommons-python**

Category: **[Modular MLPerf inference benchmark pipeline](..)**

License: **Apache 2.0**

Developers: [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh), [Thomas Zhu](https://www.linkedin.com/in/hanwen-zhu-483614189), [Grigori Fursin](https://cKnowledge.org/gfursin)
* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-mlcommons-python/README-extra.md)


---

This portable CM script is being developed by the [MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)
to modularize the *python reference implementations* of the [MLPerf inference benchmark](https://github.com/mlcommons/inference) 
using the [MLCommons CM automation meta-framework](https://github.com/mlcommons/ck).
The goal is to make it easier to run, optimize and reproduce MLPerf benchmarks 
across diverse platforms with continuously changing software and hardware.

See the current coverage of different models, devices and backends [here](README-extra.md#current-coverage).

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-mlcommons-python/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "app vision language mlcommons mlperf inference reference ref" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=app,vision,language,mlcommons,mlperf,inference,reference,ref[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "app vision language mlcommons mlperf inference reference ref [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,vision,language,mlcommons,mlperf,inference,reference,ref'
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
    cm docker script "app vision language mlcommons mlperf inference reference ref[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_3d-unet`
               - ENV variables:
                   - CM_TMP_IGNORE_MLPERF_QUERY_COUNT: `True`
                   - CM_MLPERF_MODEL_SKIP_BATCHING: `True`
        * `_beam_size.#`
               - ENV variables:
                   - GPTJ_BEAM_SIZE: `#`
        * `_bert`
               - ENV variables:
                   - CM_MLPERF_MODEL_SKIP_BATCHING: `True`
        * `_dlrm`
               - ENV variables:
                   - CM_MLPERF_MODEL_SKIP_BATCHING: `True`
        * `_multistream`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `MultiStream`
        * `_offline`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `Offline`
        * `_r2.1_default`
               - ENV variables:
                   - CM_RERUN: `yes`
                   - CM_SKIP_SYS_UTILS: `yes`
                   - CM_TEST_QUERY_COUNT: `100`
        * `_server`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `Server`
        * `_singlestream`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `SingleStream`

        </details>


      * Group "**batch-size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_batch_size.#`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_MAX_BATCHSIZE: `#`

        </details>


      * Group "**device**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_cpu`** (default)
               - ENV variables:
                   - CM_MLPERF_DEVICE: `cpu`
                   - CUDA_VISIBLE_DEVICES: ``
                   - USE_CUDA: `False`
                   - USE_GPU: `False`
        * `_cuda`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `gpu`
                   - USE_CUDA: `True`
                   - USE_GPU: `True`
        * `_rocm`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `rocm`
                   - USE_GPU: `True`
        * `_tpu`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `tpu`

        </details>


      * Group "**framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_deepsparse`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `deepsparse`
                   - CM_MLPERF_BACKEND_VERSION: `<<<CM_DEEPSPARSE_VERSION>>>`
        * `_ncnn`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `ncnn`
                   - CM_MLPERF_BACKEND_VERSION: `<<<CM_NCNN_VERSION>>>`
                   - CM_MLPERF_VISION_DATASET_OPTION: `imagenet_pytorch`
        * **`_onnxruntime`** (default)
               - ENV variables:
                   - CM_MLPERF_BACKEND: `onnxruntime`
        * `_pytorch`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `pytorch`
                   - CM_MLPERF_BACKEND_VERSION: `<<<CM_TORCH_VERSION>>>`
        * `_ray`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `ray`
                   - CM_MLPERF_BACKEND_VERSION: `<<<CM_TORCH_VERSION>>>`
        * `_tf`
              - Aliases: `_tensorflow`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tf`
                   - CM_MLPERF_BACKEND_VERSION: `<<<CM_TENSORFLOW_VERSION>>>`
        * `_tflite`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tflite`
                   - CM_MLPERF_BACKEND_VERSION: `<<<CM_TFLITE_VERSION>>>`
                   - CM_MLPERF_VISION_DATASET_OPTION: `imagenet_tflite_tpu`
        * `_tvm-onnx`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tvm-onnx`
                   - CM_MLPERF_BACKEND_VERSION: `<<<CM_ONNXRUNTIME_VERSION>>>`
        * `_tvm-pytorch`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tvm-pytorch`
                   - CM_MLPERF_BACKEND_VERSION: `<<<CM_TORCH_VERSION>>>`
                   - CM_PREPROCESS_PYTORCH: `yes`
                   - MLPERF_TVM_TORCH_QUANTIZED_ENGINE: `qnnpack`
        * `_tvm-tflite`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tvm-tflite`
                   - CM_MLPERF_BACKEND_VERSION: `<<<CM_TVM-TFLITE_VERSION>>>`

        </details>


      * Group "**implementation**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_python`** (default)
               - ENV variables:
                   - CM_MLPERF_PYTHON: `yes`
                   - CM_MLPERF_IMPLEMENTATION: `reference`

        </details>


      * Group "**models**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_3d-unet-99`
               - ENV variables:
                   - CM_MODEL: `3d-unet-99`
        * `_3d-unet-99.9`
               - ENV variables:
                   - CM_MODEL: `3d-unet-99.9`
        * `_bert-99`
               - ENV variables:
                   - CM_MODEL: `bert-99`
        * `_bert-99.9`
               - ENV variables:
                   - CM_MODEL: `bert-99.9`
        * `_dlrm-99`
               - ENV variables:
                   - CM_MODEL: `dlrm-99`
        * `_dlrm-99.9`
               - ENV variables:
                   - CM_MODEL: `dlrm-99.9`
        * `_gptj-99`
               - ENV variables:
                   - CM_MODEL: `gptj-99`
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
                   - CM_MLPERF_USE_MLCOMMONS_RUN_SCRIPT: `yes`
        * `_retinanet`
               - ENV variables:
                   - CM_MODEL: `retinanet`
                   - CM_MLPERF_USE_MLCOMMONS_RUN_SCRIPT: `yes`
                   - CM_MLPERF_LOADGEN_MAX_BATCHSIZE: `1`
        * `_rnnt`
               - ENV variables:
                   - CM_MODEL: `rnnt`
                   - CM_MLPERF_MODEL_SKIP_BATCHING: `True`
                   - CM_TMP_IGNORE_MLPERF_QUERY_COUNT: `True`
        * `_sdxl`
               - ENV variables:
                   - CM_MODEL: `stable-diffusion-xl`
                   - CM_NUM_THREADS: `1`

        </details>


      * Group "**network**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_network-lon`
               - ENV variables:
                   - CM_NETWORK_LOADGEN: `lon`
                   - CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX1: `network_loadgen`
        * `_network-sut`
               - ENV variables:
                   - CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX1: `network_sut`
                   - CM_NETWORK_LOADGEN: `sut`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_bfloat16`
               - ENV variables:
                   - CM_MLPERF_QUANTIZATION: `False`
                   - CM_MLPERF_MODEL_PRECISION: `bfloat16`
        * `_float16`
               - ENV variables:
                   - CM_MLPERF_QUANTIZATION: `False`
                   - CM_MLPERF_MODEL_PRECISION: `float16`
        * **`_fp32`** (default)
               - ENV variables:
                   - CM_MLPERF_QUANTIZATION: `False`
                   - CM_MLPERF_MODEL_PRECISION: `float32`
        * `_int8`
              - Aliases: `_quantized`
               - ENV variables:
                   - CM_MLPERF_QUANTIZATION: `True`
                   - CM_MLPERF_MODEL_PRECISION: `int8`

        </details>


    ##### Default variations

    `_cpu,_fp32,_onnxruntime,_python,_resnet50`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--clean=value`  &rarr;  `CM_MLPERF_CLEAN_SUBMISSION_DIR=value`
    * `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
    * `--dataset=value`  &rarr;  `CM_MLPERF_VISION_DATASET_OPTION=value`
    * `--dataset_args=value`  &rarr;  `CM_MLPERF_EXTRA_DATASET_ARGS=value`
    * `--docker=value`  &rarr;  `CM_RUN_DOCKER_CONTAINER=value`
    * `--hw_name=value`  &rarr;  `CM_HW_NAME=value`
    * `--imagenet_path=value`  &rarr;  `IMAGENET_PATH=value`
    * `--max_amps=value`  &rarr;  `CM_MLPERF_POWER_MAX_AMPS=value`
    * `--max_batchsize=value`  &rarr;  `CM_MLPERF_LOADGEN_MAX_BATCHSIZE=value`
    * `--max_volts=value`  &rarr;  `CM_MLPERF_POWER_MAX_VOLTS=value`
    * `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
    * `--model=value`  &rarr;  `CM_MLPERF_CUSTOM_MODEL_PATH=value`
    * `--multistream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY=value`
    * `--network=value`  &rarr;  `CM_NETWORK_LOADGEN=value`
    * `--ntp_server=value`  &rarr;  `CM_MLPERF_POWER_NTP_SERVER=value`
    * `--num_threads=value`  &rarr;  `CM_NUM_THREADS=value`
    * `--offline_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS=value`
    * `--output_dir=value`  &rarr;  `OUTPUT_BASE_DIR=value`
    * `--power=value`  &rarr;  `CM_MLPERF_POWER=value`
    * `--power_server=value`  &rarr;  `CM_MLPERF_POWER_SERVER_ADDRESS=value`
    * `--regenerate_files=value`  &rarr;  `CM_REGENERATE_MEASURE_FILES=value`
    * `--rerun=value`  &rarr;  `CM_RERUN=value`
    * `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
    * `--server_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_SERVER_TARGET_QPS=value`
    * `--singlestream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY=value`
    * `--sut_servers=value`  &rarr;  `CM_NETWORK_LOADGEN_SUT_SERVERS=value`
    * `--target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_LATENCY=value`
    * `--target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_QPS=value`
    * `--test_query_count=value`  &rarr;  `CM_TEST_QUERY_COUNT=value`
    * `--threads=value`  &rarr;  `CM_NUM_THREADS=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_MLPERF_LOADGEN_MODE: `accuracy`
    * CM_MLPERF_LOADGEN_SCENARIO: `Offline`
    * CM_OUTPUT_FOLDER_NAME: `test_results`
    * CM_MLPERF_RUN_STYLE: `test`
    * CM_TEST_QUERY_COUNT: `10`
    * CM_MLPERF_QUANTIZATION: `False`
    * CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `reference`
    * CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX: ``



___
#### Script output
```bash
cmr "app vision language mlcommons mlperf inference reference ref [variations]" [--input_flags] -j
```