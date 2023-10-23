<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM GUI](#cm-gui)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! Use `README-extra.md` to add more info.*

### Description

#### Information

* Category: *ML/AI models.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,ml-model,raw,bert,bert-large,bert-squad,language,language-processing*
* Output cached?: *True*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

##### CM pull repository

```cm pull repo mlcommons@ck```

##### CM script automation help

```cm run script --help```

#### CM CLI

1. `cm run script --tags=get,ml-model,raw,bert,bert-large,bert-squad,language,language-processing[,variations] `

2. `cm run script "get ml-model raw bert bert-large bert-squad language language-processing[,variations]" `

3. `cm run script 5e865dbdc65949d2 `

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

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


#### CM GUI

```cm run script --tags=gui --script="get,ml-model,raw,bert,bert-large,bert-squad,language,language-processing"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,raw,bert,bert-large,bert-squad,language,language-processing) to generate CM CMD.

#### CM modular Docker container

*TBD*

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
    * `_onnx,fp32,amazon-s3`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://mlperf-public.s3.us-west-2.amazonaws.com/model.onnx`
      - Workflow:
    * `_onnx,fp32,zenodo`
      - Environment variables:
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/3733910/files/model.onnx`
      - Workflow:
    * `_onnx,int8`
      - Environment variables:
        - *CM_ML_MODEL_F1*: `90.067`
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
      - Workflow:
    * `_pytorch,fp32,zenodo`
      - Environment variables:
        - *CM_ML_MODEL_F1*: `90.874`
        - *CM_PACKAGE_URL*: `https://zenodo.org/record/3733896/files/model.pytorch`
      - Workflow:
    * `_pytorch,int8`
      - Environment variables:
        - *CM_ML_MODEL_F1*: `90.633`
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
           * get,generic-python-lib,_package.setuptools_rust
             * CM names: `--adr.['setuptools_rust']...`
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
           * get,generic-python-lib,_package.onnx-simplifier
             * CM names: `--adr.['onnx-simplifier']...`
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
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad/_cm.json)***
     * download-and-extract
       * `if (CM_ML_MODEL_BERT_PACKED  != yes)`
       - CM script: [download-and-extract](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/download-and-extract)
  1. ***Run native script if exists***
     * [run-packed.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad/run-packed.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad/_cm.json)***
     * get,dataset-aux,squad-vocab
       - CM script: [get-dataset-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad-vocab)
</details>

___
### Script output
#### New environment keys (filter)

* `CM_ML_MODEL*`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_BERT_LARGE_FP32_PATH`
* `CM_ML_MODEL_BERT_LARGE_INT8_PATH`
* `CM_ML_MODEL_BERT_PACKED_PATH`
* `CM_ML_MODEL_FILE`
* `CM_ML_MODEL_FILE_WITH_PATH`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)