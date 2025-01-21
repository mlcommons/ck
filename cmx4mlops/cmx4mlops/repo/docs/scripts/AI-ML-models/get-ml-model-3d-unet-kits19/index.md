# get-ml-model-3d-unet-kits19
Automatically generated README for this automation recipe: **get-ml-model-3d-unet-kits19**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-3d-unet-kits19/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model raw 3d-unet kits19 medical-imaging" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,ml-model,raw,3d-unet,kits19,medical-imaging[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get ml-model raw 3d-unet kits19 medical-imaging [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,raw,3d-unet,kits19,medical-imaging'
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
    cm docker script "get ml-model raw 3d-unet kits19 medical-imaging[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_weights`
               - ENV variables:
                   - CM_MODEL_WEIGHTS_FILE: `yes`

        </details>


      * Group "**framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_onnx`** (default)
               - ENV variables:
                   - CM_ML_MODEL_FRAMEWORK: `onnx`
        * `_pytorch`
               - ENV variables:
                   - CM_ML_MODEL_FRAMEWORK: `pytorch`
        * `_tf`
              - Aliases: `_tensorflow`
               - ENV variables:
                   - CM_ML_MODEL_FRAMEWORK: `tensorflow`

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

___
#### Script output
```bash
cmr "get ml-model raw 3d-unet kits19 medical-imaging [variations]"  -j
```