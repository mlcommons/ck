**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/app-loadgen-generic-python).**



Automatically generated README for this automation recipe: **app-loadgen-generic-python**

Category: **Modular MLPerf inference benchmark pipeline**

License: **Apache 2.0**

Developers: [Gaz Iqbal](https://www.linkedin.com/in/gaziqbal), [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh), [Grigori Fursin](https://cKnowledge.org/gfursin)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=app-loadgen-generic-python,d3d949cc361747a6) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-loadgen-generic-python)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *python,app,generic,loadgen*
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

````cmr "python app generic loadgen" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=python,app,generic,loadgen`

`cm run script --tags=python,app,generic,loadgen[,variations] [--input_flags]`

*or*

`cmr "python app generic loadgen"`

`cmr "python app generic loadgen [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*


#### Input Flags

* --**modelpath**=Full path to file with model weights
* --**modelcodepath**=(for PyTorch models) Full path to file with model code and cmc.py
* --**modelcfgpath**=(for PyTorch models) Full path to JSON file with model cfg
* --**modelsamplepath**=(for PyTorch models) Full path to file with model sample in pickle format
* --**ep**=ONNX Execution provider
* --**scenario**=MLPerf LoadGen scenario
* --**samples**=Number of samples (*2*)
* --**runner**=MLPerf runner
* --**execmode**=MLPerf exec mode
* --**output_dir**=MLPerf output directory
* --**concurrency**=MLPerf concurrency
* --**intraop**=MLPerf intra op threads
* --**interop**=MLPerf inter op threads

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "modelpath":...}
```
#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'python,app,generic,loadgen'
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

```cmr "cm gui" --script="python,app,generic,loadgen"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=python,app,generic,loadgen) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "python app generic loadgen[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_cmc`
      - Environment variables:
        - *CM_CUSTOM_MODEL_CMC*: `True`
      - Workflow:
    * `_custom,cmc`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,ml-model,cmc
             - CM script: [get-ml-model-abtf-ssd-pytorch](https://github.com/mlcommons/cm4abtf/tree/master/script/get-ml-model-abtf-ssd-pytorch)
    * `_custom,huggingface`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,ml-model,huggingface
             * CM names: `--adr.['hf-downloader']...`
             - CM script: [get-ml-model-huggingface-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-huggingface-zoo)
    * `_huggingface`
      - Environment variables:
        - *CM_CUSTOM_MODEL_SOURCE*: `huggingface`
      - Workflow:
    * `_model-stub.#`
      - Environment variables:
        - *CM_ML_MODEL_STUB*: `#`
      - Workflow:

    </details>


  * Group "**backend**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_onnxruntime`** (default)
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `onnxruntime`
      - Workflow:
    * `_pytorch`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `pytorch`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cpu`
        - *CM_MLPERF_EXECUTION_PROVIDER*: `CPUExecutionProvider`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `gpu`
        - *CM_MLPERF_EXECUTION_PROVIDER*: `CUDAExecutionProvider`
      - Workflow:

    </details>


  * Group "**models**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_custom`
      - Environment variables:
        - *CM_MODEL*: `custom`
      - Workflow:
    * `_resnet50`
      - Environment variables:
        - *CM_MODEL*: `resnet50`
      - Workflow:
    * `_retinanet`
      - Environment variables:
        - *CM_MODEL*: `retinanet`
      - Workflow:

    </details>


#### Default variations

`_cpu,_onnxruntime`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--concurrency=value`  &rarr;  `CM_MLPERF_CONCURRENCY=value`
* `--ep=value`  &rarr;  `CM_MLPERF_EXECUTION_PROVIDER=value`
* `--execmode=value`  &rarr;  `CM_MLPERF_EXEC_MODE=value`
* `--interop=value`  &rarr;  `CM_MLPERF_INTEROP=value`
* `--intraop=value`  &rarr;  `CM_MLPERF_INTRAOP=value`
* `--loadgen_duration_sec=value`  &rarr;  `CM_MLPERF_LOADGEN_DURATION_SEC=value`
* `--loadgen_expected_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_EXPECTED_QPS=value`
* `--modelcfg=value`  &rarr;  `CM_ML_MODEL_CFG=value`
* `--modelcfgpath=value`  &rarr;  `CM_ML_MODEL_CFG_WITH_PATH=value`
* `--modelcodepath=value`  &rarr;  `CM_ML_MODEL_CODE_WITH_PATH=value`
* `--modelpath=value`  &rarr;  `CM_ML_MODEL_FILE_WITH_PATH=value`
* `--modelsamplepath=value`  &rarr;  `CM_ML_MODEL_SAMPLE_WITH_PATH=value`
* `--output_dir=value`  &rarr;  `CM_MLPERF_OUTPUT_DIR=value`
* `--runner=value`  &rarr;  `CM_MLPERF_RUNNER=value`
* `--samples=value`  &rarr;  `CM_MLPERF_LOADGEN_SAMPLES=value`
* `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "concurrency":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MLPERF_EXECUTION_MODE: `parallel`
* CM_MLPERF_BACKEND: `onnxruntime`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-loadgen-generic-python/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,generic-python-lib,_psutil
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_package.numpy
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,cuda
       * `if (CM_MLPERF_DEVICE  == gpu)`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
     * get,loadgen
       * CM names: `--adr.['loadgen']...`
       - CM script: [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)
     * get,generic-python-lib,_onnxruntime
       * `if (CM_MLPERF_BACKEND  == onnxruntime AND CM_MLPERF_DEVICE  == cpu)`
       * CM names: `--adr.['onnxruntime']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_onnxruntime_gpu
       * `if (CM_MLPERF_BACKEND  == onnxruntime AND CM_MLPERF_DEVICE  == gpu)`
       * CM names: `--adr.['onnxruntime']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_onnx
       * `if (CM_MLPERF_BACKEND  == onnxruntime)`
       * CM names: `--adr.['onnx']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torch
       * `if (CM_MLPERF_BACKEND  == pytorch AND CM_MLPERF_DEVICE  == cpu)`
       * CM names: `--adr.['torch']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torchvision
       * `if (CM_MLPERF_BACKEND  == pytorch AND CM_MLPERF_DEVICE  == cpu)`
       * CM names: `--adr.['torchvision']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torch_cuda
       * `if (CM_MLPERF_BACKEND  == pytorch AND CM_MLPERF_DEVICE  == gpu)`
       * CM names: `--adr.['torch']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torchvision_cuda
       * `if (CM_MLPERF_BACKEND  == pytorch AND CM_MLPERF_DEVICE  == gpu)`
       * CM names: `--adr.['torchvision']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,ml-model,resnet50,_onnx
       * `if (CM_MODEL  == resnet50)`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * get,ml-model,retinanet,_onnx,_fp32
       * `if (CM_MODEL  == retinanet)`
       - CM script: [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
     * get,ml-model,retinanet,_onnx,_fp32
       * `if (CM_MODEL  == retinanet)`
       - CM script: [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-loadgen-generic-python/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-loadgen-generic-python/_cm.yaml)
  1. ***Run native script if exists***
     * [run.bat](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-loadgen-generic-python/run.bat)
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-loadgen-generic-python/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-loadgen-generic-python/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-loadgen-generic-python/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-loadgen-generic-python/_cm.yaml)

___
### Script output
`cmr "python app generic loadgen [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_MLPERF_*`
#### New environment keys auto-detected from customize
