# process-mlperf-accuracy
Automatically generated README for this automation recipe: **process-mlperf-accuracy**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/process-mlperf-accuracy/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "run mlperf mlcommons accuracy mlc process process-accuracy" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=run,mlperf,mlcommons,accuracy,mlc,process,process-accuracy[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "run mlperf mlcommons accuracy mlc process process-accuracy [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,mlperf,mlcommons,accuracy,mlc,process,process-accuracy'
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
    cm docker script "run mlperf mlcommons accuracy mlc process process-accuracy[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * Group "**coco-evaluation-tool**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_default-pycocotools`** (default)
        * `_nvidia-pycocotools`

        </details>


      * Group "**dataset**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_cnndm`
               - ENV variables:
                   - CM_DATASET: `cnndm`
        * `_coco2014`
               - ENV variables:
                   - CM_DATASET: `coco2014`
        * **`_imagenet`** (default)
               - ENV variables:
                   - CM_DATASET: `imagenet`
        * `_kits19`
               - ENV variables:
                   - CM_DATASET: `kits19`
        * `_librispeech`
               - ENV variables:
                   - CM_DATASET: `librispeech`
        * `_open-orca`
               - ENV variables:
                   - CM_DATASET: `openorca`
        * `_openimages`
               - ENV variables:
                   - CM_DATASET: `openimages`
        * `_squad`
               - ENV variables:
                   - CM_DATASET: `squad`
        * `_terabyte`
               - ENV variables:
                   - CM_DATASET: `squad`

        </details>


      * Group "**precision**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_float16`
               - ENV variables:
                   - CM_ACCURACY_DTYPE: `float16`
        * **`_float32`** (default)
               - ENV variables:
                   - CM_ACCURACY_DTYPE: `float32`
        * `_float64`
               - ENV variables:
                   - CM_ACCURACY_DTYPE: `float64`
        * `_int16`
               - ENV variables:
                   - CM_ACCURACY_DTYPE: `int16`
        * `_int32`
               - ENV variables:
                   - CM_ACCURACY_DTYPE: `int32`
        * `_int64`
               - ENV variables:
                   - CM_ACCURACY_DTYPE: `int64`
        * `_int8`
               - ENV variables:
                   - CM_ACCURACY_DTYPE: `int8`

        </details>


    ##### Default variations

    `_default-pycocotools,_float32,_imagenet`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--result_dir=value`  &rarr;  `CM_MLPERF_ACCURACY_RESULTS_DIR=value`




#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/process-mlperf-accuracy/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/process-mlperf-accuracy/run.bat)
___
#### Script output
```bash
cmr "run mlperf mlcommons accuracy mlc process process-accuracy [variations]" [--input_flags] -j
```