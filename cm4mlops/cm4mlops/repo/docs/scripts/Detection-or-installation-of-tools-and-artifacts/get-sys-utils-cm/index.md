# get-sys-utils-cm
Automatically generated README for this automation recipe: **get-sys-utils-cm**

Category: **[Detection or installation of tools and artifacts](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/get-sys-utils-cm/_cm.yaml)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get sys-utils-cm" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,sys-utils-cm[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get sys-utils-cm [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,sys-utils-cm'
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
    cm docker script "get sys-utils-cm[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_user`
               - ENV variables:
                   - CM_PYTHON_PIP_USER: `--user`

        </details>

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--skip=value`  &rarr;  `CM_SKIP_SYS_UTILS=value`




#### Native script being run
=== "Linux/macOS"
     * [run-arch.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-sys-utils-cm/run-arch.sh)
     * [run-debian.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-sys-utils-cm/run-debian.sh)
     * [run-macos.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-sys-utils-cm/run-macos.sh)
     * [run-rhel.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-sys-utils-cm/run-rhel.sh)
     * [run-sles.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-sys-utils-cm/run-sles.sh)
     * [run-ubuntu.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-sys-utils-cm/run-ubuntu.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get sys-utils-cm [variations]" [--input_flags] -j
```