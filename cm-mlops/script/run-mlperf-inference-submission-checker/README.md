<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM GUI](#cm-gui)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* Category: *Modular MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *run,mlc,mlcommons,mlperf,inference,mlperf-inference,submission,checker,submission-checker,mlc-submission-checker*
* Output cached?: *False*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

##### CM pull repository

```cm pull repo mlcommons@ck```

##### CM script automation help

```cm run script --help```

#### CM CLI

1. `cm run script --tags=run,mlc,mlcommons,mlperf,inference,mlperf-inference,submission,checker,submission-checker,mlc-submission-checker[,variations] [--input_flags]`

2. `cm run script "run mlc mlcommons mlperf inference mlperf-inference submission checker submission-checker mlc-submission-checker[,variations]" [--input_flags]`

3. `cm run script 15d03ec2c1af4297 [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

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

</details>


#### CM GUI

```cm run script --tags=gui --script="run,mlc,mlcommons,mlperf,inference,mlperf-inference,submission,checker,submission-checker,mlc-submission-checker"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,mlc,mlcommons,mlperf,inference,mlperf-inference,submission,checker,submission-checker,mlc-submission-checker) to generate CM CMD.

#### CM modular Docker container

*TBD*

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

* `--extra_model_benchmark_map=value`  &rarr;  `CM_MLPERF_EXTRA_MODEL_MAPPING=value`
* `--power=value`  &rarr;  `CM_MLPERF_POWER=value`
* `--push_to_github=value`  &rarr;  `CM_MLPERF_RESULT_PUSH_TO_GITHUB=value`
* `--skip_compliance=value`  &rarr;  `CM_MLPERF_SKIP_COMPLIANCE=value`
* `--skip_power_check=value`  &rarr;  `CM_MLPERF_SKIP_POWER_CHECK=value`
* `--submission_dir=value`  &rarr;  `CM_MLPERF_SUBMISSION_DIR=value`
* `--submitter=value`  &rarr;  `CM_MLPERF_SUBMITTER=value`
* `--version=value`  &rarr;  `CM_MLPERF_VERSION=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "extra_model_benchmark_map":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MLPERF_SHORT_RUN: `no`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker/_cm.json)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,generic-python-lib,_xlsxwriter
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_pandas
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker/_cm.json)***
     * publish-results,dashboard
       * `if (CM_MLPERF_DASHBOARD  == on)`
       - CM script: [publish-results-to-dashboard](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/publish-results-to-dashboard)
     * publish-results,github
       * `if (CM_MLPERF_RESULT_PUSH_TO_GITHUB  == on)`
       * CM names: `--adr.['push-to-github']...`
       - CM script: [push-mlperf-inference-results-to-github](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/push-mlperf-inference-results-to-github)
</details>

___
### Script output
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)