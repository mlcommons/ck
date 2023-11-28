<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Summary](#summary)
* [Reuse this script in your project](#reuse-this-script-in-your-project)
  * [ Install CM automation language](#install-cm-automation-language)
  * [ Check CM script flags](#check-cm-script-flags)
  * [ Run this script from command line](#run-this-script-from-command-line)
  * [ Run this script from Python](#run-this-script-from-python)
  * [ Run this script via GUI](#run-this-script-via-gui)
  * [ Run this script via Docker (beta)](#run-this-script-via-docker-(beta))
* [Customization](#customization)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About


See extra [notes](README-extra.md) from the authors and contributors.

#### Summary

* Category: *MLPerf benchmark support.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *generate,submission,mlperf,mlperf-inference,inference,mlcommons,inference-submission,mlperf-inference-submission,mlcommons-inference-submission*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=generate,submission,mlperf,mlperf-inference,inference,mlcommons,inference-submission,mlperf-inference-submission,mlcommons-inference-submission [--input_flags]`

2. `cmr "generate submission mlperf mlperf-inference inference mlcommons inference-submission mlperf-inference-submission mlcommons-inference-submission" [--input_flags]`

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

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

</details>


#### Run this script via GUI

```cmr "cm gui" --script="generate,submission,mlperf,mlperf-inference,inference,mlcommons,inference-submission,mlperf-inference-submission,mlcommons-inference-submission"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=generate,submission,mlperf,mlperf-inference,inference,mlcommons,inference-submission,mlperf-inference-submission,mlcommons-inference-submission) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "generate submission mlperf mlperf-inference inference mlcommons inference-submission mlperf-inference-submission mlcommons-inference-submission" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--analyzer_settings_file=value`  &rarr;  `CM_MLPERF_POWER_ANALYZER_SETTINGS_FILE_PATH=value`
* `--category=value`  &rarr;  `CM_MLPERF_SUBMISSION_CATEGORY=value`
* `--clean=value`  &rarr;  `CM_MLPERF_CLEAN_SUBMISSION_DIR=value`
* `--device=value`  &rarr;  `CM_MLPERF_DEVICE=value`
* `--division=value`  &rarr;  `CM_MLPERF_SUBMISSION_DIVISION=value`
* `--duplicate=value`  &rarr;  `CM_MLPERF_DUPLICATE_SCENARIO_RESULTS=value`
* `--hw_name=value`  &rarr;  `CM_HW_NAME=value`
* `--hw_notes_extra=value`  &rarr;  `CM_MLPERF_SUT_HW_NOTES_EXTRA=value`
* `--infer_scenario_results=value`  &rarr;  `CM_MLPERF_DUPLICATE_SCENARIO_RESULTS=value`
* `--power_settings_file=value`  &rarr;  `CM_MLPERF_POWER_SETTINGS_FILE_PATH=value`
* `--preprocess=value`  &rarr;  `CM_RUN_MLPERF_SUBMISSION_PREPROCESSOR=value`
* `--preprocess_submission=value`  &rarr;  `CM_RUN_MLPERF_SUBMISSION_PREPROCESSOR=value`
* `--results_dir=value`  &rarr;  `CM_MLPERF_RESULTS_DIR=value`
* `--run_checker=value`  &rarr;  `CM_RUN_SUBMISSION_CHECKER=value`
* `--run_style=value`  &rarr;  `CM_MLPERF_RUN_STYLE=value`
* `--skip_truncation=value`  &rarr;  `CM_SKIP_TRUNCATE_ACCURACY=value`
* `--submission_dir=value`  &rarr;  `CM_MLPERF_SUBMISSION_DIR=value`
* `--submitter=value`  &rarr;  `CM_MLPERF_SUBMITTER=value`
* `--sw_notes_extra=value`  &rarr;  `CM_MLPERF_SUT_SW_NOTES_EXTRA=value`
* `--tar=value`  &rarr;  `CM_TAR_SUBMISSION_DIR=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "analyzer_settings_file":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_RUN_MLPERF_ACCURACY: `on`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission/_cm.json)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,sut,system-description
       - CM script: [get-mlperf-inference-sut-description](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission/_cm.json)***
     * accuracy,truncate,mlc
       * `if (CM_RUN_MLPERF_ACCURACY  == on) AND (CM_SKIP_TRUNCATE_ACCURACY  != yes)`
       - CM script: [truncate-mlperf-inference-accuracy-log](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/truncate-mlperf-inference-accuracy-log)
     * preprocess,mlperf,submission
       * `if (CM_RUN_MLPERF_SUBMISSION_PREPROCESSOR in ['on', 'True', 'yes', True])`
       - CM script: [preprocess-mlperf-inference-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/preprocess-mlperf-inference-submission)
     * submission,inference,checker,mlc
       * `if (CM_RUN_SUBMISSION_CHECKER  == yes)`
       * CM names: `--adr.['mlperf-inference-submission-checker', 'submission-checker']...`
       - CM script: [run-mlperf-inference-submission-checker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker)
</details>

___
### Script output
`cmr "generate submission mlperf mlperf-inference inference mlcommons inference-submission mlperf-inference-submission mlcommons-inference-submission" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)