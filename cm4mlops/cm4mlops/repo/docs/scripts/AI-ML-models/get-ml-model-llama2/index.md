# get-ml-model-llama2
Automatically generated README for this automation recipe: **get-ml-model-llama2**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-llama2/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get raw ml-model language-processing llama2 llama2-70b text-summarization" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,raw,ml-model,language-processing,llama2,llama2-70b,text-summarization[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get raw ml-model language-processing llama2 llama2-70b text-summarization [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,raw,ml-model,language-processing,llama2,llama2-70b,text-summarization'
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
    cm docker script "get raw ml-model language-processing llama2 llama2-70b text-summarization[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_batch_size.#`
               - ENV variables:
                   - CM_ML_MODEL_BATCH_SIZE: `#`

        </details>


      * Group "**framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_pytorch`** (default)
               - ENV variables:
                   - CM_ML_MODEL_FRAMEWORK: `pytorch`

        </details>


      * Group "**huggingface-stub**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_meta-llama/Llama-2-70b-chat-hf`** (default)
               - ENV variables:
                   - CM_GIT_CHECKOUT_FOLDER: `Llama-2-70b-chat-hf`
                   - CM_MODEL_ZOO_ENV_KEY: `LLAMA2`
        * `_meta-llama/Llama-2-7b-chat-hf`
               - ENV variables:
                   - CM_GIT_CHECKOUT_FOLDER: `Llama-2-7b-chat-hf`
                   - CM_MODEL_ZOO_ENV_KEY: `LLAMA2`
        * `_stub.#`
               - ENV variables:
                   - CM_MODEL_ZOO_ENV_KEY: `LLAMA2`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_fp32`** (default)
               - ENV variables:
                   - CM_ML_MODEL_INPUT_DATA_TYPES: `fp32`
                   - CM_ML_MODEL_PRECISION: `fp32`
                   - CM_ML_MODEL_WEIGHT_DATA_TYPES: `fp32`
        * `_int8`
               - ENV variables:
                   - CM_ML_MODEL_INPUT_DATA_TYPES: `int8`
                   - CM_ML_MODEL_PRECISION: `int8`
                   - CM_ML_MODEL_WEIGHT_DATA_TYPES: `int8`
        * `_uint8`
               - ENV variables:
                   - CM_ML_MODEL_INPUT_DATA_TYPES: `uint8`
                   - CM_ML_MODEL_PRECISION: `uint8`
                   - CM_ML_MODEL_WEIGHT_DATA_TYPES: `uint8`

        </details>


    ##### Default variations

    `_fp32,_meta-llama/Llama-2-70b-chat-hf,_pytorch`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--checkpoint=value`  &rarr;  `LLAMA2_CHECKPOINT_PATH=value`




___
#### Script output
```bash
cmr "get raw ml-model language-processing llama2 llama2-70b text-summarization [variations]" [--input_flags] -j
```