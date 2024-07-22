**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-mlcommons-python).**



Automatically generated README for this automation recipe: **app-mlperf-inference-mlcommons-python**

Category: **Modular MLPerf inference benchmark pipeline**

License: **Apache 2.0**

Developers: [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh), [Thomas Zhu](https://www.linkedin.com/in/hanwen-zhu-483614189), [Grigori Fursin](https://cKnowledge.org/gfursin)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=app-mlperf-inference-mlcommons-python,ff149e9781fc4b65) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---

This portable CM script is being developed by the [MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)
to modularize the *python reference implementations* of the [MLPerf inference benchmark](https://github.com/mlcommons/inference) 
using the [MLCommons CM automation meta-framework](https://github.com/mlcommons/ck).
The goal is to make it easier to run, optimize and reproduce MLPerf benchmarks 
across diverse platforms with continuously changing software and hardware.

See the current coverage of different models, devices and backends [here](README-extra.md#current-coverage).


---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-mlcommons-python)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *app,vision,language,mlcommons,mlperf,inference,reference,ref*
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

````cmr "app vision language mlcommons mlperf inference reference ref" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=app,vision,language,mlcommons,mlperf,inference,reference,ref`

`cm run script --tags=app,vision,language,mlcommons,mlperf,inference,reference,ref[,variations] [--input_flags]`

*or*

`cmr "app vision language mlcommons mlperf inference reference ref"`

`cmr "app vision language mlcommons mlperf inference reference ref [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*

#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,vision,language,mlcommons,mlperf,inference,reference,ref'
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

```cmr "cm gui" --script="app,vision,language,mlcommons,mlperf,inference,reference,ref"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=app,vision,language,mlcommons,mlperf,inference,reference,ref) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "app vision language mlcommons mlperf inference reference ref[variations]" [--input_flags]`

___
### Customization


#### Variations

  * *Internal group (variations should not be selected manually)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_gptj_`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_torch
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.datasets
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.attrs
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.accelerate
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_llama2-70b_`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_package.transformers
             * CM names: `--adr.['transformers']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.datasets
             * CM names: `--adr.['datasets']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.sentencepiece
             * CM names: `--adr.['sentencepiece']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.protobuf
             * CM names: `--adr.['protobuf']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.accelerate
             * CM names: `--adr.['accelerate']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.absl-py
             * CM names: `--adr.['absl-py']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.evaluate
             * CM names: `--adr.['evaluate']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.nltk
             * CM names: `--adr.['nltk']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.rouge-score
             * CM names: `--adr.['rouge-score']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_3d-unet`
      - Environment variables:
        - *CM_TMP_IGNORE_MLPERF_QUERY_COUNT*: `True`
        - *CM_MLPERF_MODEL_SKIP_BATCHING*: `True`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_package.nibabel
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_beam_size.#`
      - Environment variables:
        - *GPTJ_BEAM_SIZE*: `#`
      - Workflow:
    * `_bert`
      - Environment variables:
        - *CM_MLPERF_MODEL_SKIP_BATCHING*: `True`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_package.pydantic
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_tokenization
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_six
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.absl-py
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_protobuf
             * `if (CM_MLPERF_BACKEND in ['tf', 'tflite'])`
             * CM names: `--adr.['protobuf']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_boto3
             * `if (CM_MLPERF_BACKEND  == pytorch)`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_torch
             * `if (CM_MLPERF_DEVICE  != gpu)`
             * CM names: `--adr.['ml-engine-pytorch', 'pytorch']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_dlrm`
      - Environment variables:
        - *CM_MLPERF_MODEL_SKIP_BATCHING*: `True`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,dlrm,src
             * CM names: `--adr.['dlrm-src']...`
             - CM script: [get-dlrm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dlrm)
           * get,generic-python-lib,_mlperf_logging
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_opencv-python
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_tensorboard
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_protobuf
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_scikit-learn
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_tqdm
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_onnx
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.torchrec
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.pyre-extensions
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.torchsnapshot
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_llama2-70b_,cuda`
      - Workflow:
    * `_multistream`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `MultiStream`
      - Workflow:
    * `_offline`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `Offline`
      - Workflow:
    * `_onnxruntime,cpu`
      - Environment variables:
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_ONNXRUNTIME_VERSION>>>`
      - Workflow:
    * `_onnxruntime,cuda`
      - Environment variables:
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_ONNXRUNTIME_GPU_VERSION>>>`
        - *ONNXRUNTIME_PREFERRED_EXECUTION_PROVIDER*: `CUDAExecutionProvider`
      - Workflow:
    * `_onnxruntime,rocm`
      - Environment variables:
        - *ONNXRUNTIME_PREFERRED_EXECUTION_PROVIDER*: `ROCMExecutionProvider`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_ONNXRUNTIME_TRAINING_VERSION>>>`
      - Workflow:
    * `_pytorch,rocm`
      - Workflow:
    * `_r2.1_default`
      - Environment variables:
        - *CM_RERUN*: `yes`
        - *CM_SKIP_SYS_UTILS*: `yes`
        - *CM_TEST_QUERY_COUNT*: `100`
      - Workflow:
    * `_server`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `Server`
      - Workflow:
    * `_singlestream`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `SingleStream`
      - Workflow:
    * `_tf,rocm`
      - Environment variables:
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TENSORFLOW_ROCM_VERSION>>>`
      - Workflow:
    * `_tpu,tflite`
      - Workflow:

    </details>


  * Group "**batch-size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_batch_size.#`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_MAX_BATCHSIZE*: `#`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cpu`
        - *CUDA_VISIBLE_DEVICES*: ``
        - *USE_CUDA*: `False`
        - *USE_GPU*: `False`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `gpu`
        - *USE_CUDA*: `True`
        - *USE_GPU*: `True`
      - Workflow:
    * `_rocm`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `rocm`
        - *USE_GPU*: `True`
      - Workflow:
    * `_tpu`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `tpu`
      - Workflow:

    </details>


  * Group "**framework**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_deepsparse`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `deepsparse`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_DEEPSPARSE_VERSION>>>`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_deepsparse
             * `if (CM_HOST_PLATFORM_FLAVOR  != aarch64)`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.deepsparse-nightly
             * `if (CM_HOST_PLATFORM_FLAVOR  == aarch64)`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_ncnn`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `ncnn`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_NCNN_VERSION>>>`
        - *CM_MLPERF_VISION_DATASET_OPTION*: `imagenet_pytorch`
      - Workflow:
    * **`_onnxruntime`** (default)
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `onnxruntime`
      - Workflow:
    * `_pytorch`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `pytorch`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TORCH_VERSION>>>`
      - Workflow:
    * `_ray`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `ray`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TORCH_VERSION>>>`
      - Workflow:
    * `_tf`
      - Aliases: `_tensorflow`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tf`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TENSORFLOW_VERSION>>>`
      - Workflow:
    * `_tflite`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tflite`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TFLITE_VERSION>>>`
        - *CM_MLPERF_VISION_DATASET_OPTION*: `imagenet_tflite_tpu`
      - Workflow:
    * `_tvm-onnx`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tvm-onnx`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_ONNXRUNTIME_VERSION>>>`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_onnx
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,tvm
             * CM names: `--adr.['tvm']...`
             - CM script: [get-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm)
           * get,tvm-model,_onnx
             * CM names: `--adr.['tvm-model']...`
             - CM script: [get-tvm-model](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm-model)
    * `_tvm-pytorch`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tvm-pytorch`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TORCH_VERSION>>>`
        - *CM_PREPROCESS_PYTORCH*: `yes`
        - *MLPERF_TVM_TORCH_QUANTIZED_ENGINE*: `qnnpack`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_torch
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,tvm
             * CM names: `--adr.['tvm']...`
             - CM script: [get-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm)
           * get,tvm-model,_pytorch
             * CM names: `--adr.['tvm-model']...`
             - CM script: [get-tvm-model](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm-model)
    * `_tvm-tflite`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tvm-tflite`
        - *CM_MLPERF_BACKEND_VERSION*: `<<<CM_TVM-TFLITE_VERSION>>>`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_tflite
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,tvm
             * CM names: `--adr.['tvm']...`
             - CM script: [get-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm)
           * get,tvm-model,_tflite
             * CM names: `--adr.['tvm-model']...`
             - CM script: [get-tvm-model](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm-model)

    </details>


  * Group "**implementation**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_python`** (default)
      - Environment variables:
        - *CM_MLPERF_PYTHON*: `yes`
        - *CM_MLPERF_IMPLEMENTATION*: `reference`
      - Workflow:

    </details>


  * Group "**models**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_3d-unet-99`
      - Environment variables:
        - *CM_MODEL*: `3d-unet-99`
      - Workflow:
    * `_3d-unet-99.9`
      - Environment variables:
        - *CM_MODEL*: `3d-unet-99.9`
      - Workflow:
    * `_bert-99`
      - Environment variables:
        - *CM_MODEL*: `bert-99`
      - Workflow:
    * `_bert-99.9`
      - Environment variables:
        - *CM_MODEL*: `bert-99.9`
      - Workflow:
    * `_dlrm-99`
      - Environment variables:
        - *CM_MODEL*: `dlrm-99`
      - Workflow:
    * `_dlrm-99.9`
      - Environment variables:
        - *CM_MODEL*: `dlrm-99.9`
      - Workflow:
    * `_gptj-99`
      - Environment variables:
        - *CM_MODEL*: `gptj-99`
      - Workflow:
    * `_gptj-99.9`
      - Environment variables:
        - *CM_MODEL*: `gptj-99.9`
      - Workflow:
    * `_llama2-70b-99`
      - Environment variables:
        - *CM_MODEL*: `llama2-70b-99`
      - Workflow:
    * `_llama2-70b-99.9`
      - Environment variables:
        - *CM_MODEL*: `llama2-70b-99.9`
      - Workflow:
    * **`_resnet50`** (default)
      - Environment variables:
        - *CM_MODEL*: `resnet50`
        - *CM_MLPERF_USE_MLCOMMONS_RUN_SCRIPT*: `yes`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_opencv-python
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_pycocotools
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
        1. ***Read "prehook_deps" on other CM scripts***
           * get,generic-python-lib,_protobuf
             * `if (CM_MLPERF_BACKEND in ['tf', 'tflite'])`
             * CM names: `--adr.['protobuf']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_retinanet`
      - Environment variables:
        - *CM_MODEL*: `retinanet`
        - *CM_MLPERF_USE_MLCOMMONS_RUN_SCRIPT*: `yes`
        - *CM_MLPERF_LOADGEN_MAX_BATCHSIZE*: `1`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_opencv-python
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_numpy
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_pycocotools
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_rnnt`
      - Environment variables:
        - *CM_MODEL*: `rnnt`
        - *CM_MLPERF_MODEL_SKIP_BATCHING*: `True`
        - *CM_TMP_IGNORE_MLPERF_QUERY_COUNT*: `True`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_package.pydantic
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_librosa
             * CM names: `--adr.['librosa']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_inflect
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_unidecode
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_toml
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
    * `_sdxl`
      - Environment variables:
        - *CM_MODEL*: `stable-diffusion-xl`
        - *CM_NUM_THREADS*: `1`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,generic-python-lib,_package.diffusers
             * CM names: `--adr.['diffusers']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.transformers
             * CM names: `--adr.['transformers']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.accelerate
             * CM names: `--adr.['accelerate']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.torchmetrics
             * CM names: `--adr.['torchmetrics']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.torch-fidelity
             * CM names: `--adr.['torch-fidelity']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.open_clip_torch
             * CM names: `--adr.['open-clip']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.opencv-python
             * CM names: `--adr.['opencv-python']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
           * get,generic-python-lib,_package.scipy
             * CM names: `--adr.['scipy']...`
             - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)

    </details>


  * Group "**network**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_network-lon`
      - Environment variables:
        - *CM_NETWORK_LOADGEN*: `lon`
        - *CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX1*: `network_loadgen`
      - Workflow:
    * `_network-sut`
      - Environment variables:
        - *CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX1*: `network_sut`
        - *CM_NETWORK_LOADGEN*: `sut`
      - Workflow:

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bfloat16`
      - Environment variables:
        - *CM_MLPERF_QUANTIZATION*: `False`
        - *CM_MLPERF_MODEL_PRECISION*: `bfloat16`
      - Workflow:
    * `_float16`
      - Environment variables:
        - *CM_MLPERF_QUANTIZATION*: `False`
        - *CM_MLPERF_MODEL_PRECISION*: `float16`
      - Workflow:
    * **`_fp32`** (default)
      - Environment variables:
        - *CM_MLPERF_QUANTIZATION*: `False`
        - *CM_MLPERF_MODEL_PRECISION*: `float32`
      - Workflow:
    * `_int8`
      - Aliases: `_quantized`
      - Environment variables:
        - *CM_MLPERF_QUANTIZATION*: `True`
        - *CM_MLPERF_MODEL_PRECISION*: `int8`
      - Workflow:

    </details>


#### Default variations

`_cpu,_fp32,_onnxruntime,_python,_resnet50`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--clean=value`  &rarr;  `CM_MLPERF_CLEAN_SUBMISSION_DIR=value`
* `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
* `--dataset=value`  &rarr;  `CM_MLPERF_VISION_DATASET_OPTION=value`
* `--dataset_args=value`  &rarr;  `CM_MLPERF_EXTRA_DATASET_ARGS=value`
* `--docker=value`  &rarr;  `CM_RUN_DOCKER_CONTAINER=value`
* `--hw_name=value`  &rarr;  `CM_HW_NAME=value`
* `--imagenet_path=value`  &rarr;  `IMAGENET_PATH=value`
* `--max_amps=value`  &rarr;  `CM_MLPERF_POWER_MAX_AMPS=value`
* `--max_batchsize=value`  &rarr;  `CM_MLPERF_LOADGEN_MAX_BATCHSIZE=value`
* `--max_volts=value`  &rarr;  `CM_MLPERF_POWER_MAX_VOLTS=value`
* `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
* `--model=value`  &rarr;  `CM_MLPERF_CUSTOM_MODEL_PATH=value`
* `--multistream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY=value`
* `--network=value`  &rarr;  `CM_NETWORK_LOADGEN=value`
* `--ntp_server=value`  &rarr;  `CM_MLPERF_POWER_NTP_SERVER=value`
* `--num_threads=value`  &rarr;  `CM_NUM_THREADS=value`
* `--offline_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS=value`
* `--output_dir=value`  &rarr;  `OUTPUT_BASE_DIR=value`
* `--power=value`  &rarr;  `CM_MLPERF_POWER=value`
* `--power_server=value`  &rarr;  `CM_MLPERF_POWER_SERVER_ADDRESS=value`
* `--regenerate_files=value`  &rarr;  `CM_REGENERATE_MEASURE_FILES=value`
* `--rerun=value`  &rarr;  `CM_RERUN=value`
* `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
* `--server_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_SERVER_TARGET_QPS=value`
* `--singlestream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY=value`
* `--sut_servers=value`  &rarr;  `CM_NETWORK_LOADGEN_SUT_SERVERS=value`
* `--target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_LATENCY=value`
* `--target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_QPS=value`
* `--test_query_count=value`  &rarr;  `CM_TEST_QUERY_COUNT=value`
* `--threads=value`  &rarr;  `CM_NUM_THREADS=value`

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "clean":...}
```

</details>

#### Default environment

<details>
<summary>Click here to expand this section.</summary>

These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.

* CM_MLPERF_LOADGEN_MODE: `accuracy`
* CM_MLPERF_LOADGEN_SCENARIO: `Offline`
* CM_OUTPUT_FOLDER_NAME: `test_results`
* CM_MLPERF_RUN_STYLE: `test`
* CM_TEST_QUERY_COUNT: `10`
* CM_MLPERF_QUANTIZATION: `False`
* CM_MLPERF_SUT_NAME_IMPLEMENTATION_PREFIX: `reference`
* CM_MLPERF_SUT_NAME_RUN_CONFIG_SUFFIX: ``

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-mlcommons-python/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * detect,cpu
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,python
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,cuda,_cudnn
       * `if (CM_MLPERF_DEVICE  == gpu AND CM_MLPERF_BACKEND in ['onnxruntime', 'tf', 'tflite', 'pytorch'])`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
     * get,nvidia,tensorrt
       * `if (CM_MLPERF_BACKEND  == tensorrt)`
       - CM script: [get-tensorrt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tensorrt)
     * get,generic-python-lib,_onnxruntime
       * `if (CM_MLPERF_BACKEND in ['onnxruntime', 'tvm-onnx'] AND CM_MLPERF_DEVICE in ['cpu', 'rocm'])`
       * CM names: `--adr.['ml-engine-onnxruntime', 'onnxruntime']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_onnxruntime_gpu
       * `if (CM_MLPERF_BACKEND in ['onnxruntime', 'tvm-onnx'] AND CM_MLPERF_DEVICE  == gpu) AND (CM_MODEL not in ['3d-unet-99', '3d-unet-99.9'])`
       * CM names: `--adr.['ml-engine-onnxruntime-cuda']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_onnxruntime
       * `if (CM_MLPERF_BACKEND  == onnxruntime AND CM_MLPERF_DEVICE  == gpu AND CM_MODEL in ['3d-unet-99', '3d-unet-99.9', 'resnet50'])`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_onnxruntime_gpu
       * `if (CM_MLPERF_BACKEND  == onnxruntime AND CM_MLPERF_DEVICE  == gpu AND CM_MODEL in ['3d-unet-99', '3d-unet-99.9', 'resnet50'])`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torch
       * `if (CM_MLPERF_BACKEND in ['pytorch', 'tvm-pytorch'] AND CM_MLPERF_DEVICE in ['cpu', 'rocm'])`
       * CM names: `--adr.['ml-engine-pytorch', 'pytorch']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torch_cuda
       * `if (CM_MLPERF_BACKEND in ['pytorch', 'tvm-pytorch', 'ray'] AND CM_MLPERF_DEVICE  == gpu)`
       * CM names: `--adr.['ml-engine-pytorch', 'pytorch']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torchvision
       * `if (CM_MLPERF_BACKEND in ['pytorch', 'tvm-pytorch'] AND CM_MLPERF_DEVICE  == cpu)`
       * CM names: `--adr.['ml-engine-torchvision']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torchvision_cuda
       * `if (CM_MLPERF_BACKEND in ['pytorch', 'tvm-pytorch', 'ray'] AND CM_MLPERF_DEVICE  == gpu)`
       * CM names: `--adr.['ml-engine-torchvision']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_tensorrt
       * `if (CM_MLPERF_BACKEND  == ray)`
       * CM names: `--adr.['ml-engine-tensorrt']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torch_tensorrt
       * `if (CM_MLPERF_BACKEND  == ray)`
       * CM names: `--adr.['ml-engine-torch_tensorrt']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_ray
       * `if (CM_MLPERF_BACKEND  == ray)`
       * CM names: `--adr.['ray']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_async_timeout
       * `if (CM_MLPERF_BACKEND  == ray)`
       * CM names: `--adr.['async_timeout']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_transformers
       * `if (CM_MODEL in ['bert-99', 'bert-99.9', 'gptj-99', 'gptj-99.9'])`
       * CM names: `--adr.['ml-engine-transformers']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_tensorflow
       * `if (CM_MLPERF_BACKEND in ['tf', 'tflite'])`
       * CM names: `--adr.['ml-engine-tensorflow', 'tensorflow']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_package.ncnn
       * `if (CM_MLPERF_BACKEND  == ncnn)`
       * CM names: `--adr.['ml-engine-ncnn']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,ml-model,neural-magic,zoo
       * `if (CM_MLPERF_NEURALMAGIC_MODEL_ZOO_STUB  == on)`
       * CM names: `--adr.['custom-ml-model']...`
       - CM script: [get-ml-model-neuralmagic-zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-neuralmagic-zoo)
     * get,ml-model,image-classification,resnet50
       * `if (CM_MODEL  == resnet50) AND (CM_MLPERF_CUSTOM_MODEL_PATH  != on)`
       * CM names: `--adr.['ml-model', 'resnet50-model']...`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * get,ml-model,object-detection,retinanet
       * `if (CM_MODEL  == retinanet)`
       * CM names: `--adr.['ml-model', 'retinanet-model']...`
       - CM script: [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
     * get,ml-model,large-language-model,gptj
       * `if (CM_MODEL in ['gptj-99', 'gptj-99.9'])`
       * CM names: `--adr.['ml-model', 'gptj-model', 'gpt-j-model']...`
       - CM script: [get-ml-model-gptj](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-gptj)
     * get,ml-model,object-detection,resnext50,fp32,_pytorch-weights
       * `if (CM_MLPERF_BACKEND  == pytorch AND CM_MLPERF_IMPLEMENTATION  == nvidia AND CM_MODEL  == retinanet)`
       * CM names: `--adr.['ml-model', 'retinanet-model']...`
       - *Warning: no scripts found*
     * get,ml-model,language-processing,bert-large
       * `if (CM_MODEL in ['bert-99', 'bert-99.9']) AND (CM_MLPERF_CUSTOM_MODEL_PATH  != on)`
       * CM names: `--adr.['ml-model', 'bert-model']...`
       - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
     * get,ml-model,stable-diffusion,text-to-image,sdxl
       * `if (CM_MODEL  == stable-diffusion-xl) AND (CM_MLPERF_CUSTOM_MODEL_PATH  != on)`
       * CM names: `--adr.['ml-model', 'sdxl-model']...`
       - CM script: [get-ml-model-stable-diffusion](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-stable-diffusion)
     * get,ml-model,llama2
       * `if (CM_MODEL in ['llama2-70b-99', 'llama2-70b-99.9']) AND (CM_MLPERF_CUSTOM_MODEL_PATH  != on)`
       * CM names: `--adr.['ml-model', 'llama2-model']...`
       - CM script: [get-ml-model-llama2](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-llama2)
     * get,ml-model,medical-imaging,3d-unet
       * `if (CM_MODEL in ['3d-unet-99', '3d-unet-99.9'])`
       * CM names: `--adr.['ml-model', '3d-unet-model']...`
       - CM script: [get-ml-model-3d-unet-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-3d-unet-kits19)
     * get,ml-model,speech-recognition,rnnt
       * `if (CM_MODEL  == rnnt)`
       * CM names: `--adr.['ml-model', 'rnnt-model']...`
       - CM script: [get-ml-model-rnnt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt)
     * get,ml-model,recommendation,dlrm
       * `if (CM_MODEL in ['dlrm-99', 'dlrm-99.9'])`
       * CM names: `--adr.['ml-model', 'dlrm-model']...`
       - CM script: [get-ml-model-dlrm-terabyte](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte)
     * get,dataset,image-classification,imagenet,preprocessed
       * `if (CM_MODEL  == resnet50) AND (CM_MLPERF_VISION_DATASET_OPTION  != True)`
       * CM names: `--adr.['imagenet-preprocessed']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,dataset,image-classification,imagenet,preprocessed,_pytorch
       * `if (CM_MODEL  == resnet50 AND CM_MLPERF_VISION_DATASET_OPTION  == imagenet_pytorch)`
       * CM names: `--adr.['imagenet-preprocessed']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,dataset-aux,image-classification,imagenet-aux
       * `if (CM_MODEL  == resnet50)`
       - CM script: [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)
     * get,dataset,object-detection,open-images,openimages,preprocessed,_validation
       * `if (CM_MODEL  == retinanet)`
       * CM names: `--adr.['openimages-preprocessed']...`
       - CM script: [get-preprocessed-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages)
     * get,dataset,cnndm,_validation
       * `if (CM_MODEL in ['gptj-99', 'gptj-99.9'])`
       * CM names: `--adr.['cnndm-preprocessed']...`
       - CM script: [get-dataset-cnndm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-cnndm)
     * get,dataset,squad,original
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       * CM names: `--adr.['cnndm-preprocessed']...`
       - CM script: [get-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad)
     * get,dataset-aux,squad-vocab
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       - CM script: [get-dataset-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad-vocab)
     * get,dataset,coco2014,_validation
       * `if (CM_MODEL  == stable-diffusion-xl)`
       * CM names: `--adr.['coco2014-preprocessed']...`
       - CM script: [get-dataset-coco2014](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-coco2014)
     * get,preprocessed,dataset,openorca,_validation
       * `if (CM_MODEL in ['llama2-70b-99', 'llama2-70b-99.9'])`
       * CM names: `--adr.['openorca-preprocessed']...`
       - CM script: [get-preprocessed-dataset-openorca](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openorca)
     * get,dataset,kits19,preprocessed
       * `if (CM_MODEL in ['3d-unet-99', '3d-unet-99.9'])`
       * CM names: `--adr.['kits19-preprocessed']...`
       - CM script: [get-preprocessed-dataset-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-kits19)
     * get,dataset,librispeech,preprocessed
       * `if (CM_MODEL  == rnnt)`
       * CM names: `--adr.['librispeech-preprocessed']...`
       - CM script: [get-preprocessed-dataset-librispeech](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-librispeech)
     * get,dataset,criteo,preprocessed
       * `if (CM_MODEL in ['dlrm-99', 'dlrm-99.9'])`
       * CM names: `--adr.['criteo-preprocessed']...`
       - CM script: [get-preprocessed-dataset-criteo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-criteo)
     * generate,user-conf,mlperf,inference
       * CM names: `--adr.['user-conf-generator']...`
       - CM script: [generate-mlperf-inference-user-conf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-user-conf)
     * get,loadgen
       * CM names: `--adr.['loadgen', 'mlperf-inference-loadgen']...`
       - CM script: [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,mlcommons,inference,src
       * CM names: `--adr.['mlperf-implementation']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,generic-python-lib,_package.psutil
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-mlcommons-python/customize.py)***
  1. ***Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-mlcommons-python/_cm.yaml)***
     * remote,run,cmds
       * `if (CM_ASSH_RUN_COMMANDS  == on)`
       * CM names: `--adr.['remote-run-cmds']...`
       - CM script: [remote-run-commands](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands)
  1. ***Run native script if exists***
  1. ***Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-mlcommons-python/_cm.yaml)***
     * benchmark-mlperf
       * `if (CM_MLPERF_SKIP_RUN  != on)`
       * CM names: `--adr.['mlperf-runner']...`
       - CM script: [benchmark-program-mlperf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program-mlperf)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-mlcommons-python/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-mlcommons-python/_cm.yaml)***
     * save,mlperf,inference,state
       * CM names: `--adr.['save-mlperf-inference-state']...`
       - CM script: [save-mlperf-inference-implementation-state](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/save-mlperf-inference-implementation-state)

___
### Script output
`cmr "app vision language mlcommons mlperf inference reference ref [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_DATASET_*`
* `CM_HW_NAME`
* `CM_MAX_EXAMPLES`
* `CM_MLPERF_*`
* `CM_ML_MODEL_*`
#### New environment keys auto-detected from customize

* `CM_MLPERF_BACKEND`
* `CM_MLPERF_CONF`
* `CM_MLPERF_DEVICE`
* `CM_MLPERF_LOADGEN_EXTRA_OPTIONS`
* `CM_MLPERF_LOADGEN_MODE`
* `CM_MLPERF_LOADGEN_QPS_OPT`
* `CM_MLPERF_LOADGEN_SCENARIO`
* `CM_MLPERF_OUTPUT_DIR`
* `CM_MLPERF_RUN_CMD`
* `CM_ML_MODEL_FILE_WITH_PATH`