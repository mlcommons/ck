# Build LLVM compiler from sources (can take >30 min)
Automatically generated README for this automation recipe: **install-llvm-src**

Category: **[Compiler automation](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/install-llvm-src/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "install src llvm from.src src-llvm" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=install,src,llvm,from.src,src-llvm[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "install src llvm from.src src-llvm [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'install,src,llvm,from.src,src-llvm'
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
    cm docker script "install src llvm from.src src-llvm[variations]" 
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
                   - CM_LLVM_CONDA_ENV: `yes`
        * `_for-intel-mlperf-inference-v3.1-gptj`
               - ENV variables:
                   - CM_LLVM_CONDA_ENV: `yes`
                   - CM_LLVM_16_INTEL_MLPERF_INFERENCE: `yes`
                   - USE_CUDA: `0`
                   - CUDA_VISIBLE_DEVICES: ``
        * `_full-history`
        * `_runtimes.#`
               - ENV variables:
                   - CM_LLVM_ENABLE_RUNTIMES: `#`
        * `_sha.#`
               - ENV variables:
                   - CM_GIT_CHECKOUT_SHA: `#`
        * `_tag.#`
               - ENV variables:
                   - CM_GIT_CHECKOUT_TAG: `#`

        </details>


      * Group "**build-type**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_debug`
               - ENV variables:
                   - CM_LLVM_BUILD_TYPE: `debug`
        * **`_release`** (default)
               - ENV variables:
                   - CM_LLVM_BUILD_TYPE: `release`

        </details>


      * Group "**clang**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_clang`** (default)
               - ENV variables:
                   - CM_LLVM_ENABLE_PROJECTS: `clang`

        </details>


      * Group "**repo**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_repo.#`
               - ENV variables:
                   - CM_GIT_URL: `#`

        </details>


    ##### Default variations

    `_clang,_release`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/install-llvm-src/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "install src llvm from.src src-llvm [variations]"  -j
```