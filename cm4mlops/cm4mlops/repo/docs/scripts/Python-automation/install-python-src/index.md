# install-python-src
Automatically generated README for this automation recipe: **install-python-src**

Category: **[Python automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-python-src/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install src python python3 src-python3 src-python" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=install,src,python,python3,src-python3,src-python[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "install src python python3 src-python3 src-python [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,src,python,python3,src-python3,src-python'
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
    cm docker script "install src python python3 src-python3 src-python[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_lto`
               - ENV variables:
                   - CM_PYTHON_LTO_FLAG: ` --lto`
                   - CM_PYTHON_INSTALL_CACHE_TAGS: `with-lto`
        * `_optimized`
               - ENV variables:
                   - CM_PYTHON_OPTIMIZATION_FLAG: ` --enable-optimizations`
                   - CM_PYTHON_INSTALL_CACHE_TAGS: `optimized`
        * `_shared`
               - ENV variables:
                   - CM_PYTHON_INSTALL_CACHE_TAGS: `shared`
                   - CM_SHARED_BUILD: `yes`
        * `_with-custom-ssl`
               - ENV variables:
                   - CM_CUSTOM_SSL: `yes`
                   - CM_PYTHON_INSTALL_CACHE_TAGS: `with-custom-ssl`

        </details>


      * Group "**ssl**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_with-ssl`
               - ENV variables:
                   - CM_ENABLE_SSL: `yes`
                   - CM_PYTHON_INSTALL_CACHE_TAGS: `with-ssl`

        </details>

=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_ENABLE_SSL: `no`
    * CM_CUSTOM_SSL: `no`
    * CM_SHARED_BUILD: `no`
    * CM_PYTHON_OPTIMIZATION_FLAG: ``
    * CM_PYTHON_LTO_FLAG: ``
    * CM_WGET_URL: `https://www.python.org/ftp/python/[PYTHON_VERSION]/Python-[PYTHON_VERSION].tgz`


#### Versions
Default version: `3.10.13`


#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-python-src/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "install src python python3 src-python3 src-python [variations]"  -j
```