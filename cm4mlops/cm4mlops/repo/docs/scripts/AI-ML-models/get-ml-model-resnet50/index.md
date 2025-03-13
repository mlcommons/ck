# get-ml-model-resnet50
Automatically generated README for this automation recipe: **get-ml-model-resnet50**

Category: **[AI/ML models](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-resnet50/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-resnet50/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get raw ml-model resnet50 ml-model-resnet50 image-classification" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,raw,ml-model,resnet50,ml-model-resnet50,image-classification[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get raw ml-model resnet50 ml-model-resnet50 image-classification [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,raw,ml-model,resnet50,ml-model-resnet50,image-classification'
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
    cm docker script "get raw ml-model resnet50 ml-model-resnet50 image-classification[variations]" 
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
        * `_batch_size.1`
               - ENV variables:
                   - CM_ML_MODEL_BATCH_SIZE: `1`
        * `_fix-input-shape`
        * `_from-tf`
        * `_huggingface_default`
               - ENV variables:
                   - CM_PACKAGE_URL: `https://huggingface.co/ctuning/mlperf-inference-resnet50-onnx-fp32-imagenet2012-v1.0/resolve/main/resnet50_v1.onnx`

        </details>


      * Group "**framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_ncnn`
               - ENV variables:
                   - CM_ML_MODEL_FRAMEWORK: `ncnn`
        * **`_onnx`** (default)
              - Aliases: `_onnxruntime`
               - ENV variables:
                   - CM_ML_MODEL_DATA_LAYOUT: `NCHW`
                   - CM_ML_MODEL_FRAMEWORK: `onnx`
                   - CM_ML_MODEL_INPUT_LAYERS: `input_tensor:0`
                   - CM_ML_MODEL_INPUT_LAYER_NAME: `input_tensor:0`
                   - CM_ML_MODEL_INPUT_SHAPES: `\"input_tensor:0\": (BATCH_SIZE, 3, 224, 224)`
                   - CM_ML_MODEL_OUTPUT_LAYERS: `softmax_tensor:0`
                   - CM_ML_MODEL_OUTPUT_LAYER_NAME: `softmax_tensor:0`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `<<<CM_PACKAGE_URL>>>`
                   - CM_ML_MODEL_VER: `1.5`
        * `_pytorch`
               - ENV variables:
                   - CM_ML_MODEL_DATA_LAYOUT: `NCHW`
                   - CM_ML_MODEL_FRAMEWORK: `pytorch`
                   - CM_ML_MODEL_GIVEN_CHANNEL_MEANS: `?`
                   - CM_ML_MODEL_INPUT_LAYER_NAME: `input_tensor:0`
                   - CM_ML_MODEL_INPUT_SHAPES: `\"input_tensor:0\": [BATCH_SIZE, 3, 224, 224]`
                   - CM_ML_MODEL_OUTPUT_LAYERS: `output`
                   - CM_ML_MODEL_OUTPUT_LAYER_NAME: `?`
                   - CM_ML_STARTING_WEIGHTS_FILENAME: `<<<CM_PACKAGE_URL>>>`
        * `_tensorflow`
              - Aliases: `_tf`
               - ENV variables:
                   - CM_ML_MODEL_ACCURACY: `76.456`
                   - CM_ML_MODEL_DATA_LAYOUT: `NHWC`
                   - CM_ML_MODEL_FRAMEWORK: `tensorflow`
                   - CM_ML_MODEL_GIVEN_CHANNEL_MEANS: `123.68 116.78 103.94`
                   - CM_ML_MODEL_INPUT_LAYERS: `input_tensor`
                   - CM_ML_MODEL_INPUT_LAYER_NAME: `input_tensor`
                   - CM_ML_MODEL_INPUT_SHAPES: `\"input_tensor:0\": (BATCH_SIZE, 3, 224, 224)`
                   - CM_ML_MODEL_NORMALIZE_DATA: `0`
                   - CM_ML_MODEL_OUTPUT_LAYERS: `softmax_tensor`
                   - CM_ML_MODEL_OUTPUT_LAYER_NAME: `softmax_tensor`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `<<<CM_PACKAGE_URL>>>`
                   - CM_ML_MODEL_SUBTRACT_MEANS: `YES`
                   - CM_PACKAGE_URL: `https://zenodo.org/record/2535873/files/resnet50_v1.pb`
        * `_tflite`
               - ENV variables:
                   - CM_ML_MODEL_ACCURACY: `76.456`
                   - CM_ML_MODEL_DATA_LAYOUT: `NHWC`
                   - CM_ML_MODEL_FRAMEWORK: `tflite`
                   - CM_ML_MODEL_GIVEN_CHANNEL_MEANS: `123.68 116.78 103.94`
                   - CM_ML_MODEL_INPUT_LAYERS: `input_tensor`
                   - CM_ML_MODEL_INPUT_LAYER_NAME: `input_tensor`
                   - CM_ML_MODEL_INPUT_SHAPES: `\"input_tensor 2\": (BATCH_SIZE, 224, 224, 3)`
                   - CM_ML_MODEL_NORMALIZE_DATA: `0`
                   - CM_ML_MODEL_OUTPUT_LAYERS: `softmax_tensor`
                   - CM_ML_MODEL_OUTPUT_LAYER_NAME: `softmax_tensor`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `<<<CM_PACKAGE_URL>>>`
                   - CM_ML_MODEL_SUBTRACT_MEANS: `YES`

        </details>


      * Group "**model-output**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_argmax`** (default)
               - ENV variables:
                   - CM_ML_MODEL_OUTPUT_LAYER_ARGMAX: `yes`
        * `_no-argmax`
               - ENV variables:
                   - CM_ML_MODEL_OUTPUT_LAYER_ARGMAX: `no`

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

    `_argmax,_fp32,_onnx`

#### Native script being run
=== "Linux/macOS"
     * [run-fix-input.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-resnet50/run-fix-input.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get raw ml-model resnet50 ml-model-resnet50 image-classification [variations]"  -j
```