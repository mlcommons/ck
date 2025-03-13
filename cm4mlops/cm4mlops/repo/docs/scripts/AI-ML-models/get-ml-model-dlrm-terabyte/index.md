# get-ml-model-dlrm-terabyte
Automatically generated README for this automation recipe: **get-ml-model-dlrm-terabyte**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-dlrm-terabyte/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model dlrm raw terabyte criteo-terabyte criteo recommendation" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,ml-model,dlrm,raw,terabyte,criteo-terabyte,criteo,recommendation[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get ml-model dlrm raw terabyte criteo-terabyte criteo recommendation [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,dlrm,raw,terabyte,criteo-terabyte,criteo,recommendation'
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
    cm docker script "get ml-model dlrm raw terabyte criteo-terabyte criteo recommendation[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_debug`
               - ENV variables:
                   - CM_ML_MODEL_DEBUG: `yes`

        </details>


      * Group "**download-tool**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_rclone`
        * `_wget`

        </details>


      * Group "**framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_onnx`
               - ENV variables:
                   - CM_ML_MODEL_FRAMEWORK: `onnx`
        * **`_pytorch`** (default)
               - ENV variables:
                   - CM_ML_MODEL_FRAMEWORK: `pytorch`
                   - CM_TMP_MODEL_ADDITIONAL_NAME: `dlrm_terabyte.pytorch`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_fp32`** (default)
               - ENV variables:
                   - CM_ML_MODEL_INPUT_DATA_TYPES: `fp32`
                   - CM_ML_MODEL_PRECISION: `fp32`
                   - CM_ML_MODEL_WEIGHT_DATA_TYPES: `fp32`

        </details>


      * Group "**type**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_weight_sharded`** (default)
               - ENV variables:
                   - CM_DLRM_MULTIHOT_MODEL: `yes`

        </details>


    ##### Default variations

    `_fp32,_pytorch,_weight_sharded`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--dir=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
    * `--download_path=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
    * `--to=value`  &rarr;  `CM_DOWNLOAD_PATH=value`




#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-dlrm-terabyte/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get ml-model dlrm raw terabyte criteo-terabyte criteo recommendation [variations]" [--input_flags] -j
```