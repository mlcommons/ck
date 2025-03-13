# preprocess-mlperf-inference-submission
Automatically generated README for this automation recipe: **preprocess-mlperf-inference-submission**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**


* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/preprocess-mlperf-inference-submission/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "run mlc mlcommons mlperf inference submission mlperf-inference processor preprocessor preprocess" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=run,mlc,mlcommons,mlperf,inference,submission,mlperf-inference,processor,preprocessor,preprocess [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "run mlc mlcommons mlperf inference submission mlperf-inference processor preprocessor preprocess " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,mlc,mlcommons,mlperf,inference,submission,mlperf-inference,processor,preprocessor,preprocess'
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
    cm docker script "run mlc mlcommons mlperf inference submission mlperf-inference processor preprocessor preprocess" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--submission_dir=value`  &rarr;  `CM_MLPERF_INFERENCE_SUBMISSION_DIR=value`
    * `--submitter=value`  &rarr;  `CM_MLPERF_SUBMITTER=value`




#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/preprocess-mlperf-inference-submission/run.sh)
=== "Windows"

    No run file exists for Windows
___
#### Script output
```bash
cmr "run mlc mlcommons mlperf inference submission mlperf-inference processor preprocessor preprocess " [--input_flags] -j
```