**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/calibrate-model-for.qaic).**



Automatically generated README for this automation recipe: **calibrate-model-for.qaic**

Category: **AI/ML optimization**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=calibrate-model-for.qaic,817bad70df2f4e45) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/calibrate-model-for.qaic)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *qaic,calibrate,profile,qaic-profile,qaic-calibrate*
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

````cmr "qaic calibrate profile qaic-profile qaic-calibrate" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=qaic,calibrate,profile,qaic-profile,qaic-calibrate`

`cm run script --tags=qaic,calibrate,profile,qaic-profile,qaic-calibrate[,variations] `

*or*

`cmr "qaic calibrate profile qaic-profile qaic-calibrate"`

`cmr "qaic calibrate profile qaic-profile qaic-calibrate [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'qaic,calibrate,profile,qaic-profile,qaic-calibrate'
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

```cmr "cm gui" --script="qaic,calibrate,profile,qaic-profile,qaic-calibrate"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=qaic,calibrate,profile,qaic-profile,qaic-calibrate) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "qaic calibrate profile qaic-profile qaic-calibrate[variations]" `

___
### Customization


#### Variations

  * *Internal group (variations should not be selected manually)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert_`
      - Environment variables:
        - *CM_QAIC_MODEL_NAME*: `bert-large`
        - *CM_CREATE_INPUT_BATCH*: `no`
      - Workflow:

    </details>


  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_first.#`
      - Workflow:
    * `_resnet50,tf`
      - Environment variables:
        - *CM_QAIC_MODEL_TO_CONVERT*: `calibrate_resnet50_tf`
      - Workflow:

    </details>


  * Group "**batch-size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bs.#`
      - Environment variables:
        - *CM_QAIC_MODEL_BATCH_SIZE*: `#`
        - *CM_CREATE_INPUT_BATCH*: `yes`
      - Workflow:
    * `_bs.1`
      - Environment variables:
        - *CM_QAIC_MODEL_BATCH_SIZE*: `1`
        - *CM_CREATE_INPUT_BATCH*: `yes`
      - Workflow:

    </details>


  * Group "**calib-dataset-filter-size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_filter-size.#`
      - Workflow:

    </details>


  * Group "**calibration-option**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_mlperf.option1`
      - Workflow:
    * `_mlperf.option2`
      - Workflow:

    </details>


  * Group "**model**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert-99`
      - Environment variables:
        - *CM_CALIBRATE_SQUAD*: `yes`
        - *CM_QAIC_COMPILER_ARGS*: ``
        - *CM_QAIC_COMPILER_PARAMS*: `-onnx-define-symbol=batch_size,1 -onnx-define-symbol=seg_length,<<<CM_DATASET_SQUAD_TOKENIZED_MAX_SEQ_LENGTH>>> -input-list-file=<<<CM_DATASET_SQUAD_TOKENIZED_PACKED_FILENAMES_FILE>>> -num-histogram-bins=512 -profiling-threads=<<<CM_HOST_CPU_PHYSICAL_CORES_PER_SOCKET>>>`
        - *CM_QAIC_MODEL_TO_CONVERT*: `calibrate_bert_mlperf`
      - Workflow:
    * `_resnet50`
      - Environment variables:
        - *CM_QAIC_MODEL_NAME*: `resnet50`
        - *CM_CALIBRATE_IMAGENET*: `yes`
        - *CM_QAIC_COMPILER_ARGS*: ``
        - *CM_QAIC_COMPILER_PARAMS*: `-output-node-name=ArgMax -profiling-threads=<<<CM_HOST_CPU_PHYSICAL_CORES_PER_SOCKET>>>`
        - *CM_QAIC_OUTPUT_NODE_NAME*: `-output-node-name=ArgMax`
        - *CM_QAIC_MODEL_TO_CONVERT*: `calibrate_resnet50_tf`
      - Workflow:
    * `_retinanet`
      - Environment variables:
        - *CM_QAIC_MODEL_NAME*: `retinanet`
        - *CM_CALIBRATE_OPENIMAGES*: `yes`
        - *CM_QAIC_COMPILER_ARGS*: ``
        - *CM_QAIC_COMPILER_PARAMS*: `-enable-channelwise -profiling-threads=<<<CM_HOST_CPU_PHYSICAL_CORES_PER_SOCKET>>> -onnx-define-symbol=batch_size,<<<CM_QAIC_MODEL_BATCH_SIZE>>> -node-precision-info=<<<CM_ML_MODEL_RETINANET_QAIC_NODE_PRECISION_INFO_FILE_PATH>>>`
        - *CM_QAIC_MODEL_TO_CONVERT*: `calibrate_retinanet_no_nms_mlperf`
      - Workflow:

    </details>


  * Group "**model-framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_tf`
      - Workflow:

    </details>


  * Group "**seq-length**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_seq.#`
      - Environment variables:
        - *CM_DATASET_SQUAD_TOKENIZED_MAX_SEQ_LENGTH*: `#`
      - Workflow:
    * `_seq.384`
      - Environment variables:
        - *CM_DATASET_SQUAD_TOKENIZED_MAX_SEQ_LENGTH*: `#`
      - Workflow:

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/calibrate-model-for.qaic/_cm.json)***
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,qaic,apps,sdk
       * CM names: `--adr.['qaic-apps-sdk']...`
       - CM script: [get-qaic-apps-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-qaic-apps-sdk)
     * get,preprocessed,dataset,_calibration,openimages,_for.retinanet.onnx,_NCHW,_fp32,_custom-annotations
       * `if (CM_CALIBRATE_OPENIMAGES  == yes)`
       * CM names: `--adr.['openimages-cal', 'preprocessed-dataset']...`
       - CM script: [get-preprocessed-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages)
     * get,dataset,imagenet,preprocessed,_calibration,_for.resnet50,_float32,_rgb32
       * `if (CM_CALIBRATE_IMAGENET  == yes)`
       * CM names: `--adr.['imagenet-cal', 'preprocessed-calibration-dataset']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,dataset,preprocessed,_calib1,squad,_pickle,_seq-length.384,_packed
       * `if (CM_CALIBRATE_SQUAD  == on)`
       * CM names: `--adr.['squad-cal', 'preprocessed-dataset']...`
       - CM script: [get-preprocessed-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad)
     * get,ml-model
       * CM names: `--adr.['model-src']...`
       - CM script: [get-ml-model-abtf-ssd-pytorch](https://github.com/mlcommons/cm4abtf/tree/master/script/get-ml-model-abtf-ssd-pytorch)
       - CM script: [get-ml-model-3d-unet-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-3d-unet-kits19)
       - CM script: [get-ml-model-bert-base-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-base-squad)
       - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
       - CM script: [get-ml-model-dlrm-terabyte](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte)
       - CM script: [get-ml-model-efficientnet-lite](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-efficientnet-lite)
       - CM script: [get-ml-model-gptj](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj)
       - CM script: [get-ml-model-huggingface-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-huggingface-zoo)
       - CM script: [get-ml-model-llama2](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-llama2)
       - CM script: [get-ml-model-mobilenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet)
       - CM script: [get-ml-model-neuralmagic-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo)
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
       - CM script: [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
       - CM script: [get-ml-model-retinanet-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet-nvidia)
       - CM script: [get-ml-model-rnnt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt)
       - CM script: [get-ml-model-stable-diffusion](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-stable-diffusion)
       - CM script: [get-ml-model-tiny-resnet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-tiny-resnet)
       - CM script: [get-ml-model-using-imagenet-from-model-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-using-imagenet-from-model-zoo)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/calibrate-model-for.qaic/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/calibrate-model-for.qaic/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/calibrate-model-for.qaic/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/calibrate-model-for.qaic/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/calibrate-model-for.qaic/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/calibrate-model-for.qaic/_cm.json)

___
### Script output
`cmr "qaic calibrate profile qaic-profile qaic-calibrate [,variations]"  -j`
#### New environment keys (filter)

* `CM_QAIC_MODEL_PROFILE_*`
#### New environment keys auto-detected from customize

* `CM_QAIC_MODEL_PROFILE_WITH_PATH`