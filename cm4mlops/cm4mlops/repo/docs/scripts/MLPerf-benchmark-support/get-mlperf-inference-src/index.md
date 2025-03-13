# get-mlperf-inference-src
Automatically generated README for this automation recipe: **get-mlperf-inference-src**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-src/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-src/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get src source inference inference-src inference-source mlperf mlcommons" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,src,source,inference,inference-src,inference-source,mlperf,mlcommons[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get src source inference inference-src inference-source mlperf mlcommons [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,src,source,inference,inference-src,inference-source,mlperf,mlcommons'
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
    cm docker script "get src source inference inference-src inference-source mlperf mlcommons[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_3d-unet`
               - ENV variables:
                   - CM_SUBMODULE_3D_UNET: `yes`
        * `_deeplearningexamples`
               - ENV variables:
                   - CM_SUBMODULE_DEEPLEARNINGEXAMPLES: `yes`
        * `_deepsparse`
               - ENV variables:
                   - CM_GIT_CHECKOUT: `deepsparse`
                   - CM_GIT_URL: `https://github.com/neuralmagic/inference`
                   - CM_MLPERF_LAST_RELEASE: `v4.0`
        * `_gn`
               - ENV variables:
                   - CM_SUBMODULE_GN: `yes`
        * `_no-recurse-submodules`
               - ENV variables:
                   - CM_GIT_RECURSE_SUBMODULES: ``
        * `_nvidia-pycocotools`
               - ENV variables:
                   - CM_GIT_PATCH_FILENAME: `coco.patch`
        * `_octoml`
               - ENV variables:
                   - CM_GIT_URL: `https://github.com/octoml/inference`
        * `_openimages-nvidia-pycocotools`
               - ENV variables:
                   - CM_GIT_PATCH_FILENAME: `openimages-pycocotools.patch`
        * `_patch`
               - ENV variables:
                   - CM_GIT_PATCH: `yes`
        * `_pybind`
               - ENV variables:
                   - CM_SUBMODULE_PYBIND: `yes`
        * `_recurse-submodules`
               - ENV variables:
                   - CM_GIT_RECURSE_SUBMODULES: ` --recurse-submodules`
        * `_repo.#`
               - ENV variables:
                   - CM_GIT_URL: `#`
        * `_submodules.#`
               - ENV variables:
                   - CM_GIT_SUBMODULES: `#`

        </details>


      * Group "**checkout**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_branch.#`
               - ENV variables:
                   - CM_GIT_CHECKOUT: `#`
        * `_sha.#`
               - ENV variables:
                   - CM_GIT_SHA: `#`

        </details>


      * Group "**git-history**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_full-history`
               - ENV variables:
                   - CM_GIT_DEPTH: ``
        * **`_short-history`** (default)
               - ENV variables:
                   - CM_GIT_DEPTH: `--depth 10`

        </details>


    ##### Default variations

    `_short-history`
=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_GIT_CHECKOUT_FOLDER: `inference`
    * CM_GIT_DEPTH: `--depth 4`
    * CM_GIT_PATCH: `no`
    * CM_GIT_RECURSE_SUBMODULES: ``
    * CM_GIT_URL: `https://github.com/mlcommons/inference.git`


#### Versions
Default version: `master`

* `custom`
* `deepsparse`
* `main`
* `master`
* `pybind_fix`
* `r2.1`
* `r3.0`
* `r3.1`
* `tvm`

___
#### Script output
```bash
cmr "get src source inference inference-src inference-source mlperf mlcommons [variations]"  -j
```