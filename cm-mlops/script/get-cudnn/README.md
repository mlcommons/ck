**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/get-cudnn).**



Automatically generated README for this automation recipe: **get-cudnn**

Category: **CUDA automation**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=get-cudnn,d73ee19baee14df8) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cudnn)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* All CM tags to find and reuse this script (see in above meta description): *get,cudnn,nvidia*
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

````cmr "get cudnn nvidia" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=get,cudnn,nvidia`

`cm run script --tags=get,cudnn,nvidia [--input_flags]`

*or*

`cmr "get cudnn nvidia"`

`cmr "get cudnn nvidia " [--input_flags]`



#### Input Flags

* --**input**=Full path to the installed cuDNN library
* --**tar_file**=Full path to the cuDNN Tar file downloaded from Nvidia website (https://developer.nvidia.com/cudnn)

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "input":...}
```
#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'get,cudnn,nvidia'
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

```cmr "cm gui" --script="get,cudnn,nvidia"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=get,cudnn,nvidia) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "get cudnn nvidia" [--input_flags]`

___
### Customization


#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--input=value`  &rarr;  `CM_INPUT=value`
* `--tar_file=value`  &rarr;  `CM_CUDNN_TAR_FILE_PATH=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "input":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_SUDO: `sudo`
* CM_INPUT: ``

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cudnn/_cm.json)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,cuda
       * `if (CM_CUDA_PATH_LIB  != on OR CM_CUDA_PATH_INCLUDE  != on)`
       * CM names: `--adr.['cuda']...`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cudnn/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cudnn/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cudnn/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cudnn/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cudnn/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cudnn/_cm.json)

___
### Script output
`cmr "get cudnn nvidia " [--input_flags] -j`
#### New environment keys (filter)

* `+CPLUS_INCLUDE_PATH`
* `+C_INCLUDE_PATH`
* `+DYLD_FALLBACK_LIBRARY_PATH`
* `+LD_LIBRARY_PATH`
* `+PATH`
* `CM_CUDA_PATH_INCLUDE_CUDNN`
* `CM_CUDA_PATH_LIB_CUDNN`
* `CM_CUDA_PATH_LIB_CUDNN_EXISTS`
* `CM_CUDNN_*`
#### New environment keys auto-detected from customize

* `CM_CUDA_PATH_INCLUDE_CUDNN`
* `CM_CUDA_PATH_LIB_CUDNN`
* `CM_CUDA_PATH_LIB_CUDNN_EXISTS`
* `CM_CUDNN_VERSION`