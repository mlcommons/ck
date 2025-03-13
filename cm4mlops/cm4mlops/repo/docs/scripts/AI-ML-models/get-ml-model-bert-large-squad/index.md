# get-ml-model-bert-large-squad
Automatically generated README for this automation recipe: **get-ml-model-bert-large-squad**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-bert-large-squad/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model raw bert bert-large bert-squad language language-processing" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,ml-model,raw,bert,bert-large,bert-squad,language,language-processing[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get ml-model raw bert bert-large bert-squad language language-processing [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


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


=== "Docker"
    ##### Run this script via Docker (beta)

    ```bash
    cm docker script "get ml-model raw bert bert-large bert-squad language language-processing[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_onnxruntime`
        * `_tensorflow`

        </details>


      * Group "**download-source**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_amazon-s3`
        * `_armi`
        * `_custom-url.#`
               - ENV variables:
                   - CM_PACKAGE_URL: `#`
        * `_github`
        * `_zenodo`

        </details>


      * Group "**framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_deepsparse`
               - ENV variables:
                   - CM_ML_MODEL_FRAMEWORK: `deepsparse`
                   - CM_ML_MODEL_INPUT_IDS_NAME: `input_ids`
                   - CM_ML_MODEL_INPUT_MASK_NAME: `input_mask`
                   - CM_ML_MODEL_INPUT_SEGMENTS_NAME: `segment_ids`
                   - CM_ML_MODEL_OUTPUT_END_LOGITS_NAME: `output_end_logits`
                   - CM_ML_MODEL_OUTPUT_START_LOGITS_NAME: `output_start_logits`
        * **`_onnx`** (default)
               - ENV variables:
                   - CM_ML_MODEL_FRAMEWORK: `onnx`
                   - CM_ML_MODEL_INPUT_IDS_NAME: `input_ids`
                   - CM_ML_MODEL_INPUT_MASK_NAME: `input_mask`
                   - CM_ML_MODEL_INPUT_SEGMENTS_NAME: `segment_ids`
                   - CM_ML_MODEL_OUTPUT_END_LOGITS_NAME: `output_end_logits`
                   - CM_ML_MODEL_OUTPUT_START_LOGITS_NAME: `output_start_logits`
        * `_pytorch`
               - ENV variables:
                   - CM_ML_MODEL_FRAMEWORK: `pytorch`
                   - CM_ML_MODEL_INPUT_IDS_NAME: `input_ids`
                   - CM_ML_MODEL_INPUT_MASK_NAME: `input_mask`
                   - CM_ML_MODEL_INPUT_SEGMENTS_NAME: `segment_ids`
                   - CM_ML_MODEL_OUTPUT_END_LOGITS_NAME: `output_end_logits`
                   - CM_ML_MODEL_OUTPUT_START_LOGITS_NAME: `output_start_logits`
        * `_tf`
               - ENV variables:
                   - CM_ML_MODEL_FRAMEWORK: `tf`
                   - CM_ML_MODEL_INPUT_IDS_NAME: `input_ids`
                   - CM_ML_MODEL_INPUT_MASK_NAME: `input_mask`
                   - CM_ML_MODEL_INPUT_SEGMENTS_NAME: `segment_ids`
                   - CM_ML_MODEL_OUTPUT_END_LOGITS_NAME: `output_end_logits`
                   - CM_ML_MODEL_OUTPUT_START_LOGITS_NAME: `output_start_logits`

        </details>


      * Group "**packing**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_packed`
               - ENV variables:
                   - CM_ML_MODEL_BERT_PACKED: `yes`
        * **`_unpacked`** (default)
               - ENV variables:
                   - CM_ML_MODEL_BERT_PACKED: `no`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_fp32`** (default)
               - ENV variables:
                   - CM_ML_MODEL_PRECISION: `fp32`
        * `_int8`
               - ENV variables:
                   - CM_ML_MODEL_PRECISION: `int8`
                   - CM_ML_MODEL_QUANTIZED: `yes`

        </details>


    ##### Default variations

    `_fp32,_onnx,_unpacked`

#### Native script being run
=== "Linux/macOS"
     * [run-packed.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-bert-large-squad/run-packed.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get ml-model raw bert bert-large bert-squad language language-processing [variations]"  -j
```