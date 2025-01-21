# get-ml-model-rnnt
Automatically generated README for this automation recipe: **get-ml-model-rnnt**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-rnnt/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model rnnt raw librispeech speech-recognition" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,ml-model,rnnt,raw,librispeech,speech-recognition[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get ml-model rnnt raw librispeech speech-recognition [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,rnnt,raw,librispeech,speech-recognition'
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
    cm docker script "get ml-model rnnt raw librispeech speech-recognition[variations]" 
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


      * Group "**download-src**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_amazon-s3`
        * **`_zenodo`** (default)

        </details>


      * Group "**framework**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_pytorch`** (default)
               - ENV variables:
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

    `_fp32,_pytorch,_zenodo`

___
#### Script output
```bash
cmr "get ml-model rnnt raw librispeech speech-recognition [variations]"  -j
```