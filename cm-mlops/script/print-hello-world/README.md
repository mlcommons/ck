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
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About

#### Summary

* Category: *Tests.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *print,hello-world,hello world,hello,world,native-script,native,script*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=print,hello-world,hello world,hello,world,native-script,native,script [--input_flags]`

2. `cmr "print hello-world hello world hello world native-script native script" [--input_flags]`

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'print,hello-world,hello world,hello,world,native-script,native,script'
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

```cmr "cm gui" --script="print,hello-world,hello world,hello,world,native-script,native,script"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=print,hello-world,hello world,hello,world,native-script,native,script) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "print hello-world hello world hello world native-script native script" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--test1=value`  &rarr;  `CM_ENV_TEST1=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "test1":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_ENV_TEST1: `TEST1`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world/_cm.json)
  1. Run "preprocess" function from customize.py
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world/_cm.json)
  1. Run "postrocess" function from customize.py
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world/_cm.json)
</details>

___
### Script output
`cmr "print hello-world hello world hello world native-script native script" [--input_flags] -j`
#### New environment keys (filter)

* `CM_ENV_TEST*`
#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)