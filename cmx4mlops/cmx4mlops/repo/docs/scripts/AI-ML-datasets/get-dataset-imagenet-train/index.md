# get-dataset-imagenet-train
Automatically generated README for this automation recipe: **get-dataset-imagenet-train**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-imagenet-train/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get imagenet train dataset original" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,imagenet,train,dataset,original [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get imagenet train dataset original " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,imagenet,train,dataset,original'
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
    cm docker script "get imagenet train dataset original" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--input=value`  &rarr;  `IMAGENET_TRAIN_PATH=value`
    * `--torrent=value`  &rarr;  `CM_DATASET_IMAGENET_TRAIN_TORRENT_PATH=value`




#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-imagenet-train/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get imagenet train dataset original " [--input_flags] -j
```