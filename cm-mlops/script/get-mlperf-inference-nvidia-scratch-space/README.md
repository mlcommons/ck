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

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-scratch-space)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *get,mlperf,inference,nvidia,scratch,space*
* Output cached?: *True*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

##### CM pull repository

```cm pull repo mlcommons@ck```

##### CM script automation help

```cm run script --help```

#### CM CLI

1. `cm run script --tags=get,mlperf,inference,nvidia,scratch,space [--input_flags]`

2. `cm run script "get mlperf inference nvidia scratch space" [--input_flags]`

3. `cm run script 0b2bec8b29fb4ab7 [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,mlperf,inference,nvidia,scratch,space'
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

```cm run script --tags=gui --script="get,mlperf,inference,nvidia,scratch,space"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,mlperf,inference,nvidia,scratch,space) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--scratch_path=value`  &rarr;  `MLPERF_SCRATCH_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "scratch_path":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-scratch-space/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-scratch-space/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-scratch-space/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-scratch-space/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-scratch-space/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-scratch-space/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-scratch-space/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-scratch-space/_cm.json)
</details>

___
### Script output
#### New environment keys (filter)

* `CM_NVIDIA_MLPERF_SCRATCH_PATH`
* `MLPERF_SCRATCH_PATH`
#### New environment keys auto-detected from customize

* `CM_NVIDIA_MLPERF_SCRATCH_PATH`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)