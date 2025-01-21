# get-dataset-imagenet-aux
Automatically generated README for this automation recipe: **get-dataset-imagenet-aux**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-imagenet-aux/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get aux dataset-aux image-classification imagenet-aux" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,aux,dataset-aux,image-classification,imagenet-aux[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get aux dataset-aux image-classification imagenet-aux [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,aux,dataset-aux,image-classification,imagenet-aux'
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
    cm docker script "get aux dataset-aux image-classification imagenet-aux[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_2012`
               - ENV variables:
                   - CM_DATASET_AUX_VER: `2012`

        </details>


      * Group "**download-source**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_from.berkeleyvision`
               - ENV variables:
                   - CM_WGET_URL: `http://dl.caffe.berkeleyvision.org/caffe_ilsvrc12.tar.gz`
        * **`_from.dropbox`** (default)
               - ENV variables:
                   - CM_WGET_URL: `https://www.dropbox.com/s/92n2fyej3lzy3s3/caffe_ilsvrc12.tar.gz`

        </details>


    ##### Default variations

    `_from.dropbox`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-imagenet-aux/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-imagenet-aux/run.bat)
___
#### Script output
```bash
cmr "get aux dataset-aux image-classification imagenet-aux [variations]"  -j
```