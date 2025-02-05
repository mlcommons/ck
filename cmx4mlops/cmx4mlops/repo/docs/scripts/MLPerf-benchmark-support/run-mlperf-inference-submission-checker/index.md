# run-mlperf-inference-submission-checker
Automatically generated README for this automation recipe: **run-mlperf-inference-submission-checker**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-inference-submission-checker/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-inference-submission-checker/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "run mlc mlcommons mlperf inference mlperf-inference submission checker submission-checker mlc-submission-checker" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=run,mlc,mlcommons,mlperf,inference,mlperf-inference,submission,checker,submission-checker,mlc-submission-checker[,variations] [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "run mlc mlcommons mlperf inference mlperf-inference submission checker submission-checker mlc-submission-checker [variations]" [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,mlc,mlcommons,mlperf,inference,mlperf-inference,submission,checker,submission-checker,mlc-submission-checker'
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
    cm docker script "run mlc mlcommons mlperf inference mlperf-inference submission checker submission-checker mlc-submission-checker[variations]" [--input_flags]
    ```
___

=== "Variations"


    #### Variations

      * *No group (any combination of variations can be selected)*
        <details>
        <summary>Click here to expand this section.</summary>

        * `_short-run`
               - ENV variables:
                   - CM_MLPERF_SHORT_RUN: `yes`

        </details>

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--extra_args=value`  &rarr;  `CM_MLPERF_SUBMISSION_CHECKER_EXTRA_ARGS=value`
    * `--extra_model_benchmark_map=value`  &rarr;  `CM_MLPERF_EXTRA_MODEL_MAPPING=value`
    * `--input=value`  &rarr;  `CM_MLPERF_INFERENCE_SUBMISSION_DIR=value`
    * `--power=value`  &rarr;  `CM_MLPERF_POWER=value`
    * `--push_to_github=value`  &rarr;  `CM_MLPERF_RESULT_PUSH_TO_GITHUB=value`
    * `--skip_compliance=value`  &rarr;  `CM_MLPERF_SKIP_COMPLIANCE=value`
    * `--skip_power_check=value`  &rarr;  `CM_MLPERF_SKIP_POWER_CHECK=value`
    * `--src_version=value`  &rarr;  `CM_MLPERF_SUBMISSION_CHECKER_VERSION=value`
    * `--submission_dir=value`  &rarr;  `CM_MLPERF_INFERENCE_SUBMISSION_DIR=value`
    * `--submitter=value`  &rarr;  `CM_MLPERF_SUBMITTER=value`
    * `--tar=value`  &rarr;  `CM_TAR_SUBMISSION_DIR=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_MLPERF_SHORT_RUN: `no`


#### Versions
Default version: `master`

* `master`
* `r3.0`
* `r3.1`
* `r4.0`

#### Native script being run
=== "Linux/macOS"
     * [run.sh](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-inference-submission-checker/run.sh)
=== "Windows"

     * [run.bat](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-inference-submission-checker/run.bat)
___
#### Script output
```bash
cmr "run mlc mlcommons mlperf inference mlperf-inference submission checker submission-checker mlc-submission-checker [variations]" [--input_flags] -j
```