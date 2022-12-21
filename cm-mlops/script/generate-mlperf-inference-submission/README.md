*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Default environment](#default-environment)
* [CM script workflow](#cm-script-workflow)
* [New environment export](#new-environment-export)
* [New environment detected from customize](#new-environment-detected-from-customize)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
  * [ Script input flags mapped to environment](#script-input-flags-mapped-to-environment)
* [Maintainers](#maintainers)

</details>

___
### About

*TBD*
___
### Category

Modular MLPerf benchmarks.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
generate,submission,mlperf,mlperf-inference,inference,mlcommons,inference-submission,mlperf-inference-submission,mlcommons-inference-submission

___
### Default environment

___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission/_cm.json)***
     * get,python
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
       * `if (CM_RUN_MLPERF_ACCURACY == ['on']) AND (CM_SKIP_TRUNCATE_ACCURACY != ['yes'])`
       - CM script: [truncate-mlperf-inference-accuracy-log](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/truncate-mlperf-inference-accuracy-log)
     * submission,checker,mlc
       * `if (CM_RUN_SUBMISSION_CHECKER == ['yes'])`
       * CM names: `--adr.['mlperf-inference-submission-checker', 'submission-checker']...`
       - CM script: [run-mlperf-inference-submission-checker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker)
     * run,tar
       * `if (CM_TAR_SUBMISSION_DIR == ['yes'])`
       - CM script: [tar-my-folder](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/tar-my-folder)
___
### New environment export

___
### New environment detected from customize

* **CM_MLPERF_SUBMISSION_DIR**
* **CM_MLPERF_SUBMITTER**
* **CM_TAR_INPUT_DIR**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="generate,submission,mlperf,mlperf-inference,inference,mlcommons,inference-submission,mlperf-inference-submission,mlcommons-inference-submission"`

*or*

`cm run script "generate submission mlperf mlperf-inference inference mlcommons inference-submission mlperf-inference-submission mlcommons-inference-submission"`

*or*

`cm run script 5f8ab2d0b5874d53`

#### CM Python API

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

#### CM modular Docker container
*TBD*

#### Script input flags mapped to environment

* results_dir --> **CM_MLPERF_RESULTS_DIR**
* run_checker --> **CM_RUN_SUBMISSION_CHECKER**
* run_style --> **CM_MLPERF_RUN_STYLE**
* skip_truncation --> **CM_SKIP_TRUNCATE_ACCURACY**
* submission_dir --> **CM_MLPERF_SUBMISSION_DIR**
* clean --> **CM_MLPERF_CLEAN_SUBMISSION_DIR**

Examples:

```bash
cm run script "generate submission mlperf mlperf-inference inference mlcommons inference-submission mlperf-inference-submission mlcommons-inference-submission" --results_dir=...
```
```python
r=cm.access({... , "results_dir":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)