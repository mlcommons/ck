# get-preprocessed-dataset-openimages
Automatically generated README for this automation recipe: **get-preprocessed-dataset-openimages**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-openimages/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-openimages/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dataset openimages open-images object-detection preprocessed" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,dataset,openimages,open-images,object-detection,preprocessed[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get dataset openimages open-images object-detection preprocessed [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,openimages,open-images,object-detection,preprocessed'
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
    cm docker script "get dataset openimages open-images object-detection preprocessed[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_filter`
        * `_for.retinanet.onnx`
               - ENV variables:
                   - CM_ML_MODEL_NAME: `retinanet`
                   - CM_DATASET_SUBTRACT_MEANS: `1`
                   - CM_DATASET_GIVEN_CHANNEL_MEANS: `0.485 0.456 0.406`
                   - CM_DATASET_GIVEN_CHANNEL_STDS: `0.229 0.224 0.225`
                   - CM_DATASET_NORMALIZE_DATA: `0`
                   - CM_DATASET_NORMALIZE_LOWER: `0.0`
                   - CM_DATASET_NORMALIZE_UPPER: `1.0`
                   - CM_DATASET_CONVERT_TO_BGR: `0`
                   - CM_DATASET_CROP_FACTOR: `100.0`
        * `_nvidia`
               - ENV variables:
                   - CM_PREPROCESSING_BY_NVIDIA: `yes`
        * `_quant-offset.#`
        * `_quant-scale.#`

        </details>


      * Group "**annotations**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_custom-annotations`
        * **`_default-annotations`** (default)

        </details>


      * Group "**dataset-count**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_50`** (default)
               - ENV variables:
                   - CM_DATASET_SIZE: `50`
        * `_500`
               - ENV variables:
                   - CM_DATASET_SIZE: `500`
        * `_full`
        * `_size.#`
               - ENV variables:
                   - CM_DATASET_SIZE: `#`

        </details>


      * Group "**dataset-layout**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_NCHW`** (default)
               - ENV variables:
                   - CM_DATASET_DATA_LAYOUT: `NCHW`
        * `_NHWC`
               - ENV variables:
                   - CM_DATASET_DATA_LAYOUT: `NHWC`

        </details>


      * Group "**dataset-precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_fp32`** (default)
               - ENV variables:
                   - CM_DATASET_DTYPE: `fp32`
                   - CM_DATASET_INPUT_DTYPE: `fp32`
                   - CM_DATASET_QUANTIZE: `0`
                   - CM_DATASET_CONVERT_TO_UNSIGNED: `0`
        * `_int8`
               - ENV variables:
                   - CM_DATASET_DTYPE: `int8`
                   - CM_DATASET_INPUT_DTYPE: `fp32`
                   - CM_DATASET_QUANTIZE: `1`
                   - CM_DATASET_CONVERT_TO_UNSIGNED: `0`
        * `_uint8`
               - ENV variables:
                   - CM_DATASET_DTYPE: `uint8`
                   - CM_DATASET_INPUT_DTYPE: `fp32`
                   - CM_DATASET_QUANTIZE: `1`
                   - CM_DATASET_CONVERT_TO_UNSIGNED: `1`

        </details>


      * Group "**dataset-type**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_calibration`
               - ENV variables:
                   - CM_DATASET_PATH: `<<<CM_CALIBRATION_DATASET_PATH>>>`
                   - CM_DATASET_ANNOTATIONS_FILE_PATH: `<<<CM_DATASET_CALIBRATION_ANNOTATIONS_FILE_PATH>>>`
                   - CM_DATASET_TYPE: `calibration`
        * **`_validation`** (default)
               - ENV variables:
                   - CM_DATASET_TYPE: `validation`

        </details>


      * Group "**extension**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_npy`
               - ENV variables:
                   - CM_DATASET_PREPROCESSED_EXTENSION: `npy`
        * `_raw`
               - ENV variables:
                   - CM_DATASET_PREPROCESSED_EXTENSION: `raw`
        * `_rgb32`
               - ENV variables:
                   - CM_DATASET_PREPROCESSED_EXTENSION: `rgb32`
        * `_rgb8`
               - ENV variables:
                   - CM_DATASET_PREPROCESSED_EXTENSION: `rgb8`

        </details>


      * Group "**filter-size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_filter-size.#`

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


    ##### Default variations

    `_50,_NCHW,_default-annotations,_fp32,_mlcommons-reference-preprocessor,_validation`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--dir=value`  &rarr;  `CM_DATASET_PREPROCESSED_PATH=value`
    * `--threads=value`  &rarr;  `CM_NUM_PREPROCESS_THREADS=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_DATASET: `OPENIMAGES`
    * CM_DATASET_DTYPE: `fp32`
    * CM_DATASET_INPUT_SQUARE_SIDE: `800`
    * CM_DATASET_CROP_FACTOR: `100.0`
    * CM_DATASET_QUANT_SCALE: `1`
    * CM_DATASET_QUANTIZE: `0`
    * CM_DATASET_QUANT_OFFSET: `0`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-openimages/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-openimages/run.bat)
___
#### Script output
```bash
cmr "get dataset openimages open-images object-detection preprocessed [variations]" [--input_flags] -j
```