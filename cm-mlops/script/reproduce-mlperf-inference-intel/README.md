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

* Category: *Modular MLPerf benchmarks.*
* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-intel)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* CM "database" tags to find this script: *reproduce,mlcommons,mlperf,inference,harness,intel-harness,intel,intel-harness,intel*
* Output cached? *False*
___
### Reuse this script in your project

#### Install CM automation language

* [Installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
* [CM intro](https://doi.org/10.5281/zenodo.8105339)

#### Pull CM repository with this automation

```cm pull repo mlcommons@ck```


#### Run this script from command line

1. `cm run script --tags=reproduce,mlcommons,mlperf,inference,harness,intel-harness,intel,intel-harness,intel[,variations] [--input_flags]`

2. `cmr "reproduce mlcommons mlperf inference harness intel-harness intel intel-harness intel[ variations]" [--input_flags]`

* `variations` can be seen [here](#variations)

* `input_flags` can be seen [here](#script-flags-mapped-to-environment)

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,mlcommons,mlperf,inference,harness,intel-harness,intel,intel-harness,intel'
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

```cmr "cm gui" --script="reproduce,mlcommons,mlperf,inference,harness,intel-harness,intel,intel-harness,intel"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=reproduce,mlcommons,mlperf,inference,harness,intel-harness,intel,intel-harness,intel) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "reproduce mlcommons mlperf inference harness intel-harness intel intel-harness intel[ variations]" [--input_flags]`

___
### Customization


#### Variations

  * *Internal group (variations should not be selected manually)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert_`
      - Environment variables:
        - *CM_BENCHMARK*: `STANDALONE_BERT`
        - *dataset_squad_tokenized_max_seq_length*: `384`
        - *loadgen_buffer_size*: `10833`
        - *loadgen_dataset_size*: `10833`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * install,transformers,from.src,_for-intel-mlperf-inference
             - CM script: [install-transformers-from.src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-transformers-from.src)
    * `_build_harness,bert_`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,dataset,original,squad
             * CM names: `--adr.['squad-original']...`
             - CM script: [get-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad)
           * get,ml-model,bert-large,_pytorch,_int8
             * CM names: `--adr.['bert-large', 'ml-model']...`
             - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
           * get,generic-python-lib,_package.tokenization
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_activation-count.#`
      - Environment variables:
        - *CM_MODEL_BATCH_SIZE*: `#`
      - Workflow:
    * `_bert_,network-client`
      - Environment variables:
        - *CM_BENCHMARK*: `NETWORK_BERT_CLIENT`
      - Workflow:
    * `_bert_,network-server`
      - Environment variables:
        - *CM_BENCHMARK*: `NETWORK_BERT_SERVER`
      - Workflow:
    * `_bs.#`
      - Environment variables:
        - *ML_MLPERF_MODEL_BATCH_SIZE*: `#`
      - Workflow:
    * `_loadgen-batch-size.#`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_BATCH_SIZE*: `#`
      - Workflow:
    * `_resnet50,uint8`
      - Environment variables:
        - *CM_IMAGENET_ACCURACY_DTYPE*: `int8`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cpu`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_pytorch`** (default)
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `pytorch`
        - *CM_MLPERF_BACKEND_LIB_NAMESPEC*: `pytorch`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,pytorch,from.src,_for-intel-mlperf-inference
             - CM script: [install-pytorch-from.src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-pytorch-from.src)
           * install,onednn,from.src,_for-intel-mlperf-inference
             - CM script: [install-onednn-from.src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-onednn-from.src)

    </details>


  * Group "**loadgen-scenario**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_multistream`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `MultiStream`
      - Workflow:
    * `_offline`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `Offline`
      - Workflow:
    * `_server`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `Server`
      - Workflow:
    * `_singlestream`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `SingleStream`
      - Workflow:

    </details>


  * Group "**model**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert-99`
      - Environment variables:
        - *CM_MODEL*: `bert-99`
        - *CM_SQUAD_ACCURACY_DTYPE*: `float32`
        - *CM_NOT_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/3750364/files/bert_large_v1_1_fake_quant.onnx`
      - Workflow:
    * `_bert-99.9`
      - Environment variables:
        - *CM_MODEL*: `bert-99.9`
        - *CM_NOT_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/3733910/files/model.onnx`
      - Workflow:
    * **`_resnet50`** (default)
      - Environment variables:
        - *CM_MODEL*: `resnet50`
        - *dataset_imagenet_preprocessed_input_square_side*: `224`
        - *ml_model_has_background_class*: `YES`
        - *ml_model_image_height*: `224`
        - *loadgen_buffer_size*: `1024`
        - *loadgen_dataset_size*: `50000`
        - *CM_BENCHMARK*: `STANDALONE_CLASSIFICATION`
      - Workflow:
    * `_retinanet`
      - Environment variables:
        - *CM_MODEL*: `retinanet`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/6617981/files/resnext50_32x4d_fpn.pth`
        - *dataset_imagenet_preprocessed_input_square_side*: `224`
        - *ml_model_image_height*: `800`
        - *ml_model_image_width*: `800`
        - *loadgen_buffer_size*: `64`
        - *loadgen_dataset_size*: `24576`
        - *CM_BENCHMARK*: `STANDALONE_OBJECT_DETECTION`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * Group "**network-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_network-server`
      - Environment variables:
        - *CM_MLPERF_NETWORK_RUN_MODE*: `network-server`
      - Workflow:
    * **`_standalone`** (default)
      - Environment variables:
        - *CM_MLPERF_NETWORK_RUN_MODE*: `standalone`
      - Workflow:

    </details>


  * Group "**network-run-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_network-client`
      - Environment variables:
        - *CM_MLPERF_NETWORK_RUN_MODE*: `network-client`
      - Workflow:

    </details>


  * Group "**power-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_maxn`
      - Environment variables:
        - *CM_MLPERF_NVIDIA_HARNESS_MAXN*: `True`
      - Workflow:
    * `_maxq`
      - Environment variables:
        - *CM_MLPERF_NVIDIA_HARNESS_MAXQ*: `True`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_fp32`
      - Environment variables:
        - *CM_IMAGENET_ACCURACY_DTYPE*: `float32`
      - Workflow:
    * `_uint8`
      - Workflow:

    </details>


  * Group "**run-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_build_harness`
      - Environment variables:
        - *CM_LOCAL_MLPERF_INFERENCE_INTEL_RUN_MODE*: `build_harness`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-sys-util,_rsync
             - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
           * install,llvm,from.src,_for-intel-mlperf-inference
             - CM script: [install-llvm-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-src)
    * **`_run_harness`** (default)
      - Environment variables:
        - *CM_LOCAL_MLPERF_INFERENCE_INTEL_RUN_MODE*: `run_harness`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * reproduce,mlperf,inference,intel,harness,_build_harness
             * CM names: `--adr.['build-harness']...`
             - CM script: [reproduce-mlperf-inference-intel](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-intel)
           * get,mlcommons,inference,src
             * CM names: `--adr.['inference-src']...`
             - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
           * generate,user-conf,mlperf,inference
             * CM names: `--adr.['user-conf-generator']...`
             - CM script: [generate-mlperf-inference-user-conf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf)

    </details>


#### Default variations

`_cpu,_pytorch,_resnet50,_run_harness,_standalone`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
* `--max_batchsize=value`  &rarr;  `CM_MLPERF_LOADGEN_MAX_BATCHSIZE=value`
* `--mlperf_conf=value`  &rarr;  `CM_MLPERF_CONF=value`
* `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
* `--multistream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY=value`
* `--offline_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS=value`
* `--output_dir=value`  &rarr;  `CM_MLPERF_OUTPUT_DIR=value`
* `--performance_sample_count=value`  &rarr;  `CM_MLPERF_LOADGEN_PERFORMANCE_SAMPLE_COUNT=value`
* `--rerun=value`  &rarr;  `CM_RERUN=value`
* `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
* `--server_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_SERVER_TARGET_QPS=value`
* `--singlestream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY=value`
* `--skip_preprocess=value`  &rarr;  `CM_SKIP_PREPROCESS_DATASET=value`
* `--skip_preprocessing=value`  &rarr;  `CM_SKIP_PREPROCESS_DATASET=value`
* `--target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_LATENCY=value`
* `--target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_QPS=value`
* `--user_conf=value`  &rarr;  `CM_MLPERF_USER_CONF=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "count":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_BATCH_COUNT: `1`
* CM_BATCH_SIZE: `1`
* CM_FAST_COMPILATION: `yes`
* CM_MLPERF_LOADGEN_SCENARIO: `Offline`
* CM_MLPERF_LOADGEN_MODE: `performance`
* CM_SKIP_PREPROCESS_DATASET: `no`
* CM_SKIP_MODEL_DOWNLOAD: `no`
* CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `intel`
* CM_MLPERF_SKIP_RUN: `no`
* verbosity: `1`
* loadgen_trigger_cold_run: `0`

</details>

___
### Script workflow, dependencies and native scripts

<details>
<summary>Click here to expand this section.</summary>

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-intel/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,generic-python-lib,_mlperf_logging
       * CM names: `--adr.['mlperf-logging']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,conda,_name.bert-pt
       - CM script: [get-conda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-conda)
     * get,generic,conda-package,_package.python
       - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
     * get,generic-sys-util,_numactl
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
     * get,generic,conda-package,_package.jemalloc,_source.conda-forge
       - CM script: [install-generic-conda-package](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-conda-package)
     * get,ml-model,resnet50,_fp32,_onnx,_from-tf
       * `if (CM_MODEL  == resnet50)`
       * CM names: `--adr.['resnet50-model', 'ml-model']...`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * compile,intel,model,_resnet50
       * `if (CM_MODEL  == resnet50)`
       * CM names: `--adr.['resnet50-compiler']...`
       - *Warning: no scripts found*
     * get,dataset,imagenet,preprocessed,_for.resnet50,_NHWC,_full
       * `if (CM_MODEL  == resnet50)`
       * CM names: `--adr.['imagenet-preprocessed', 'dataset-preprocessed']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * compile,intel,model,_retinanet
       * `if (CM_MODEL  == retinanet)`
       * CM names: `--adr.['retinanet-compiler']...`
       - *Warning: no scripts found*
     * get,dataset,preprocessed,openimages,_for.retinanet.onnx,_NCHW,_validation,_custom-annotations
       * `if (CM_MODEL  == retinanet)`
       * CM names: `--adr.['openimages-preprocessed', 'dataset-preprocessed']...`
       - CM script: [get-preprocessed-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages)
     * get,mlperf,inference,results
       - CM script: [get-mlperf-inference-results](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-results)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-intel/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-intel/_cm.yaml)
  1. ***Run native script if exists***
     * [run_harness.sh](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-intel/run_harness.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-intel/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-intel/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-intel/_cm.yaml)***
     * benchmark-mlperf
       * `if (CM_MLPERF_SKIP_RUN not in ['yes', True])`
       * CM names: `--adr.['runner', 'mlperf-runner']...`
       - CM script: [benchmark-program-mlperf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program-mlperf)
</details>

___
### Script output
`cmr "reproduce mlcommons mlperf inference harness intel-harness intel intel-harness intel[,variations]" [--input_flags] -j`
#### New environment keys (filter)

#### New environment keys auto-detected from customize

___
### Maintainers

* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)