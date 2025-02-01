# get-ml-model-using-imagenet-from-model-zoo
Automatically generated README for this automation recipe: **get-ml-model-using-imagenet-from-model-zoo**

Category: **[AI/ML models](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-ml-model-using-imagenet-from-model-zoo/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get ml-model model-zoo zoo imagenet image-classification" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,ml-model,model-zoo,zoo,imagenet,image-classification[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get ml-model model-zoo zoo imagenet image-classification [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,ml-model,model-zoo,zoo,imagenet,image-classification'
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
    cm docker script "get ml-model model-zoo zoo imagenet image-classification[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * Group "**model-source**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_model.#`
        * `_model.resnet101-pytorch-base`
        * `_model.resnet50-pruned95-uniform-quant`

        </details>


___
#### Script output
```bash
cmr "get ml-model model-zoo zoo imagenet image-classification [variations]"  -j
```