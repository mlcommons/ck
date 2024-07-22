**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-power-client).**



Automatically generated README for this automation recipe: **run-mlperf-power-client**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=run-mlperf-power-client,bf6a6d0cc97b48ae) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-client)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *run,mlc,mlcommons,mlperf,power,client,power-client*
* Output cached? *False*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "run mlc mlcommons mlperf power client power-client" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=run,mlc,mlcommons,mlperf,power,client,power-client`

`cm run script --tags=run,mlc,mlcommons,mlperf,power,client,power-client [--input_flags]`

*or*

`cmr "run mlc mlcommons mlperf power client power-client"`

`cmr "run mlc mlcommons mlperf power client power-client " [--input_flags]`


#### Run this script from Python

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


#### Run this script via GUI

```cmr "cm gui" --script="run,mlc,mlcommons,mlperf,power,client,power-client"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,mlc,mlcommons,mlperf,power,client,power-client) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "run mlc mlcommons mlperf power client power-client" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--loadgen_logs_dir=value`  &rarr;  `CM_MLPERF_LOADGEN_LOGS_DIR=value`
* `--log_dir=value`  &rarr;  `CM_MLPERF_POWER_LOG_DIR=value`
* `--max_amps=value`  &rarr;  `CM_MLPERF_POWER_MAX_AMPS=value`
* `--max_volts=value`  &rarr;  `CM_MLPERF_POWER_MAX_VOLTS=value`
* `--ntp_server=value`  &rarr;  `CM_MLPERF_POWER_NTP_SERVER=value`
* `--port=value`  &rarr;  `CM_MLPERF_POWER_SERVER_PORT=value`
* `--power_server=value`  &rarr;  `CM_MLPERF_POWER_SERVER_ADDRESS=value`
* `--run_cmd=value`  &rarr;  `CM_MLPERF_RUN_CMD=value`
* `--server=value`  &rarr;  `CM_MLPERF_POWER_SERVER_ADDRESS=value`
* `--server_port=value`  &rarr;  `CM_MLPERF_POWER_SERVER_PORT=value`
* `--timestamp=value`  &rarr;  `CM_MLPERF_POWER_TIMESTAMP=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "loadgen_logs_dir":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MLPERF_POWER_LOG_DIR: `logs`
* CM_MLPERF_RUN_CMD: ``
* CM_MLPERF_POWER_SERVER_ADDRESS: `localhost`
* CM_MLPERF_POWER_NTP_SERVER: `time.google.com`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-client/_cm.json)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlperf,power,src
       * CM names: `--adr.['power-src']...`
       - CM script: [get-mlperf-power-dev](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-power-dev)
     * get,generic-sys-util,_ntpdate
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-client/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-client/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-client/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-client/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-client/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-client/_cm.json)

___
### Script output
`cmr "run mlc mlcommons mlperf power client power-client " [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
