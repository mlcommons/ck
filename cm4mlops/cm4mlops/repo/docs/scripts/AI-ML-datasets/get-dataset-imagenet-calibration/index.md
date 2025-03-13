# get-dataset-imagenet-calibration
Automatically generated README for this automation recipe: **get-dataset-imagenet-calibration**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-imagenet-calibration/_cm.yaml)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dataset imagenet calibration" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,dataset,imagenet,calibration[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get dataset imagenet calibration [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,imagenet,calibration'
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
    cm docker script "get dataset imagenet calibration[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * Group "**calibration-option**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_mlperf.option1`** (default)
               - ENV variables:
                   - CM_MLPERF_IMAGENET_CALIBRATION_OPTION: `one`
                   - CM_DOWNLOAD_CHECKSUM: `f09719174af3553119e2c621157773a6`
        * `_mlperf.option2`
               - ENV variables:
                   - CM_MLPERF_IMAGENET_CALIBRATION_OPTION: `two`
                   - CM_DOWNLOAD_CHECKSUM: `e44582af00e3b4fc3fac30efd6bdd05f`

        </details>


    ##### Default variations

    `_mlperf.option1`

___
#### Script output
```bash
cmr "get dataset imagenet calibration [variations]"  -j
```