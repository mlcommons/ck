**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-retinanet).**



Automatically generated README for this automation recipe: **get-ml-model-retinanet**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-ml-model-retinanet,427bc5665e4541c2) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-retinanet)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,ml-model,raw,resnext50,retinanet,object-detection*
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

````cmr "get ml-model raw resnext50 retinanet object-detection" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,ml-model,raw,resnext50,retinanet,object-detection`

`cm run script --tags=get,ml-model,raw,resnext50,retinanet,object-detection[,variations] `

*or*

`cmr "get ml-model raw resnext50 retinanet object-detection"`

`cmr "get ml-model raw resnext50 retinanet object-detection [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,raw,resnext50,retinanet,object-detection'
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

```cmr "cm gui" --script="get,ml-model,raw,resnext50,retinanet,object-detection"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,raw,resnext50,retinanet,object-detection) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ml-model raw resnext50 retinanet object-detection[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_no-nms`
      - Environment variables:
        - *CM_TMP_ML_MODEL_RETINANET_NO_NMS*: `yes`
        - *CM_ML_MODEL_RETINANET_NO_NMS*: `yes`
        - *CM_QAIC_PRINT_NODE_PRECISION_INFO*: `yes`
      - Workflow:
    * `_onnx,fp32`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/6617879/files/resnext50_32x4d_fpn.onnx`
        - *CM_DOWNLOAD_CHECKSUM*: `4544f4e56e0a4684215831cc937ea45c`
        - *CM_ML_MODEL_ACCURACY*: `0.3757`
      - Workflow:
    * `_onnx,no-nms`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,python3
             * CM names: `--adr.['python, python3']...`
             - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
           * get,generic-python-lib,_package.onnx
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.onnxsim
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * download,file,_url.https://raw.githubusercontent.com/arjunsuresh/ck-qaic/main/package/model-onnx-mlperf-retinanet-no-nms/remove-nms-and-extract-priors.patch
             - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
           * get,git,repo,_repo.https://github.com/mlcommons/training.git,_patch
             * CM names: `--adr.['mlperf-training-src']...`
             - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
           * get,ml-model,retinanet,_pytorch,_fp32,_weights
             * CM names: `--adr.['pytorch-weights']...`
             - CM script: [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
           * get,generic-python-lib,_package.torch
             * CM names: `--adr.['torch', 'pytorch']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_pytorch,fp32`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/6617981/files/resnext50_32x4d_fpn.pth`
        - *CM_ML_MODEL_ACCURACY*: `0.3755`
      - Workflow:
    * `_pytorch,fp32,weights`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/6605272/files/retinanet_model_10.zip?download=1`
        - *CM_UNZIP*: `yes`
        - *CM_ML_MODEL_FILE*: `retinanet_model_10.pth`
        - *CM_ML_MODEL_ACCURACY*: `0.3755`
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
        - *CM_ML_MODEL_DATA_LAYOUT*: `NCHW`
        - *CM_ML_MODEL_FRAMEWORK*: `onnx`
      - Workflow:
    * `_pytorch`
      - Environment variables:
        - *CM_ML_MODEL_DATA_LAYOUT*: `NCHW`
        - *CM_ML_MODEL_FRAMEWORK*: `pytorch`
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


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-retinanet/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-retinanet/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-retinanet/_cm.json)***
     * download-and-extract
       * `if (CM_TMP_ML_MODEL_RETINANET_NO_NMS  != yes)`
       * CM names: `--adr.['dae']...`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run native script if exists***
     * [run-no-nms.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-retinanet/run-no-nms.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-retinanet/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-retinanet/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-retinanet/_cm.json)

___
### Script output
`cmr "get ml-model raw resnext50 retinanet object-detection [,variations]"  -j`
#### New environment keys (filter)

* `<<<CM_ENV_NAME_ML_MODEL_FILE>>>`
* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_FILE`
* `CM_ML_MODEL_FILE_WITH_PATH`
* `CM_ML_MODEL_RETINANET_QAIC_NODE_PRECISION_INFO_FILE_PATH`