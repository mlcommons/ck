# get-zephyr
Automatically generated README for this automation recipe: **get-zephyr**

Category: **[TinyML automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-zephyr/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-zephyr/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get zephyr" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,zephyr 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get zephyr " 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,zephyr'
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
    cm docker script "get zephyr" 
    ```
___

#### Versions
Default version: `v2.7`

* `v2.7`

#### Native script being run
=== "Linux/macOS"
     * [run-ubuntu.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-zephyr/run-ubuntu.sh)
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-zephyr/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get zephyr "  -j
```