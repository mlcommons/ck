# app-mlperf-inference-mlcommons-cpp
Automatically generated README for this automation recipe: **app-mlperf-inference-mlcommons-cpp**

Category: **[Modular MLPerf inference benchmark pipeline](..)**

License: **Apache 2.0**

Developers: [Thomas Zhu](https://www.linkedin.com/in/hanwen-zhu-483614189), [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh), [Grigori Fursin](https://cKnowledge.org/gfursin)
* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-mlcommons-cpp/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-mlcommons-cpp/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "app mlcommons mlperf inference cpp" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=app,mlcommons,mlperf,inference,cpp[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "app mlcommons mlperf inference cpp [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,mlcommons,mlperf,inference,cpp'
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
    cm docker script "app mlcommons mlperf inference cpp[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * Group "**batch-size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_batch-size.#`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_MAX_BATCHSIZE: `#`

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


      * Group "**framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_onnxruntime`** (default)
               - ENV variables:
                   - CM_MLPERF_BACKEND: `onnxruntime`
                   - CM_MLPERF_BACKEND_LIB_NAMESPEC: `onnxruntime`
        * `_pytorch`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `pytorch`
        * `_tf`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tf`
        * `_tflite`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tflite`
        * `_tvm-onnx`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tvm-onnx`

        </details>


      * Group "**loadgen-scenario**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_multistream`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `MultiStream`
        * **`_offline`** (default)
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `Offline`
        * `_server`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `Server`
        * `_singlestream`
               - ENV variables:
                   - CM_MLPERF_LOADGEN_SCENARIO: `SingleStream`
                   - CM_MLPERF_LOADGEN_MAX_BATCHSIZE: `1`

        </details>


      * Group "**model**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_resnet50`** (default)
               - ENV variables:
                   - CM_MODEL: `resnet50`
        * `_retinanet`
               - ENV variables:
                   - CM_MODEL: `retinanet`

        </details>


    ##### Default variations

    `_cpu,_offline,_onnxruntime,_resnet50`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
    * `--max_batchsize=value`  &rarr;  `CM_MLPERF_LOADGEN_MAX_BATCHSIZE=value`
    * `--mlperf_conf=value`  &rarr;  `CM_MLPERF_CONF=value`
    * `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
    * `--output_dir=value`  &rarr;  `CM_MLPERF_OUTPUT_DIR=value`
    * `--performance_sample_count=value`  &rarr;  `CM_MLPERF_LOADGEN_PERFORMANCE_SAMPLE_COUNT=value`
    * `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
    * `--user_conf=value`  &rarr;  `CM_MLPERF_USER_CONF=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_BATCH_COUNT: `1`
    * CM_BATCH_SIZE: `1`
    * CM_FAST_COMPILATION: `yes`
    * CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `cpp`



___
#### Script output
```bash
cmr "app mlcommons mlperf inference cpp [variations]" [--input_flags] -j
```