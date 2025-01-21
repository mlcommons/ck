# install-bazel
Automatically generated README for this automation recipe: **install-bazel**

Category: **[Detection or installation of tools and artifacts](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-bazel/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install script bazel" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=install,script,bazel 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "install script bazel " 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,script,bazel'
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
    cm docker script "install script bazel" 
    ```
___

#### Versions
Default version: `7.0.2`


#### Native script being run
=== "Linux/macOS"
     * [run-aarch64.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-bazel/run-aarch64.sh)
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-bazel/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/install-bazel/run.bat)
___
#### Script output
```bash
cmr "install script bazel "  -j
```