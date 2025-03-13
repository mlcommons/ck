# app-mlperf-training-nvidia
Automatically generated README for this automation recipe: **app-mlperf-training-nvidia**

Category: **[Modular MLPerf training benchmark pipeline](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-training-nvidia/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "app vision language mlcommons mlperf training nvidia" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=app,vision,language,mlcommons,mlperf,training,nvidia[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "app vision language mlcommons mlperf training nvidia [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,vision,language,mlcommons,mlperf,training,nvidia'
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
    cm docker script "app vision language mlcommons mlperf training nvidia[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_bert`
               - ENV variables:
                   - CM_MLPERF_MODEL: `bert`

        </details>


      * Group "**device**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_cuda`** (default)
               - ENV variables:
                   - CM_MLPERF_DEVICE: `cuda`
                   - USE_CUDA: `True`
        * `_tpu`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `tpu`
                   - CUDA_VISIBLE_DEVICES: ``
                   - USE_CUDA: `False`

        </details>


      * Group "**framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_pytorch`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `pytorch`
                   - CM_MLPERF_BACKEND_VERSION: `<<<CM_TORCH_VERSION>>>`
        * `_tf`
              - Aliases: `_tensorflow`
               - ENV variables:
                   - CM_MLPERF_BACKEND: `tf`
                   - CM_MLPERF_BACKEND_VERSION: `<<<CM_TENSORFLOW_VERSION>>>`

        </details>


    ##### Default variations

    `_cuda`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--clean=value`  &rarr;  `CM_MLPERF_CLEAN_SUBMISSION_DIR=value`
    * `--docker=value`  &rarr;  `CM_RUN_DOCKER_CONTAINER=value`
    * `--hw_name=value`  &rarr;  `CM_HW_NAME=value`
    * `--model=value`  &rarr;  `CM_MLPERF_CUSTOM_MODEL_PATH=value`
    * `--num_threads=value`  &rarr;  `CM_NUM_THREADS=value`
    * `--output_dir=value`  &rarr;  `OUTPUT_BASE_DIR=value`
    * `--rerun=value`  &rarr;  `CM_RERUN=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `nvidia`



#### Native script being run
=== "Linux/macOS"
     * [run-bert-training.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-training-nvidia/run-bert-training.sh)
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-training-nvidia/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "app vision language mlcommons mlperf training nvidia [variations]" [--input_flags] -j
```