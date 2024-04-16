**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-openimages).**



Automatically generated README for this automation recipe: **get-preprocessed-dataset-openimages**

Category: **AI/ML datasets**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-preprocessed-dataset-openimages,9842f1be8cba4c7b) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-openimages)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,dataset,openimages,open-images,object-detection,preprocessed*
* Output cached? *True*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "get dataset openimages open-images object-detection preprocessed" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,dataset,openimages,open-images,object-detection,preprocessed`

`cm run script --tags=get,dataset,openimages,open-images,object-detection,preprocessed[,variations] [--input_flags]`

*or*

`cmr "get dataset openimages open-images object-detection preprocessed"`

`cmr "get dataset openimages open-images object-detection preprocessed [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

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

</details>


#### Run this script via GUI

```cmr "cm gui" --script="get,dataset,openimages,open-images,object-detection,preprocessed"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,dataset,openimages,open-images,object-detection,preprocessed) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get dataset openimages open-images object-detection preprocessed[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_filter`
      - Workflow:
    * `_filter,calibration`
      - Environment variables:
        - *CM_DATASET_CALIBRATION_FILTER*: `yes`
      - Workflow:
    * `_for.retinanet.onnx`
      - Environment variables:
        - *CM_ML_MODEL_NAME*: `retinanet`
        - *CM_DATASET_SUBTRACT_MEANS*: `1`
        - *CM_DATASET_GIVEN_CHANNEL_MEANS*: `0.485 0.456 0.406`
        - *CM_DATASET_GIVEN_CHANNEL_STDS*: `0.229 0.224 0.225`
        - *CM_DATASET_NORMALIZE_DATA*: `0`
        - *CM_DATASET_NORMALIZE_LOWER*: `0.0`
        - *CM_DATASET_NORMALIZE_UPPER*: `1.0`
        - *CM_DATASET_CONVERT_TO_BGR*: `0`
        - *CM_DATASET_CROP_FACTOR*: `100.0`
      - Workflow:
    * `_for.retinanet.onnx,fp32`
      - Workflow:
    * `_for.retinanet.onnx,uint8`
      - Environment variables:
        - *CM_DATASET_QUANT_SCALE*: `0.0186584499`
        - *CM_DATASET_QUANT_OFFSET*: `114`
      - Workflow:
    * `_full,validation`
      - Environment variables:
        - *CM_DATASET_SIZE*: `24781`
      - Workflow:
    * `_nvidia`
      - Environment variables:
        - *CM_PREPROCESSING_BY_NVIDIA*: `yes`
      - Workflow:
    * `_quant-offset.#`
      - Workflow:
    * `_quant-scale.#`
      - Workflow:

    </details>


  * Group "**annotations**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_custom-annotations`
      - Workflow:
    * **`_default-annotations`** (default)
      - Workflow:

    </details>


  * Group "**dataset-count**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_50`** (default)
      - Environment variables:
        - *CM_DATASET_SIZE*: `50`
      - Workflow:
    * `_500`
      - Environment variables:
        - *CM_DATASET_SIZE*: `500`
      - Workflow:
    * `_full`
      - Workflow:
    * `_size.#`
      - Environment variables:
        - *CM_DATASET_SIZE*: `#`
      - Workflow:

    </details>


  * Group "**dataset-layout**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_NCHW`** (default)
      - Environment variables:
        - *CM_DATASET_DATA_LAYOUT*: `NCHW`
      - Workflow:
    * `_NHWC`
      - Environment variables:
        - *CM_DATASET_DATA_LAYOUT*: `NHWC`
      - Workflow:

    </details>


  * Group "**dataset-precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_fp32`** (default)
      - Environment variables:
        - *CM_DATASET_DTYPE*: `fp32`
        - *CM_DATASET_INPUT_DTYPE*: `fp32`
        - *CM_DATASET_QUANTIZE*: `0`
        - *CM_DATASET_CONVERT_TO_UNSIGNED*: `0`
      - Workflow:
    * `_int8`
      - Environment variables:
        - *CM_DATASET_DTYPE*: `int8`
        - *CM_DATASET_INPUT_DTYPE*: `fp32`
        - *CM_DATASET_QUANTIZE*: `1`
        - *CM_DATASET_CONVERT_TO_UNSIGNED*: `0`
      - Workflow:
    * `_uint8`
      - Environment variables:
        - *CM_DATASET_DTYPE*: `uint8`
        - *CM_DATASET_INPUT_DTYPE*: `fp32`
        - *CM_DATASET_QUANTIZE*: `1`
        - *CM_DATASET_CONVERT_TO_UNSIGNED*: `1`
      - Workflow:

    </details>


  * Group "**dataset-type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_calibration`
      - Environment variables:
        - *CM_DATASET_PATH*: `<<<CM_CALIBRATION_DATASET_PATH>>>`
        - *CM_DATASET_ANNOTATIONS_FILE_PATH*: `<<<CM_DATASET_CALIBRATION_ANNOTATIONS_FILE_PATH>>>`
        - *CM_DATASET_TYPE*: `calibration`
      - Workflow:
    * **`_validation`** (default)
      - Environment variables:
        - *CM_DATASET_TYPE*: `validation`
      - Workflow:

    </details>


  * Group "**extension**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_npy`
      - Environment variables:
        - *CM_DATASET_PREPROCESSED_EXTENSION*: `npy`
      - Workflow:
    * `_raw`
      - Environment variables:
        - *CM_DATASET_PREPROCESSED_EXTENSION*: `raw`
      - Workflow:
    * `_rgb32`
      - Environment variables:
        - *CM_DATASET_PREPROCESSED_EXTENSION*: `rgb32`
      - Workflow:
    * `_rgb8`
      - Environment variables:
        - *CM_DATASET_PREPROCESSED_EXTENSION*: `rgb8`
      - Workflow:

    </details>


  * Group "**filter-size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_filter-size.#`
      - Workflow:

    </details>


  * Group "**interpolation-method**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_inter.area`
      - Environment variables:
        - *CM_DATASET_INTERPOLATION_METHOD*: `INTER_AREA`
      - Workflow:
    * `_inter.linear`
      - Environment variables:
        - *CM_DATASET_INTERPOLATION_METHOD*: `INTER_LINEAR`
      - Workflow:

    </details>


  * Group "**preprocessing-source**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_generic-preprocessor`
      - Environment variables:
        - *CM_DATASET_REFERENCE_PREPROCESSOR*: `0`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_torch
             * CM names: `--adr.['torch', 'pytorch']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torchvision
             * CM names: `--adr.['torchvision']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
        1. ***Read "prehook_deps" on other CM scripts***
           * get,generic,image-preprocessor
             - CM script: [get-preprocesser-script-generic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocesser-script-generic)
    * **`_mlcommons-reference-preprocessor`** (default)
      - Environment variables:
        - *CM_DATASET_REFERENCE_PREPROCESSOR*: `1`
      - Workflow:

    </details>


#### Default variations

`_50,_NCHW,_default-annotations,_fp32,_mlcommons-reference-preprocessor,_validation`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--dir=value`  &rarr;  `CM_DATASET_PREPROCESSED_PATH=value`
* `--threads=value`  &rarr;  `CM_NUM_PREPROCESS_THREADS=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "dir":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_DATASET: `OPENIMAGES`
* CM_DATASET_DTYPE: `fp32`
* CM_DATASET_INPUT_SQUARE_SIDE: `800`
* CM_DATASET_CROP_FACTOR: `100.0`
* CM_DATASET_QUANT_SCALE: `1`
* CM_DATASET_QUANTIZE: `0`
* CM_DATASET_QUANT_OFFSET: `0`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-openimages/_cm.json)***
     * get,python3
       * CM names: `--adr.['python3', 'python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,dataset,object-detection,openimages,original
       * CM names: `--adr.['original-dataset']...`
       - CM script: [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
     * mlperf,mlcommons,inference,source,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,generic-python-lib,_pycocotools
       * CM names: `--adr.['pycocotools']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_opencv-python
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_pillow
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_package.ujson
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_numpy
       * CM names: `--adr.['numpy']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_numpy
       * CM names: `--adr.['numpy']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-openimages/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-openimages/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-openimages/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-openimages/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-openimages/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-openimages/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-openimages/_cm.json)

___
### Script output
`cmr "get dataset openimages open-images object-detection preprocessed [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_DATASET_*`
#### New environment keys auto-detected from customize

* `CM_DATASET_ANNOTATIONS_DIR_PATH`
* `CM_DATASET_ANNOTATIONS_FILE_PATH`
* `CM_DATASET_PREPROCESSED_IMAGENAMES_LIST`
* `CM_DATASET_PREPROCESSED_IMAGES_LIST`
* `CM_DATASET_PREPROCESSED_PATH`
* `CM_DATASET_QUANT_OFFSET`
* `CM_DATASET_QUANT_SCALE`
* `CM_DATASET_TYPE`