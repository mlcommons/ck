# compile-model-for.qaic
Automatically generated README for this automation recipe: **compile-model-for.qaic**

Category: **[AI/ML optimization](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/compile-model-for.qaic/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "qaic compile model model-compile qaic-compile" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=qaic,compile,model,model-compile,qaic-compile[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "qaic compile model model-compile qaic-compile [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'qaic,compile,model,model-compile,qaic-compile'
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
    cm docker script "qaic compile model model-compile qaic-compile[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_bert-99`
               - ENV variables:
                   - CM_COMPILE_BERT: `on`
                   - CM_QAIC_MODEL_TO_CONVERT: `calibrate_bert_mlperf`
                   - CM_QAIC_MODEL_COMPILER_PARAMS_BASE: `-aic-hw -aic-hw-version=2.0 -execute-nodes-in-fp16=Add,Div,Erf,Softmax -quantization-schema=symmetric_with_uint8 -quantization-precision=Int8 -quantization-precision-bias=Int32 -vvv -compile-only -onnx-define-symbol=batch_size,1 -onnx-define-symbol=seg_length,384 -multicast-weights -combine-inputs=false -combine-outputs=false`
                   - CM_QAIC_MODEL_COMPILER_ARGS: ``
        * `_bert-99.9`
               - ENV variables:
                   - CM_COMPILE_BERT: `on`
                   - CM_QAIC_MODEL_TO_CONVERT: `bert_mlperf`
                   - CM_QAIC_MODEL_COMPILER_PARAMS_BASE: `-aic-hw -aic-hw-version=2.0 -convert-to-fp16 -vvv -compile-only -onnx-define-symbol=batch_size,1 -onnx-define-symbol=seg_length,384 -combine-inputs=false -combine-outputs=false`
                   - CM_QAIC_MODEL_COMPILER_ARGS: ``
        * `_resnet50`
               - ENV variables:
                   - CM_COMPILE_RESNET: `on`
                   - CM_QAIC_MODEL_TO_CONVERT: `compile_resnet50_tf`
                   - CM_QAIC_MODEL_COMPILER_PARAMS_BASE: `-aic-hw -aic-hw-version=2.0 -quantization-schema=symmetric_with_uint8 -quantization-precision=Int8 -output-node-name=ArgMax -vvv -compile-only -use-producer-dma=1`
        * `_retinanet`
               - ENV variables:
                   - CM_COMPILE_RETINANET: `on`
                   - CM_QAIC_MODEL_TO_CONVERT: `calibrate_retinanet_no_nms_mlperf`
                   - CM_QAIC_MODEL_COMPILER_ARGS: `-aic-enable-depth-first`
                   - CM_QAIC_MODEL_COMPILER_PARAMS_BASE: `-aic-hw -aic-hw-version=2.0 -compile-only -enable-channelwise -onnx-define-symbol=batch_size,1 -node-precision-info=<<<CM_ML_MODEL_RETINANET_QAIC_NODE_PRECISION_INFO_FILE_PATH>>> -quantization-schema-constants=symmetric_with_uint8 -quantization-schema-activations=asymmetric -quantization-calibration=None`

        </details>


      * Group "**batch-size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_bs.#`
               - ENV variables:
                   - CM_QAIC_MODEL_BATCH_SIZE: `#`
        * `_bs.1`
               - ENV variables:
                   - CM_QAIC_MODEL_BATCH_SIZE: `1`

        </details>


      * Group "**calib-dataset-filter-size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_filter-size.#`

        </details>


      * Group "**mlperf-scenario**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_multistream`
        * `_offline`
        * `_server`
        * **`_singlestream`** (default)

        </details>


      * Group "**model-framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_tf`

        </details>


      * Group "**nsp**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_nsp.14`
        * `_nsp.16`
        * `_nsp.8`
        * `_nsp.9`

        </details>


      * Group "**percentile-calibration**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_pc.#`
               - ENV variables:
                   - CM_QAIC_MODEL_COMPILER_PERCENTILE_CALIBRATION_VALUE: `#`
                   - CM_QAIC_MODEL_COMPILER_QUANTIZATION_PARAMS: `-quantization-calibration=Percentile  -percentile-calibration-value=<<<CM_QAIC_MODEL_COMPILER_PERCENTILE_CALIBRATION_VALUE>>>`

        </details>


      * Group "**quantization**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_no-quantized`
               - ENV variables:
                   - CM_QAIC_MODEL_QUANTIZATION: `no`
        * **`_quantized`** (default)
               - ENV variables:
                   - CM_QAIC_MODEL_QUANTIZATION: `yes`

        </details>


    ##### Default variations

    `_quantized,_singlestream`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--register=value`  &rarr;  `CM_REGISTER_CACHE=value`




#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/compile-model-for.qaic/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "qaic compile model model-compile qaic-compile [variations]" [--input_flags] -j
```