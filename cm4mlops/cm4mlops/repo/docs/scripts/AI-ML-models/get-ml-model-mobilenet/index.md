# get-ml-model-mobilenet
Automatically generated README for this automation recipe: **get-ml-model-mobilenet**

Category: **[AI/ML models](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-mobilenet/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-mobilenet/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model mobilenet raw ml-model-mobilenet image-classification" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,ml-model,mobilenet,raw,ml-model-mobilenet,image-classification[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get ml-model mobilenet raw ml-model-mobilenet image-classification [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,mobilenet,raw,ml-model-mobilenet,image-classification'
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
    cm docker script "get ml-model mobilenet raw ml-model-mobilenet image-classification[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_tflite`

        </details>


      * Group "**framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_onnx`
               - ENV variables:
                   - CM_ML_MODEL_DATA_LAYOUT: `NCHW`
                   - CM_ML_MODEL_FRAMEWORK: `onnx`
        * **`_tf`** (default)
               - ENV variables:
                   - CM_ML_MODEL_DATA_LAYOUT: `NHWC`
                   - CM_ML_MODEL_NORMALIZE_DATA: `yes`
                   - CM_ML_MODEL_SUBTRACT_MEANS: `no`
                   - CM_ML_MODEL_INPUT_LAYER_NAME: `input`

        </details>


      * Group "**kind**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_large`
               - ENV variables:
                   - CM_ML_MODEL_MOBILENET_KIND: `large`
        * `_large-minimalistic`
               - ENV variables:
                   - CM_ML_MODEL_MOBILENET_KIND: `large-minimalistic`
        * `_small`
               - ENV variables:
                   - CM_ML_MODEL_MOBILENET_KIND: `small`
        * `_small-minimalistic`
               - ENV variables:
                   - CM_ML_MODEL_MOBILENET_KIND: `small-minimalistic`

        </details>


      * Group "**multiplier**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_multiplier-0.25`
               - ENV variables:
                   - CM_ML_MODEL_MOBILENET_MULTIPLIER: `0.25`
                   - CM_ML_MODEL_MOBILENET_MULTIPLIER_PERCENTAGE: `25`
        * `_multiplier-0.35`
               - ENV variables:
                   - CM_ML_MODEL_MOBILENET_MULTIPLIER: `0.35`
                   - CM_ML_MODEL_MOBILENET_MULTIPLIER_PERCENTAGE: `35`
        * `_multiplier-0.5`
               - ENV variables:
                   - CM_ML_MODEL_MOBILENET_MULTIPLIER: `0.5`
                   - CM_ML_MODEL_MOBILENET_MULTIPLIER_PERCENTAGE: `50`
        * `_multiplier-0.75`
               - ENV variables:
                   - CM_ML_MODEL_MOBILENET_MULTIPLIER: `0.75`
                   - CM_ML_MODEL_MOBILENET_MULTIPLIER_PERCENTAGE: `75`
        * `_multiplier-1.0`
               - ENV variables:
                   - CM_ML_MODEL_MOBILENET_MULTIPLIER: `1.0`
                   - CM_ML_MODEL_MOBILENET_MULTIPLIER_PERCENTAGE: `100`

        </details>


      * Group "**opset-version**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_opset-11`
               - ENV variables:
                   - CM_ML_MODEL_ONNX_OPSET: `11`
        * `_opset-8`
               - ENV variables:
                   - CM_ML_MODEL_ONNX_OPSET: `8`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_fp32`** (default)
               - ENV variables:
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_PRECISION: `fp32`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_MOBILENET_PRECISION: `float`
        * `_int8`
               - ENV variables:
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int8`
                   - CM_ML_MODEL_PRECISION: `int8`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `int8`
                   - CM_ML_MODEL_MOBILENET_PRECISION: `int8`
        * `_uint8`
               - ENV variables:
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `uint8`
                   - CM_ML_MODEL_PRECISION: `uint8`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `uint8`
                   - CM_ML_MODEL_MOBILENET_PRECISION: `uint8`

        </details>


      * Group "**resolution**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_resolution-128`
               - ENV variables:
                   - CM_ML_MODEL_MOBILENET_RESOLUTION: `128`
                   - CM_ML_MODEL_IMAGE_HEIGHT: `128`
                   - CM_ML_MODEL_IMAGE_WIDTH: `128`
                   - CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS: `_resolution.128`
        * `_resolution-160`
               - ENV variables:
                   - CM_ML_MODEL_MOBILENET_RESOLUTION: `160`
                   - CM_ML_MODEL_IMAGE_HEIGHT: `160`
                   - CM_ML_MODEL_IMAGE_WIDTH: `160`
                   - CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS: `_resolution.160`
        * `_resolution-192`
               - ENV variables:
                   - CM_ML_MODEL_MOBILENET_RESOLUTION: `192`
                   - CM_ML_MODEL_IMAGE_HEIGHT: `192`
                   - CM_ML_MODEL_IMAGE_WIDTH: `192`
                   - CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS: `_resolution.192`
        * `_resolution-224`
               - ENV variables:
                   - CM_ML_MODEL_MOBILENET_RESOLUTION: `224`
                   - CM_ML_MODEL_IMAGE_HEIGHT: `224`
                   - CM_ML_MODEL_IMAGE_WIDTH: `224`
                   - CM_DATASET_PREPROCESSED_IMAGENET_DEP_TAGS: `_resolution.224`

        </details>


      * Group "**source**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_from.google`
               - ENV variables:
                   - CM_DOWNLOAD_SOURCE: `google`
        * `_from.zenodo`
               - ENV variables:
                   - CM_DOWNLOAD_SOURCE: `zenodo`

        </details>


      * Group "**version**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_v1`
               - ENV variables:
                   - CM_ML_MODEL_MOBILENET_VERSION: `1`
                   - CM_ML_MODEL_FULL_NAME: `mobilenet-v1-precision_<<<CM_ML_MODEL_MOBILENET_PRECISION>>>-<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>-<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>`
        * `_v2`
               - ENV variables:
                   - CM_ML_MODEL_MOBILENET_VERSION: `2`
                   - CM_ML_MODEL_VER: `2`
                   - CM_ML_MODEL_FULL_NAME: `mobilenet-v2-precision_<<<CM_ML_MODEL_MOBILENET_PRECISION>>>-<<<CM_ML_MODEL_MOBILENET_MULTIPLIER>>>-<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>`
        * **`_v3`** (default)
               - ENV variables:
                   - CM_ML_MODEL_MOBILENET_VERSION: `3`
                   - CM_ML_MODEL_VER: `3`
                   - CM_ML_MODEL_FULL_NAME: `mobilenet-v3-precision_<<<CM_ML_MODEL_MOBILENET_PRECISION>>>-<<<CM_ML_MODEL_MOBILENET_KIND>>>-<<<CM_ML_MODEL_MOBILENET_RESOLUTION>>>`

        </details>


    ##### Default variations

    `_fp32,_tf,_v3`
=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_ML_MODEL: `mobilenet`
    * CM_ML_MODEL_DATASET: `imagenet2012-val`
    * CM_ML_MODEL_RETRAINING: `no`
    * CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `no`
    * CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
    * CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp32`
    * CM_ML_MODEL_MOBILENET_NAME_SUFFIX: ``



___
#### Script output
```bash
cmr "get ml-model mobilenet raw ml-model-mobilenet image-classification [variations]"  -j
```