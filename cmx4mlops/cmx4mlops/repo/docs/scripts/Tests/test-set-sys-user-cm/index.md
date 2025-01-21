# test-set-sys-user-cm
Automatically generated README for this automation recipe: **test-set-sys-user-cm**

Category: **[Tests](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/test-set-sys-user-cm/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "demo set sys-user cm sys-user-cm" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=demo,set,sys-user,cm,sys-user-cm 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "demo set sys-user cm sys-user-cm " 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'demo,set,sys-user,cm,sys-user-cm'
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
    cm docker script "demo set sys-user cm sys-user-cm" 
    ```
___

=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_SUDO: `sudo`



#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/test-set-sys-user-cm/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "demo set sys-user cm sys-user-cm "  -j
```