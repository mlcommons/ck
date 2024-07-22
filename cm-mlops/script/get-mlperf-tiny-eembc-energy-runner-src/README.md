**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-mlperf-tiny-eembc-energy-runner-src).**



Automatically generated README for this automation recipe: **get-mlperf-tiny-eembc-energy-runner-src**

Category: **MLPerf benchmark support**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-mlperf-tiny-eembc-energy-runner-src,c7da8d1ce4164a4b) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-tiny-eembc-energy-runner-src)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,src,source,eembc,energyrunner,energy-runner,eembc-energy-runner,tinymlperf-energy-runner*
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

````cmr "get src source eembc energyrunner energy-runner eembc-energy-runner tinymlperf-energy-runner" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,src,source,eembc,energyrunner,energy-runner,eembc-energy-runner,tinymlperf-energy-runner`

`cm run script --tags=get,src,source,eembc,energyrunner,energy-runner,eembc-energy-runner,tinymlperf-energy-runner `

*or*

`cmr "get src source eembc energyrunner energy-runner eembc-energy-runner tinymlperf-energy-runner"`

`cmr "get src source eembc energyrunner energy-runner eembc-energy-runner tinymlperf-energy-runner " `


#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,src,source,eembc,energyrunner,energy-runner,eembc-energy-runner,tinymlperf-energy-runner'
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

```cmr "cm gui" --script="get,src,source,eembc,energyrunner,energy-runner,eembc-energy-runner,tinymlperf-energy-runner"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,src,source,eembc,energyrunner,energy-runner,eembc-energy-runner,tinymlperf-energy-runner) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get src source eembc energyrunner energy-runner eembc-energy-runner tinymlperf-energy-runner" `

___
### Customization

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_GIT_CHECKOUT: `main`
* CM_GIT_PATCH: `no`
* CM_GIT_RECURSE_SUBMODULES: ``
* CM_GIT_URL: `https://github.com/eembc/energyrunner`

</details>

___
### Dependencies on other CM scripts


  1. Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-tiny-eembc-energy-runner-src/_cm.json)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-tiny-eembc-energy-runner-src/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-tiny-eembc-energy-runner-src/_cm.json)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-tiny-eembc-energy-runner-src/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-tiny-eembc-energy-runner-src/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-tiny-eembc-energy-runner-src/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-tiny-eembc-energy-runner-src/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-tiny-eembc-energy-runner-src/_cm.json)

___
### Script output
`cmr "get src source eembc energyrunner energy-runner eembc-energy-runner tinymlperf-energy-runner "  -j`
#### New environment keys (filter)

* `+PYTHONPATH`
* `CM_EEMBC_ENERGY_RUNNER_*`
#### New environment keys auto-detected from customize

* `CM_EEMBC_ENERGY_RUNNER_DATASETS`
* `CM_EEMBC_ENERGY_RUNNER_SESSIONS`
* `CM_EEMBC_ENERGY_RUNNER_SRC`
* `CM_EEMBC_ENERGY_RUNNER_SRC_DATASETS`