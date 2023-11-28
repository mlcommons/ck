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
  * [ Variations](#variations)
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
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,mlperf,inference,sut,configs,sut-configs*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=get,mlperf,inference,sut,configs,sut-configs[,variations] [--input_flags]`

2. `cmr "get mlperf inference sut configs sut-configs[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

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


#### Run this script via GUI

```cmr "cm gui" --script="get,mlperf,inference,sut,configs,sut-configs"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,mlperf,inference,sut,configs,sut-configs) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get mlperf inference sut configs sut-configs[ variations]" [--input_flags]`

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

* `--configs_git_url=value`  &rarr;  `CM_GIT_URL=value`
* `--repo_path=value`  &rarr;  `CM_SUT_CONFIGS_PATH=value`
* `--run_config=value`  &rarr;  `CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "configs_git_url":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_SUT_CONFIGS_PATH: ``
* CM_GIT_URL: ``

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs/_cm.json)
  1. Run "preprocess" function from customize.py
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs/_cm.json)
</details>

___
### Script output
`cmr "get mlperf inference sut configs sut-configs[,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_HW_*`
* `CM_SUT_*`
#### New environment keys auto-detected from customize

* `CM_HW_NAME`
* `CM_SUT_NAME`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)