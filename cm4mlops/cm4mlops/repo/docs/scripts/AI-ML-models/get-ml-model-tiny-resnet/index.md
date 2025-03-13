# get-ml-model-tiny-resnet
Automatically generated README for this automation recipe: **get-ml-model-tiny-resnet**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-tiny-resnet/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get raw ml-model resnet pretrained tiny model ic ml-model-tiny-resnet image-classification" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,raw,ml-model,resnet,pretrained,tiny,model,ic,ml-model-tiny-resnet,image-classification[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get raw ml-model resnet pretrained tiny model ic ml-model-tiny-resnet image-classification [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,raw,ml-model,resnet,pretrained,tiny,model,ic,ml-model-tiny-resnet,image-classification'
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
    cm docker script "get raw ml-model resnet pretrained tiny model ic ml-model-tiny-resnet image-classification[variations]" 
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


      * Group "**framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_onnx`
               - ENV variables:
                   - CM_TMP_ML_MODEL_TF2ONNX: `yes`
        * **`_tflite`** (default)
               - ENV variables:
                   - CM_ML_MODEL_ACCURACY: `85`
                   - CM_ML_MODEL_DATA_LAYOUT: `NHWC`
                   - CM_ML_MODEL_FRAMEWORK: `tflite`
                   - CM_ML_MODEL_GIVEN_CHANNEL_MEANS: ``
                   - CM_ML_MODEL_INPUT_LAYERS: ``
                   - CM_ML_MODEL_INPUT_LAYER_NAME: ``
                   - CM_ML_MODEL_INPUT_SHAPES: ``
                   - CM_ML_MODEL_NORMALIZE_DATA: `0`
                   - CM_ML_MODEL_OUTPUT_LAYERS: ``
                   - CM_ML_MODEL_OUTPUT_LAYER_NAME: ``
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `<<<CM_PACKAGE_URL>>>`
                   - CM_ML_MODEL_SUBTRACT_MEANS: `YES`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_fp32`
               - ENV variables:
                   - CM_ML_MODEL_INPUT_DATA_TYPES: `fp32`
                   - CM_ML_MODEL_PRECISION: `fp32`
                   - CM_ML_MODEL_WEIGHT_DATA_TYPES: `fp32`
        * **`_int8`** (default)
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

    `_int8,_tflite`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-tiny-resnet/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get raw ml-model resnet pretrained tiny model ic ml-model-tiny-resnet image-classification [variations]"  -j
```