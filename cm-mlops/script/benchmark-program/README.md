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

* Category: *Application automation.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *program,benchmark,benchmark-program*
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

1. `cm run script --tags=program,benchmark,benchmark-program[,variations] `

2. `cm run script "program benchmark benchmark-program[,variations]" `

3. `cm run script 19f369ef47084895 `

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'program,benchmark,benchmark-program'
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

```cm run script --tags=gui --script="program,benchmark,benchmark-program"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=program,benchmark,benchmark-program) to generate CM CMD.

#### CM modular Docker container

*TBD*

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_numactl`
      - Workflow:
    * `_numactl-interleave`
      - Workflow:
    * `_profile`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,profiler
             - *Warning: no scripts found*

    </details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_ENABLE_NUMACTL: `0`
* CM_ENABLE_PROFILING: `0`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program/_cm.json)***
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * set,performance,mode,_performance
       * `if (CM_SET_PERFORMANCE_MODE in ['on', 'yes', 'True', True])`
       - CM script: [set-performance-mode](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-performance-mode)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program/_cm.json)
  1. ***Run native script if exists***
     * [run-ubuntu.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program/run-ubuntu.sh)
     * [run.bat](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program/_cm.json)
</details>

___
### Script output
#### New environment keys (filter)

* `CM_RUN_CMD`
#### New environment keys auto-detected from customize

* `CM_RUN_CMD`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)