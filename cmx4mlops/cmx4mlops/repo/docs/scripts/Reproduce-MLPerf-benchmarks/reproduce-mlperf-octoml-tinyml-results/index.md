# reproduce-mlperf-octoml-tinyml-results
Automatically generated README for this automation recipe: **reproduce-mlperf-octoml-tinyml-results**

Category: **[Reproduce MLPerf benchmarks](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-mlperf-octoml-tinyml-results/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-mlperf-octoml-tinyml-results/_cm.json)*
* Output cached? *True*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "reproduce tiny results mlperf octoml mlcommons" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=reproduce,tiny,results,mlperf,octoml,mlcommons[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "reproduce tiny results mlperf octoml mlcommons [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,tiny,results,mlperf,octoml,mlcommons'
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
    cm docker script "reproduce tiny results mlperf octoml mlcommons[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_NRF`
               - ENV variables:
                   - CM_TINY_BOARD: `NRF5340DK`
        * `_NUCLEO`
               - ENV variables:
                   - CM_TINY_BOARD: `NUCLEO_L4R5ZI`
        * `_ad`
               - ENV variables:
                   - CM_TINY_MODEL: `ad`
        * `_cmsis_nn`
               - ENV variables:
                   - CM_MICROTVM_VARIANT: `microtvm_cmsis_nn`
        * `_ic`
               - ENV variables:
                   - CM_TINY_MODEL: `ic`
        * `_kws`
               - ENV variables:
                   - CM_TINY_MODEL: `kws`
        * `_native`
               - ENV variables:
                   - CM_MICROTVM_VARIANT: `microtvm_native`
        * `_vww`
               - ENV variables:
                   - CM_TINY_MODEL: `vww`

        </details>

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--flash=value`  &rarr;  `CM_FLASH_BOARD=value`
    * `--recreate_binary=value`  &rarr;  `CM_RECREATE_BINARY=value`



#### Versions
Default version: `r1.0`

* `r1.0`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-mlperf-octoml-tinyml-results/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "reproduce tiny results mlperf octoml mlcommons [variations]" [--input_flags] -j
```