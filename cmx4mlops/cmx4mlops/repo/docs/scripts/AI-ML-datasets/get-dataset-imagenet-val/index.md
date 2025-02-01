# get-dataset-imagenet-val
Automatically generated README for this automation recipe: **get-dataset-imagenet-val**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-imagenet-val/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-imagenet-val/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get val validation dataset imagenet ILSVRC image-classification original" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,val,validation,dataset,imagenet,ILSVRC,image-classification,original[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get val validation dataset imagenet ILSVRC image-classification original [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,val,validation,dataset,imagenet,ILSVRC,image-classification,original'
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
    cm docker script "get val validation dataset imagenet ILSVRC image-classification original[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_2012-500`
        * `_2012-full`
        * `_run-during-docker-build`

        </details>


      * Group "**count**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_full`
               - ENV variables:
                   - CM_DATASET_SIZE: `50000`
                   - CM_IMAGENET_FULL: `yes`
                   - CM_DAE_FILENAME: `ILSVRC2012_img_val.tar`
                   - CM_DAE_DOWNLOADED_CHECKSUM: `29b22e2961454d5413ddabcf34fc5622`
        * `_size.#`
               - ENV variables:
                   - CM_DATASET_SIZE: `#`
        * **`_size.500`** (default)
               - ENV variables:
                   - CM_DATASET_SIZE: `500`
                   - CM_DAE_FILENAME: `ILSVRC2012_img_val_500.tar`
                   - CM_DAE_URL: `http://cKnowledge.org/ai/data/ILSVRC2012_img_val_500.tar`

        </details>


      * Group "**dataset-version**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_2012`** (default)
               - ENV variables:
                   - CM_DATASET_VER: `2012`

        </details>


    ##### Default variations

    `_2012,_size.500`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--imagenet_path=value`  &rarr;  `IMAGENET_PATH=value`
    * `--torrent=value`  &rarr;  `CM_DATASET_IMAGENET_VAL_TORRENT_PATH=value`




#### Native script being run
=== "Linux/macOS"
    No run file exists for Linux/macOS
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-imagenet-val/run.bat)
___
#### Script output
```bash
cmr "get val validation dataset imagenet ILSVRC image-classification original [variations]" [--input_flags] -j
```