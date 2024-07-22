**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-sut-configs).**



Automatically generated README for this automation recipe: **get-mlperf-inference-sut-configs**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-mlperf-inference-sut-configs,c2fbf72009e2445b) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-configs)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,mlperf,inference,sut,configs,sut-configs*
* Output cached? *True*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "get mlperf inference sut configs sut-configs" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,mlperf,inference,sut,configs,sut-configs`

`cm run script --tags=get,mlperf,inference,sut,configs,sut-configs[,variations] [--input_flags]`

*or*

`cmr "get mlperf inference sut configs sut-configs"`

`cmr "get mlperf inference sut configs sut-configs [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

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

`cm docker script "get mlperf inference sut configs sut-configs[variations]" [--input_flags]`

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
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-configs/_cm.json)
  1. Run "preprocess" function from customize.py
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-configs/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-configs/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-configs/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-configs/_cm.json)

___
### Script output
`cmr "get mlperf inference sut configs sut-configs [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_HW_*`
* `CM_SUT_*`
#### New environment keys auto-detected from customize

* `CM_HW_NAME`
* `CM_SUT_NAME`