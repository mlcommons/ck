# get-ml-model-neuralmagic-zoo
Automatically generated README for this automation recipe: **get-ml-model-neuralmagic-zoo**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-neuralmagic-zoo/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model model zoo deepsparse model-zoo sparse-zoo neuralmagic neural-magic" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,ml-model,model,zoo,deepsparse,model-zoo,sparse-zoo,neuralmagic,neural-magic[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get ml-model model zoo deepsparse model-zoo sparse-zoo neuralmagic neural-magic [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


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


=== "Docker"
    ##### Run this script via Docker (beta)

    ```bash
    cm docker script "get ml-model model zoo deepsparse model-zoo sparse-zoo neuralmagic neural-magic[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_bert-base-pruned90-none`
              - Aliases: `_model-stub.zoo:nlp/question_answering/bert-base/pytorch/huggingface/squad/pruned90-none`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/bert-base/pytorch/huggingface/squad/pruned90-none`
                   - CM_ML_MODEL_FULL_NAME: `bert-base-pruned90-none-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://huggingface.co/bert-base-uncased`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_RETRAINING: `no`
        * `_bert-base-pruned95_obs_quant-none`
              - Aliases: `_model-stub.zoo:nlp/question_answering/bert-base/pytorch/huggingface/squad/pruned95_obs_quant-none`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/bert-base/pytorch/huggingface/squad/pruned95_obs_quant-none`
                   - CM_ML_MODEL_FULL_NAME: `bert-base-pruned95_obs_quant-none-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://huggingface.co/bert-base-uncased`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `int8`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int64`
                   - CM_ML_MODEL_RETRAINING: `yes`
        * `_bert-base_cased-pruned90-none`
              - Aliases: `_model-stub.zoo:nlp/question_answering/bert-base_cased/pytorch/huggingface/squad/pruned90-none`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/bert-base_cased/pytorch/huggingface/squad/pruned90-none`
                   - CM_ML_MODEL_FULL_NAME: `bert-base_cased-pruned90-none-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://huggingface.co/bert-base-cased`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_RETRAINING: `no`
        * `_bert-large-base-none`
              - Aliases: `_model-stub.zoo:nlp/question_answering/bert-large/pytorch/huggingface/squad/base-none`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/bert-large/pytorch/huggingface/squad/base-none`
                   - CM_ML_MODEL_FULL_NAME: `bert-large-base-none-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://huggingface.co/bert-large-uncased`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_RETRAINING: `no`
        * `_bert-large-pruned80_quant-none-vnni`
              - Aliases: `_model-stub.zoo:nlp/question_answering/bert-large/pytorch/huggingface/squad/pruned80_quant-none-vnni`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/bert-large/pytorch/huggingface/squad/pruned80_quant-none-vnni`
                   - CM_ML_MODEL_FULL_NAME: `bert-large-pruned80_quant-none-vnni-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://huggingface.co/bert-large-uncased`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `int8`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int64`
                   - CM_ML_MODEL_RETRAINING: `no`
        * `_mobilebert-14layer_pruned50-none-vnni`
              - Aliases: `_model-stub.zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50-none-vnni`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50-none-vnni`
                   - CM_ML_MODEL_FULL_NAME: `mobilebert-14layer_pruned50-none-vnni-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://storage.googleapis.com/cloud-tpu-checkpoints/mobilebert/uncased_L-24_H-128_B-512_A-4_F-4_OPT.tar.gz`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_RETRAINING: `no`
        * `_mobilebert-14layer_pruned50_quant-none-vnni`
              - Aliases: `_model-stub.zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50_quant-none-vnni`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50_quant-none-vnni`
                   - CM_ML_MODEL_FULL_NAME: `mobilebert-14layer_pruned50_quant-none-vnni-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://storage.googleapis.com/cloud-tpu-checkpoints/mobilebert/uncased_L-24_H-128_B-512_A-4_F-4_OPT.tar.gz`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `int8`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int64`
                   - CM_ML_MODEL_RETRAINING: `yes`
        * `_mobilebert-base_quant-none`
              - Aliases: `_model-stub.zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/base_quant-none`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/base_quant-none`
                   - CM_ML_MODEL_FULL_NAME: `mobilebert-base_quant-none-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://storage.googleapis.com/cloud-tpu-checkpoints/mobilebert/uncased_L-24_H-128_B-512_A-4_F-4_OPT.tar.gz`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `int8`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int64`
                   - CM_ML_MODEL_RETRAINING: `yes`
        * `_mobilebert-none-base-none`
              - Aliases: `_model-stub.zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/base-none`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/base-none`
                   - CM_ML_MODEL_FULL_NAME: `mobilebert-none-base-none-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://storage.googleapis.com/cloud-tpu-checkpoints/mobilebert/uncased_L-24_H-128_B-512_A-4_F-4_OPT.tar.gz`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_RETRAINING: `no`
        * `_model-stub.#`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `#`
        * `_obert-base-pruned90-none`
              - Aliases: `_model-stub.zoo:nlp/question_answering/obert-base/pytorch/huggingface/squad/pruned90-none`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/obert-base/pytorch/huggingface/squad/pruned90-none`
                   - CM_ML_MODEL_FULL_NAME: `obert-base-pruned90-none-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://huggingface.co/bert-large-uncased`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_RETRAINING: `no`
        * `_obert-large-base-none`
              - Aliases: `_model-stub.zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/base-none`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/base-none`
                   - CM_ML_MODEL_FULL_NAME: `obert-large-base-none-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://huggingface.co/bert-large-uncased`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_RETRAINING: `no`
        * `_obert-large-pruned95-none-vnni`
              - Aliases: `_model-stub.zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned95-none-vnni`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned95-none-vnni`
                   - CM_ML_MODEL_FULL_NAME: `obert-large-pruned95-none-vnni-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://huggingface.co/bert-large-uncased`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_RETRAINING: `no`
        * `_obert-large-pruned95_quant-none-vnni`
              - Aliases: `_model-stub.zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned95_quant-none-vnni`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned95_quant-none-vnni`
                   - CM_ML_MODEL_FULL_NAME: `obert-large-pruned95_quant-none-vnni-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://huggingface.co/bert-large-uncased`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `int8`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int64`
                   - CM_ML_MODEL_RETRAINING: `yes`
        * `_obert-large-pruned97-none`
              - Aliases: `_model-stub.zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned97-none`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned97-none`
                   - CM_ML_MODEL_FULL_NAME: `obert-large-pruned97-none-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://huggingface.co/bert-large-uncased`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `fp32`
                   - CM_ML_MODEL_RETRAINING: `no`
        * `_obert-large-pruned97-quant-none`
              - Aliases: `_model-stub.zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned97_quant-none`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned97_quant-none`
                   - CM_ML_MODEL_FULL_NAME: `obert-large-pruned97-quant-none-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://huggingface.co/bert-large-uncased`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `int8`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int64`
                   - CM_ML_MODEL_RETRAINING: `no`
        * `_oberta-base-pruned90-quant-none`
              - Aliases: `_model-stub.zoo:nlp/question_answering/oberta-base/pytorch/huggingface/squad/pruned90_quant-none`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/oberta-base/pytorch/huggingface/squad/pruned90_quant-none`
                   - CM_ML_MODEL_FULL_NAME: `oberta-base-pruned90-quant-none-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://huggingface.co/roberta-base`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `int8`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int64`
                   - CM_ML_MODEL_RETRAINING: `no`
        * `_roberta-base-pruned85-quant-none`
              - Aliases: `_model-stub.zoo:nlp/question_answering/roberta-base/pytorch/huggingface/squad/pruned85_quant-none`
               - ENV variables:
                   - CM_MODEL_ZOO_STUB: `zoo:nlp/question_answering/roberta-base/pytorch/huggingface/squad/pruned85_quant-none`
                   - CM_ML_MODEL_FULL_NAME: `roberta-base-pruned85-quant-none-bert-99`
                   - CM_ML_MODEL_STARTING_WEIGHTS_FILENAME: `https://huggingface.co/roberta-base`
                   - CM_ML_MODEL_WEIGHT_TRANSFORMATIONS: `quantization, unstructured pruning`
                   - CM_ML_MODEL_WEIGHTS_DATA_TYPE: `int8`
                   - CM_ML_MODEL_INPUTS_DATA_TYPE: `int64`
                   - CM_ML_MODEL_RETRAINING: `no`

        </details>


#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-neuralmagic-zoo/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-neuralmagic-zoo/run.bat)
___
#### Script output
```bash
cmr "get ml-model model zoo deepsparse model-zoo sparse-zoo neuralmagic neural-magic [variations]"  -j
```