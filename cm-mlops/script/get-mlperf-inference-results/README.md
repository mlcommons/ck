**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-results).**



Automatically generated README for this automation recipe: **get-mlperf-inference-results**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-mlperf-inference-results,36bae5b25dbe41da) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-results)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,results,inference,inference-results,mlcommons,mlperf*
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

````cmr "get results inference inference-results mlcommons mlperf" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,results,inference,inference-results,mlcommons,mlperf`

`cm run script --tags=get,results,inference,inference-results,mlcommons,mlperf[,variations] `

*or*

`cmr "get results inference inference-results mlcommons mlperf"`

`cmr "get results inference inference-results mlcommons mlperf [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,results,inference,inference-results,mlcommons,mlperf'
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

```cmr "cm gui" --script="get,results,inference,inference-results,mlcommons,mlperf"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,results,inference,inference-results,mlcommons,mlperf) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get results inference inference-results mlcommons mlperf[variations]" `

___
### Customization


#### Variations

  * Group "**source-repo**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_ctuning`
      - Environment variables:
        - *GITHUB_REPO_OWNER*: `ctuning`
      - Workflow:
    * `_custom`
      - Environment variables:
        - *GITHUB_REPO_OWNER*: `arjunsuresh`
      - Workflow:
    * **`_mlcommons`** (default)
      - Environment variables:
        - *GITHUB_REPO_OWNER*: `mlcommons`
      - Workflow:
    * `_nvidia-only`
      - Environment variables:
        - *GITHUB_REPO_OWNER*: `GATEOverflow`
        - *NVIDIA_ONLY*: `yes`
      - Workflow:

    </details>


#### Default variations

`_mlcommons`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GIT_CHECKOUT: `master`
* CM_GIT_DEPTH: `--depth 1`
* CM_GIT_PATCH: `no`

</details>

#### Versions
Default version: `v3.1`

* `v2.1`
* `v3.0`
* `v3.1`
___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-results/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-results/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-results/_cm.json)***
     * get,git,repo
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-results/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-results/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-results/_cm.json)

___
### Script output
`cmr "get results inference inference-results mlcommons mlperf [,variations]"  -j`
#### New environment keys (filter)

* `CM_MLPERF_INFERENCE_RESULTS_*`
#### New environment keys auto-detected from customize

* `CM_MLPERF_INFERENCE_RESULTS_PATH`