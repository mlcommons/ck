# Build oneDNN from sources
Automatically generated README for this automation recipe: **install-onednn-from-src**

Category: **[Compiler automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-onednn-from-src/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install get src from.src onednn src-onednn" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=install,get,src,from.src,onednn,src-onednn[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "install get src from.src onednn src-onednn [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,get,src,from.src,onednn,src-onednn'
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
    cm docker script "install get src from.src onednn src-onednn[variations]" 
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
        * `_for-intel-mlperf-inference-v3.1-bert`
               - ENV variables:
                   - CM_CONDA_ENV: `yes`
                   - CM_FOR_INTEL_MLPERF_INFERENCE: `yes`
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
        * **`_repo.https://github.com/oneapi-src/oneDNN`** (default)
               - ENV variables:
                   - CM_GIT_URL: `https://github.com/oneapi-src/oneDNN`

        </details>


    ##### Default variations

    `_repo.https://github.com/oneapi-src/oneDNN`

#### Native script being run
=== "Linux/macOS"
     * [run-intel-mlperf-inference.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-onednn-from-src/run-intel-mlperf-inference.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "install get src from.src onednn src-onednn [variations]"  -j
```