# get-preprocessed-dataset-kits19
Automatically generated README for this automation recipe: **get-preprocessed-dataset-kits19**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-kits19/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dataset medical-imaging kits19 preprocessed" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,dataset,medical-imaging,kits19,preprocessed[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get dataset medical-imaging kits19 preprocessed [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,medical-imaging,kits19,preprocessed'
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
    cm docker script "get dataset medical-imaging kits19 preprocessed[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_nvidia`
               - ENV variables:
                   - CM_PREPROCESSING_BY_NVIDIA: `yes`

        </details>


      * Group "**dataset-count**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_1`
               - ENV variables:
                   - CM_DATASET_SIZE: `1`
        * `_5`
               - ENV variables:
                   - CM_DATASET_SIZE: `5`
        * `_50`
               - ENV variables:
                   - CM_DATASET_SIZE: `50`
        * `_500`
               - ENV variables:
                   - CM_DATASET_SIZE: `500`
        * `_full`
               - ENV variables:
                   - CM_DATASET_SIZE: ``

        </details>


      * Group "**dataset-precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_fp32`** (default)
               - ENV variables:
                   - CM_DATASET_DTYPE: `fp32`
        * `_int8`
               - ENV variables:
                   - CM_DATASET_DTYPE: `int8`

        </details>


      * Group "**dataset-type**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_calibration`
               - ENV variables:
                   - CM_DATASET_PATH: `<<<CM_CALIBRATION_DATASET_PATH>>>`
        * **`_validation`** (default)

        </details>


    ##### Default variations

    `_fp32,_validation`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--dir=value`  &rarr;  `CM_DATASET_PREPROCESSED_PATH=value`
    * `--threads=value`  &rarr;  `CM_NUM_PREPROCESS_THREADS=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_DATASET: `kits19`
    * CM_DATASET_DTYPE: `fp32`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-kits19/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get dataset medical-imaging kits19 preprocessed [variations]" [--input_flags] -j
```