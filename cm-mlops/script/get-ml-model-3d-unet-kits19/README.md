**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-3d-unet-kits19).**



Automatically generated README for this automation recipe: **get-ml-model-3d-unet-kits19**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-ml-model-3d-unet-kits19,fb7e31419c0f4226) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-3d-unet-kits19)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,ml-model,raw,3d-unet,kits19,medical-imaging*
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

````cmr "get ml-model raw 3d-unet kits19 medical-imaging" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,ml-model,raw,3d-unet,kits19,medical-imaging`

`cm run script --tags=get,ml-model,raw,3d-unet,kits19,medical-imaging[,variations] `

*or*

`cmr "get ml-model raw 3d-unet kits19 medical-imaging"`

`cmr "get ml-model raw 3d-unet kits19 medical-imaging [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,raw,3d-unet,kits19,medical-imaging'
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

```cmr "cm gui" --script="get,ml-model,raw,3d-unet,kits19,medical-imaging"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,raw,3d-unet,kits19,medical-imaging) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ml-model raw 3d-unet kits19 medical-imaging[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_onnx,fp32`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.86170`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/5597155/files/3dunet_kits19_128x128x128_dynbatch.onnx?download=1`
      - Workflow:
    * `_pytorch,fp32`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.86170`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/5597155/files/3dunet_kits19_pytorch.ptc?download=1`
      - Workflow:
    * `_pytorch,fp32,weights`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.86170`
        - *CM_ML_MODEL_FILE*: `retinanet_model_10.pth`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/5597155/files/3dunet_kits19_pytorch_checkpoint.pth?download=1`
        - *CM_UNZIP*: `yes`
      - Workflow:
    * `_tf,fp32`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.86170`
        - *CM_ML_MODEL_FILE*: `3dunet_kits19_128x128x128.tf`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/5597155/files/3dunet_kits19_128x128x128.tf.zip?download=1`
        - *CM_UNZIP*: `yes`
      - Workflow:
    * `_weights`
      - Environment variables:
        - *CM_MODEL_WEIGHTS_FILE*: `yes`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_onnx`** (default)
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `onnx`
      - Workflow:
    * `_pytorch`
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `pytorch`
      - Workflow:
    * `_tf`
      - Aliases: `_tensorflow`
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `tensorflow`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_fp32`** (default)
      - Environment variables:
        - *CM_ML_MODEL_INPUT_DATA_TYPES*: `fp32`
        - *CM_ML_MODEL_PRECISION*: `fp32`
        - *CM_ML_MODEL_WEIGHT_DATA_TYPES*: `fp32`
      - Workflow:

    </details>


#### Default variations

`_fp32,_onnx`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-3d-unet-kits19/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-3d-unet-kits19/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-3d-unet-kits19/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-3d-unet-kits19/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-3d-unet-kits19/_cm.json)

___
### Script output
`cmr "get ml-model raw 3d-unet kits19 medical-imaging [,variations]"  -j`
#### New environment keys (filter)

* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_FILE`
* `CM_ML_MODEL_FILE_WITH_PATH`
* `CM_ML_MODEL_PATH`