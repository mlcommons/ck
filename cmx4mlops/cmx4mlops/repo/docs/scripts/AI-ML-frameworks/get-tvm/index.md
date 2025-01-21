# get-tvm
Automatically generated README for this automation recipe: **get-tvm**

Category: **[AI/ML frameworks](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-tvm/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-tvm/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get tvm get-tvm" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,tvm,get-tvm[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get tvm get-tvm [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,tvm,get-tvm'
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
    cm docker script "get tvm get-tvm[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_cuda`
               - ENV variables:
                   - CM_TVM_USE_CUDA: `yes`
        * `_openmp`
               - ENV variables:
                   - CM_TVM_USE_OPENMP: `yes`

        </details>


      * Group "**installation-type**"
        <details>
        <summary>Click here to expand this section.</summary>

        * **`_llvm`** (default)
               - ENV variables:
                   - CM_TVM_USE_LLVM: `yes`
        * `_pip-install`
               - ENV variables:
                   - CM_TVM_PIP_INSTALL: `yes`

        </details>


    ##### Default variations

    `_llvm`
=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_GIT_CHECKOUT: `main`
    * CM_GIT_URL: `https://github.com/apache/tvm`
    * CM_TVM_PIP_INSTALL: `no`


#### Versions
* `main`
* `v0.10.0`
* `v0.7.0`
* `v0.8.0`
* `v0.9.0`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-tvm/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "get tvm get-tvm [variations]"  -j
```