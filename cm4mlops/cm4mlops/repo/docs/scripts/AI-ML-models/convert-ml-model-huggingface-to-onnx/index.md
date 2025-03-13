# convert-ml-model-huggingface-to-onnx
Automatically generated README for this automation recipe: **convert-ml-model-huggingface-to-onnx**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/convert-ml-model-huggingface-to-onnx/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "ml-model model huggingface-to-onnx onnx huggingface convert" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=ml-model,model,huggingface-to-onnx,onnx,huggingface,convert[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "ml-model model huggingface-to-onnx onnx huggingface convert [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'ml-model,model,huggingface-to-onnx,onnx,huggingface,convert'
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
    cm docker script "ml-model model huggingface-to-onnx onnx huggingface convert[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_model-path.#`
               - ENV variables:
                   - CM_MODEL_HUGG_PATH: `#`

        </details>


#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/convert-ml-model-huggingface-to-onnx/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "ml-model model huggingface-to-onnx onnx huggingface convert [variations]"  -j
```