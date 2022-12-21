*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
* [Variations](#variations)
  * [ All variations](#all-variations)
  * [ Variations by groups](#variations-by-groups)
* [Default environment](#default-environment)
* [CM script workflow](#cm-script-workflow)
* [New environment export](#new-environment-export)
* [New environment detected from customize](#new-environment-detected-from-customize)
* [Usage](#usage)
  * [ CM installation](#cm-installation)
  * [ CM script automation help](#cm-script-automation-help)
  * [ CM CLI](#cm-cli)
  * [ CM Python API](#cm-python-api)
  * [ CM modular Docker container](#cm-modular-docker-container)
  * [ Script input flags mapped to environment](#script-input-flags-mapped-to-environment)
* [Maintainers](#maintainers)

</details>

___
### About

*TBD*
___
### Category

Modular MLPerf benchmarks.
___
### Origin

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.yaml](_cm.yaml)

___
### Tags
app,vision,language,mlcommons,mlperf,inference,reference,ref

___
### Variations
#### All variations
* bert
* bert-99
  - *ENV CM_MODEL*: `bert-99`
* bert-99.9
  - *ENV CM_MODEL*: `bert-99.9`
* **cpu** (default)
  - *ENV CM_MLPERF_DEVICE*: `cpu`
  - *ENV CUDA_VISIBLE_DEVICES*: ``
  - *ENV USE_CUDA*: `False`
  - *ENV USE_GPU*: `False`
* cuda
  - *ENV CM_MLPERF_DEVICE*: `gpu`
  - *ENV USE_CUDA*: `True`
  - *ENV USE_GPU*: `True`
* fast
  - *ENV CM_FAST_FACTOR*: `5`
  - *ENV CM_OUTPUT_FOLDER_NAME*: `fast_results`
  - *ENV CM_MLPERF_RUN_STYLE*: `fast`
* **onnxruntime** (default)
  - *ENV CM_MLPERF_BACKEND*: `onnxruntime`
  - *ENV CM_MLPERF_BACKEND_VERSION*: `<<<CM_ONNXRUNTIME_VERSION>>>`
* **python** (default)
  - *ENV CM_MLPERF_PYTHON*: `yes`
  - *ENV CM_MLPERF_IMPLEMENTATION*: `reference`
* pytorch
  - *ENV CM_MLPERF_BACKEND*: `pytorch`
  - *ENV CM_MLPERF_BACKEND_VERSION*: `<<<CM_PYTORCH_VERSION>>>`
* quantized
  - *ENV CM_MLPERF_QUANTIZATION*: `True`
* r2.1_default
  - *ENV CM_RERUN*: `yes`
  - *ENV CM_SKIP_SYS_UTILS*: `yes`
  - *ENV CM_TEST_QUERY_COUNT*: `100`
* **resnet50** (default)
  - *ENV CM_MODEL*: `resnet50`
* retinanet
  - *ENV CM_MODEL*: `retinanet`
* tensorflow
* **test** (default)
  - *ENV CM_OUTPUT_FOLDER_NAME*: `test_results`
  - *ENV CM_MLPERF_RUN_STYLE*: `test`
* tf
  - *ENV CM_MLPERF_BACKEND*: `tf`
  - *ENV CM_MLPERF_BACKEND_VERSION*: `<<<CM_TENSORFLOW_VERSION>>>`
* tvm-onnx
  - *ENV CM_MLPERF_BACKEND*: `tvm-onnx`
  - *ENV CM_MLPERF_BACKEND_VERSION*: `<<<CM_ONNXRUNTIME_VERSION>>>`
* tvm-pytorch
  - *ENV CM_MLPERF_BACKEND*: `tvm-pytorch`
  - *ENV CM_MLPERF_BACKEND_VERSION*: `<<<CM_PYTORCH_VERSION>>>`
  - *ENV MLPERF_TVM_TORCH_QUANTIZED_ENGINE*: `qnnpack`
* valid
  - *ENV CM_OUTPUT_FOLDER_NAME*: `valid_results`
  - *ENV CM_MLPERF_RUN_STYLE*: `valid`

#### Variations by groups

  * device,
    * **cpu** (default)
      - *ENV CM_MLPERF_DEVICE*: `cpu`
      - *ENV CUDA_VISIBLE_DEVICES*: ``
      - *ENV USE_CUDA*: `False`
      - *ENV USE_GPU*: `False`
    * cuda
      - *ENV CM_MLPERF_DEVICE*: `gpu`
      - *ENV USE_CUDA*: `True`
      - *ENV USE_GPU*: `True`

  * execution-mode,
    * fast
      - *ENV CM_FAST_FACTOR*: `5`
      - *ENV CM_OUTPUT_FOLDER_NAME*: `fast_results`
      - *ENV CM_MLPERF_RUN_STYLE*: `fast`
    * **test** (default)
      - *ENV CM_OUTPUT_FOLDER_NAME*: `test_results`
      - *ENV CM_MLPERF_RUN_STYLE*: `test`
    * valid
      - *ENV CM_OUTPUT_FOLDER_NAME*: `valid_results`
      - *ENV CM_MLPERF_RUN_STYLE*: `valid`

  * framework,
    * **onnxruntime** (default)
      - *ENV CM_MLPERF_BACKEND*: `onnxruntime`
      - *ENV CM_MLPERF_BACKEND_VERSION*: `<<<CM_ONNXRUNTIME_VERSION>>>`
    * pytorch
      - *ENV CM_MLPERF_BACKEND*: `pytorch`
      - *ENV CM_MLPERF_BACKEND_VERSION*: `<<<CM_PYTORCH_VERSION>>>`
    * tf
      - *ENV CM_MLPERF_BACKEND*: `tf`
      - *ENV CM_MLPERF_BACKEND_VERSION*: `<<<CM_TENSORFLOW_VERSION>>>`
    * tvm-onnx
      - *ENV CM_MLPERF_BACKEND*: `tvm-onnx`
      - *ENV CM_MLPERF_BACKEND_VERSION*: `<<<CM_ONNXRUNTIME_VERSION>>>`
    * tvm-pytorch
      - *ENV CM_MLPERF_BACKEND*: `tvm-pytorch`
      - *ENV CM_MLPERF_BACKEND_VERSION*: `<<<CM_PYTORCH_VERSION>>>`
      - *ENV MLPERF_TVM_TORCH_QUANTIZED_ENGINE*: `qnnpack`

  * implementation,
    * **python** (default)
      - *ENV CM_MLPERF_PYTHON*: `yes`
      - *ENV CM_MLPERF_IMPLEMENTATION*: `reference`

  * models,
    * bert-99
      - *ENV CM_MODEL*: `bert-99`
    * bert-99.9
      - *ENV CM_MODEL*: `bert-99.9`
    * **resnet50** (default)
      - *ENV CM_MODEL*: `resnet50`
    * retinanet
      - *ENV CM_MODEL*: `retinanet`
___
### Default environment

* CM_BATCH_COUNT: **1**
* CM_BATCH_SIZE: **1**
* CM_MLPERF_LOADGEN_MODE: **accuracy**
* CM_MLPERF_LOADGEN_SCENARIO: **Offline**
* CM_OUTPUT_FOLDER_NAME: **test_results**
* CM_MLPERF_RUN_STYLE: **test**
* CM_TEST_QUERY_COUNT: **10**
* CM_MLPERF_QUANTIZATION: **False**
___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference/_cm.yaml)***
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
       * `if (CM_MLPERF_DEVICE  == gpu)`
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
     * get,nvidia,tensorrt
       * `if (CM_MLPERF_DEVICE  == gpu)`
       - CM script: [get-tensorrt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tensorrt)
     * get,generic-python-lib,_onnxruntime
       * `if (CM_MLPERF_BACKEND in ['onnxruntime', 'tvm-onnx'] AND CM_MLPERF_DEVICE  == cpu)`
       * CM names: `--adr.['ml-engine-onnxruntime']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_onnxruntime_gpu
       * `if (CM_MLPERF_BACKEND in ['onnxruntime', 'tvm-onnx'] AND CM_MLPERF_DEVICE  == gpu)`
       * CM names: `--adr.['ml-engine-onnxruntime-cuda']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torch
       * `if (CM_MLPERF_BACKEND in ['pytorch', 'tvm-pytorch'])`
       * CM names: `--adr.['ml-engine-pytorch']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_torchvision
       * `if (CM_MLPERF_BACKEND in ['pytorch', 'tvm-pytorch'])`
       * CM names: `--adr.['ml-engine-torchvision']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_transformers
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       * CM names: `--adr.['ml-engine-transformers']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,generic-python-lib,_tensorflow
       * `if (CM_MLPERF_BACKEND in ['tf', 'tflite'])`
       * CM names: `--adr.['ml-engine-tensorflow']...`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
     * get,loadgen
       * CM names: `--adr.['loadgen']...`
       - CM script: [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,sut,configs
       - CM script: [get-mlperf-inference-sut-configs](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs)
     * get,dataset,image-classification,imagenet,preprocessed
       * `if (CM_MODEL  == resnet50)`
       * CM names: `--adr.['imagenet-preprocessed']...`
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
     * get,dataset-aux,image-classification,imagenet-aux
       * `if (CM_MODEL  == resnet50)`
       - CM script: [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)
     * get,dataset,object-detection,open-images,openimages,preprocessed,_validation
       * `if (CM_MODEL  == retinanet)`
       * CM names: `--adr.['openimages-preprocessed']...`
       - CM script: [get-preprocessed-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages)
     * get,dataset,squad,original
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       - CM script: [get-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad)
     * get,ml-model,raw,image-classification,resnet50,_onnx
       * `if (CM_MLPERF_BACKEND  == onnxruntime AND CM_MODEL  == resnet50)`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * get,ml-model,tvm-model,resnet50,_onnx
       * `if (CM_MLPERF_BACKEND  == tvm-onnx AND CM_MODEL  == resnet50)`
       * CM names: `--adr.['resnet50-model', 'ml-model', 'tvm-model']...`
       - CM script: [get-ml-model-resnet50-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm)
     * get,ml-model,raw,image-classification,resnet50,_tensorflow
       * `if (CM_MLPERF_BACKEND in ['tf', 'tflite'] AND CM_MODEL  == resnet50)`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * get,ml-model,raw,image-classification,resnet50,_pytorch,_fp32
       * `if (CM_MLPERF_BACKEND  == pytorch AND CM_MODEL  == resnet50)`
       * CM names: `--adr.['resnet50-model', 'ml-model']...`
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
     * get,ml-model,tvm-model,resnet50,_pytorch,_int8
       * `if (CM_MLPERF_BACKEND  == tvm-pytorch AND CM_MODEL  == resnet50)`
       * CM names: `--adr.['resnet50-model', 'ml-model', 'tvm-model']...`
       - CM script: [get-ml-model-resnet50-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm)
     * get,ml-model,object-detection,retinanet,_onnx,_fp32
       * `if (CM_MLPERF_BACKEND  == onnxruntime AND CM_MODEL  == retinanet)`
       - CM script: [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
     * get,ml-model,object-detection,retinanet,_pytorch,_fp32
       * `if (CM_MLPERF_BACKEND  == pytorch AND CM_MODEL  == retinanet) AND (CM_MLPERF_IMPLEMENTATION  != nvidia)`
       - CM script: [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
     * get,ml-model,object-detection,resnext50,fp32,_pytorch-weights
       * `if (CM_MLPERF_BACKEND  == pytorch AND CM_MLPERF_IMPLEMENTATION  == nvidia AND CM_MODEL  == retinanet)`
       - *Warning: no scripts found*
     * get,ml-model,language-processing,bert,_onnx,_fp32
       * `if (CM_MLPERF_BACKEND  == onnxruntime AND CM_MODEL in ['bert-99', 'bert-99.9']) AND (CM_MLPERF_QUANTIZATION  != True)`
       - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
     * get,ml-model,language-processing,bert,_onnx,_int8
       * `if (CM_MLPERF_BACKEND  == onnxruntime AND CM_MODEL  == bert-99 AND CM_MLPERF_QUANTIZATION  == True)`
       - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
     * get,ml-model,language-processing,bert,_tf
       * `if (CM_MLPERF_BACKEND  == tf AND CM_MODEL in ['bert-99', 'bert-99.9'])`
       - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
     * get,ml-model,language-processing,bert,_pytorch,_fp32
       * `if (CM_MLPERF_BACKEND in ['pytorch', 'tvm-pytorch'] AND CM_MODEL in ['bert-99', 'bert-99.9'])`
       - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
     * get,generic-python-lib,_tokenization
       * `if (CM_MODEL in ['bert-99', 'bert-99.9'])`
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference/_cm.yaml)
  1. ***Run native script if exists***
  1. ***Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference/_cm.yaml)***
     * benchmark,program
       * CM names: `--adr.['runner']...`
       - CM script: [benchmark-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference/_cm.yaml)
___
### New environment export

* **CM_DATASET_***
* **CM_MLPERF_***
___
### New environment detected from customize

* **CM_MLPERF_CONF**
* **CM_MLPERF_LOADGEN_EXTRA_OPTIONS**
* **CM_MLPERF_LOADGEN_MODE**
* **CM_MLPERF_LOADGEN_QPS_OPT**
* **CM_MLPERF_LOADGEN_SCENARIO**
* **CM_MLPERF_OUTPUT_DIR**
* **CM_MLPERF_RESULTS_DIR**
* **CM_MLPERF_RUN_CMD**
* **CM_MODEL**
* **CM_NUM_THREADS**
* **CM_PYTHON_BIN_WITH_PATH**
* **CM_RUN_CMD**
* **CM_RUN_DIR**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="app,vision,language,mlcommons,mlperf,inference,reference,ref"`

*or*

`cm run script "app vision language mlcommons mlperf inference reference ref"`

*or*

`cm run script ff149e9781fc4b65`

#### CM Python API

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

#### CM modular Docker container
*TBD*

#### Script input flags mapped to environment

* count --> **CM_MLPERF_LOADGEN_QUERY_COUNT**
* docker --> **CM_RUN_DOCKER_CONTAINER**
* hw_name --> **CM_HW_NAME**
* imagenet_path --> **IMAGENET_PATH**
* max_batchsize --> **CM_MLPERF_LOADGEN_MAX_BATCHSIZE**
* mode --> **CM_MLPERF_LOADGEN_MODE**
* num_threads --> **CM_NUM_THREADS**
* output_dir --> **OUTPUT_BASE_DIR**
* power --> **CM_SYSTEM_POWER**
* regenerate_files --> **CM_REGENERATE_MEASURE_FILES**
* rerun --> **CM_RERUN**
* scenario --> **CM_MLPERF_LOADGEN_SCENARIO**
* test_query_count --> **CM_TEST_QUERY_COUNT**
* clean --> **CM_MLPERF_CLEAN_SUBMISSION_DIR**

Examples:

```bash
cm run script "app vision language mlcommons mlperf inference reference ref" --count=...
```
```python
r=cm.access({... , "count":"..."}
```
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)