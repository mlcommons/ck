# flash-tinyml-binary
Automatically generated README for this automation recipe: **flash-tinyml-binary**

Category: **[TinyML automation](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/flash-tinyml-binary/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/flash-tinyml-binary/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "flash tiny mlperf mlcommons" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=flash,tiny,mlperf,mlcommons[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "flash tiny mlperf mlcommons [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'flash,tiny,mlperf,mlcommons'
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
    cm docker script "flash tiny mlperf mlcommons[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_NRF`
        * `_NUCLEO`
        * `_ad`
        * `_cmsis_nn`
        * `_ic`
        * `_kws`
        * `_native`
        * `_vww`

        </details>

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--build_dir=value`  &rarr;  `CM_TINY_BUILD_DIR=value`



#### Versions
Default version: `r1.0`


#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/flash-tinyml-binary/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "flash tiny mlperf mlcommons [variations]" [--input_flags] -j
```