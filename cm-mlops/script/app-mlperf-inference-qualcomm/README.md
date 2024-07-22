**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-qualcomm).**



Automatically generated README for this automation recipe: **app-mlperf-inference-qualcomm**

Category: **Modular MLPerf benchmarks**

License: **Apache 2.0**

Maintainers: [Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=app-mlperf-inference-qualcomm,eef1aca5d7c0470e) ]*

---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-qualcomm)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *reproduce,mlcommons,mlperf,inference,harness,qualcomm-harness,qualcomm,kilt-harness,kilt*
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

````cmr "reproduce mlcommons mlperf inference harness qualcomm-harness qualcomm kilt-harness kilt" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=reproduce,mlcommons,mlperf,inference,harness,qualcomm-harness,qualcomm,kilt-harness,kilt`

`cm run script --tags=reproduce,mlcommons,mlperf,inference,harness,qualcomm-harness,qualcomm,kilt-harness,kilt[,variations] [--input_flags]`

*or*

`cmr "reproduce mlcommons mlperf inference harness qualcomm-harness qualcomm kilt-harness kilt"`

`cmr "reproduce mlcommons mlperf inference harness qualcomm-harness qualcomm kilt-harness kilt [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'reproduce,mlcommons,mlperf,inference,harness,qualcomm-harness,qualcomm,kilt-harness,kilt'
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

```cmr "cm gui" --script="reproduce,mlcommons,mlperf,inference,harness,qualcomm-harness,qualcomm,kilt-harness,kilt"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=reproduce,mlcommons,mlperf,inference,harness,qualcomm-harness,qualcomm,kilt-harness,kilt) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "reproduce mlcommons mlperf inference harness qualcomm-harness qualcomm kilt-harness kilt[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *Internal group (variations should not be selected manually)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bert_`
      - Environment variables:
        - *CM_BENCHMARK*: `STANDALONE_BERT`
        - *kilt_model_name*: `bert`
        - *kilt_model_seq_length*: `384`
        - *kilt_model_bert_variant*: `BERT_PACKED`
        - *kilt_input_format*: `INT64,1,384:INT64,1,8:INT64,1,384:INT64,1,384`
        - *kilt_output_format*: `FLOAT32,1,384:FLOAT32,1,384`
        - *dataset_squad_tokenized_max_seq_length*: `384`
        - *loadgen_buffer_size*: `10833`
        - *loadgen_dataset_size*: `10833`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_transformers
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_safetensors
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_onnx
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_activation-count.#`
      - Environment variables:
        - *CM_MLPERF_QAIC_ACTIVATION_COUNT*: `#`
      - Workflow:
    * `_bert-99,offline`
      - Workflow:
    * `_bert-99,qaic`
      - Environment variables:
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `https://github.com/mlcommons/inference_results_v3.1/blob/main/closed/Qualcomm/calibration.md`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `int32`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `int8,fp16`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * compile,qaic,model,_bert-99,_pc.99.9980
             * `if (CM_MLPERF_SKIP_RUN  != True)`
             * CM names: `--adr.['qaic-model-compiler', 'bert-99-compiler']...`
             - CM script: [compile-model-for.qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-model-for.qaic)
    * `_bert-99.9,offline`
      - Workflow:
    * `_bert-99.9,qaic`
      - Environment variables:
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `https://github.com/mlcommons/inference_results_v3.1/blob/main/closed/Qualcomm/calibration.md`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `int32`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `fp16`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * compile,qaic,model,_bert-99.9
             * `if (CM_MLPERF_SKIP_RUN  != True)`
             * CM names: `--adr.['qaic-model-compiler', 'bert-99.9-compiler']...`
             - CM script: [compile-model-for.qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-model-for.qaic)
    * `_bert_,network-client`
      - Environment variables:
        - *CM_BENCHMARK*: `NETWORK_BERT_CLIENT`
      - Workflow:
    * `_bert_,network-server`
      - Environment variables:
        - *CM_BENCHMARK*: `NETWORK_BERT_SERVER`
      - Workflow:
    * `_bert_,qaic`
      - Environment variables:
        - *kilt_model_batch_size*: `1`
        - *kilt_input_format*: `UINT32,1,384:UINT32,1,8:UINT32,1,384:UINT32,1,384`
        - *kilt_input_formata*: `UINT32,1,384:UINT32,1,384:UINT32,1,384`
        - *kilt_output_formatia*: `UINT8,1,384:UINT8,1,384`
        - *kilt_device_qaic_skip_stage*: `convert`
      - Workflow:
    * `_bert_,singlestream`
      - Environment variables:
        - *kilt_model_batch_size*: `1`
      - Workflow:
    * `_dl2q.24xlarge,bert-99,offline`
      - Environment variables:
        - *qaic_activation_count*: `14`
      - Workflow:
    * `_dl2q.24xlarge,bert-99.9,offline`
      - Environment variables:
        - *qaic_activation_count*: `7`
      - Workflow:
    * `_dl2q.24xlarge,bert-99.9,server`
      - Environment variables:
        - *qaic_activation_count*: `7`
      - Workflow:
    * `_dl2q.24xlarge,resnet50,multistream`
      - Environment variables:
        - *qaic_activation_count*: `1`
      - Workflow:
    * `_dl2q.24xlarge,resnet50,offline`
      - Environment variables:
        - *qaic_activation_count*: `3`
      - Workflow:
    * `_dl2q.24xlarge,resnet50,server`
      - Environment variables:
        - *qaic_activation_count*: `3`
      - Workflow:
    * `_dl2q.24xlarge,retinanet,offline`
      - Environment variables:
        - *qaic_activation_count*: `14`
      - Workflow:
    * `_dl2q.24xlarge,retinanet,server`
      - Environment variables:
        - *qaic_activation_count*: `14`
      - Workflow:
    * `_dl2q.24xlarge,singlestream`
      - Environment variables:
        - *CM_QAIC_DEVICES*: `0`
        - *qaic_activation_count*: `1`
      - Workflow:
    * `_num-devices.4`
      - Environment variables:
        - *CM_QAIC_DEVICES*: `0,1,2,3`
      - Workflow:
    * `_pro`
      - Environment variables:
        - *qaic_queue_length*: `10`
      - Workflow:
    * `_pro,num-devices.4,bert-99,offline`
      - Environment variables:
        - *qaic_activation_count*: `16`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * set,device,qaic,_vc.15
             - CM script: [set-device-settings-qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-device-settings-qaic)
    * `_pro,num-devices.4,bert-99,server`
      - Environment variables:
        - *qaic_activation_count*: `16`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * set,device,qaic,_vc.13
             - CM script: [set-device-settings-qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-device-settings-qaic)
    * `_pro,num-devices.4,bert-99.9,offline`
      - Environment variables:
        - *qaic_activation_count*: `8`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * set,device,qaic,_vc.13
             - CM script: [set-device-settings-qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-device-settings-qaic)
    * `_pro,num-devices.4,bert-99.9,server`
      - Environment variables:
        - *qaic_activation_count*: `8`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * set,device,qaic,_vc.13
             - CM script: [set-device-settings-qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-device-settings-qaic)
    * `_pro,num-devices.4,resnet50,offline`
      - Environment variables:
        - *qaic_activation_count*: `4`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * set,device,qaic,_vc.16
             - CM script: [set-device-settings-qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-device-settings-qaic)
    * `_pro,num-devices.4,resnet50,server`
      - Environment variables:
        - *qaic_activation_count*: `4`
      - Workflow:
    * `_pro,num-devices.4,retinanet,offline`
      - Environment variables:
        - *qaic_activation_count*: `16`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * set,device,qaic,_vc.17
             - CM script: [set-device-settings-qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-device-settings-qaic)
    * `_pro,num-devices.4,retinanet,server`
      - Environment variables:
        - *qaic_activation_count*: `16`
      - Workflow:
    * `_pro,num-devices.4,singlestream`
      - Environment variables:
        - *CM_QAIC_DEVICES*: `0`
        - *qaic_activation_count*: `1`
      - Workflow:
    * `_rb6,bert-99,offline`
      - Environment variables:
        - *qaic_activation_count*: `9`
      - Workflow:
    * `_rb6,resnet50,multistream`
      - Environment variables:
        - *qaic_activation_count*: `2`
      - Workflow:
    * `_rb6,resnet50,offline`
      - Environment variables:
        - *qaic_activation_count*: `2`
      - Workflow:
    * `_rb6,retinanet,multistream`
      - Environment variables:
        - *qaic_activation_count*: `8`
      - Workflow:
    * `_rb6,retinanet,offline`
      - Environment variables:
        - *qaic_activation_count*: `9`
      - Workflow:
    * `_rb6,singlestream`
      - Environment variables:
        - *qaic_activation_count*: `1`
      - Workflow:
    * `_resnet50,uint8`
      - Environment variables:
        - *kilt_input_format*: `UINT8,-1,224,224,3`
        - *kilt_device_qaic_skip_stage*: `convert`
        - *CM_IMAGENET_ACCURACY_DTYPE*: `int8`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `https://github.com/mlcommons/inference_results_v3.1/blob/main/closed/Qualcomm/calibration.md`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `int8`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `int8`
      - Workflow:
    * `_retinanet,qaic,uint8`
      - Environment variables:
        - *kilt_device_qaic_skip_stage*: `convert`
        - *kilt_input_format*: `UINT8,1,3,800,800`
        - *kilt_output_format*: `INT8,1,1000:INT8,1,1000:INT8,1,1000:INT8,1,1000:INT8,1,1000:INT8,1,1000:INT8,1,1000:INT8,1,1000:INT8,1,1000:INT8,1,1000:INT8,1,4,1000:INT8,14,1000:INT8,1,4,1000:INT8,1,4,1000:INT8,1,4,1000`
        - *CM_ML_MODEL_WEIGHT_TRANSFORMATIONS*: `https://github.com/mlcommons/inference_results_v3.1/blob/main/closed/Qualcomm/calibration.md`
        - *CM_ML_MODEL_WEIGHTS_DATA_TYPE*: `int8`
        - *CM_ML_MODEL_INPUTS_DATA_TYPE*: `int8`
      - Workflow:
    * `_singlestream,resnet50`
      - Workflow:
    * `_singlestream,retinanet`
      - Workflow:

    </details>


  * Group "**batch-size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bs.#`
      - Environment variables:
        - *kilt_model_batch_size*: `#`
      - Workflow:
    * `_bs.0`
      - Environment variables:
        - *kilt_model_batch_size*: `1`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cpu`
        - *kilt_backend_type*: `cpu`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `gpu`
        - *CM_MLPERF_DEVICE_LIB_NAMESPEC*: `cudart`
        - *kilt_backend_type*: `gpu`
      - Workflow:
    * `_qaic`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `qaic`
        - *CM_MLPERF_DEVICE_LIB_NAMESPEC*: `QAic`
        - *kilt_backend_type*: `qaic`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,qaic,platform,sdk
             * `if (CM_MLPERF_SKIP_RUN  != True)`
             - CM script: [get-qaic-platform-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-qaic-platform-sdk)
           * get,lib,protobuf,_tag.v3.11.4
             * `if (CM_MLPERF_SKIP_RUN  != True)`
             - CM script: [get-lib-protobuf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-lib-protobuf)
           * set,device,mode,qaic
             * `if (CM_QAIC_VC in on)`
             - CM script: [set-device-settings-qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-device-settings-qaic)
           * set,device,mode,qaic,_ecc
             * `if (CM_QAIC_ECC in yes)`
             - CM script: [set-device-settings-qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-device-settings-qaic)

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_glow`
      - Environment variables:
        - *device*: `qaic`
        - *CM_MLPERF_BACKEND*: `glow`
        - *CM_MLPERF_BACKEND_LIB_NAMESPEC*: `QAic`
      - Workflow:
    * **`_onnxruntime`** (default)
      - Environment variables:
        - *device*: `onnxrt`
        - *CM_MLPERF_BACKEND*: `onnxruntime`
        - *CM_MLPERF_BACKEND_LIB_NAMESPEC*: `onnxruntime`
      - Workflow:
    * `_tensorrt`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tensorrt`
        - *device*: `tensorrt`
        - *CM_MLPERF_BACKEND_NAME*: `TensorRT`
      - Workflow:

    </details>


  * Group "**loadgen-batch-size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_loadgen-batch-size.#`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_BATCH_SIZE*: `#`
      - Workflow:

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
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/3750364/files/bert_large_v1_1_fake_quant.onnx`
      - Workflow:
    * `_bert-99.9`
      - Environment variables:
        - *CM_MODEL*: `bert-99.9`
        - *CM_ML_MODEL_STARTING_WEIGHTS_FILENAME*: `https://zenodo.org/record/3733910/files/model.onnx`
      - Workflow:
    * **`_resnet50`** (default)
      - Environment variables:
        - *CM_MODEL*: `resnet50`
        - *kilt_model_name*: `resnet50`
        - *kilt_input_count*: `1`
        - *kilt_output_count*: `1`
        - *kilt_input_format*: `FLOAT32,-1,224,224,3`
        - *kilt_output_format*: `INT64,-1`
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
        - *kilt_model_name*: `retinanet`
        - *kilt_input_count*: `1`
        - *kilt_model_max_detections*: `600`
        - *kilt_output_count*: `1`
        - *kilt_input_format*: `FLOAT32,-1,3,800,800`
        - *kilt_output_format*: `INT64,-1`
        - *dataset_imagenet_preprocessed_input_square_side*: `224`
        - *ml_model_image_height*: `800`
        - *ml_model_image_width*: `800`
        - *loadgen_buffer_size*: `64`
        - *loadgen_dataset_size*: `24576`
        - *CM_BENCHMARK*: `STANDALONE_OBJECT_DETECTION`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_Pillow
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torch
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torchvision
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_opencv-python
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_pycocotools
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * Group "**nsp**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_nsp.#`
      - Workflow:
    * `_nsp.14`
      - Workflow:
    * `_nsp.16`
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

    * `_fp16`
      - Workflow:
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

    * `_network-client`
      - Environment variables:
        - *CM_RUN_MODE*: `network-client`
      - Workflow:
    * `_network-server`
      - Environment variables:
        - *CM_RUN_MODE*: `network-server`
      - Workflow:
    * **`_standalone`** (default)
      - Environment variables:
        - *CM_RUN_MODE*: `standalone`
      - Workflow:

    </details>


  * Group "**sut**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_dl2q.24xlarge`
      - Environment variables:
        - *CM_QAIC_DEVICES*: `0,1,2,3,4,5,6,7`
        - *qaic_queue_length*: `4`
      - Workflow:
    * `_rb6`
      - Environment variables:
        - *CM_QAIC_DEVICES*: `0`
        - *qaic_queue_length*: `6`
      - Workflow:

    </details>


#### Default variations

`_cpu,_onnxruntime,_resnet50,_standalone`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
* `--devices=value`  &rarr;  `CM_QAIC_DEVICES=value`
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
* CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `kilt`
* CM_MLPERF_SKIP_RUN: `no`
* CM_KILT_REPO_URL: `https://github.com/GATEOverflow/kilt-mlperf`
* CM_QAIC_DEVICES: `0`
* kilt_max_wait_abs: `10000`
* verbosity: `0`
* loadgen_trigger_cold_run: `0`

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-qualcomm/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,git,repo
       * CM names: `--adr.['kilt-repo']...`
       - CM script: [get-git-repo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-git-repo)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,mlcommons,inference,loadgen
       * CM names: `--adr.['inference-loadgen']...`
       - CM script: [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)
     * generate,user-conf,mlperf,inference
       * CM names: `--adr.['user-conf-generator']...`
       - CM script: [generate-mlperf-inference-user-conf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf)
     * get,generic-python-lib,_mlperf_logging
       * CM names: `--adr.['mlperf-logging']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,ml-model,resnet50,_fp32,_onnx,_from-tf
       * `if (CM_MODEL  == resnet50) AND (CM_MLPERF_DEVICE  != qaic)`
       * CM names: `--adr.['resnet50-model', 'ml-model']...`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * compile,qaic,model,_resnet50
       * `if (CM_MODEL  == resnet50 AND CM_MLPERF_DEVICE  == qaic) AND (CM_MLPERF_SKIP_RUN  != True)`
       * CM names: `--adr.['qaic-model-compiler', 'resnet50-compiler']...`
       - CM script: [compile-model-for.qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-model-for.qaic)
     * get,dataset,imagenet,preprocessed,_for.resnet50,_NHWC,_full
       * `if (CM_MODEL  == resnet50) AND (CM_MLPERF_SKIP_RUN  != True)`
       * CM names: `--adr.['imagenet-preprocessed', 'dataset-preprocessed']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,squad-vocab
       * `if (CM_MODEL in ['bert-99', 'bert-99.9']) AND (CM_MLPERF_SKIP_RUN  != True)`
       * CM names: `--adr.['bert-vocab']...`
       - CM script: [get-dataset-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad-vocab)
     * get,dataset,tokenized,squad,_raw
       * `if (CM_MODEL in ['bert-99', 'bert-99.9']) AND (CM_MLPERF_SKIP_RUN  != True)`
       * CM names: `--adr.['squad-tokenized']...`
       - CM script: [get-preprocessed-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-squad)
     * compile,qaic,model,_retinanet
       * `if (CM_MODEL  == retinanet AND CM_MLPERF_DEVICE  == qaic) AND (CM_MLPERF_SKIP_RUN  != True)`
       * CM names: `--adr.['qaic-model-compiler', 'retinanet-compiler']...`
       - CM script: [compile-model-for.qaic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-model-for.qaic)
     * get,dataset,preprocessed,openimages,_for.retinanet.onnx,_NCHW,_validation,_custom-annotations
       * `if (CM_MODEL  == retinanet) AND (CM_MLPERF_SKIP_RUN  != True)`
       * CM names: `--adr.['openimages-preprocessed', 'dataset-preprocessed']...`
       - CM script: [get-preprocessed-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages)
     * get,lib,onnxruntime,lang-cpp,_cpu
       * `if (CM_MLPERF_BACKEND  == onnxruntime AND CM_MLPERF_DEVICE  == cpu)`
       - CM script: [get-onnxruntime-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt)
     * get,lib,onnxruntime,lang-cpp,_cuda
       * `if (CM_MLPERF_BACKEND  == onnxruntime AND CM_MLPERF_DEVICE  == gpu)`
       - CM script: [get-onnxruntime-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-qualcomm/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-qualcomm/_cm.yaml)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-qualcomm/run.sh)
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-qualcomm/_cm.yaml)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-qualcomm/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-qualcomm/_cm.yaml)***
     * compile,cpp-program
       * `if (CM_MLPERF_SKIP_RUN  != True)`
       * CM names: `--adr.['compile-program']...`
       - CM script: [compile-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program)
     * benchmark-mlperf
       * `if (CM_MLPERF_SKIP_RUN not in ['yes', True])`
       * CM names: `--adr.['runner', 'mlperf-runner']...`
       - CM script: [benchmark-program-mlperf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program-mlperf)
     * save,mlperf,inference,state
       * CM names: `--adr.['save-mlperf-inference-state']...`
       - CM script: [save-mlperf-inference-implementation-state](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/save-mlperf-inference-implementation-state)

___
### Script output
`cmr "reproduce mlcommons mlperf inference harness qualcomm-harness qualcomm kilt-harness kilt [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_DATASET_*`
* `CM_HW_NAME`
* `CM_IMAGENET_ACCURACY_DTYPE`
* `CM_MAX_EXAMPLES`
* `CM_MLPERF_*`
* `CM_ML_MODEL_*`
* `CM_SQUAD_ACCURACY_DTYPE`
#### New environment keys auto-detected from customize

* `CM_DATASET_LIST`
* `CM_MLPERF_CONF`
* `CM_MLPERF_DEVICE`
* `CM_MLPERF_USER_CONF`