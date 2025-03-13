# get-ml-model-gptj
Automatically generated README for this automation recipe: **get-ml-model-gptj**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-gptj/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get raw ml-model gptj gpt-j large-language-model" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,raw,ml-model,gptj,gpt-j,large-language-model[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get raw ml-model gptj gpt-j large-language-model [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,raw,ml-model,gptj,gpt-j,large-language-model'
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
    cm docker script "get raw ml-model gptj gpt-j large-language-model[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_batch_size.#`
               - ENV variables:
                   - CM_ML_MODEL_BATCH_SIZE: `#`

        </details>


      * Group "**download-tool**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_rclone`** (default)
               - ENV variables:
                   - CM_DOWNLOAD_FILENAME: `checkpoint`
                   - CM_DOWNLOAD_URL: `<<<CM_RCLONE_URL>>>`
        * `_wget`
               - ENV variables:
                   - CM_DOWNLOAD_URL: `<<<CM_PACKAGE_URL>>>`
                   - CM_DOWNLOAD_FILENAME: `checkpoint.zip`

        </details>


      * Group "**framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_pytorch`** (default)
               - ENV variables:
                   - CM_ML_MODEL_DATA_LAYOUT: `NCHW`
                   - CM_ML_MODEL_FRAMEWORK: `pytorch`
                   - CM_ML_STARTING_WEIGHTS_FILENAME: `<<<CM_PACKAGE_URL>>>`
        * `_saxml`

        </details>


      * Group "**model-provider**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_intel`
        * **`_mlcommons`** (default)
        * `_nvidia`
               - ENV variables:
                   - CM_TMP_ML_MODEL_PROVIDER: `nvidia`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_fp32`
               - ENV variables:
                   - CM_ML_MODEL_INPUT_DATA_TYPES: `fp32`
                   - CM_ML_MODEL_PRECISION: `fp32`
                   - CM_ML_MODEL_WEIGHT_DATA_TYPES: `fp32`
        * `_fp8`
               - ENV variables:
                   - CM_ML_MODEL_INPUT_DATA_TYPES: `fp8`
                   - CM_ML_MODEL_WEIGHT_DATA_TYPES: `fp8`
        * `_int4`
               - ENV variables:
                   - CM_ML_MODEL_INPUT_DATA_TYPES: `int4`
                   - CM_ML_MODEL_WEIGHT_DATA_TYPES: `int4`
        * `_int8`
               - ENV variables:
                   - CM_ML_MODEL_INPUT_DATA_TYPES: `int8`
                   - CM_ML_MODEL_PRECISION: `int8`
                   - CM_ML_MODEL_WEIGHT_DATA_TYPES: `int8`
        * `_uint8`
               - ENV variables:
                   - CM_ML_MODEL_INPUT_DATA_TYPES: `uint8`
                   - CM_ML_MODEL_PRECISION: `uint8`
                   - CM_ML_MODEL_WEIGHT_DATA_TYPES: `uint8`

        </details>


    ##### Default variations

    `_mlcommons,_pytorch,_rclone`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--checkpoint=value`  &rarr;  `GPTJ_CHECKPOINT_PATH=value`
    * `--download_path=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
    * `--to=value`  &rarr;  `CM_DOWNLOAD_PATH=value`




#### Native script being run
=== "Linux/macOS"
     * [run-int4-calibration.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-gptj/run-int4-calibration.sh)
     * [run-intel.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-gptj/run-intel.sh)
     * [run-nvidia.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-gptj/run-nvidia.sh)
     * [run-saxml-quantized.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-gptj/run-saxml-quantized.sh)
     * [run-saxml.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-gptj/run-saxml.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get raw ml-model gptj gpt-j large-language-model [variations]" [--input_flags] -j
```