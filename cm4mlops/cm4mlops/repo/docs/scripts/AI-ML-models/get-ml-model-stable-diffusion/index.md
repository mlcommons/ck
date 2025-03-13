# get-ml-model-stable-diffusion
Automatically generated README for this automation recipe: **get-ml-model-stable-diffusion**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-stable-diffusion/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get raw ml-model stable-diffusion sdxl text-to-image" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,raw,ml-model,stable-diffusion,sdxl,text-to-image[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get raw ml-model stable-diffusion sdxl text-to-image [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,raw,ml-model,stable-diffusion,sdxl,text-to-image'
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
    cm docker script "get raw ml-model stable-diffusion sdxl text-to-image[variations]" [--input_flags]
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


      * Group "**download-source**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_huggingface`
        * **`_mlcommons`** (default)

        </details>


      * Group "**download-tool**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_git`
               - ENV variables:
                   - CM_DOWNLOAD_TOOL: `git`
        * `_rclone`
               - ENV variables:
                   - CM_RCLONE_CONFIG_CMD: `rclone config create mlc-inference s3 provider=Cloudflare access_key_id=f65ba5eef400db161ea49967de89f47b secret_access_key=fbea333914c292b854f14d3fe232bad6c5407bf0ab1bebf78833c2b359bdfd2b endpoint=https://c2686074cb2caf5cbaf6d134bdba8b47.r2.cloudflarestorage.com`
                   - CM_DOWNLOAD_TOOL: `rclone`
        * `_wget`
               - ENV variables:
                   - CM_DOWNLOAD_TOOL: `wget`

        </details>


      * Group "**framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_pytorch`** (default)
               - ENV variables:
                   - CM_ML_MODEL_FRAMEWORK: `pytorch`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_fp16`
               - ENV variables:
                   - CM_ML_MODEL_INPUT_DATA_TYPES: `fp16`
                   - CM_ML_MODEL_PRECISION: `fp16`
                   - CM_ML_MODEL_WEIGHT_DATA_TYPES: `fp16`
        * **`_fp32`** (default)
               - ENV variables:
                   - CM_ML_MODEL_INPUT_DATA_TYPES: `fp32`
                   - CM_ML_MODEL_PRECISION: `fp32`
                   - CM_ML_MODEL_WEIGHT_DATA_TYPES: `fp32`
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

    `_fp32,_mlcommons,_pytorch`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--checkpoint=value`  &rarr;  `SDXL_CHECKPOINT_PATH=value`
    * `--download_path=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
    * `--to=value`  &rarr;  `CM_DOWNLOAD_PATH=value`




___
#### Script output
```bash
cmr "get raw ml-model stable-diffusion sdxl text-to-image [variations]" [--input_flags] -j
```