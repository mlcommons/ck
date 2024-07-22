**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/reproduce-mlperf-training-nvidia).**



Automatically generated README for this automation recipe: **reproduce-mlperf-training-nvidia**

Category: **Reproduce MLPerf benchmarks**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=reproduce-mlperf-training-nvidia,f183628f292341e2) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-training-nvidia)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *reproduce,mlcommons,mlperf,train,training,nvidia-training,nvidia*
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

````cmr "reproduce mlcommons mlperf train training nvidia-training nvidia" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=reproduce,mlcommons,mlperf,train,training,nvidia-training,nvidia`

`cm run script --tags=reproduce,mlcommons,mlperf,train,training,nvidia-training,nvidia[,variations] [--input_flags]`

*or*

`cmr "reproduce mlcommons mlperf train training nvidia-training nvidia"`

`cmr "reproduce mlcommons mlperf train training nvidia-training nvidia [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,mlcommons,mlperf,train,training,nvidia-training,nvidia'
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

```cmr "cm gui" --script="reproduce,mlcommons,mlperf,train,training,nvidia-training,nvidia"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=reproduce,mlcommons,mlperf,train,training,nvidia-training,nvidia) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "reproduce mlcommons mlperf train training nvidia-training nvidia[variations]" [--input_flags]`

___
### Customization


#### Variations

  * Group "**benchmark**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_resnet`
      - Environment variables:
        - *CM_MLPERF_TRAINING_BENCHMARK*: `resnet`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * prepare,mlperf,training,resnet,_nvidia
             * CM names: `--adr.['prepare-training-data', 'nvidia-training-data']...`
             - CM script: [prepare-training-data-resnet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prepare-training-data-resnet)
           * get,nvidia,training,code
             * CM names: `--adr.['nvidia-training-code']...`
             - CM script: [get-mlperf-training-nvidia-code](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-nvidia-code)

    </details>


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--results_dir=value`  &rarr;  `CM_MLPERF_RESULTS_DIR=value`
* `--system_conf_name=value`  &rarr;  `CM_MLPERF_NVIDIA_TRAINING_SYSTEM_CONF_NAME=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "results_dir":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

#### Versions
* `r2.1`
* `r3.0`
___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-training-nvidia/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,nvidia-docker
       - CM script: [get-nvidia-docker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-nvidia-docker)
     * get,cuda
       * CM names: `--adr.['cuda']...`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-training-nvidia/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-training-nvidia/_cm.yaml)
  1. ***Run native script if exists***
     * [run-resnet.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-training-nvidia/run-resnet.sh)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-training-nvidia/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-training-nvidia/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-training-nvidia/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-training-nvidia/_cm.yaml)

___
### Script output
`cmr "reproduce mlcommons mlperf train training nvidia-training nvidia [,variations]" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize
