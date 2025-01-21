# get-dataset-cifar10
Automatically generated README for this automation recipe: **get-dataset-cifar10**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-cifar10/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dataset cifar10 image-classification validation training" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,dataset,cifar10,image-classification,validation,training[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get dataset cifar10 image-classification validation training [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,cifar10,image-classification,validation,training'
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
    cm docker script "get dataset cifar10 image-classification validation training[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_tiny`
               - ENV variables:
                   - CM_DATASET_CONVERT_TO_TINYMLPERF: `yes`

        </details>


      * Group "**data_format**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_python`** (default)
               - ENV variables:
                   - CM_DATASET: `CIFAR10`
                   - CM_DATASET_FILENAME: `cifar-10-python.tar.gz`
                   - CM_DATASET_FILENAME1: `cifar-10-python.tar`
                   - CM_DATASET_CIFAR10: `https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz`

        </details>


    ##### Default variations

    `_python`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-cifar10/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-cifar10/run.bat)
___
#### Script output
```bash
cmr "get dataset cifar10 image-classification validation training [variations]"  -j
```