# print-python-version
Automatically generated README for this automation recipe: **print-python-version**

Category: **[Tests](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/print-python-version/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "print python version python-version" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=print,python,version,python-version 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "print python version python-version " 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'print,python,version,python-version'
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
    cm docker script "print python version python-version" 
    ```
___


#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/print-python-version/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/print-python-version/run.bat)
___
#### Script output
```bash
cmr "print python version python-version "  -j
```