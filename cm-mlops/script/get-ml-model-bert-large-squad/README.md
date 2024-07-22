**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-bert-large-squad).**



Automatically generated README for this automation recipe: **get-ml-model-bert-large-squad**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-ml-model-bert-large-squad,5e865dbdc65949d2) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-large-squad)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,ml-model,raw,bert,bert-large,bert-squad,language,language-processing*
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

````cmr "get ml-model raw bert bert-large bert-squad language language-processing" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,ml-model,raw,bert,bert-large,bert-squad,language,language-processing`

`cm run script --tags=get,ml-model,raw,bert,bert-large,bert-squad,language,language-processing[,variations] `

*or*

`cmr "get ml-model raw bert bert-large bert-squad language language-processing"`

`cmr "get ml-model raw bert bert-large bert-squad language language-processing [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,raw,bert,bert-large,bert-squad,language,language-processing'
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

```cmr "cm gui" --script="get,ml-model,raw,bert,bert-large,bert-squad,language,language-processing"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,raw,bert,bert-large,bert-squad,language,language-processing) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ml-model raw bert bert-large bert-squad language language-processing[variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_deepsparse,int8`
      - Environment variables:
        - *CM_ML_MODEL_F1*: `90.21282641816266`
        - *CM_ML_MODEL_FILE*: `oBERT-Large_95sparse_block4_qat.onnx`
        - *CM_DAE_EXTRACT_DOWNLOADED*: `yes`
      - Workflow:
    * `_deepsparse,int8,github`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://github.com/mlcommons/inference_results_v2.1/raw/master/open/NeuralMagic/code/bert/deepsparse/models/oBERT-Large_95sparse_block4_qat.onnx.tar.xz`
      - Workflow:
    * `_onnx,fp32`
      - Environment variables:
        - *CM_ML_MODEL_F1*: `90.874`
      - Workflow:
    * `_onnx,fp32,armi`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://armi.in/files/model.onnx`
        - *CM_PACKAGE_URL1*: `https://zenodo.org/record/3733910/files/model.onnx`
      - Workflow:
    * `_onnx,fp32,zenodo`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/3733910/files/model.onnx`
      - Workflow:
    * `_onnx,int8`
      - Environment variables:
        - *CM_ML_MODEL_F1*: `90.067`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/3750364/files/bert_large_v1_1_fake_quant.onnx`
      - Workflow:
    * `_onnx,int8,amazon-s3`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://mlperf-public.s3.us-west-2.amazonaws.com/bert_large_v1_1_fake_quant.onnx`
      - Workflow:
    * `_onnx,int8,zenodo`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/3750364/files/bert_large_v1_1_fake_quant.onnx`
      - Workflow:
    * `_onnxruntime`
      - Workflow:
    * `_pytorch,fp32`
      - Environment variables:
        - *CM_ML_MODEL_F1*: `90.874`
        - *CM_DOWNLOAD_CHECKSUM*: `00fbcbfaebfa20d87ac9885120a6e9b4`
      - Workflow:
    * `_pytorch,fp32,armi`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://armi.in/files/fp32/model.pytorch`
        - *CM_PACKAGE_URL1*: `https://zenodo.org/record/3733896/files/model.pytorch`
      - Workflow:
    * `_pytorch,fp32,zenodo`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/3733896/files/model.pytorch`
      - Workflow:
    * `_pytorch,int8`
      - Environment variables:
        - *CM_ML_MODEL_F1*: `90.633`
      - Workflow:
    * `_pytorch,int8,armi`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://armi.in/files/int8/pytorch_model.bin`
        - *CM_PACKAGE_URL1*: `https://zenodo.org/record/4792496/files/pytorch_model.bin`
      - Workflow:
    * `_pytorch,int8,zenodo`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/4792496/files/pytorch_model.bin`
      - Workflow:
    * `_tensorflow`
      - Workflow:
    * `_tf,fp32`
      - Environment variables:
        - *CM_ML_MODEL_F1*: `90.874`
      - Workflow:
    * `_tf,fp32,zenodo`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/3939747/files/model.pb`
      - Workflow:

    </details>


  * Group "**download-source**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_amazon-s3`
      - Workflow:
    * `_armi`
      - Workflow:
    * `_custom-url.#`
      - Environment variables:
        - *CM_PACKAGE_URL*: `#`
      - Workflow:
    * `_github`
      - Workflow:
    * `_zenodo`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_deepsparse`
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `deepsparse`
        - *CM_ML_MODEL_INPUT_IDS_NAME*: `input_ids`
        - *CM_ML_MODEL_INPUT_MASK_NAME*: `input_mask`
        - *CM_ML_MODEL_INPUT_SEGMENTS_NAME*: `segment_ids`
        - *CM_ML_MODEL_OUTPUT_END_LOGITS_NAME*: `output_end_logits`
        - *CM_ML_MODEL_OUTPUT_START_LOGITS_NAME*: `output_start_logits`
      - Workflow:
    * **`_onnx`** (default)
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `onnx`
        - *CM_ML_MODEL_INPUT_IDS_NAME*: `input_ids`
        - *CM_ML_MODEL_INPUT_MASK_NAME*: `input_mask`
        - *CM_ML_MODEL_INPUT_SEGMENTS_NAME*: `segment_ids`
        - *CM_ML_MODEL_OUTPUT_END_LOGITS_NAME*: `output_end_logits`
        - *CM_ML_MODEL_OUTPUT_START_LOGITS_NAME*: `output_start_logits`
      - Workflow:
    * `_pytorch`
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `pytorch`
        - *CM_ML_MODEL_INPUT_IDS_NAME*: `input_ids`
        - *CM_ML_MODEL_INPUT_MASK_NAME*: `input_mask`
        - *CM_ML_MODEL_INPUT_SEGMENTS_NAME*: `segment_ids`
        - *CM_ML_MODEL_OUTPUT_END_LOGITS_NAME*: `output_end_logits`
        - *CM_ML_MODEL_OUTPUT_START_LOGITS_NAME*: `output_start_logits`
      - Workflow:
    * `_tf`
      - Environment variables:
        - *CM_ML_MODEL_FRAMEWORK*: `tf`
        - *CM_ML_MODEL_INPUT_IDS_NAME*: `input_ids`
        - *CM_ML_MODEL_INPUT_MASK_NAME*: `input_mask`
        - *CM_ML_MODEL_INPUT_SEGMENTS_NAME*: `segment_ids`
        - *CM_ML_MODEL_OUTPUT_END_LOGITS_NAME*: `output_end_logits`
        - *CM_ML_MODEL_OUTPUT_START_LOGITS_NAME*: `output_start_logits`
      - Workflow:

    </details>


  * Group "**packing**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_packed`
      - Environment variables:
        - *CM_ML_MODEL_BERT_PACKED*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,python3
             * CM names: `--adr.['python', 'python3']...`
             - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
           * get,generic-python-lib,_torch
             * CM names: `--adr.['torch', 'pytorch']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.tensorflow
             * CM names: `--adr.['tensorflow']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.transformers
             * CM names: `--adr.['transformers']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.protobuf
             * CM names: `--adr.['protobuf']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.onnx
             * CM names: `--adr.['onnx']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_onnx-graphsurgeon
             * CM names: `--adr.['onnx-graphsurgeon']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_numpy
             * CM names: `--adr.['numpy']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,mlperf,inference,src
             * CM names: `--adr.['inference-src']...`
             - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
        1. ***Read "prehook_deps" on other CM scripts***
           * download,file,_wget,_url.https://zenodo.org/record/3733868/files/model.ckpt-5474.data-00000-of-00001
             - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
           * download,file,_wget,_url.https://zenodo.org/record/3733868/files/model.ckpt-5474.index
             - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
           * download,file,_wget,_url.https://zenodo.org/record/3733868/files/model.ckpt-5474.meta
             - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
           * download,file,_wget,_url.https://zenodo.org/record/3733868/files/vocab.txt
             - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
           * download,file,_wget,_url.https://raw.githubusercontent.com/krai/axs2kilt/main/model_onnx_bert_large_packed_recipe/convert_model.py
             - CM script: [download-file](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-file)
    * **`_unpacked`** (default)
      - Environment variables:
        - *CM_ML_MODEL_BERT_PACKED*: `no`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_fp32`** (default)
      - Environment variables:
        - *CM_ML_MODEL_PRECISION*: `fp32`
      - Workflow:
    * `_int8`
      - Environment variables:
        - *CM_ML_MODEL_PRECISION*: `int8`
        - *CM_ML_MODEL_QUANTIZED*: `yes`
      - Workflow:

    </details>


#### Default variations

`_fp32,_onnx,_unpacked`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-large-squad/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-large-squad/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-large-squad/_cm.json)***
     * download-and-extract
       * `if (CM_ML_MODEL_BERT_PACKED  != yes)`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run native script if exists***
     * [run-packed.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-large-squad/run-packed.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-large-squad/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-large-squad/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-large-squad/_cm.json)***
     * get,dataset-aux,squad-vocab
       - CM script: [get-dataset-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad-vocab)

___
### Script output
`cmr "get ml-model raw bert bert-large bert-squad language language-processing [,variations]"  -j`
#### New environment keys (filter)

* `CM_ML_MODEL*`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_BERT_LARGE_FP32_PATH`
* `CM_ML_MODEL_BERT_LARGE_INT8_PATH`
* `CM_ML_MODEL_BERT_PACKED_PATH`
* `CM_ML_MODEL_FILE`
* `CM_ML_MODEL_FILE_WITH_PATH`