**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/run-mlperf-power-server).**



Automatically generated README for this automation recipe: **run-mlperf-power-server**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=run-mlperf-power-server,5bc68aaf389a40bd) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-server)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *run,mlc,mlcommons,mlperf,power,server,power-server*
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

````cmr "run mlc mlcommons mlperf power server power-server" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=run,mlc,mlcommons,mlperf,power,server,power-server`

`cm run script --tags=run,mlc,mlcommons,mlperf,power,server,power-server [--input_flags]`

*or*

`cmr "run mlc mlcommons mlperf power server power-server"`

`cmr "run mlc mlcommons mlperf power server power-server " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

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

</details>


#### Run this script via GUI

```cmr "cm gui" --script="run,mlc,mlcommons,mlperf,power,server,power-server"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=run,mlc,mlcommons,mlperf,power,server,power-server) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "run mlc mlcommons mlperf power server power-server" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--device_port=value`  &rarr;  `CM_MLPERF_POWER_DEVICE_PORT=value`
* `--device_type=value`  &rarr;  `CM_MLPERF_POWER_DEVICE_TYPE=value`
* `--interface_flag=value`  &rarr;  `CM_MLPERF_POWER_INTERFACE_FLAG=value`
* `--ntp_server=value`  &rarr;  `CM_MLPERF_POWER_NTP_SERVER=value`
* `--screen=value`  &rarr;  `CM_MLPERF_POWER_SERVER_USE_SCREEN=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "device_port":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MLPERF_POWER_NTP_SERVER: `time.google.com`
* CM_MLPERF_POWER_INTERFACE_FLAG: ``
* CM_MLPERF_POWER_DEVICE_TYPE: `49`
* CM_MLPERF_POWER_SERVER_ADDRESS: `0.0.0.0`
* CM_MLPERF_POWER_SERVER_PORT: `4950`
* CM_MLPERF_POWER_DEVICE_PORT: `/dev/usbtmc0`
* CM_MLPERF_POWER_SERVER_USE_SCREEN: `no`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-server/_cm.json)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,mlperf,power,src
       * CM names: `--adr.['power-src']...`
       - CM script: [get-mlperf-power-dev](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-power-dev)
     * get,mlperf,power,daemon
       * CM names: `--adr.['power-damenon']...`
       - CM script: [get-spec-ptd](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-spec-ptd)
     * get,generic,sys-util,_screen
       * `if (CM_HOST_OS_TYPE not in windows)`
       * CM names: `--adr.['screen']...`
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,generic-python-lib,_package.pypiwin32
       * `if (CM_HOST_OS_TYPE in windows)`
       * CM names: `--adr.['win32']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-server/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-server/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-server/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-server/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-server/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-server/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-server/_cm.json)

___
### Script output
`cmr "run mlc mlcommons mlperf power server power-server " [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
