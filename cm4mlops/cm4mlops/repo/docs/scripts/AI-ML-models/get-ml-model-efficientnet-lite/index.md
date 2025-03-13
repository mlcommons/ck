# get-ml-model-efficientnet-lite
Automatically generated README for this automation recipe: **get-ml-model-efficientnet-lite**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-efficientnet-lite/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model efficientnet raw ml-model-efficientnet ml-model-efficientnet-lite lite tflite image-classification" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,ml-model,efficientnet,raw,ml-model-efficientnet,ml-model-efficientnet-lite,lite,tflite,image-classification[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get ml-model efficientnet raw ml-model-efficientnet ml-model-efficientnet-lite lite tflite image-classification [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,efficientnet,raw,ml-model-efficientnet,ml-model-efficientnet-lite,lite,tflite,image-classification'
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
    cm docker script "get ml-model efficientnet raw ml-model-efficientnet ml-model-efficientnet-lite lite tflite image-classification[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_tflite`

        </details>


      * Group "**kind**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_lite0`** (default)
               - ENV variables:
                   - CM_ML_MODEL_EFFICIENTNET_LITE_KIND: `lite0`
        * `_lite1`
               - ENV variables:
                   - CM_ML_MODEL_EFFICIENTNET_LITE_KIND: `lite1`
        * `_lite2`
               - ENV variables:
                   - CM_ML_MODEL_EFFICIENTNET_LITE_KIND: `lite2`
        * `_lite3`
               - ENV variables:
                   - CM_ML_MODEL_EFFICIENTNET_LITE_KIND: `lite3`
        * `_lite4`
               - ENV variables:
                   - CM_ML_MODEL_EFFICIENTNET_LITE_KIND: `lite4`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_fp32`** (default)
               - ENV variables:
                   - CM_ML_MODEL_EFFICIENTNET_LITE_PRECISION: `fp32`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_PRECISION: `fp32`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp32`
        * `_uint8`
              - Aliases: `_int8`
               - ENV variables:
                   - CM_ML_MODEL_EFFICIENTNET_LITE_PRECISION: `int8`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `uint8`
                   - CM_ML_MODEL_PRECISION: `uint8`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `uint8`

        </details>


      * Group "**resolution**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_resolution-224`** (default)
               - ENV variables:
                   - CM_ML_MODEL_IMAGE_HEIGHT: `224`
                   - CM_ML_MODEL_IMAGE_WIDTH: `224`
                   - CM_ML_MODEL_MOBILENET_RESOLUTION: `224`
                   - CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS: `_resolution.224`
        * `_resolution-240`
               - ENV variables:
                   - CM_ML_MODEL_IMAGE_HEIGHT: `240`
                   - CM_ML_MODEL_IMAGE_WIDTH: `240`
                   - CM_ML_MODEL_MOBILENET_RESOLUTION: `240`
                   - CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS: `_resolution.240`
        * `_resolution-260`
               - ENV variables:
                   - CM_ML_MODEL_IMAGE_HEIGHT: `260`
                   - CM_ML_MODEL_IMAGE_WIDTH: `260`
                   - CM_ML_MODEL_MOBILENET_RESOLUTION: `260`
                   - CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS: `_resolution.260`
        * `_resolution-280`
               - ENV variables:
                   - CM_ML_MODEL_IMAGE_HEIGHT: `280`
                   - CM_ML_MODEL_IMAGE_WIDTH: `280`
                   - CM_ML_MODEL_MOBILENET_RESOLUTION: `280`
                   - CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS: `_resolution.280`
        * `_resolution-300`
               - ENV variables:
                   - CM_ML_MODEL_IMAGE_HEIGHT: `300`
                   - CM_ML_MODEL_IMAGE_WIDTH: `300`
                   - CM_ML_MODEL_MOBILENET_RESOLUTION: `300`
                   - CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS: `_resolution.300`

        </details>


    ##### Default variations

    `_fp32,_lite0,_resolution-224`
=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
    * CM_ML_MODEL_PRECISION: `fp32`
    * CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp32`



___
#### Script output
```bash
cmr "get ml-model efficientnet raw ml-model-efficientnet ml-model-efficientnet-lite lite tflite image-classification [variations]"  -j
```