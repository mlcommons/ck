# generate-mlperf-tiny-report
Automatically generated README for this automation recipe: **generate-mlperf-tiny-report**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

Developers: [Grigori Fursin](https://cKnowledge.org/gfursin)
* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/generate-mlperf-tiny-report/README-extra.md)

* CM meta description for this script: *[_cm.yaml](https://github.com/mlcommons/cm4mlops/tree/main/script/generate-mlperf-tiny-report/_cm.yaml)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "generate mlperf tiny mlperf-tiny report" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=generate,mlperf,tiny,mlperf-tiny,report [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "generate mlperf tiny mlperf-tiny report " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'generate,mlperf,tiny,mlperf-tiny,report'
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
    cm docker script "generate mlperf tiny mlperf-tiny report" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--repo_tags=value`  &rarr;  `CM_IMPORT_TINYMLPERF_REPO_TAGS=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_IMPORT_TINYMLPERF_REPO_TAGS: `1.1-private`



#### Native script being run
=== "Linux/macOS"
     * [run_submission_checker.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/generate-mlperf-tiny-report/run_submission_checker.sh)
=== "Windows"

     * [run_submission_checker.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/generate-mlperf-tiny-report/run_submission_checker.bat)
___
#### Script output
```bash
cmr "generate mlperf tiny mlperf-tiny report " [--input_flags] -j
```