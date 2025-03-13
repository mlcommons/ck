# app-image-classification-tf-onnx-cpp
Automatically generated README for this automation recipe: **app-image-classification-tf-onnx-cpp**

Category: **[Modular AI/ML application pipeline](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/app-image-classification-tf-onnx-cpp/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/app-image-classification-tf-onnx-cpp/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "app image-classification cpp tensorflow onnx" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=app,image-classification,cpp,tensorflow,onnx 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "app image-classification cpp tensorflow onnx " 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,image-classification,cpp,tensorflow,onnx'
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
    cm docker script "app image-classification cpp tensorflow onnx" 
    ```
___

=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_BATCH_COUNT: `1`
    * CM_BATCH_SIZE: `1`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/app-image-classification-tf-onnx-cpp/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "app image-classification cpp tensorflow onnx "  -j
```