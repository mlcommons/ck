*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Variations](#variations)
  * [ All variations](#all-variations)
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
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
run,mlc,mlcommons,mlperf,inference,mlperf-inference,submission,checker,submission-checker,mlc-submission-checker

___
### Variations
#### All variations
* short-run
  - *ENV CM_MLPERF_SHORT_RUN*: `yes`
___
### Default environment

* CM_MLPERF_SHORT_RUN: **no**
___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker/_cm.json)***
     * get,python
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
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
       * `if (CM_MLPERF_DASHBOARD == ['on'])`
       - CM script: [publish-results-to-dashboard](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/publish-results-to-dashboard)
___
### New environment export

___
### New environment detected from customize

* **CM_MLPERF_SHORT_RUN**
* **CM_RUN_CMD**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="run,mlc,mlcommons,mlperf,inference,mlperf-inference,submission,checker,submission-checker,mlc-submission-checker"`

*or*

`cm run script "run mlc mlcommons mlperf inference mlperf-inference submission checker submission-checker mlc-submission-checker"`

*or*

`cm run script 15d03ec2c1af4297`

#### CM Python API

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

#### CM modular Docker container
*TBD*

#### Script input flags mapped to environment

* skip_compliance --> **CM_MLPERF_SKIP_COMPLIANCE**
* submission_dir --> **CM_MLPERF_SUBMISSION_DIR**
* submitter --> **CM_MLPERF_SUBMITTER**

Examples:

```bash
cm run script "run mlc mlcommons mlperf inference mlperf-inference submission checker submission-checker mlc-submission-checker" --skip_compliance=...
```
```python
r=cm.access({... , "skip_compliance":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)