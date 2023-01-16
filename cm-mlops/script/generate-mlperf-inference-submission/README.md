<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys](#new-environment-keys)
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* Category: *Modular MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *generate,submission,mlperf,mlperf-inference,inference,mlcommons,inference-submission,mlperf-inference-submission,mlcommons-inference-submission*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=generate,submission,mlperf,mlperf-inference,inference,mlcommons,inference-submission,mlperf-inference-submission,mlcommons-inference-submission(,variations from below) (flags from below)`

*or*

`cm run script "generate submission mlperf mlperf-inference inference mlcommons inference-submission mlperf-inference-submission mlcommons-inference-submission (variations from below)" (flags from below)`

*or*

`cm run script 5f8ab2d0b5874d53`

#### CM Python API

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

#### CM modular Docker container
*TBD*
___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* --**results_dir**=value --> **CM_MLPERF_RESULTS_DIR**=value
* --**run_checker**=value --> **CM_RUN_SUBMISSION_CHECKER**=value
* --**run_style**=value --> **CM_MLPERF_RUN_STYLE**=value
* --**skip_truncation**=value --> **CM_SKIP_TRUNCATE_ACCURACY**=value
* --**submission_dir**=value --> **CM_MLPERF_SUBMISSION_DIR**=value
* --**clean**=value --> **CM_MLPERF_CLEAN_SUBMISSION_DIR**=value

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "results_dir":"..."}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

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
     * submission,checker,mlc
       * `if (CM_RUN_SUBMISSION_CHECKER  == yes)`
       * CM names: `--adr.['mlperf-inference-submission-checker', 'submission-checker']...`
       - CM script: [run-mlperf-inference-submission-checker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker)
     * run,tar
       * `if (CM_TAR_SUBMISSION_DIR  == yes)`
       - CM script: [tar-my-folder](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/tar-my-folder)
___
### Script output
#### New environment keys

#### New environment keys auto-detected from customize

* **CM_MLPERF_SUBMISSION_DIR**
* **CM_MLPERF_SUBMITTER**
* **CM_TAR_INPUT_DIR**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)