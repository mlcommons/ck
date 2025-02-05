# get-mlperf-inference-results-dir
Automatically generated README for this automation recipe: **get-mlperf-inference-results-dir**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-results-dir/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "get mlperf inference results dir directory" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=get,mlperf,inference,results,dir,directory[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "get mlperf inference results dir directory [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,mlperf,inference,results,dir,directory'
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
    cm docker script "get mlperf inference results dir directory[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * Group "**version**"
        <details>
        <summary>Click here to expand this section.</summary>

        * `_version.#`
               - ENV variables:
                   - CM_MLPERF_INFERENCE_RESULTS_VERSION: `#`
        * **`_version.4_0`** (default)
               - ENV variables:
                   - CM_MLPERF_INFERENCE_RESULTS_VERSION: `4_0`

        </details>


    ##### Default variations

    `_version.4_0`
=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--results_dir=value`  &rarr;  `CM_MLPERF_INFERENCE_RESULTS_DIR=value`




___
#### Script output
```bash
cmr "get mlperf inference results dir directory [variations]" [--input_flags] -j
```