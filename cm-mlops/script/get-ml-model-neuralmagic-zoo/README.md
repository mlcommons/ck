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
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,ml-model,model,zoo,deepsparse,model-zoo,sparse-zoo,neuralmagic,neural-magic*
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

1. `cm run script --tags=get,ml-model,model,zoo,deepsparse,model-zoo,sparse-zoo,neuralmagic,neural-magic[,variations] `

2. `cm run script "get ml-model model zoo deepsparse model-zoo sparse-zoo neuralmagic neural-magic[,variations]" `

3. `cm run script adbb3f2525a14f97 `

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,model,zoo,deepsparse,model-zoo,sparse-zoo,neuralmagic,neural-magic'
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

```cm run script --tags=gui --script="get,ml-model,model,zoo,deepsparse,model-zoo,sparse-zoo,neuralmagic,neural-magic"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,model,zoo,deepsparse,model-zoo,sparse-zoo,neuralmagic,neural-magic) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert-base-pruned90-none`
      - Aliases: `_model-stub.zoo:nlp/question_answering/bert-base/pytorch/huggingface/squad/pruned90-none`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/bert-base/pytorch/huggingface/squad/pruned90-none`
        - *CM_ML_MODEL_FULL_NAME*: `bert-base-pruned90-none-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://huggingface.co/bert-base-uncased`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_RETRAINING*: `no`
      - Workflow:
    * `_bert-base-pruned95_obs_quant-none`
      - Aliases: `_model-stub.zoo:nlp/question_answering/bert-base/pytorch/huggingface/squad/pruned95_obs_quant-none`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/bert-base/pytorch/huggingface/squad/pruned95_obs_quant-none`
        - *CM_ML_MODEL_FULL_NAME*: `bert-base-pruned95_obs_quant-none-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://huggingface.co/bert-base-uncased`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `quantization, unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `int8`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `int64`
        - *CM_ML_MODEL_RETRAINING*: `yes`
      - Workflow:
    * `_bert-base_cased-pruned90-none`
      - Aliases: `_model-stub.zoo:nlp/question_answering/bert-base_cased/pytorch/huggingface/squad/pruned90-none`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/bert-base_cased/pytorch/huggingface/squad/pruned90-none`
        - *CM_ML_MODEL_FULL_NAME*: `bert-base_cased-pruned90-none-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://huggingface.co/bert-base-cased`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_RETRAINING*: `no`
      - Workflow:
    * `_bert-large-base-none`
      - Aliases: `_model-stub.zoo:nlp/question_answering/bert-large/pytorch/huggingface/squad/base-none`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/bert-large/pytorch/huggingface/squad/base-none`
        - *CM_ML_MODEL_FULL_NAME*: `bert-large-base-none-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://huggingface.co/bert-large-uncased`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_RETRAINING*: `no`
      - Workflow:
    * `_bert-large-pruned80_quant-none-vnni`
      - Aliases: `_model-stub.zoo:nlp/question_answering/bert-large/pytorch/huggingface/squad/pruned80_quant-none-vnni`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/bert-large/pytorch/huggingface/squad/pruned80_quant-none-vnni`
        - *CM_ML_MODEL_FULL_NAME*: `bert-large-pruned80_quant-none-vnni-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://huggingface.co/bert-large-uncased`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `quantization, unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `int8`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `int64`
        - *CM_ML_MODEL_RETRAINING*: `no`
      - Workflow:
    * `_mobilebert-14layer_pruned50-none-vnni`
      - Aliases: `_model-stub.zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50-none-vnni`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50-none-vnni`
        - *CM_ML_MODEL_FULL_NAME*: `mobilebert-14layer_pruned50-none-vnni-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://storage.googleapis.com/cloud-tpu-checkpoints/mobilebert/uncased_L-24_H-128_B-512_A-4_F-4_OPT.tar.gz`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_RETRAINING*: `no`
      - Workflow:
    * `_mobilebert-14layer_pruned50_quant-none-vnni`
      - Aliases: `_model-stub.zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50_quant-none-vnni`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50_quant-none-vnni`
        - *CM_ML_MODEL_FULL_NAME*: `mobilebert-14layer_pruned50_quant-none-vnni-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://storage.googleapis.com/cloud-tpu-checkpoints/mobilebert/uncased_L-24_H-128_B-512_A-4_F-4_OPT.tar.gz`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `quantization, unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `int8`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `int64`
        - *CM_ML_MODEL_RETRAINING*: `yes`
      - Workflow:
    * `_mobilebert-base_quant-none`
      - Aliases: `_model-stub.zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/base_quant-none`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/base_quant-none`
        - *CM_ML_MODEL_FULL_NAME*: `mobilebert-base_quant-none-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://storage.googleapis.com/cloud-tpu-checkpoints/mobilebert/uncased_L-24_H-128_B-512_A-4_F-4_OPT.tar.gz`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `quantization, unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `int8`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `int64`
        - *CM_ML_MODEL_RETRAINING*: `yes`
      - Workflow:
    * `_mobilebert-none-base-none`
      - Aliases: `_model-stub.zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/base-none`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/base-none`
        - *CM_ML_MODEL_FULL_NAME*: `mobilebert-none-base-none-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://storage.googleapis.com/cloud-tpu-checkpoints/mobilebert/uncased_L-24_H-128_B-512_A-4_F-4_OPT.tar.gz`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_RETRAINING*: `no`
      - Workflow:
    * `_model-stub.#`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `#`
      - Workflow:
    * `_obert-base-pruned90-none`
      - Aliases: `_model-stub.zoo:nlp/question_answering/obert-base/pytorch/huggingface/squad/pruned90-none`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/obert-base/pytorch/huggingface/squad/pruned90-none`
        - *CM_ML_MODEL_FULL_NAME*: `obert-base-pruned90-none-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://huggingface.co/bert-large-uncased`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_RETRAINING*: `no`
      - Workflow:
    * `_obert-large-base-none`
      - Aliases: `_model-stub.zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/base-none`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/base-none`
        - *CM_ML_MODEL_FULL_NAME*: `obert-large-base-none-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://huggingface.co/bert-large-uncased`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_RETRAINING*: `no`
      - Workflow:
    * `_obert-large-pruned95-none-vnni`
      - Aliases: `_model-stub.zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned95-none-vnni`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned95-none-vnni`
        - *CM_ML_MODEL_FULL_NAME*: `obert-large-pruned95-none-vnni-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://huggingface.co/bert-large-uncased`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_RETRAINING*: `no`
      - Workflow:
    * `_obert-large-pruned95_quant-none-vnni`
      - Aliases: `_model-stub.zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned95_quant-none-vnni`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned95_quant-none-vnni`
        - *CM_ML_MODEL_FULL_NAME*: `obert-large-pruned95_quant-none-vnni-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://huggingface.co/bert-large-uncased`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `quantization, unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `int8`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `int64`
        - *CM_ML_MODEL_RETRAINING*: `yes`
      - Workflow:
    * `_obert-large-pruned97-none`
      - Aliases: `_model-stub.zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned97-none`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned97-none`
        - *CM_ML_MODEL_FULL_NAME*: `obert-large-pruned97-none-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://huggingface.co/bert-large-uncased`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `fp32`
        - *CM_ML_MODEL_RETRAINING*: `no`
      - Workflow:
    * `_obert-large-pruned97-quant-none`
      - Aliases: `_model-stub.zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned97_quant-none`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned97_quant-none`
        - *CM_ML_MODEL_FULL_NAME*: `obert-large-pruned97-quant-none-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://huggingface.co/bert-large-uncased`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `quantization, unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `int8`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `int64`
        - *CM_ML_MODEL_RETRAINING*: `no`
      - Workflow:
    * `_oberta-base-pruned90-quant-none`
      - Aliases: `_model-stub.zoo:nlp/question_answering/oberta-base/pytorch/huggingface/squad/pruned90_quant-none`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/oberta-base/pytorch/huggingface/squad/pruned90_quant-none`
        - *CM_ML_MODEL_FULL_NAME*: `oberta-base-pruned90-quant-none-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://huggingface.co/roberta-base`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `quantization, unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `int8`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `int64`
        - *CM_ML_MODEL_RETRAINING*: `no`
      - Workflow:
    * `_roberta-base-pruned85-quant-none`
      - Aliases: `_model-stub.zoo:nlp/question_answering/roberta-base/pytorch/huggingface/squad/pruned85_quant-none`
      - Environment variables:
        - *CM_MODEL_ZOO_STUB*: `zoo:nlp/question_answering/roberta-base/pytorch/huggingface/squad/pruned85_quant-none`
        - *CM_ML_MODEL_FULL_NAME*: `roberta-base-pruned85-quant-none-bert-99`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://huggingface.co/roberta-base`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `quantization, unstructured pruning`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `int8`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `int64`
        - *CM_ML_MODEL_RETRAINING*: `no`
      - Workflow:

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo/_cm.json)***
     * get,python3
       * CM names: `--adr.['python3', 'python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-python-lib,_sparsezoo
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo/_cm.json)
</details>

___
### Script output
#### New environment keys (filter)

* `CM_GET_DEPENDENT_CACHED_PATH`
* `CM_MLPERF_CUSTOM_MODEL_PATH`
* `CM_ML_MODEL*`
* `CM_MODEL_ZOO_STUB`
#### New environment keys auto-detected from customize

* `CM_GET_DEPENDENT_CACHED_PATH`
* `CM_MLPERF_CUSTOM_MODEL_PATH`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)