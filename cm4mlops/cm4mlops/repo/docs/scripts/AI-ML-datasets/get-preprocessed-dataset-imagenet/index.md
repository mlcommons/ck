# get-preprocessed-dataset-imagenet
Automatically generated README for this automation recipe: **get-preprocessed-dataset-imagenet**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-imagenet/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-imagenet/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dataset imagenet ILSVRC image-classification preprocessed" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,dataset,imagenet,ILSVRC,image-classification,preprocessed[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get dataset imagenet ILSVRC image-classification preprocessed [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,imagenet,ILSVRC,image-classification,preprocessed'
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
    cm docker script "get dataset imagenet ILSVRC image-classification preprocessed[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_default`
        * `_pytorch`
               - ENV variables:
                   - CM_PREPROCESS_PYTORCH: `yes`
                   - CM_MODEL: `resnet50`
        * `_tflite_tpu`
               - ENV variables:
                   - CM_MODEL: `resnet50`
                   - CM_PREPROCESS_TFLITE_TPU: `yes`

        </details>


      * Group "**calibration-option**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_mlperf.option1`
               - ENV variables:
                   - CM_DATASET_CALIBRATION_OPTION: `one`
        * `_mlperf.option2`
               - ENV variables:
                   - CM_DATASET_CALIBRATION_OPTION: `two`

        </details>


      * Group "**dataset-type**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_calibration`
               - ENV variables:
                   - CM_DATASET_TYPE: `calibration`
        * **`_validation`** (default)
               - ENV variables:
                   - CM_DATASET_TYPE: `validation`

        </details>


      * Group "**extension**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_rgb32`
               - ENV variables:
                   - CM_DATASET_PREPROCESSED_EXTENSION: `rgb32`
        * `_rgb8`
               - ENV variables:
                   - CM_DATASET_PREPROCESSED_EXTENSION: `rgb8`

        </details>


      * Group "**interpolation-method**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_inter.area`
               - ENV variables:
                   - CM_DATASET_INTERPOLATION_METHOD: `INTER_AREA`
        * `_inter.linear`
               - ENV variables:
                   - CM_DATASET_INTERPOLATION_METHOD: `INTER_LINEAR`

        </details>


      * Group "**layout**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_NCHW`** (default)
               - ENV variables:
                   - CM_DATASET_DATA_LAYOUT: `NCHW`
        * `_NHWC`
               - ENV variables:
                   - CM_DATASET_DATA_LAYOUT: `NHWC`

        </details>


      * Group "**model**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_for.mobilenet`
        * `_for.resnet50`
               - ENV variables:
                   - CM_DATASET_SUBTRACT_MEANS: `1`
                   - CM_DATASET_GIVEN_CHANNEL_MEANS: `123.68 116.78 103.94`
                   - CM_DATASET_NORMALIZE_DATA: `0`
                   - CM_DATASET_INTERPOLATION_METHOD: `INTER_AREA`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_float32`
               - ENV variables:
                   - CM_DATASET_DATA_TYPE: `float32`
                   - CM_DATASET_QUANTIZE: `0`
                   - CM_DATASET_CONVERT_TO_UNSIGNED: `0`
        * `_int8`
               - ENV variables:
                   - CM_DATASET_DATA_TYPE: `int8`
                   - CM_DATASET_QUANTIZE: `1`
                   - CM_DATASET_CONVERT_TO_UNSIGNED: `0`
        * `_uint8`
               - ENV variables:
                   - CM_DATASET_DATA_TYPE: `uint8`
                   - CM_DATASET_DATA_TYPE_INPUT: `float32`
                   - CM_DATASET_QUANTIZE: `1`
                   - CM_DATASET_CONVERT_TO_UNSIGNED: `1`

        </details>


      * Group "**preprocessing-source**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_generic-preprocessor`
               - ENV variables:
                   - CM_DATASET_REFERENCE_PREPROCESSOR: `0`
        * **`_mlcommons-reference-preprocessor`** (default)
               - ENV variables:
                   - CM_DATASET_REFERENCE_PREPROCESSOR: `1`

        </details>


      * Group "**resolution**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_resolution.#`
               - ENV variables:
                   - CM_DATASET_INPUT_SQUARE_SIDE: `#`
        * **`_resolution.224`** (default)
               - ENV variables:
                   - CM_DATASET_INPUT_SQUARE_SIDE: `224`

        </details>


      * Group "**size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_1`
               - ENV variables:
                   - CM_DATASET_SIZE: `1`
        * `_500`
               - ENV variables:
                   - CM_DATASET_SIZE: `500`
        * `_full`
               - ENV variables:
                   - CM_DATASET_SIZE: `50000`
        * `_size.#`
               - ENV variables:
                   - CM_DATASET_SIZE: `#`

        </details>


    ##### Default variations

    `_NCHW,_mlcommons-reference-preprocessor,_resolution.224,_validation`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--dir=value`  &rarr;  `CM_DATASET_PREPROCESSED_PATH=value`
    * `--imagenet_path=value`  &rarr;  `CM_IMAGENET_PATH=value`
    * `--imagenet_preprocessed_path=value`  &rarr;  `CM_IMAGENET_PREPROCESSED_PATH=value`
    * `--threads=value`  &rarr;  `CM_NUM_PREPROCESS_THREADS=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_DATASET_CROP_FACTOR: `87.5`
    * CM_DATASET_DATA_TYPE: `float32`
    * CM_DATASET_DATA_LAYOUT: `NCHW`
    * CM_DATASET_QUANT_SCALE: `1`
    * CM_DATASET_QUANTIZE: `0`
    * CM_DATASET_QUANT_OFFSET: `0`
    * CM_DATASET_PREPROCESSED_EXTENSION: `npy`
    * CM_DATASET_CONVERT_TO_UNSIGNED: `0`
    * CM_DATASET_REFERENCE_PREPROCESSOR: `1`
    * CM_PREPROCESS_VGG: `yes`
    * CM_MODEL: `resnet50`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-imagenet/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-imagenet/run.bat)
___
#### Script output
```bash
cmr "get dataset imagenet ILSVRC image-classification preprocessed [variations]" [--input_flags] -j
```