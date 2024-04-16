**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-inference-sut-description).**



Automatically generated README for this automation recipe: **get-mlperf-inference-sut-description**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-mlperf-inference-sut-description,e49a3f758b2d4e7b) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-description)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,mlperf,sut,description,system-under-test,system-description*
* Output cached? *True*
* See [pipeline of dependencies](#dependencies-on-other-cm-scripts) on other CM scripts


---
### Reuse this script in your project

#### Install MLCommons CM automation meta-framework

* [Install CM](https://access.cknowledge.org/playground/?action=install)
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)

#### Pull CM repository with this automation recipe (CM script)

```cm pull repo mlcommons@ck```

#### Print CM help from the command line

````cmr "get mlperf sut description system-under-test system-description" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,mlperf,sut,description,system-under-test,system-description`

`cm run script --tags=get,mlperf,sut,description,system-under-test,system-description [--input_flags]`

*or*

`cmr "get mlperf sut description system-under-test system-description"`

`cmr "get mlperf sut description system-under-test system-description " [--input_flags]`


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,mlperf,sut,description,system-under-test,system-description'
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

```cmr "cm gui" --script="get,mlperf,sut,description,system-under-test,system-description"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,mlperf,sut,description,system-under-test,system-description) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get mlperf sut description system-under-test system-description" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--name=value`  &rarr;  `CM_HW_NAME=value`
* `--submitter=value`  &rarr;  `CM_MLPERF_SUBMITTER=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "name":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_SUT_DESC_CACHE: `no`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-description/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,python3
       * CM names: `--adr.['python3', 'python']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,compiler
       * CM names: `--adr.['compiler']...`
       - CM script: [get-cl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl)
       - CM script: [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)
       - CM script: [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)
     * get,cuda-devices
       * `if (CM_MLPERF_DEVICE in ['gpu', 'cuda'])`
       - CM script: [get-cuda-devices](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-devices)
     * detect,sudo
       * `if (CM_DETERMINE_MEMORY_CONFIGURATION  == yes AND CM_HOST_OS_TYPE  == linux)`
       - CM script: [detect-sudo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-sudo)
     * get,generic-python-lib,_package.dmiparser
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-description/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-description/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-description/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-description/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-description/_cm.json)

___
### Script output
`cmr "get mlperf sut description system-under-test system-description " [--input_flags] -j`
#### New environment keys (filter)

* `CM_HW_*`
* `CM_SUT_*`
#### New environment keys auto-detected from customize

* `CM_HW_NAME`