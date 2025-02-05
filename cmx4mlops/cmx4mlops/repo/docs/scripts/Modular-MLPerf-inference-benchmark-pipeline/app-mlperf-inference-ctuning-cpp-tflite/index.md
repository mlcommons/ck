# app-mlperf-inference-ctuning-cpp-tflite
Automatically generated README for this automation recipe: **app-mlperf-inference-ctuning-cpp-tflite**

Category: **[Modular MLPerf inference benchmark pipeline](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-ctuning-cpp-tflite/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "app mlperf inference tflite-cpp" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=app,mlperf,inference,tflite-cpp[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "app mlperf inference tflite-cpp [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,mlperf,inference,tflite-cpp'
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
    cm docker script "app mlperf inference tflite-cpp[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_armnn`
               - ENV variables:
                   - CM_MLPERF_TFLITE_USE_ARMNN: `yes`
                   - CM_TMP_LINK_LIBS: `tensorflowlite,armnn`

        </details>


      * Group "**backend**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_tf`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tf`
        * **`_tflite`** (default)
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tflite`
                   - CM_MLPERF_BACKEND_VERSION: `master`
                   - CM_TMP_LINK_LIBS: `tensorflowlite`
                   - CM_TMP_SRC_FOLDER: `src`

        </details>


      * Group "**device**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_cpu`** (default)
               - ENV variables:
                   - CM_MLPERF_DEVICE: `cpu`
        * `_gpu`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `gpu`
                   - CM_MLPERF_DEVICE_LIB_NAMESPEC: `cudart`

        </details>


      * Group "**loadgen-scenario**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_singlestream`** (default)
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `SingleStream`

        </details>


      * Group "**model**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_efficientnet`
               - ENV variables:
                   - CM_MODEL: `efficientnet`
        * `_mobilenet`
               - ENV variables:
                   - CM_MODEL: `mobilenet`
        * **`_resnet50`** (default)
               - ENV variables:
                   - CM_MODEL: `resnet50`

        </details>


      * Group "**optimization-target**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_use-neon`
               - ENV variables:
                   - CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX1: `using_neon`
                   - CM_MLPERF_TFLITE_USE_NEON: `1`
        * `_use-opencl`
               - ENV variables:
                   - CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX1: `using_opencl`
                   - CM_MLPERF_TFLITE_USE_OPENCL: `1`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_fp32`** (default)
               - ENV variables:
                   - CM_MLPERF_MODEL_PRECISION: `float32`
        * `_int8`
               - ENV variables:
                   - CM_DATASET_COMPRESSED: `on`
                   - CM_MLPERF_MODEL_PRECISION: `int8`
        * `_uint8`
               - ENV variables:
                   - CM_DATASET_COMPRESSED: `on`
                   - CM_MLPERF_MODEL_PRECISION: `uint8`

        </details>


    ##### Default variations

    `_cpu,_fp32,_resnet50,_singlestream,_tflite`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--compressed_dataset=value`  &rarr;  `CM_DATASET_COMPRESSED=value`
    * `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
    * `--mlperf_conf=value`  &rarr;  `CM_MLPERF_CONF=value`
    * `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
    * `--output_dir=value`  &rarr;  `CM_MLPERF_OUTPUT_DIR=value`
    * `--performance_sample_count=value`  &rarr;  `CM_MLPERF_LOADGEN_PERFORMANCE_SAMPLE_COUNT=value`
    * `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
    * `--user_conf=value`  &rarr;  `CM_MLPERF_USER_CONF=value`
    * `--verbose=value`  &rarr;  `CM_VERBOSE=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_DATASET_COMPRESSED: `off`
    * CM_DATASET_INPUT_SQUARE_SIDE: `224`
    * CM_FAST_COMPILATION: `yes`
    * CM_LOADGEN_BUFFER_SIZE: `1024`
    * CM_MLPERF_LOADGEN_MODE: `accuracy`
    * CM_MLPERF_LOADGEN_SCENARIO: `SingleStream`
    * CM_MLPERF_LOADGEN_TRIGGER_COLD_RUN: `0`
    * CM_MLPERF_OUTPUT_DIR: `.`
    * CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `tflite_cpp`
    * CM_MLPERF_TFLITE_USE_NEON: `0`
    * CM_MLPERF_TFLITE_USE_OPENCL: `0`
    * CM_ML_MODEL_GIVEN_CHANNEL_MEANS: `123.68 116.78 103.94`
    * CM_ML_MODEL_NORMALIZE_DATA: `0`
    * CM_ML_MODEL_SUBTRACT_MEANS: `1`
    * CM_VERBOSE: `0`



___
#### Script output
```bash
cmr "app mlperf inference tflite-cpp [variations]" [--input_flags] -j
```