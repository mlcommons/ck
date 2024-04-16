**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-neuralmagic-zoo).**



Automatically generated README for this automation recipe: **get-ml-model-neuralmagic-zoo**

Category: **AI/ML models**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-ml-model-neuralmagic-zoo,adbb3f2525a14f97) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-neuralmagic-zoo)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,ml-model,model,zoo,deepsparse,model-zoo,sparse-zoo,neuralmagic,neural-magic*
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

````cmr "get ml-model model zoo deepsparse model-zoo sparse-zoo neuralmagic neural-magic" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,ml-model,model,zoo,deepsparse,model-zoo,sparse-zoo,neuralmagic,neural-magic`

`cm run script --tags=get,ml-model,model,zoo,deepsparse,model-zoo,sparse-zoo,neuralmagic,neural-magic[,variations] `

*or*

`cmr "get ml-model model zoo deepsparse model-zoo sparse-zoo neuralmagic neural-magic"`

`cmr "get ml-model model zoo deepsparse model-zoo sparse-zoo neuralmagic neural-magic [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

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


#### Run this script via GUI

```cmr "cm gui" --script="get,ml-model,model,zoo,deepsparse,model-zoo,sparse-zoo,neuralmagic,neural-magic"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,ml-model,model,zoo,deepsparse,model-zoo,sparse-zoo,neuralmagic,neural-magic) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get ml-model model zoo deepsparse model-zoo sparse-zoo neuralmagic neural-magic[variations]" `

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
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-neuralmagic-zoo/_cm.json)***
     * get,python3
       * CM names: `--adr.['python3', 'python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-python-lib,_package.protobuf
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_sparsezoo
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-neuralmagic-zoo/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-neuralmagic-zoo/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-neuralmagic-zoo/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-neuralmagic-zoo/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-neuralmagic-zoo/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-neuralmagic-zoo/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-neuralmagic-zoo/_cm.json)

___
### Script output
`cmr "get ml-model model zoo deepsparse model-zoo sparse-zoo neuralmagic neural-magic [,variations]"  -j`
#### New environment keys (filter)

* `CM_GET_DEPENDENT_CACHED_PATH`
* `CM_MLPERF_CUSTOM_MODEL_PATH`
* `CM_ML_MODEL*`
* `CM_MODEL_ZOO_STUB`
#### New environment keys auto-detected from customize

* `CM_GET_DEPENDENT_CACHED_PATH`
* `CM_MLPERF_CUSTOM_MODEL_PATH`