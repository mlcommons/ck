# get-mlperf-inference-results
Automatically generated README for this automation recipe: **get-mlperf-inference-results**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-results/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-results/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get results inference inference-results mlcommons mlperf" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,results,inference,inference-results,mlcommons,mlperf[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get results inference inference-results mlcommons mlperf [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,results,inference,inference-results,mlcommons,mlperf'
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
    cm docker script "get results inference inference-results mlcommons mlperf[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * Group "**source-repo**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_ctuning`
               - ENV variables:
                   - GITHUB_REPO_OWNER: `ctuning`
        * `_custom`
               - ENV variables:
                   - GITHUB_REPO_OWNER: `arjunsuresh`
        * `_go`
               - ENV variables:
                   - GITHUB_REPO_OWNER: `GATEOverflow`
        * **`_mlcommons`** (default)
               - ENV variables:
                   - GITHUB_REPO_OWNER: `mlcommons`
        * `_nvidia-only`
               - ENV variables:
                   - GITHUB_REPO_OWNER: `GATEOverflow`
                   - NVIDIA_ONLY: `yes`

        </details>


    ##### Default variations

    `_mlcommons`
=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_GIT_CHECKOUT: `master`
    * CM_GIT_DEPTH: `--depth 1`
    * CM_GIT_PATCH: `no`


#### Versions
Default version: `v3.1`

* `v2.1`
* `v3.0`
* `v3.1`
* `v4.0`

___
#### Script output
```bash
cmr "get results inference inference-results mlcommons mlperf [variations]"  -j
```