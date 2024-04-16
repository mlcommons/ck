**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-training-nvidia-code).**



Automatically generated README for this automation recipe: **get-mlperf-training-nvidia-code**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-mlperf-training-nvidia-code,fdc630b1d41743c5) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-nvidia-code)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,nvidia,mlperf,training,code,training-code*
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

````cmr "get nvidia mlperf training code training-code" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,nvidia,mlperf,training,code,training-code`

`cm run script --tags=get,nvidia,mlperf,training,code,training-code[,variations] `

*or*

`cmr "get nvidia mlperf training code training-code"`

`cmr "get nvidia mlperf training code training-code [variations]" `


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,nvidia,mlperf,training,code,training-code'
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

```cmr "cm gui" --script="get,nvidia,mlperf,training,code,training-code"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,nvidia,mlperf,training,code,training-code) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get nvidia mlperf training code training-code[variations]" `

___
### Customization


#### Variations

  * Group "**repo-owner**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_ctuning`
      - Environment variables:
        - *CM_TMP_TRAINING_SRC*: `ctuning`
      - Workflow:
    * `_custom`
      - Workflow:
    * **`_mlcommons`** (default)
      - Environment variables:
        - *CM_TMP_TRAINING_SRC*: `mlcommons`
      - Workflow:
    * `_nvidia-only`
      - Environment variables:
        - *CM_TMP_TRAINING_SRC*: `GATEOverflow`
      - Workflow:

    </details>


#### Default variations

`_mlcommons`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `r3.0`

* `r2.1`
* `r3.0`
* `r3.1`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-nvidia-code/_cm.json)***
     * get,git,repo
       * CM names: `--adr.['mlperf-training-results']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-nvidia-code/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-nvidia-code/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-nvidia-code/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-nvidia-code/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-nvidia-code/_cm.json)

___
### Script output
`cmr "get nvidia mlperf training code training-code [,variations]"  -j`
#### New environment keys (filter)

* `CM_MLPERF_TRAINING_NVIDIA_CODE_PATH`
#### New environment keys auto-detected from customize

* `CM_MLPERF_TRAINING_NVIDIA_CODE_PATH`