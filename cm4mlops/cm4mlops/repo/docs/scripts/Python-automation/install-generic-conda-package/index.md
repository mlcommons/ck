# install-generic-conda-package
Automatically generated README for this automation recipe: **install-generic-conda-package**

Category: **[Python automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-generic-conda-package/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get install generic generic-conda-lib conda-lib conda-package generic-conda-package" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,install,generic,generic-conda-lib,conda-lib,conda-package,generic-conda-package[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get install generic generic-conda-lib conda-lib conda-package generic-conda-package [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,install,generic,generic-conda-lib,conda-lib,conda-package,generic-conda-package'
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
    cm docker script "get install generic generic-conda-lib conda-lib conda-package generic-conda-package[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_name.#`
        * `_package.#`
               - ENV variables:
                   - CM_CONDA_PKG_NAME: `#`

        </details>


      * Group "**package-source**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_source.#`
               - ENV variables:
                   - CM_CONDA_PKG_SRC: `#`

        </details>


#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-generic-conda-package/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get install generic generic-conda-lib conda-lib conda-package generic-conda-package [variations]"  -j
```