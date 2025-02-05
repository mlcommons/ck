# get-dataset-coco2014
Automatically generated README for this automation recipe: **get-dataset-coco2014**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-coco2014/_cm.yaml)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dataset coco2014 object-detection original" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,dataset,coco2014,object-detection,original[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get dataset coco2014 object-detection original [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,coco2014,object-detection,original'
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
    cm docker script "get dataset coco2014 object-detection original[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * Group "**annotations**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_custom-annotations`
               - ENV variables:
                   - CM_DATASET_COCO2014_CUSTOM_ANNOTATIONS: `yes`
        * **`_default-annotations`** (default)
               - ENV variables:
                   - CM_DATASET_COCO2014_CUSTOM_ANNOTATIONS: `no`

        </details>


      * Group "**dataset-type**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_calibration`
               - ENV variables:
                   - CM_DATASET_CALIBRATION: `yes`
        * **`_validation`** (default)
               - ENV variables:
                   - CM_DATASET_CALIBRATION: `no`

        </details>


      * Group "**size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_50`** (default)
               - ENV variables:
                   - CM_DATASET_SIZE: `50`
        * `_500`
               - ENV variables:
                   - CM_DATASET_SIZE: `500`
        * `_full`
               - ENV variables:
                   - CM_DATASET_SIZE: ``
        * `_size.#`
               - ENV variables:
                   - CM_DATASET_SIZE: `#`

        </details>


    ##### Default variations

    `_50,_default-annotations,_validation`
=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_DATASET_CALIBRATION: `no`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-coco2014/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-coco2014/run.bat)
___
#### Script output
```bash
cmr "get dataset coco2014 object-detection original [variations]"  -j
```