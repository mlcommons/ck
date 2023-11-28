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
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Versions](#versions)
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

* Category: *Reproduce MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml [--input_flags]`

2. `cmr "run generate-tiny generate submission tiny generate-tiny-submission results mlcommons mlperf octoml" [--input_flags]`

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml'
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

```cmr "cm gui" --script="run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "run generate-tiny generate submission tiny generate-tiny-submission results mlcommons mlperf octoml" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--flash=value`  &rarr;  `CM_FLASH_BOARD=value`
* `--recreate_binary=value`  &rarr;  `CM_RECREATE_BINARY=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "flash":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
Default version: `r1.0`

* `r1.0`
___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/_cm.json)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/_cm.json)
</details>

___
### Script output
`cmr "run generate-tiny generate submission tiny generate-tiny-submission results mlcommons mlperf octoml" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)