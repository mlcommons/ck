# Install prebuilt LLVM compiler
Automatically generated README for this automation recipe: **install-llvm-prebuilt**

Category: **[Compiler automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/install-llvm-prebuilt/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-llvm-prebuilt/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install prebuilt llvm prebuilt-llvm install-prebuilt-llvm" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=install,prebuilt,llvm,prebuilt-llvm,install-prebuilt-llvm 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "install prebuilt llvm prebuilt-llvm install-prebuilt-llvm " 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,prebuilt,llvm,prebuilt-llvm,install-prebuilt-llvm'
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
    cm docker script "install prebuilt llvm prebuilt-llvm install-prebuilt-llvm" 
    ```
___

#### Versions
Default version: `15.0.6`


#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-llvm-prebuilt/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/install-llvm-prebuilt/run.bat)
___
#### Script output
```bash
cmr "install prebuilt llvm prebuilt-llvm install-prebuilt-llvm "  -j
```