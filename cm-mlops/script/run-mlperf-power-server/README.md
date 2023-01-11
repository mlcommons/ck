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
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
run,mlc,mlcommons,mlperf,power,server,power-server

___
### Default environment

* CM_MLPERF_POWER_NTP_SERVER: **time.google.com**
* CM_MLPERF_POWER_INTERFACE_FLAG: ****
* CM_MLPERF_POWER_DEVICE_TYPE: **49**
* CM_MLPERF_POWER_SERVER_ADDRESS: **0.0.0.0**
* CM_MLPERF_POWER_SERVER_PORT: **4950**
* CM_MLPERF_POWER_DEVICE_PORT: **/dev/usbtmc0**
___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server/_cm.json)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlperf,power,src
       * CM names: `--adr.['power-src']...`
       - CM script: [get-mlperf-power-dev](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-power-dev)
     * get,mlperf,power,daemon
       * CM names: `--adr.['power-damenon']...`
       - CM script: [get-spec-ptd](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-spec-ptd)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server/_cm.json)
___
### New environment export

___
### New environment detected from customize

___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="run,mlc,mlcommons,mlperf,power,server,power-server"`

*or*

`cm run script "run mlc mlcommons mlperf power server power-server"`

*or*

`cm run script 5bc68aaf389a40bd`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'run,mlc,mlcommons,mlperf,power,server,power-server'
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

* interface_flag --> **CM_MLPERF_POWER_INTERFACE_FLAG**
* device_port --> **CM_MLPERF_POWER_DEVICE_PORT**
* device_type --> **CM_MLPERF_POWER_DEVICE_TYPE**
* ntp_server --> **CM_MLPERF_POWER_NTP_SERVER**

Examples:

```bash
cm run script "run mlc mlcommons mlperf power server power-server" --interface_flag=...
```
```python
r=cm.access({... , "interface_flag":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)