<details>
<summary>Click here to see the table of contents.</summary>

* [Description](#description)
* [Information](#information)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
* [Customization](#customization)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys](#new-environment-keys)
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit! See [more info](README-extra.md).*

### Description


See [more info](README-extra.md).

#### Information

* Category: *Modular MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *run,mlc,mlcommons,mlperf,power,client,power-client*
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags=run,mlc,mlcommons,mlperf,power,client,power-client(,variations from below) (flags from below)`

*or*

`cm run script "run mlc mlcommons mlperf power client power-client (variations from below)" (flags from below)`

*or*

`cm run script bf6a6d0cc97b48ae`

#### CM Python API

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,mlc,mlcommons,mlperf,power,client,power-client'
                  'out':'con',
                  ...
                  (other input keys for this script)
                  ...
                 })

if r['return']>0:
    print (r['error'])

```

</details>

#### CM modular Docker container
*TBD*
___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* --**log_dir**=value --> **CM_MLPERF_POWER_LOG_DIR**=value
* --**power_server**=value --> **CM_MLPERF_POWER_SERVER_ADDRESS**=value
* --**loadgen_logs_dir**=value --> **CM_MLPERF_LOADGEN_LOGS_DIR**=value
* --**ntp_server**=value --> **CM_MLPERF_POWER_NTP_SERVER**=value
* --**run_cmd**=value --> **CM_MLPERF_RUN_CMD**=value
* --**max_amps**=value --> **CM_MLPERF_POWER_MAX_AMPS**=value
* --**max_volts**=value --> **CM_MLPERF_POWER_MAX_VOLTS**=value

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "log_dir":"..."}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via --env.KEY=VALUE or "env" dictionary in @input.json or using script flags.

* CM_MLPERF_POWER_LOG_DIR: **logs**
* CM_MLPERF_RUN_CMD: ****
* CM_MLPERF_POWER_SERVER_ADDRESS: **localhost**
* CM_MLPERF_LOADGEN_LOGS_DIR: **loadgen_logs**
* CM_MLPERF_POWER_NTP_SERVER: **time.google.com**
* CM_MLPERF_POWER_MAX_AMPS: **0**
* CM_MLPERF_POWER_MAX_VOLTS: **0**

</details>

___
### Script workflow, dependencies and native scripts

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client/_cm.json)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlperf,power,src,_octoml
       * CM names: `--adr.['power-src']...`
       - CM script: [get-mlperf-power-dev](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-power-dev)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client/_cm.json)
___
### Script output
#### New environment keys

#### New environment keys auto-detected from customize

* **CM_MLPERF_POWER_RUN_CMD**
* **CM_MLPERF_RUN_CMD**
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)