# get-tvm-model
Automatically generated README for this automation recipe: **get-tvm-model**

Category: **[AI/ML models](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-tvm-model/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-tvm-model/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model-tvm tvm-model" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,ml-model-tvm,tvm-model[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get ml-model-tvm tvm-model [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model-tvm,tvm-model'
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
    cm docker script "get ml-model-tvm tvm-model[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_tune-model`
               - ENV variables:
                   - CM_TUNE_TVM_MODEL: `yes`

        </details>


      * Group "**batchsize**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_batch_size.#`
               - ENV variables:
                   - CM_ML_MODEL_MAX_BATCH_SIZE: `#`

        </details>


      * Group "**frontend**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_onnx`** (default)
               - ENV variables:
                   - CM_TVM_FRONTEND_FRAMEWORK: `onnx`
        * `_pytorch`
              - Aliases: `_torch`
               - ENV variables:
                   - CM_TVM_FRONTEND_FRAMEWORK: `pytorch`
        * `_tensorflow`
              - Aliases: `_tf`
               - ENV variables:
                   - CM_TVM_FRONTEND_FRAMEWORK: `tensorflow`
        * `_tflite`
               - ENV variables:
                   - CM_TVM_FRONTEND_FRAMEWORK: `tflite`

        </details>


      * Group "**model**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_model.#`
               - ENV variables:
                   - CM_ML_MODEL: `#`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_fp32`** (default)
        * `_int8`
        * `_uint8`

        </details>


      * Group "**runtime**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_graph_executor`
               - ENV variables:
                   - CM_TVM_USE_VM: `no`
        * **`_virtual_machine`** (default)
               - ENV variables:
                   - CM_TVM_USE_VM: `yes`

        </details>


    ##### Default variations

    `_fp32,_onnx,_virtual_machine`
=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_ML_MODEL_MAX_BATCH_SIZE: `1`
    * CM_TUNE_TVM_MODEL: `no`
    * CM_TVM_USE_VM: `yes`
    * CM_TVM_FRONTEND_FRAMEWORK: `onnx`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-tvm-model/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get ml-model-tvm tvm-model [variations]"  -j
```