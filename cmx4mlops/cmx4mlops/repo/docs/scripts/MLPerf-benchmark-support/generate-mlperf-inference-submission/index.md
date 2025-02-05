# generate-mlperf-inference-submission
Automatically generated README for this automation recipe: **generate-mlperf-inference-submission**

Category: **[MLPerf benchmark support](..)**

License: **Apache 2.0**

* Notes from the authors, contributors and users: [*README-extra*](https://github.com/mlcommons/cm4mlops/tree/main/script/generate-mlperf-inference-submission/README-extra.md)

* CM meta description for this script: *[_cm.json](https://github.com/mlcommons/cm4mlops/tree/main/script/generate-mlperf-inference-submission/_cm.json)*
* Output cached? *False*

---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://docs.mlcommons.org/ck/install)
* [CM Getting Started Guide](https://docs.mlcommons.org/ck/getting-started/)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@cm4mlops```

#### Print CM help from the command line

````cmr "generate submission mlperf mlperf-inference inference mlcommons inference-submission mlperf-inference-submission mlcommons-inference-submission" --help````

#### Run this script

=== "CLI"
    ##### Run this script via CLI

    ```bash
    cm run script --tags=generate,submission,mlperf,mlperf-inference,inference,mlcommons,inference-submission,mlperf-inference-submission,mlcommons-inference-submission [--input_flags]
    ```
=== "CLI Alt"
    ##### Run this script via CLI (alternative)


    ```bash
    cmr "generate submission mlperf mlperf-inference inference mlcommons inference-submission mlperf-inference-submission mlcommons-inference-submission " [--input_flags]
    ```

=== "Python"
    ##### Run this script from Python


    ```python

    import cmind

    r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'generate,submission,mlperf,mlperf-inference,inference,mlcommons,inference-submission,mlperf-inference-submission,mlcommons-inference-submission'
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
    cm docker script "generate submission mlperf mlperf-inference inference mlcommons inference-submission mlperf-inference-submission mlcommons-inference-submission" [--input_flags]
    ```
___

=== "Input Flag Mapping"


    #### Script flags mapped to environment

    * `--analyzer_settings_file=value`  &rarr;  `CM_MLPERF_POWER_ANALYZER_SETTINGS_FILE_PATH=value`
    * `--category=value`  &rarr;  `CM_MLPERF_SUBMISSION_CATEGORY=value`
    * `--clean=value`  &rarr;  `CM_MLPERF_CLEAN_SUBMISSION_DIR=value`
    * `--dashboard=value`  &rarr;  `CM_MLPERF_DASHBOARD=value`
    * `--dashboard_wb_project=value`  &rarr;  `CM_MLPERF_DASHBOARD_WANDB_PROJECT=value`
    * `--device=value`  &rarr;  `CM_MLPERF_DEVICE=value`
    * `--division=value`  &rarr;  `CM_MLPERF_SUBMISSION_DIVISION=value`
    * `--duplicate=value`  &rarr;  `CM_MLPERF_DUPLICATE_SCENARIO_RESULTS=value`
    * `--hw_name=value`  &rarr;  `CM_HW_NAME=value`
    * `--hw_notes_extra=value`  &rarr;  `CM_MLPERF_SUT_HW_NOTES_EXTRA=value`
    * `--infer_scenario_results=value`  &rarr;  `CM_MLPERF_DUPLICATE_SCENARIO_RESULTS=value`
    * `--power_settings_file=value`  &rarr;  `CM_MLPERF_POWER_SETTINGS_FILE_PATH=value`
    * `--preprocess=value`  &rarr;  `CM_RUN_MLPERF_SUBMISSION_PREPROCESSOR=value`
    * `--preprocess_submission=value`  &rarr;  `CM_RUN_MLPERF_SUBMISSION_PREPROCESSOR=value`
    * `--results_dir=value`  &rarr;  `CM_MLPERF_INFERENCE_RESULTS_DIR_=value`
    * `--run_checker=value`  &rarr;  `CM_RUN_SUBMISSION_CHECKER=value`
    * `--run_style=value`  &rarr;  `CM_MLPERF_RUN_STYLE=value`
    * `--skip_truncation=value`  &rarr;  `CM_SKIP_TRUNCATE_ACCURACY=value`
    * `--submission_dir=value`  &rarr;  `CM_MLPERF_INFERENCE_SUBMISSION_DIR=value`
    * `--submitter=value`  &rarr;  `CM_MLPERF_SUBMITTER=value`
    * `--sw_notes_extra=value`  &rarr;  `CM_MLPERF_SUT_SW_NOTES_EXTRA=value`
    * `--tar=value`  &rarr;  `CM_TAR_SUBMISSION_DIR=value`



=== "Default environment"

    #### Default environment


    These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

    * CM_RUN_MLPERF_ACCURACY: `on`
    * CM_MLPERF_RUN_STYLE: `valid`



___
#### Script output
```bash
cmr "generate submission mlperf mlperf-inference inference mlcommons inference-submission mlperf-inference-submission mlcommons-inference-submission " [--input_flags] -j
```