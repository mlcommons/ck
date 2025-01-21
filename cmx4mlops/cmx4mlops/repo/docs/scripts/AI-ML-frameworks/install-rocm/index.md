# install-rocm
Automatically generated README for this automation recipe: **install-rocm**

Category: **[AI/ML frameworks](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-rocm/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install rocm install-rocm" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=install,rocm,install-rocm 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "install rocm install-rocm " 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,rocm,install-rocm'
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
    cm docker script "install rocm install-rocm" 
    ```
___

#### Versions
Default version: `5.7.1`


#### Native script being run
=== "Linux/macOS"
     * [run-rhel.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-rocm/run-rhel.sh)
     * [run-ubuntu.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-rocm/run-ubuntu.sh)
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-rocm/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "install rocm install-rocm "  -j
```