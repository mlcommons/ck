# wrapper-reproduce-octoml-tinyml-submission
Automatically generated README for this automation recipe: **wrapper-reproduce-octoml-tinyml-submission**

Category: **[Reproduce MLPerf benchmarks](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/wrapper-reproduce-octoml-tinyml-submission/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/wrapper-reproduce-octoml-tinyml-submission/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "run generate-tiny generate submission tiny generate-tiny-submission results mlcommons mlperf octoml" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "run generate-tiny generate submission tiny generate-tiny-submission results mlcommons mlperf octoml " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml'
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
    cm docker script "run generate-tiny generate submission tiny generate-tiny-submission results mlcommons mlperf octoml" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--flash=value`  &rarr;  `CM_FLASH_BOARD=value`
    * `--recreate_binary=value`  &rarr;  `CM_RECREATE_BINARY=value`



#### Versions
Default version: `r1.0`

* `r1.0`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/wrapper-reproduce-octoml-tinyml-submission/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "run generate-tiny generate submission tiny generate-tiny-submission results mlcommons mlperf octoml " [--input_flags] -j
```