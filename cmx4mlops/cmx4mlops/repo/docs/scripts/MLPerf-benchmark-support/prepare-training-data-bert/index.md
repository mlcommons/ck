# prepare-training-data-bert
Automatically generated README for this automation recipe: **prepare-training-data-bert**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/prepare-training-data-bert/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "prepare mlperf training data input bert" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=prepare,mlperf,training,data,input,bert[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "prepare mlperf training data input bert [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'prepare,mlperf,training,data,input,bert'
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
    cm docker script "prepare mlperf training data input bert[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * Group "**implementation**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_nvidia`** (default)
               - ENV variables:
                   - CM_TMP_VARIATION: `nvidia`
        * `_reference`
               - ENV variables:
                   - CM_TMP_VARIATION: `reference`

        </details>


    ##### Default variations

    `_nvidia`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--clean=value`  &rarr;  `CM_MLPERF_TRAINING_CLEAN_TFRECORDS=value`
    * `--data_dir=value`  &rarr;  `CM_DATA_DIR=value`




#### Native script being run
=== "Linux/macOS"
     * [run-nvidia.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/prepare-training-data-bert/run-nvidia.sh)
     * [run-reference.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/prepare-training-data-bert/run-reference.sh)
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/prepare-training-data-bert/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "prepare mlperf training data input bert [variations]" [--input_flags] -j
```