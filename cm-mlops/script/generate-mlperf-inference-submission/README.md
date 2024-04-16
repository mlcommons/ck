**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/generate-mlperf-inference-submission).**



Automatically generated README for this automation recipe: **generate-mlperf-inference-submission**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=generate-mlperf-inference-submission,5f8ab2d0b5874d53) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-submission)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *generate,submission,mlperf,mlperf-inference,inference,mlcommons,inference-submission,mlperf-inference-submission,mlcommons-inference-submission*
* Output cached? *False*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "generate submission mlperf mlperf-inference inference mlcommons inference-submission mlperf-inference-submission mlcommons-inference-submission" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=generate,submission,mlperf,mlperf-inference,inference,mlcommons,inference-submission,mlperf-inference-submission,mlcommons-inference-submission`

`cm run script --tags=generate,submission,mlperf,mlperf-inference,inference,mlcommons,inference-submission,mlperf-inference-submission,mlcommons-inference-submission [--input_flags]`

*or*

`cmr "generate submission mlperf mlperf-inference inference mlcommons inference-submission mlperf-inference-submission mlcommons-inference-submission"`

`cmr "generate submission mlperf mlperf-inference inference mlcommons inference-submission mlperf-inference-submission mlcommons-inference-submission " [--input_flags]`


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
* CM_MLPERF_RUN_STYLE: `valid`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-submission/_cm.json)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,sut,system-description
       - CM script: [get-mlperf-inference-sut-description](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description)
     * install,pip-package,for-cmind-python,_package.tabulate
       - CM script: [install-pip-package-for-cmind-python](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pip-package-for-cmind-python)
     * get,mlperf,inference,utils
       - CM script: [get-mlperf-inference-utils](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-utils)
     * get,mlperf,results,dir
       * `if (CM_MLPERF_INFERENCE_RESULTS_DIR_  != on)`
       * CM names: `--adr.['get-mlperf-results-dir']...`
       - CM script: [get-mlperf-inference-results-dir](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-results-dir)
     * get,mlperf,submission,dir
       * `if (CM_MLPERF_INFERENCE_SUBMISSION_DIR  != on)`
       * CM names: `--adr.['get-mlperf-submission-dir']...`
       - CM script: [get-mlperf-inference-submission-dir](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-submission-dir)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-submission/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-submission/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-submission/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-submission/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-submission/_cm.json)***
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

___
### Script output
`cmr "generate submission mlperf mlperf-inference inference mlcommons inference-submission mlperf-inference-submission mlcommons-inference-submission " [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
