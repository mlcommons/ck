**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-dlrm-terabyte).**



Automatically generated README for this automation recipe: **get-ml-model-dlrm-terabyte**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-ml-model-dlrm-terabyte,8fa7582c603a4db3) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-dlrm-terabyte)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,ml-model,dlrm,raw,terabyte,criteo-terabyte,criteo,recommendation*
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

````cmr "get ml-model dlrm raw terabyte criteo-terabyte criteo recommendation" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,ml-model,dlrm,raw,terabyte,criteo-terabyte,criteo,recommendation`

`cm run script --tags=get,ml-model,dlrm,raw,terabyte,criteo-terabyte,criteo,recommendation[,variations] [--input_flags]`

*or*

`cmr "get ml-model dlrm raw terabyte criteo-terabyte criteo recommendation"`

`cmr "get ml-model dlrm raw terabyte criteo-terabyte criteo recommendation [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,dlrm,raw,terabyte,criteo-terabyte,criteo,recommendation'
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

```cmr "cm gui" --script="get,ml-model,dlrm,raw,terabyte,criteo-terabyte,criteo,recommendation"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,dlrm,raw,terabyte,criteo-terabyte,criteo,recommendation) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ml-model dlrm raw terabyte criteo-terabyte criteo recommendation[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_debug`
      - Environment variables:
        - *CM_ML_MODEL_DEBUG*: `yes`
      - Workflow:
    * `_onnx,fp32`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.8025`
        - *CM_PACKAGE_URL*: `https://dlrm.s3-us-west-1.amazonaws.com/models/tb00_40M.onnx.tar`
        - *CM_UNTAR*: `yes`
        - *CM_ML_MODEL_FILE*: `tb00_40M.onnx`
        - *CM_ML_MODEL_DLRM_MAX_INDEX_RANGE*: `40000000`
      - Workflow:
    * `_onnx,fp32,debug`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.8107`
        - *CM_PACKAGE_URL*: `https://dlrm.s3-us-west-1.amazonaws.com/models/tb0875_10M.onnx.tar`
        - *CM_ML_MODEL_DLRM_MAX_INDEX_RANGE*: `10000000`
        - *CM_UNTAR*: `yes`
        - *CM_ML_MODEL_FILE*: `tb0875_10M.onnx`
      - Workflow:
    * `_pytorch,fp32`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.8025`
        - *CM_PACKAGE_URL*: `https://dlrm.s3-us-west-1.amazonaws.com/models/tb00_40M.pt`
        - *CM_ML_MODEL_DLRM_MAX_INDEX_RANGE*: `40000000`
        - *CM_DOWNLOAD_CHECKSUM*: `2d49a5288cddb37c3c64860a06d79bb9`
      - Workflow:
    * `_pytorch,fp32,debug`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.8107`
        - *CM_PACKAGE_URL*: `https://dlrm.s3-us-west-1.amazonaws.com/models/tb0875_10M.pt`
        - *CM_ML_MODEL_DLRM_MAX_INDEX_RANGE*: `10000000`
      - Workflow:
    * `_pytorch,fp32,weight_sharded`
      - Environment variables:
        - *CM_ML_MODEL_ACCURACY*: `0.8025`
        - *CM_ML_MODEL_DLRM_MAX_INDEX_RANGE*: `40000000`
        - *CM_ML_MODEL_FILE*: `model_weights`
        - *CM_TMP_MODEL_ADDITIONAL_NAME*: ``
        - *CM_DOWNLOAD_CHECKSUM*: ``
      - Workflow:
    * `_pytorch,fp32,weight_sharded,rclone`
      - Environment variables:
        - *CM_RCLONE_CONFIG_CMD*: `rclone config create mlc-inference s3 provider=Cloudflare access_key_id=f65ba5eef400db161ea49967de89f47b secret_access_key=fbea333914c292b854f14d3fe232bad6c5407bf0ab1bebf78833c2b359bdfd2b endpoint=https://c2686074cb2caf5cbaf6d134bdba8b47.r2.cloudflarestorage.com`
        - *CM_PACKAGE_URL*: `mlc-inference:mlcommons-inference-wg-public/model_weights`
      - Workflow:
    * `_pytorch,fp32,weight_sharded,wget`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://cloud.mlcommons.org/index.php/s/XzfSeLgW8FYfR3S/download`
        - *CM_DAE_EXTRACT_DOWNLOADED*: `yes`
        - *CM_DOWNLOAD_FILENAME*: `download`
        - *CM_EXTRACT_UNZIP*: `yes`
      - Workflow:

    </details>


  * Group "**download-tool**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_rclone`
      - Workflow:
    * `_wget`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_onnx`
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `onnx`
      - Workflow:
    * **`_pytorch`** (default)
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `pytorch`
        - *CM_TMP_MODEL_ADDITIONAL_NAME*: `dlrm_terabyte.pytorch`
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


  * Group "**type**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_weight_sharded`** (default)
      - Environment variables:
        - *CM_DLRM_MULTIHOT_MODEL*: `yes`
      - Workflow:

    </details>


#### Default variations

`_fp32,_pytorch,_weight_sharded`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--dir=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
* `--download_path=value`  &rarr;  `CM_DOWNLOAD_PATH=value`
* `--to=value`  &rarr;  `CM_DOWNLOAD_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "dir":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-dlrm-terabyte/_cm.json)
  1. Run "preprocess" function from customize.py
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-dlrm-terabyte/_cm.json)***
     * download-and-extract
       * CM names: `--adr.['dae']...`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-dlrm-terabyte/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-dlrm-terabyte/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-dlrm-terabyte/_cm.json)

___
### Script output
`cmr "get ml-model dlrm raw terabyte criteo-terabyte criteo recommendation [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize
