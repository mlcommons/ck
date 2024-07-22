**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-training-submission-checker).**



Automatically generated README for this automation recipe: **run-mlperf-training-submission-checker**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=run-mlperf-training-submission-checker,cb5cb60ac9a74d09) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-training-submission-checker)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *run,mlc,mlcommons,mlperf,training,train,mlperf-training,submission,checker,submission-checker,mlc-submission-checker*
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

````cmr "run mlc mlcommons mlperf training train mlperf-training submission checker submission-checker mlc-submission-checker" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=run,mlc,mlcommons,mlperf,training,train,mlperf-training,submission,checker,submission-checker,mlc-submission-checker`

`cm run script --tags=run,mlc,mlcommons,mlperf,training,train,mlperf-training,submission,checker,submission-checker,mlc-submission-checker[,variations] [--input_flags]`

*or*

`cmr "run mlc mlcommons mlperf training train mlperf-training submission checker submission-checker mlc-submission-checker"`

`cmr "run mlc mlcommons mlperf training train mlperf-training submission checker submission-checker mlc-submission-checker [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,mlc,mlcommons,mlperf,training,train,mlperf-training,submission,checker,submission-checker,mlc-submission-checker'
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

```cmr "cm gui" --script="run,mlc,mlcommons,mlperf,training,train,mlperf-training,submission,checker,submission-checker,mlc-submission-checker"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,mlc,mlcommons,mlperf,training,train,mlperf-training,submission,checker,submission-checker,mlc-submission-checker) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "run mlc mlcommons mlperf training train mlperf-training submission checker submission-checker mlc-submission-checker[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_short-run`
      - Environment variables:
        - *CM_MLPERF_SHORT_RUN*: `yes`
      - Workflow:

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--extra_args=value`  &rarr;  `CM_MLPERF_SUBMISSION_CHECKER_EXTRA_ARGS=value`
* `--input=value`  &rarr;  `CM_MLPERF_SUBMISSION_DIR=value`
* `--power=value`  &rarr;  `CM_MLPERF_POWER=value`
* `--push_to_github=value`  &rarr;  `CM_MLPERF_RESULT_PUSH_TO_GITHUB=value`
* `--skip_compliance=value`  &rarr;  `CM_MLPERF_SKIP_COMPLIANCE=value`
* `--skip_power_check=value`  &rarr;  `CM_MLPERF_SKIP_POWER_CHECK=value`
* `--src_version=value`  &rarr;  `CM_MLPERF_SUBMISSION_CHECKER_VERSION=value`
* `--submission_dir=value`  &rarr;  `CM_MLPERF_SUBMISSION_DIR=value`
* `--submitter=value`  &rarr;  `CM_MLPERF_SUBMITTER=value`
* `--tar=value`  &rarr;  `CM_TAR_SUBMISSION_DIR=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "extra_args":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MLPERF_SHORT_RUN: `no`

</details>

#### Versions
Default version: `master`

* `master`
* `r3.0`
* `r3.1`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-training-submission-checker/_cm.json)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src', 'submission-checker-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * install,mlperf,logging,from.src
       - CM script: [install-mlperf-logging-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-mlperf-logging-from-src)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-training-submission-checker/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-training-submission-checker/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-training-submission-checker/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-training-submission-checker/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-training-submission-checker/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-training-submission-checker/_cm.json)***
     * publish-results,github
       * `if (CM_MLPERF_RESULT_PUSH_TO_GITHUB  == on)`
       * CM names: `--adr.['push-to-github']...`
       - CM script: [push-mlperf-inference-results-to-github](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/push-mlperf-inference-results-to-github)
     * run,tar
       * `if (CM_TAR_SUBMISSION_DIR  == yes)`
       - CM script: [tar-my-folder](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/tar-my-folder)

___
### Script output
`cmr "run mlc mlcommons mlperf training train mlperf-training submission checker submission-checker mlc-submission-checker [,variations]" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
