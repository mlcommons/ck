<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Summary](#summary)
* [Reuse this script in your project](#reuse-this-script-in-your-project)
  * [ Install CM automation language](#install-cm-automation-language)
  * [ Check CM script flags](#check-cm-script-flags)
  * [ Run this script from command line](#run-this-script-from-command-line)
  * [ Run this script from Python](#run-this-script-from-python)
  * [ Run this script via GUI](#run-this-script-via-gui)
  * [ Run this script via Docker (beta)](#run-this-script-via-docker-(beta))
* [Customization](#customization)
  * [ Variations](#variations)
  * [ Script flags mapped to environment](#script-flags-mapped-to-environment)
  * [ Default environment](#default-environment)
* [Script workflow, dependencies and native scripts](#script-workflow-dependencies-and-native-scripts)
* [Script output](#script-output)
* [New environment keys (filter)](#new-environment-keys-(filter))
* [New environment keys auto-detected from customize](#new-environment-keys-auto-detected-from-customize)
* [Maintainers](#maintainers)

</details>

*Note that this README is automatically generated - don't edit!*

### About

#### Summary

* Category: *AI/ML optimization.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-model-for.qaic)*
* CM meta description for this script: *[_cm.json](_cm.json)*
* CM "database" tags to find this script: *qaic,compile,model,model-compile,qaic-compile*
* Output cached? *True*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=qaic,compile,model,model-compile,qaic-compile[,variations] [--input_flags]`

2. `cmr "qaic compile model model-compile qaic-compile[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'qaic,compile,model,model-compile,qaic-compile'
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

```cmr "cm gui" --script="qaic,compile,model,model-compile,qaic-compile"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=qaic,compile,model,model-compile,qaic-compile) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "qaic compile model model-compile qaic-compile[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert-99`
      - Environment variables:
        - *CM_COMPILE_BERT*: `on`
        - *CM_QAIC_MODEL_TO_CONVERT*: `calibrate_bert_mlperf`
        - *CM_QAIC_MODEL_COMPILER_PARAMS_BASE*: `-aic-hw -aic-hw-version=2.0 -execute-nodes-in-fp16=Mul,Sqrt,Div,Add,ReduceMean,Softmax,Sub,Gather,Erf,Pow,Concat,Tile,LayerNormalization -quantization-schema=symmetric_with_uint8 -quantization-precision=Int8 -quantization-precision-bias=Int32 -vvv -compile-only -onnx-define-symbol=batch_size,1 -onnx-define-symbol=seg_length,384 -multicast-weights -combine-inputs=false -combine-outputs=false`
        - *CM_QAIC_MODEL_COMPILER_ARGS*: ``
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * calibrate,qaic,_bert-99
             * CM names: `--adr.['bert-profile', 'qaic-profile']...`
             - CM script: [calibrate-model-for.qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/calibrate-model-for.qaic)
    * `_bert-99,offline`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS*: `-allocator-dealloc-delay=2 -size-split-granularity=1536 -vtcm-working-set-limit-ratio=1`
        - *CM_QAIC_MODEL_COMPILER_ARGS_SUT*: `-aic-num-cores=1 -mos=1 -ols=3`
      - Workflow:
    * `_bert-99,offline,nsp.14`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS_SUT*: `-aic-num-cores=1 -mos=1 -ols=3`
      - Workflow:
    * `_bert-99,server`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS*: `-allocator-dealloc-delay=2 -size-split-granularity=1536 -vtcm-working-set-limit-ratio=1`
        - *CM_QAIC_MODEL_COMPILER_ARGS_SUT*: `-aic-num-cores=1 -mos=1 -ols=3`
      - Workflow:
    * `_bert-99,server,nsp.14`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS_SUT*: `-aic-num-cores=1 -mos=1 -ols=3`
      - Workflow:
    * `_bert-99,singlestream`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS*: ``
        - *CM_QAIC_MODEL_COMPILER_ARGS_SUT*: `-aic-num-cores=8 -mos=8 -ols=1`
      - Workflow:
    * `_bert-99,singlestream,nsp.14`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS_SUT*: `-aic-num-cores=8 -mos=8 -ols=1`
      - Workflow:
    * `_resnet50`
      - Environment variables:
        - *CM_COMPILE_RESNET*: `on`
        - *CM_QAIC_MODEL_TO_CONVERT*: `compile_resnet50_tf`
        - *CM_QAIC_MODEL_COMPILER_PARAMS_BASE*: `-aic-hw -aic-hw-version=2.0 -quantization-schema=symmetric_with_uint8 -quantization-precision=Int8 -output-node-name=ArgMax -vvv -compile-only -use-producer-dma=1`
      - Workflow:
    * `_resnet50,multistream`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS*: `-sdp-cluster-sizes=4,4 -mos=1,4`
      - Workflow:
    * `_resnet50,multistream,nsp.14`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS_SUT*: `-aic-num-cores=4`
      - Workflow:
    * `_resnet50,offline`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS*: `-sdp-cluster-sizes=2,2 -multicast-weights`
        - *CM_QAIC_MODEL_COMPILER_ARGS_SUT*: `-aic-num-cores=4 -mos=1,2 -ols=4`
      - Workflow:
    * `_resnet50,offline,nsp.14`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS_SUT*: `-aic-num-cores=4 -mos=1,2 -ols=4`
      - Workflow:
    * `_resnet50,server`
      - Workflow:
    * `_resnet50,server,nsp.14`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS_SUT*: `-aic-num-cores=4 -ols=4`
        - *CM_QAIC_MODEL_COMPILER_ARGS*: `-sdp-cluster-sizes=2,2 -mos=1,2 -multicast-weights`
      - Workflow:
    * `_resnet50,server,nsp.16`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS_SUT*: `-aic-num-cores=4 -ols=4`
        - *CM_QAIC_MODEL_COMPILER_ARGS*: `-sdp-cluster-sizes=4,4 -mos=1,4`
      - Workflow:
    * `_resnet50,singlestream`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS*: `-aic-num-of-instances=1`
        - *CM_QAIC_MODEL_COMPILER_ARGS_SUT*: `-aic-num-cores=8 -mos=1 -ols=1`
      - Workflow:
    * `_resnet50,singlestream,nsp.14`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS_SUT*: `-aic-num-cores=8 -mos=1 -ols=1`
      - Workflow:
    * `_resnet50,tf`
      - Environment variables:
        - *CM_QAIC_MODEL_TO_CONVERT*: `calibrate_resnet50_tf`
      - Workflow:
    * `_retinanet`
      - Environment variables:
        - *CM_COMPILE_RETINANET*: `on`
        - *CM_QAIC_MODEL_TO_CONVERT*: `calibrate_retinanet_no_nms_mlperf`
        - *CM_QAIC_MODEL_COMPILER_ARGS*: `-aic-enable-depth-first`
        - *CM_QAIC_MODEL_COMPILER_PARAMS_BASE*: `-aic-hw -aic-hw-version=2.0 -compile-only -enable-channelwise -onnx-define-symbol=batch_size,1 -node-precision-info=<<<CM_ML_MODEL_RETINANET_QAIC_NODE_PRECISION_INFO_FILE_PATH>>> -quantization-schema-constants=symmetric_with_uint8 -quantization-schema-activations=asymmetric -quantization-calibration=None`
      - Workflow:
    * `_retinanet,multistream`
      - Workflow:
    * `_retinanet,nsp.14`
      - Workflow:
    * `_retinanet,offline`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS_SUT*: `-aic-num-cores=1 -mos=1 -ols=1`
      - Workflow:
    * `_retinanet,offline,nsp.14`
      - Workflow:
    * `_retinanet,server`
      - Workflow:
    * `_retinanet,server,nsp.14`
      - Workflow:
    * `_retinanet,singlestream`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS*: ``
        - *CM_QAIC_MODEL_COMPILER_ARGS_SUT*: `-aic-num-cores=8 -mos=1 -ols=1`
      - Workflow:
    * `_retinanet,singlestream,nsp.14`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_ARGS_SUT*: `-aic-num-cores=8 -mos=1 -ols=1`
      - Workflow:

    </details>


  * Group "**batch-size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bs.#`
      - Environment variables:
        - *CM_QAIC_MODEL_BATCH_SIZE*: `#`
      - Workflow:
    * `_bs.1`
      - Environment variables:
        - *CM_QAIC_MODEL_BATCH_SIZE*: `1`
      - Workflow:

    </details>


  * Group "**calib-dataset-filter-size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_filter-size.#`
      - Workflow:

    </details>


  * Group "**mlperf-scenario**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_multistream`
      - Workflow:
    * `_offline`
      - Workflow:
    * `_server`
      - Workflow:
    * **`_singlestream`** (default)
      - Workflow:

    </details>


  * Group "**model-framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_tf`
      - Workflow:

    </details>


  * Group "**nsp**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_nsp.14`
      - Workflow:
    * `_nsp.16`
      - Workflow:
    * `_nsp.8`
      - Workflow:
    * `_nsp.9`
      - Workflow:

    </details>


  * Group "**percentile-calibration**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_pc.#`
      - Environment variables:
        - *CM_QAIC_MODEL_COMPILER_PERCENTILE_CALIBRATION_VALUE*: `#`
        - *CM_QAIC_MODEL_COMPILER_QUANTIZATION_PARAMS*: `-quantization-calibration=Percentile  -percentile-calibration-value=<<<CM_QAIC_MODEL_COMPILER_PERCENTILE_CALIBRATION_VALUE>>>`
      - Workflow:

    </details>


  * Group "**quantization**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_no-quantized`
      - Environment variables:
        - *CM_QAIC_MODEL_QUANTIZATION*: `no`
      - Workflow:
    * **`_quantized`** (default)
      - Environment variables:
        - *CM_QAIC_MODEL_QUANTIZATION*: `yes`
      - Workflow:

    </details>


#### Default variations

`_quantized,_singlestream`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--register=value`  &rarr;  `CM_REGISTER_CACHE=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "register":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.


</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-model-for.qaic/_cm.json)***
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,qaic,apps,sdk
       * `if (CM_REGISTER_CACHE  != on)`
       * CM names: `--adr.['qaic-apps-sdk']...`
       - CM script: [get-qaic-apps-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-qaic-apps-sdk)
     * qaic,calibrate,_retinanet
       * `if (CM_COMPILE_RETINANET  == yes)`
       * CM names: `--adr.['retinanet-profile', 'qaic-profile']...`
       - CM script: [calibrate-model-for.qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/calibrate-model-for.qaic)
     * qaic,calibrate,_resnet50
       * `if (CM_COMPILE_RESNET  == on) AND (CM_REGISTER_CACHE  != on)`
       * CM names: `--adr.['resnet-profile', 'qaic-profile']...`
       - CM script: [calibrate-model-for.qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/calibrate-model-for.qaic)
     * get,ml-model
       * CM names: `--adr.['model-src']...`
       - CM script: [get-ml-model-3d-unet-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-3d-unet-kits19)
       - CM script: [get-ml-model-abtf-ssd-pytorch](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-abtf-ssd-pytorch)
       - CM script: [get-ml-model-bert-base-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-base-squad)
       - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
       - CM script: [get-ml-model-dlrm-terabyte](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte)
       - CM script: [get-ml-model-efficientnet-lite](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-efficientnet-lite)
       - CM script: [get-ml-model-gptj](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj)
       - CM script: [get-ml-model-huggingface-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-huggingface-zoo)
       - CM script: [get-ml-model-llama2](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-llama2)
       - CM script: [get-ml-model-mobilenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet)
       - CM script: [get-ml-model-neuralmagic-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo)
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
       - CM script: [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
       - CM script: [get-ml-model-retinanet-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet-nvidia)
       - CM script: [get-ml-model-rnnt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt)
       - CM script: [get-ml-model-stable-diffusion](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-stable-diffusion)
       - CM script: [get-ml-model-tiny-resnet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-tiny-resnet)
       - CM script: [get-ml-model-using-imagenet-from-model-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-using-imagenet-from-model-zoo)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-model-for.qaic/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-model-for.qaic/_cm.json)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-model-for.qaic/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-model-for.qaic/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-model-for.qaic/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-model-for.qaic/_cm.json)
</details>

___
### Script output
`cmr "qaic compile model model-compile qaic-compile[,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_ML_MODEL_FILE_WITH_PATH`
* `CM_QAIC_*`
#### New environment keys auto-detected from customize

* `CM_ML_MODEL_FILE_WITH_PATH`
* `CM_QAIC_MODEL_COMPILED_BINARY_WITH_PATH`
___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)