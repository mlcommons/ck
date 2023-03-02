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
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,mlperf,inference,sut,configs,sut-configs*
* Output cached?: *False*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help

```cm run script --help```

#### CM CLI

`cm run script --tags=get,mlperf,inference,sut,configs,sut-configs(,variations from below) (flags from below)`

*or*

`cm run script "get mlperf inference sut configs sut-configs (variations from below)" (flags from below)`

*or*

`cm run script c2fbf72009e2445b`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,mlperf,inference,sut,configs,sut-configs'
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

```cm run script --tags=gui --script="get,mlperf,inference,sut,configs,sut-configs"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,mlperf,inference,sut,configs,sut-configs) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_octoml`
      - Environment variables:
        - *CM_SUT_USE_EXTERNAL_CONFIG_REPO*: `yes`
        - *CM_GIT_CHECKOUT_FOLDER*: `configs`
        - *CM_GIT_URL*: `https://github.com/arjunsuresh/mlperf-inference-configs`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * get,git,repo,_repo.mlperf_inference_configs_octoml
             - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* --**configs_git_url**=value --> **CM_GIT_URL**=value
* --**repo_path**=value --> **CM_SUT_CONFIGS_PATH**=value
* --**run_config**=value --> **CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX**=value

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "configs_git_url":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.

* CM_SUT_CONFIGS_PATH: ****
* CM_GIT_URL: ****

</details>

___
### Script workflow, dependencies and native scripts

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs/_cm.json)
  1. Run "preprocess" function from customize.py
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs/_cm.json)
___
### Script output
#### New environment keys (filter)

* **CM_HW_***
* **CM_SUT_***
#### New environment keys auto-detected from customize

* **CM_HW_NAME**
* **CM_SUT_NAME**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)