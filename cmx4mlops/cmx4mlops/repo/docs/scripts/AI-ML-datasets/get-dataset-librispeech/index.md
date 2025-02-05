# get-dataset-librispeech
Automatically generated README for this automation recipe: **get-dataset-librispeech**

Category: **[AI/ML datasets](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-librispeech/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-librispeech/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get dataset speech speech-recognition librispeech validation audio training original" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,dataset,speech,speech-recognition,librispeech,validation,audio,training,original 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get dataset speech speech-recognition librispeech validation audio training original " 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,dataset,speech,speech-recognition,librispeech,validation,audio,training,original'
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
    cm docker script "get dataset speech speech-recognition librispeech validation audio training original" 
    ```
___

#### Versions
Default version: `dev-clean`

* `dev-clean`
* `dev-other`
* `test-clean`
* `test-other`
* `train-clean-100`
* `train-clean-360`
* `train-other-500`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-dataset-librispeech/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get dataset speech speech-recognition librispeech validation audio training original "  -j
```