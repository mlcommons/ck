# calibrate-model-for.qaic
Automatically generated README for this automation recipe: **calibrate-model-for.qaic**

Category: **[AI/ML optimization](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/calibrate-model-for.qaic/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "qaic calibrate profile qaic-profile qaic-calibrate" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=qaic,calibrate,profile,qaic-profile,qaic-calibrate[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "qaic calibrate profile qaic-profile qaic-calibrate [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


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


=== "Docker"
    ##### Run this script via Docker (beta)

    ```bash
    cm docker script "qaic calibrate profile qaic-profile qaic-calibrate[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_first.#`

        </details>


      * Group "**batch-size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_bs.#`
               - ENV variables:
                   - CM_QAIC_MODEL_BATCH_SIZE: `#`
                   - CM_CREATE_INPUT_BATCH: `yes`
        * `_bs.1`
               - ENV variables:
                   - CM_QAIC_MODEL_BATCH_SIZE: `1`
                   - CM_CREATE_INPUT_BATCH: `yes`

        </details>


      * Group "**calib-dataset-filter-size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_filter-size.#`

        </details>


      * Group "**calibration-option**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_mlperf.option1`
        * `_mlperf.option2`

        </details>


      * Group "**model**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_bert-99`
               - ENV variables:
                   - CM_CALIBRATE_SQUAD: `yes`
                   - CM_QAIC_COMPILER_ARGS: ``
                   - CM_QAIC_COMPILER_PARAMS: `-onnx-define-symbol=batch_size,1 -onnx-define-symbol=seg_length,<<<CM_DATASET_SQUAD_TOKENIZED_MAX_SEQ_LENGTH>>> -input-list-file=<<<CM_DATASET_SQUAD_TOKENIZED_PACKED_FILENAMES_FILE>>> -num-histogram-bins=512 -profiling-threads=<<<CM_HOST_CPU_PHYSICAL_CORES_PER_SOCKET>>>`
                   - CM_QAIC_MODEL_TO_CONVERT: `calibrate_bert_mlperf`
        * `_resnet50`
               - ENV variables:
                   - CM_QAIC_MODEL_NAME: `resnet50`
                   - CM_CALIBRATE_IMAGENET: `yes`
                   - CM_QAIC_COMPILER_ARGS: ``
                   - CM_QAIC_COMPILER_PARAMS: `-output-node-name=ArgMax -profiling-threads=<<<CM_HOST_CPU_PHYSICAL_CORES_PER_SOCKET>>>`
                   - CM_QAIC_OUTPUT_NODE_NAME: `-output-node-name=ArgMax`
                   - CM_QAIC_MODEL_TO_CONVERT: `calibrate_resnet50_tf`
        * `_retinanet`
               - ENV variables:
                   - CM_QAIC_MODEL_NAME: `retinanet`
                   - CM_CALIBRATE_OPENIMAGES: `yes`
                   - CM_QAIC_COMPILER_ARGS: ``
                   - CM_QAIC_COMPILER_PARAMS: `-enable-channelwise -profiling-threads=<<<CM_HOST_CPU_PHYSICAL_CORES_PER_SOCKET>>> -onnx-define-symbol=batch_size,<<<CM_QAIC_MODEL_BATCH_SIZE>>> -node-precision-info=<<<CM_ML_MODEL_RETINANET_QAIC_NODE_PRECISION_INFO_FILE_PATH>>>`
                   - CM_QAIC_MODEL_TO_CONVERT: `calibrate_retinanet_no_nms_mlperf`

        </details>


      * Group "**model-framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_tf`

        </details>


      * Group "**seq-length**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_seq.#`
               - ENV variables:
                   - CM_DATASET_SQUAD_TOKENIZED_MAX_SEQ_LENGTH: `#`
        * `_seq.384`
               - ENV variables:
                   - CM_DATASET_SQUAD_TOKENIZED_MAX_SEQ_LENGTH: `#`

        </details>


#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/calibrate-model-for.qaic/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "qaic calibrate profile qaic-profile qaic-calibrate [variations]"  -j
```