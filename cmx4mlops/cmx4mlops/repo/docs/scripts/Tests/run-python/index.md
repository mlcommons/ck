# run-python
Automatically generated README for this automation recipe: **run-python**

Category: **[Tests](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/run-python/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "run python" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=run,python [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "run python " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,python'
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
    cm docker script "run python" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--command=value`  &rarr;  `CM_RUN_PYTHON_CMD=value`




#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/run-python/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/run-python/run.bat)
___
#### Script output
```bash
cmr "run python " [--input_flags] -j
```