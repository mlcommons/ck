# test-cm-script-pipeline
Automatically generated README for this automation recipe: **test-cm-script-pipeline**

Category: **[Tests](..)**

License: **Apache 2.0**

Developers: Grigori Fursin
* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/test-cm-script-pipeline/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/test-cm-script-pipeline/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "test cm-script pipeline" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=test,cm-script,pipeline 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "test cm-script pipeline " 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'test,cm-script,pipeline'
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
    cm docker script "test cm-script pipeline" 
    ```
___


#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/test-cm-script-pipeline/run.sh)
     * [run2.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/test-cm-script-pipeline/run2.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/test-cm-script-pipeline/run.bat)
     * [run2.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/test-cm-script-pipeline/run2.bat)
___
#### Script output
```bash
cmr "test cm-script pipeline "  -j
```