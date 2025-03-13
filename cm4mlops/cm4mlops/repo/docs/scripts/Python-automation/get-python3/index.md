# get-python3
Automatically generated README for this automation recipe: **get-python3**

Category: **[Python automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-python3/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-python3/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get python python3 get-python get-python3" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,python,python3,get-python,get-python3[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get python python3 get-python get-python3 [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,python,python3,get-python,get-python3'
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
    cm docker script "get python python3 get-python get-python3[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_conda.#`
               - ENV variables:
                   - CM_PYTHON_CONDA: `yes`
                   - CM_PYTHON_INSTALL_CACHE_TAGS: `_conda.#`
        * `_custom-path.#`
               - ENV variables:
                   - CM_PYTHON_BIN_WITH_PATH: `#`
        * `_lto`
        * `_optimized`
        * `_shared`
        * `_with-custom-ssl`
        * `_with-ssl`

        </details>


#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-python3/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-python3/run.bat)
___
#### Script output
```bash
cmr "get python python3 get-python get-python3 [variations]"  -j
```