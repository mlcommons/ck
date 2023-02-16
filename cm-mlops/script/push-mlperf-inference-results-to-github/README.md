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
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! Use `README-extra.md` to add more info.*

### Description

#### Information

* Category: *Modular MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/push-mlperf-inference-results-to-github)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *push,mlperf-inference-results,publish-results,github*
* Output cached?: *False*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help

```cm run script --help```

#### CM CLI

`cm run script --tags=push,mlperf-inference-results,publish-results,github(,variations from below) (flags from below)`

*or*

`cm run script "push mlperf-inference-results publish-results github (variations from below)" (flags from below)`

*or*

`cm run script 36c2ffd5df5d453a`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'push,mlperf-inference-results,publish-results,github'
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

```cm run script --tags=gui --script="push,mlperf-inference-results,publish-results,github"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=push,mlperf-inference-results,publish-results,github) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* --**repo_url**=value --> **CM_MLPERF_RESULTS_GIT_REPO_URL**=value
* --**submission_dir**=value --> **CM_MLPERF_SUBMISSION_DIR**=value

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "repo_url":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.

* CM_MLPERF_RESULTS_GIT_REPO_URL: **https://github.com/ctuning/mlperf_inference_submissions_v3.0**

</details>

___
### Script workflow, dependencies and native scripts

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/push-mlperf-inference-results-to-github/_cm.json)***
     * get,python3
       * CM names: `--adr.['python3', 'python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/push-mlperf-inference-results-to-github/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/push-mlperf-inference-results-to-github/_cm.json)***
     * get,git,repo
       * CM names: `--adr.['get-git-repo']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/push-mlperf-inference-results-to-github/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/push-mlperf-inference-results-to-github/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/push-mlperf-inference-results-to-github/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/push-mlperf-inference-results-to-github/_cm.json)
___
### Script output
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)