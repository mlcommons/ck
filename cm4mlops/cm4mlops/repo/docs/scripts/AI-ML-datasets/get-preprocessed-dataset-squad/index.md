# get-preprocessed-dataset-squad
Automatically generated README for this automation recipe: **get-preprocessed-dataset-squad**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-squad/_cm.yaml)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dataset preprocessed tokenized squad" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,dataset,preprocessed,tokenized,squad[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get dataset preprocessed tokenized squad [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,preprocessed,tokenized,squad'
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
    cm docker script "get dataset preprocessed tokenized squad[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * Group "**calibration-set**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_calib1`
               - ENV variables:
                   - CM_DATASET_SQUAD_CALIBRATION_SET: `one`
        * `_calib2`
               - ENV variables:
                   - CM_DATASET_SQUAD_CALIBRATION_SET: `two`
        * **`_no-calib`** (default)
               - ENV variables:
                   - CM_DATASET_SQUAD_CALIBRATION_SET: ``

        </details>


      * Group "**doc-stride**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_doc-stride.#`
               - ENV variables:
                   - CM_DATASET_DOC_STRIDE: `#`
        * **`_doc-stride.128`** (default)
               - ENV variables:
                   - CM_DATASET_DOC_STRIDE: `128`

        </details>


      * Group "**packing**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_packed`
               - ENV variables:
                   - CM_DATASET_SQUAD_PACKED: `yes`

        </details>


      * Group "**raw**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_pickle`
               - ENV variables:
                   - CM_DATASET_RAW: `no`
        * **`_raw`** (default)
               - ENV variables:
                   - CM_DATASET_RAW: `yes`

        </details>


      * Group "**seq-length**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_seq-length.#`
               - ENV variables:
                   - CM_DATASET_MAX_SEQ_LENGTH: `#`
        * **`_seq-length.384`** (default)
               - ENV variables:
                   - CM_DATASET_MAX_SEQ_LENGTH: `384`

        </details>


    ##### Default variations

    `_doc-stride.128,_no-calib,_raw,_seq-length.384`

#### Native script being run
=== "Linux/macOS"
     * [run-packed.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-squad/run-packed.sh)
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-preprocessed-dataset-squad/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get dataset preprocessed tokenized squad [variations]"  -j
```