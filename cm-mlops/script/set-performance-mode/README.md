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
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About

#### Summary

* Category: *DevOps automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-performance-mode)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *set,system,performance,power,mode*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=set,system,performance,power,mode[,variations] `

2. `cmr "set system performance power mode[ variations]" `

* `variations` can be seen [here](#variations)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'set,system,performance,power,mode'
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

```cmr "cm gui" --script="set,system,performance,power,mode"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=set,system,performance,power,mode) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "set system performance power mode[ variations]" `

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_reproducibility`
      - Environment variables:
        - *CM_SET_OS_PERFORMANCE_REPRODUCIBILITY_MODE*: `yes`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_SET_PERFORMANCE_MODE_OF*: `cpu`
      - Workflow:

    </details>


  * Group "**performance-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_performance`** (default)
      - Environment variables:
        - *CM_SET_PERFORMANCE_MODE*: `performance`
      - Workflow:

    </details>


  * Group "**power**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_power`
      - Environment variables:
        - *CM_SET_PERFORMANCE_MODE*: `power`
      - Workflow:

    </details>


#### Default variations

`_cpu,_performance`
#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-performance-mode/_cm.json)***
     * detect-os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect-cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-performance-mode/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-performance-mode/_cm.json)
  1. ***Run native script if exists***
     * [run-ubuntu.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-performance-mode/run-ubuntu.sh)
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-performance-mode/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-performance-mode/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-performance-mode/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-performance-mode/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-performance-mode/_cm.json)
</details>

___
### Script output
`cmr "set system performance power mode[,variations]"  -j`
#### New environment keys (filter)

* `OMP_*`
#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)