# get-dataset-coco
Automatically generated README for this automation recipe: **get-dataset-coco**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-coco/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-coco/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dataset object-detection coco" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,dataset,object-detection,coco[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get dataset object-detection coco [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,object-detection,coco'
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
    cm docker script "get dataset object-detection coco[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * Group "**size**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_complete`** (default)
               - ENV variables:
                   - CM_DATASET_COCO_SIZE: `complete`
        * `_small`
               - ENV variables:
                   - CM_DATASET_COCO_SIZE: `small`

        </details>


      * Group "**type**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_train`
               - ENV variables:
                   - CM_DATASET_COCO_TYPE: `train`
        * **`_val`** (default)
               - ENV variables:
                   - CM_DATASET_COCO_TYPE: `val`

        </details>


      * Group "**version**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_2017`** (default)
               - ENV variables:
                   - CM_DATASET_COCO_VERSION: `2017`

        </details>


    ##### Default variations

    `_2017,_complete,_val`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--from=value`  &rarr;  `CM_FROM=value`
    * `--home=value`  &rarr;  `CM_HOME_DIR=value`
    * `--store=value`  &rarr;  `CM_STORE=value`
    * `--to=value`  &rarr;  `CM_TO=value`




___
#### Script output
```bash
cmr "get dataset object-detection coco [variations]" [--input_flags] -j
```