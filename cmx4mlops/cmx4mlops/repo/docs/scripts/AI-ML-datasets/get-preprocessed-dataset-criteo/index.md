# get-preprocessed-dataset-criteo
Automatically generated README for this automation recipe: **get-preprocessed-dataset-criteo**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-criteo/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-criteo/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dataset criteo recommendation dlrm preprocessed" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,dataset,criteo,recommendation,dlrm,preprocessed[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get dataset criteo recommendation dlrm preprocessed [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,criteo,recommendation,dlrm,preprocessed'
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
    cm docker script "get dataset criteo recommendation dlrm preprocessed[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_1`
               - ENV variables:
                   - CM_DATASET_SIZE: `1`
        * `_50`
               - ENV variables:
                   - CM_DATASET_SIZE: `50`
        * `_fake`
               - ENV variables:
                   - CM_CRITEO_FAKE: `yes`
        * `_full`
        * `_validation`

        </details>


      * Group "**type**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_multihot`** (default)
               - ENV variables:
                   - CM_DATASET_CRITEO_MULTIHOT: `yes`

        </details>


    ##### Default variations

    `_multihot`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--dir=value`  &rarr;  `CM_DATASET_PREPROCESSED_PATH=value`
    * `--output_dir=value`  &rarr;  `CM_DATASET_PREPROCESSED_OUTPUT_PATH=value`
    * `--threads=value`  &rarr;  `CM_NUM_PREPROCESS_THREADS=value`




#### Native script being run
=== "Linux/macOS"
     * [run-multihot.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-criteo/run-multihot.sh)
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-criteo/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get dataset criteo recommendation dlrm preprocessed [variations]" [--input_flags] -j
```