# get-tensorrt
Automatically generated README for this automation recipe: **get-tensorrt**

Category: **[CUDA automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-tensorrt/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-tensorrt/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get tensorrt nvidia" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,tensorrt,nvidia[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get tensorrt nvidia [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,tensorrt,nvidia'
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
    cm docker script "get tensorrt nvidia[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_dev`
               - ENV variables:
                   - CM_TENSORRT_REQUIRE_DEV: `yes`

        </details>

=== "Input Flags"


    #### Input Flags

    * --**input:** Full path to the installed TensorRT library (nvinfer)
    * --**tar_file:** Full path to the TensorRT Tar file downloaded from the Nvidia website (https://developer.nvidia.com/tensorrt)
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--input=value`  &rarr;  `CM_INPUT=value`
    * `--tar_file=value`  &rarr;  `CM_TENSORRT_TAR_FILE_PATH=value`




#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-tensorrt/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get tensorrt nvidia [variations]" [--input_flags] -j
```