*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Variations](#variations)
  * [ All variations](#all-variations)
  * [ Variations by groups](#variations-by-groups)
* [Default environment](#default-environment)
* [CM script workflow](#cm-script-workflow)
* [New environment export](#new-environment-export)
* [New environment detected from customize](#new-environment-detected-from-customize)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Maintainers](#maintainers)

</details>

___
### About

*TBD*
___
### Category

ML/AI models.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
get,ml-model,bert,bert-large,bert-squad,language,language-processing

___
### Variations
#### All variations
* **fp32** (default)
  - *ENV CM_ML_MODEL_PRECISION: fp32*
* int8
  - *ENV CM_ML_MODEL_PRECISION: int8*
  - *ENV CM_ML_MODEL_QUANTIZED: yes*
  - *ENV CM_PACKAGE_URL: https://zenodo.org/record/3750364/files/bert_large_v1_1_fake_quant.onnx*
* **onnx** (default)
  - *ENV CM_ML_MODEL_FRAMEWORK: onnx*
  - *ENV CM_ML_MODEL_INPUT_IDS_NAME: input_ids*
  - *ENV CM_ML_MODEL_INPUT_MASK_NAME: input_mask*
  - *ENV CM_ML_MODEL_INPUT_SEGMENTS_NAME: segment_ids*
  - *ENV CM_ML_MODEL_OUTPUT_END_LOGITS_NAME: output_end_logits*
  - *ENV CM_ML_MODEL_OUTPUT_START_LOGITS_NAME: output_start_logits*
* onnx,fp32
  - *ENV CM_ML_MODEL_F1: 90.874*
  - *ENV CM_PACKAGE_URL: https://zenodo.org/record/3733910/files/model.onnx*
* onnx,int8
  - *ENV CM_ML_MODEL_F1: 90.067*
  - *ENV CM_PACKAGE_URL: https://zenodo.org/record/3750364/files/bert_large_v1_1_fake_quant.onnx*
* onnxruntime
* pytorch
  - *ENV CM_ML_MODEL_FRAMEWORK: pytorch*
  - *ENV CM_ML_MODEL_INPUT_IDS_NAME: input_ids*
  - *ENV CM_ML_MODEL_INPUT_MASK_NAME: input_mask*
  - *ENV CM_ML_MODEL_INPUT_SEGMENTS_NAME: segment_ids*
  - *ENV CM_ML_MODEL_OUTPUT_END_LOGITS_NAME: output_end_logits*
  - *ENV CM_ML_MODEL_OUTPUT_START_LOGITS_NAME: output_start_logits*
* pytorch,fp32
  - *ENV CM_ML_MODEL_F1: 90.874*
  - *ENV CM_PACKAGE_URL: https://zenodo.org/record/3733896/files/model.pytorch*
* pytorch,int8
  - *ENV CM_ML_MODEL_F1: 90.633*
  - *ENV CM_PACKAGE_URL: https://zenodo.org/record/4792496/files/pytorch_model.bin*
* tensorflow
* tf
  - *ENV CM_ML_MODEL_F1: 90.874*
  - *ENV CM_ML_MODEL_FRAMEWORK: tf*
  - *ENV CM_ML_MODEL_INPUT_IDS_NAME: input_ids*
  - *ENV CM_ML_MODEL_INPUT_MASK_NAME: input_mask*
  - *ENV CM_ML_MODEL_INPUT_SEGMENTS_NAME: segment_ids*
  - *ENV CM_ML_MODEL_OUTPUT_END_LOGITS_NAME: output_end_logits*
  - *ENV CM_ML_MODEL_OUTPUT_START_LOGITS_NAME: output_start_logits*
  - *ENV CM_VOCAB_FILE_URL: https://zenodo.org/record/3733868/files/vocab.txt*
  - *ENV CM_PACKAGE_URL: https://zenodo.org/record/3939747/files/model.pb*

#### Variations by groups

  * framework
    * **onnx** (default)
      - *ENV CM_ML_MODEL_FRAMEWORK: onnx*
      - *ENV CM_ML_MODEL_INPUT_IDS_NAME: input_ids*
      - *ENV CM_ML_MODEL_INPUT_MASK_NAME: input_mask*
      - *ENV CM_ML_MODEL_INPUT_SEGMENTS_NAME: segment_ids*
      - *ENV CM_ML_MODEL_OUTPUT_END_LOGITS_NAME: output_end_logits*
      - *ENV CM_ML_MODEL_OUTPUT_START_LOGITS_NAME: output_start_logits*
    * pytorch
      - *ENV CM_ML_MODEL_FRAMEWORK: pytorch*
      - *ENV CM_ML_MODEL_INPUT_IDS_NAME: input_ids*
      - *ENV CM_ML_MODEL_INPUT_MASK_NAME: input_mask*
      - *ENV CM_ML_MODEL_INPUT_SEGMENTS_NAME: segment_ids*
      - *ENV CM_ML_MODEL_OUTPUT_END_LOGITS_NAME: output_end_logits*
      - *ENV CM_ML_MODEL_OUTPUT_START_LOGITS_NAME: output_start_logits*
    * tf
      - *ENV CM_ML_MODEL_F1: 90.874*
      - *ENV CM_ML_MODEL_FRAMEWORK: tf*
      - *ENV CM_ML_MODEL_INPUT_IDS_NAME: input_ids*
      - *ENV CM_ML_MODEL_INPUT_MASK_NAME: input_mask*
      - *ENV CM_ML_MODEL_INPUT_SEGMENTS_NAME: segment_ids*
      - *ENV CM_ML_MODEL_OUTPUT_END_LOGITS_NAME: output_end_logits*
      - *ENV CM_ML_MODEL_OUTPUT_START_LOGITS_NAME: output_start_logits*
      - *ENV CM_VOCAB_FILE_URL: https://zenodo.org/record/3733868/files/vocab.txt*
      - *ENV CM_PACKAGE_URL: https://zenodo.org/record/3939747/files/model.pb*

  * precision
    * **fp32** (default)
      - *ENV CM_ML_MODEL_PRECISION: fp32*
    * int8
      - *ENV CM_ML_MODEL_PRECISION: int8*
      - *ENV CM_ML_MODEL_QUANTIZED: yes*
      - *ENV CM_PACKAGE_URL: https://zenodo.org/record/3750364/files/bert_large_v1_1_fake_quant.onnx*
___
### Default environment

___
### CM script workflow

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad/_cm.json)
___
### New environment export

* **CM_ML_MODEL***
___
### New environment detected from customize

* **CM_ML_MODEL_BERT_VOCAB_FILE_WITH_PATH**
* **CM_ML_MODEL_FILE**
* **CM_ML_MODEL_FILE_WITH_PATH**
* **CM_ML_MODEL_PATH**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="get,ml-model,bert,bert-large,bert-squad,language,language-processing"`

*or*

`cm run script "get ml-model bert bert-large bert-squad language language-processing"`

*or*

`cm run script 5e865dbdc65949d2`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,bert,bert-large,bert-squad,language,language-processing'
                  'out':'con'})

if r['return']>0:
    print (r['error'])
```

#### CM modular Docker container
*TBD*
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)