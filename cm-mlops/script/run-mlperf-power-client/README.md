*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Default environment](#default-environment)
* [CM script workflow](#cm-script-workflow)
* [New environment export](#new-environment-export)
* [New environment detected from customize](#new-environment-detected-from-customize)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
  * [ Script input flags mapped to environment](#script-input-flags-mapped-to-environment)
* [Maintainers](#maintainers)

</details>

___
### About

*TBD*
___
### Category

Modular MLPerf benchmarks.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
run,mlc,mlcommons,mlperf,power,client,power-client

___
### Default environment

* CM_MLPERF_POWER_LOG_DIR: **logs**
* CM_MLPERF_RUN_CMD: ****
* CM_MLPERF_POWER_SERVER_ADDRESS: **localhost**
* CM_MLPERF_LOADGEN_LOGS_DIR: **loadgen_logs**
* CM_MLPERF_POWER_NTP_SERVER: **time.google.com**
* CM_MLPERF_POWER_MAX_AMPS: **0**
* CM_MLPERF_POWER_MAX_VOLTS: **0**
___
### CM script workflow

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
### New environment export

___
### New environment detected from customize

* **CM_MLPERF_POWER_RUN_CMD**
* **CM_MLPERF_RUN_CMD**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="run,mlc,mlcommons,mlperf,power,client,power-client"`

*or*

`cm run script "run mlc mlcommons mlperf power client power-client"`

*or*

`cm run script bf6a6d0cc97b48ae`

#### CM Python API

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

#### CM modular Docker container
*TBD*

#### Script input flags mapped to environment

* log_dir --> **CM_MLPERF_POWER_LOG_DIR**
* power_server --> **CM_MLPERF_POWER_SERVER_ADDRESS**
* loadgen_logs_dir --> **CM_MLPERF_LOADGEN_LOGS_DIR**
* ntp_server --> **CM_MLPERF_POWER_NTP_SERVER**
* run_cmd --> **CM_MLPERF_RUN_CMD**
* max_amps --> **CM_MLPERF_POWER_MAX_AMPS**
* max_volts --> **CM_MLPERF_POWER_MAX_VOLTS**

Examples:

```bash
cm run script "run mlc mlcommons mlperf power client power-client" --log_dir=...
```
```python
r=cm.access({... , "log_dir":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)