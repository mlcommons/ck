# get-ml-model-retinanet
Automatically generated README for this automation recipe: **get-ml-model-retinanet**

Category: **[AI/ML models](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-retinanet/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-retinanet/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model raw resnext50 retinanet object-detection" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,ml-model,raw,resnext50,retinanet,object-detection[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get ml-model raw resnext50 retinanet object-detection [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,raw,resnext50,retinanet,object-detection'
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
    cm docker script "get ml-model raw resnext50 retinanet object-detection[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_no-nms`
               - ENV variables:
                   - CM_TMP_ML_MODEL_RETINANET_NO_NMS: `yes`
                   - CM_ML_MODEL_RETINANET_NO_NMS: `yes`
                   - CM_QAIC_PRINT_NODE_PRECISION_INFO: `yes`
        * `_weights`
               - ENV variables:
                   - CM_MODEL_WEIGHTS_FILE: `yes`

        </details>


      * Group "**framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_onnx`** (default)
               - ENV variables:
                   - CM_ML_MODEL_DATA_LAYOUT: `NCHW`
                   - CM_ML_MODEL_FRAMEWORK: `onnx`
        * `_pytorch`
               - ENV variables:
                   - CM_ML_MODEL_DATA_LAYOUT: `NCHW`
                   - CM_ML_MODEL_FRAMEWORK: `pytorch`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_fp32`** (default)
               - ENV variables:
                   - CM_ML_MODEL_INPUT_DATA_TYPES: `fp32`
                   - CM_ML_MODEL_PRECISION: `fp32`
                   - CM_ML_MODEL_WEIGHT_DATA_TYPES: `fp32`

        </details>


    ##### Default variations

    `_fp32,_onnx`

#### Native script being run
=== "Linux/macOS"
     * [run-no-nms.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-retinanet/run-no-nms.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get ml-model raw resnext50 retinanet object-detection [variations]"  -j
```