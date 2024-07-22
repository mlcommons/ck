**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-training-nvidia).**



Automatically generated README for this automation recipe: **app-mlperf-training-nvidia**

Category: **Modular MLPerf training benchmark pipeline**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=app-mlperf-training-nvidia,1e2e357618cc4674) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-training-nvidia)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *app,vision,language,mlcommons,mlperf,training,nvidia*
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

````cmr "app vision language mlcommons mlperf training nvidia" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=app,vision,language,mlcommons,mlperf,training,nvidia`

`cm run script --tags=app,vision,language,mlcommons,mlperf,training,nvidia[,variations] [--input_flags]`

*or*

`cmr "app vision language mlcommons mlperf training nvidia"`

`cmr "app vision language mlcommons mlperf training nvidia [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,vision,language,mlcommons,mlperf,training,nvidia'
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

```cmr "cm gui" --script="app,vision,language,mlcommons,mlperf,training,nvidia"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=app,vision,language,mlcommons,mlperf,training,nvidia) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "app vision language mlcommons mlperf training nvidia[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert`
      - Environment variables:
        - *CM_MLPERF_MODEL*: `bert`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_protobuf
             * `if (CM_MLPERF_BACKEND in ['tf', 'tflite'])`
             * CM names: `--adr.['protobuf']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torch
             * CM names: `--adr.['ml-engine-pytorch']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cuda`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cuda`
        - *USE_CUDA*: `True`
      - Workflow:
    * `_tpu`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `tpu`
        - *CUDA_VISIBLE_DEVICES*: ``
        - *USE_CUDA*: `False`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_pytorch`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `pytorch`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TORCH_VERSION>>>`
      - Workflow:
    * `_tf`
      - Aliases: `_tensorflow`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tf`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TENSORFLOW_VERSION>>>`
      - Workflow:

    </details>


#### Default variations

`_cuda`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--clean=value`  &rarr;  `CM_MLPERF_CLEAN_SUBMISSION_DIR=value`
* `--docker=value`  &rarr;  `CM_RUN_DOCKER_CONTAINER=value`
* `--hw_name=value`  &rarr;  `CM_HW_NAME=value`
* `--model=value`  &rarr;  `CM_MLPERF_CUSTOM_MODEL_PATH=value`
* `--num_threads=value`  &rarr;  `CM_NUM_THREADS=value`
* `--output_dir=value`  &rarr;  `OUTPUT_BASE_DIR=value`
* `--rerun=value`  &rarr;  `CM_RERUN=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "clean":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `nvidia`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-training-nvidia/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,python
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlperf,training,src
       * CM names: `--adr.['training-src', 'mlperf-training-src']...`
       - CM script: [get-mlperf-training-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-src)
     * get,git,repo,_repo.https://github.com/mlcommons/training_results_v2.1
       * CM names: `--adr.['training-results', 'mlperf-training-results']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
     * get,cuda
       * `if (CM_MLPERF_DEVICE  == cuda)`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
     * get,generic-python-lib,_torchvision_cuda
       * `if (CM_MLPERF_BACKEND  == pytorch AND CM_MLPERF_DEVICE  == cuda)`
       * CM names: `--adr.['ml-engine-torchvision']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_mlperf_logging
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * prepare,mlperf,training,data,bert,_nvidia
       * `if (CM_MLPERF_MODEL  == bert)`
       * CM names: `--adr.['prepare-data', 'bert-model']...`
       - CM script: [prepare-training-data-bert](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prepare-training-data-bert)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-training-nvidia/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-training-nvidia/_cm.yaml)
  1. ***Run native script if exists***
     * [run-bert-training.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-training-nvidia/run-bert-training.sh)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-training-nvidia/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-training-nvidia/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-training-nvidia/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-training-nvidia/_cm.yaml)

___
### Script output
`cmr "app vision language mlcommons mlperf training nvidia [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_DATASET_*`
* `CM_HW_NAME`
* `CM_MLPERF_*`
* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize
