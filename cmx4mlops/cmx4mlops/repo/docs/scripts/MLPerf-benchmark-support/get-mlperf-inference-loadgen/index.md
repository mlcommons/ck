# get-mlperf-inference-loadgen
Automatically generated README for this automation recipe: **get-mlperf-inference-loadgen**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-loadgen/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-loadgen/_cm.yaml)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get loadgen inference inference-loadgen mlperf mlcommons" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,loadgen,inference,inference-loadgen,mlperf,mlcommons[,variations] 
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get loadgen inference inference-loadgen mlperf mlcommons [variations]" 
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,loadgen,inference,inference-loadgen,mlperf,mlcommons'
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
    cm docker script "get loadgen inference inference-loadgen mlperf mlcommons[variations]" 
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_copy`
        * `_custom-python`
               - ENV variables:
                   - CM_TMP_USE_CUSTOM_PYTHON: `on`
        * `_download`
               - ENV variables:
                   - CM_DOWNLOAD_CHECKSUM: `af3f9525965b2c1acc348fb882a5bfd1`
                   - CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD: `YES`
                   - CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD_URL: `https://www.dropbox.com/scl/fi/36dgoiur26i2tvwgsaatf/loadgen.zip?rlkey=ab68i7uza9anvaw0hk1xvf0qk&dl=0`
                   - CM_MLPERF_INFERENCE_LOADGEN_VERSION: `v3.1`
                   - CM_VERIFY_SSL: `False`
        * `_download_v3.1`
               - ENV variables:
                   - CM_DOWNLOAD_CHECKSUM: `af3f9525965b2c1acc348fb882a5bfd1`
                   - CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD: `YES`
                   - CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD_URL: `https://www.dropbox.com/scl/fi/36dgoiur26i2tvwgsaatf/loadgen.zip?rlkey=ab68i7uza9anvaw0hk1xvf0qk&dl=0`
                   - CM_MLPERF_INFERENCE_LOADGEN_VERSION: `v3.1`
                   - CM_VERIFY_SSL: `False`
        * `_download_v4.0`
               - ENV variables:
                   - CM_DOWNLOAD_CHECKSUM: `b4d97525d9ad0539a64667f2a3ca20c5`
                   - CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD: `YES`
                   - CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD_URL: `https://www.dropbox.com/scl/fi/gk5e9kziju5t56umxyzyx/loadgen.zip?rlkey=vsie4xnzml1inpjplm5cg7t54&dl=0`
                   - CM_MLPERF_INFERENCE_LOADGEN_VERSION: `v4.0`
                   - CM_VERIFY_SSL: `False`

        </details>

=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_SHARED_BUILD: `no`


#### Versions
Default version: `master`

* `custom`
* `main`
* `master`
* `pybind_fix`
* `r2.1`
* `r3.0`
* `r3.1`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-loadgen/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-loadgen/run.bat)
___
#### Script output
```bash
cmr "get loadgen inference inference-loadgen mlperf mlcommons [variations]"  -j
```