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
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-mlperf-inference-retinanet-win)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *test,mlperf-inference-win,retinanet,windows*
* Output cached?: *False*
___
### Usage

#### CM installation

[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

##### CM pull repository

```cm pull repo mlcommons@ck```

##### CM script automation help

```cm run script --help```

#### CM CLI

1. `cm run script --tags=test,mlperf-inference-win,retinanet,windows `

2. `cm run script "test mlperf-inference-win retinanet windows" `

3. `cm run script 1cedbc3b642a403a `

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'test,mlperf-inference-win,retinanet,windows'
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

```cm run script --tags=gui --script="test,mlperf-inference-win,retinanet,windows"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=test,mlperf-inference-win,retinanet,windows) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-mlperf-inference-retinanet-win/_cm.json)***
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-python-lib,_requests
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,loadgen
       * CM names: `--adr.['loadgen', 'mlperf-inference-loadgen']...`
       - CM script: [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)
     * mlperf,inference,source
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,dataset,open-images,original
       - CM script: [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
     * get,raw,ml-model,retinanet
       - CM script: [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-mlperf-inference-retinanet-win/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-mlperf-inference-retinanet-win/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-mlperf-inference-retinanet-win/run.bat)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-mlperf-inference-retinanet-win/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-mlperf-inference-retinanet-win/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-mlperf-inference-retinanet-win/_cm.json)
</details>

___
### Script output
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)