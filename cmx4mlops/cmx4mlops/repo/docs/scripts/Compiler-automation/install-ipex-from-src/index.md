# Build IPEX from sources
Automatically generated README for this automation recipe: **install-ipex-from-src**

Category: **[Compiler automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-ipex-from-src/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install get src from.src ipex src-ipex" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=install,get,src,from.src,ipex,src-ipex[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "install get src from.src ipex src-ipex [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,get,src,from.src,ipex,src-ipex'
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
    cm docker script "install get src from.src ipex src-ipex[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_branch.#`
               - ENV variables:
                   - CM_GIT_CHECKOUT: `#`
        * `_for-intel-mlperf-inference-v3.1-gptj`
               - ENV variables:
                   - CM_CONDA_ENV: `yes`
        * `_sha.#`
               - ENV variables:
                   - CM_GIT_CHECKOUT_SHA: `#`
        * `_tag.#`
               - ENV variables:
                   - CM_GIT_CHECKOUT_TAG: `#`

        </details>


      * Group "**repo**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_repo.#`
               - ENV variables:
                   - CM_GIT_URL: `#`
        * **`_repo.https://github.com/intel/intel-extension-for-pytorch`** (default)
               - ENV variables:
                   - CM_GIT_URL: `https://github.com/intel/intel-extension-for-pytorch`

        </details>


    ##### Default variations

    `_repo.https://github.com/intel/intel-extension-for-pytorch`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-ipex-from-src/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "install get src from.src ipex src-ipex [variations]"  -j
```