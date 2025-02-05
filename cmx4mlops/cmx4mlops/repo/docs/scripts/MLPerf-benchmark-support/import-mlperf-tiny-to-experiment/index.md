# import-mlperf-tiny-to-experiment
Automatically generated README for this automation recipe: **import-mlperf-tiny-to-experiment**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

Developers: [Grigori Fursin](https://cKnowledge.org/gfursin)
* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/import-mlperf-tiny-to-experiment/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/import-mlperf-tiny-to-experiment/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "import mlperf tiny mlperf-tiny experiment 2experiment to-experiment" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=import,mlperf,tiny,mlperf-tiny,experiment,2experiment,to-experiment [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "import mlperf tiny mlperf-tiny experiment 2experiment to-experiment " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'import,mlperf,tiny,mlperf-tiny,experiment,2experiment,to-experiment'
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
    cm docker script "import mlperf tiny mlperf-tiny experiment 2experiment to-experiment" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--target_repo=value`  &rarr;  `CM_IMPORT_TINYMLPERF_TARGET_REPO=value`




___
#### Script output
```bash
cmr "import mlperf tiny mlperf-tiny experiment 2experiment to-experiment " [--input_flags] -j
```