# generate-nvidia-engine
Automatically generated README for this automation recipe: **generate-nvidia-engine**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**



---

This CM script is in draft stage

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/generate-nvidia-engine/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "generate engine mlperf inference nvidia" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=generate,engine,mlperf,inference,nvidia[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "generate engine mlperf inference nvidia [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'generate,engine,mlperf,inference,nvidia'
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
    cm docker script "generate engine mlperf inference nvidia[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_batch_size.#`
               - ENV variables:
                   - CM_MODEL_BATCH_SIZE: `None`
        * `_copy_streams.#`
               - ENV variables:
                   - CM_GPU_COPY_STREAMS: `None`
        * `_cuda`
               - ENV variables:
                   - CM_MLPERF_DEVICE: `gpu`
                   - CM_MLPERF_DEVICE_LIB_NAMESPEC: `cudart`

        </details>


      * Group "**device**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_cpu`** (default)
               - ENV variables:
                   - CM_MLPERF_DEVICE: `cpu`

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

    `_cpu,_resnet50`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--output_dir=value`  &rarr;  `CM_MLPERF_OUTPUT_DIR=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_BATCH_COUNT: `1`
    * CM_BATCH_SIZE: `1`
    * CM_LOADGEN_SCENARIO: `Offline`
    * CM_GPU_COPY_STREAMS: `1`
    * CM_TENSORRT_WORKSPACE_SIZE: `4194304`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/generate-nvidia-engine/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "generate engine mlperf inference nvidia [variations]" [--input_flags] -j
```