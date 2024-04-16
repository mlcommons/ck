**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference).**



Automatically generated README for this automation recipe: **app-mlperf-inference**

Category: **Modular MLPerf inference benchmark pipeline**

License: **Apache 2.0**

Developers: [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh), [Thomas Zhu](https://www.linkedin.com/in/hanwen-zhu-483614189), [Grigori Fursin](https://cKnowledge.org/gfursin)

---
*[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name=app-mlperf-inference,d775cac873ee4231) ] [ [Notes from the authors, contributors and users](README-extra.md) ]*

---

﻿This CM script provides a unified interface to prepare and run a modular version of the [MLPerf inference benchmark](https://arxiv.org/abs/1911.02549)
across diverse ML models, data sets, frameworks, libraries, run-time systems and platforms
using the [cross-platform automation meta-framework (MLCommons CM)](https://github.com/mlcommons/ck).

It is assembled from reusable and interoperable [CM scripts for DevOps and MLOps](../list_of_scripts.md)
being developed by the [open MLCommons taskforce on automation and reproducibility](../mlperf-education-workgroup.md).

It is a higher-level wrapper to several other CM scripts modularizing the MLPerf inference benchmark:
* [Reference Python implementation](../app-mlperf-inference-reference)
* [Universal C++ implementation](../app-mlperf-inference-cpp)
* [TFLite C++ implementation](../app-mlperf-inference-tflite-cpp)
* [NVidia optimized implementation](app-mlperf-inference-nvidia)

See [this SCC'23 tutorial](https://github.com/mlcommons/ck/blob/master/docs/tutorials/sc22-scc-mlperf.md) 
to use this script to run a reference (unoptimized) Python implementation of the MLPerf object detection benchmark 
with RetinaNet model, Open Images dataset, ONNX runtime and CPU target.

See this [CM script](../run-mlperf-inference-app) to automate and validate your MLPerf inference submission.

Get in touch with the [open taskforce on automation and reproducibility at MLCommons](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)
if you need help with your submission or if you would like to participate in further modularization of MLPerf 
and collaborative design space exploration and optimization of ML Systems.


---
#### Summary

* CM GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops)*
* GitHub directory for this script: *[GitHub](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference)*
* CM meta description for this script: *[_cm.yaml](_cm.yaml)*
* All CM tags to find and reuse this script (see in above meta description): *app,vision,language,mlcommons,mlperf,inference,generic*
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

````cmr "app vision language mlcommons mlperf inference generic" --help````

#### Customize and run this script from the command line with different variations and flags

`cm run script --tags=app,vision,language,mlcommons,mlperf,inference,generic`

`cm run script --tags=app,vision,language,mlcommons,mlperf,inference,generic[,variations] [--input_flags]`

*or*

`cmr "app vision language mlcommons mlperf inference generic"`

`cmr "app vision language mlcommons mlperf inference generic [variations]" [--input_flags]`


* *See the list of `variations` [here](#variations) and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.*


#### Input Flags

* --**scenario**=MLPerf inference scenario {Offline,Server,SingleStream,MultiStream} (*Offline*)
* --**mode**=MLPerf inference mode {performance,accuracy} (*accuracy*)
* --**test_query_count**=Specifies the number of samples to be processed during a test run
* --**target_qps**=Target QPS
* --**target_latency**=Target Latency
* --**max_batchsize**=Maximum batchsize to be used
* --**num_threads**=Number of CPU threads to launch the application with
* --**hw_name**=Valid value - any system description which has a config file (under same name) defined [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-configs-sut-mlperf-inference/configs)
* --**output_dir**=Location where the outputs are produced
* --**rerun**=Redo the run even if previous run files exist (*True*)
* --**regenerate_files**=Regenerates measurement files including accuracy.txt files even if a previous run exists. This option is redundant if `--rerun` is used
* --**adr.python.name**=Python virtual environment name (optional) (*mlperf*)
* --**adr.python.version_min**=Minimal Python version (*3.8*)
* --**adr.python.version**=Force Python version (must have all system deps)
* --**adr.compiler.tags**=Compiler for loadgen (*gcc*)
* --**adr.inference-src-loadgen.env.CM_GIT_URL**=Git URL for MLPerf inference sources to build LoadGen (to enable non-reference implementations)
* --**adr.inference-src.env.CM_GIT_URL**=Git URL for MLPerf inference sources to run benchmarks (to enable non-reference implementations)
* --**quiet**=Quiet run (select default values for all questions) (*False*)
* --**readme**=Generate README with the reproducibility report
* --**debug**=Debug MLPerf script

**Above CLI flags can be used in the Python CM API as follows:**

```python
r=cm.access({... , "scenario":...}
```
#### Run this script from Python

<details>
<summary>Click here to expand this section.</summary>

```python

import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'app,vision,language,mlcommons,mlperf,inference,generic'
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

```cmr "cm gui" --script="app,vision,language,mlcommons,mlperf,inference,generic"```

Use this [online GUI](https://cKnowledge.org/cm-gui/?tags=app,vision,language,mlcommons,mlperf,inference,generic) to generate CM CMD.

#### Run this script via Docker (beta)

`cm docker script "app vision language mlcommons mlperf inference generic[variations]" [--input_flags]`

___
### Customization


#### Variations

  * Group "**implementation**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_cpp`
      - Aliases: `_mil,_mlcommons-cpp`
      - Environment variables:
        - *CM_MLPERF_CPP*: `yes`
        - *CM_MLPERF_IMPLEMENTATION*: `mlcommons_cpp`
        - *CM_IMAGENET_ACCURACY_DTYPE*: `float32`
        - *CM_OPENIMAGES_ACCURACY_DTYPE*: `float32`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * app,mlperf,cpp,inference
             * `if (CM_SKIP_RUN  != True)`
             * CM names: `--adr.['cpp-mlperf-inference', 'mlperf-inference-implementation']...`
             - CM script: [app-mlperf-inference-mlcommons-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-mlcommons-cpp)
    * `_intel-original`
      - Aliases: `_intel`
      - Environment variables:
        - *CM_MLPERF_IMPLEMENTATION*: `intel`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * reproduce,mlperf,inference,intel
             * `if (CM_SKIP_RUN  != True)`
             * CM names: `--adr.['intel', 'intel-harness', 'mlperf-inference-implementation']...`
             - CM script: [app-mlperf-inference-intel](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-intel)
    * `_kilt`
      - Aliases: `_qualcomm`
      - Environment variables:
        - *CM_MLPERF_IMPLEMENTATION*: `qualcomm`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * reproduce,mlperf,inference,kilt
             * `if (CM_SKIP_RUN  != True)`
             * CM names: `--adr.['kilt', 'kilt-harness', 'mlperf-inference-implementation']...`
             - CM script: [app-mlperf-inference-qualcomm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-qualcomm)
    * `_nvidia-original`
      - Aliases: `_nvidia`
      - Environment variables:
        - *CM_MLPERF_IMPLEMENTATION*: `nvidia`
        - *CM_SQUAD_ACCURACY_DTYPE*: `float16`
        - *CM_IMAGENET_ACCURACY_DTYPE*: `int32`
        - *CM_CNNDM_ACCURACY_DTYPE*: `int32`
        - *CM_LIBRISPEECH_ACCURACY_DTYPE*: `int8`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,cuda-devices
             * `if (CM_CUDA_DEVICE_PROP_GLOBAL_MEMORY not in ['yes', 'on'])`
             - CM script: [get-cuda-devices](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-devices)
        1. ***Read "prehook_deps" on other CM scripts***
           * reproduce,mlperf,nvidia,inference,_run_harness
             * `if (CM_SKIP_RUN  != True)`
             * CM names: `--adr.['nvidia-original-mlperf-inference', 'nvidia-harness', 'mlperf-inference-implementation']...`
             - CM script: [app-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-nvidia)
    * **`_reference`** (default)
      - Aliases: `_mlcommons-python,_python`
      - Environment variables:
        - *CM_MLPERF_PYTHON*: `yes`
        - *CM_MLPERF_IMPLEMENTATION*: `mlcommons_python`
        - *CM_SQUAD_ACCURACY_DTYPE*: `float32`
        - *CM_IMAGENET_ACCURACY_DTYPE*: `float32`
        - *CM_OPENIMAGES_ACCURACY_DTYPE*: `float32`
        - *CM_LIBRISPEECH_ACCURACY_DTYPE*: `float32`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * app,mlperf,reference,inference
             * `if (CM_SKIP_RUN  != True)`
             * CM names: `--adr.['python-reference-mlperf-inference', 'mlperf-inference-implementation']...`
             - CM script: [app-mlperf-inference-mlcommons-python](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-mlcommons-python)
    * `_tflite-cpp`
      - Aliases: `_ctuning-cpp-tflite`
      - Environment variables:
        - *CM_MLPERF_TFLITE_CPP*: `yes`
        - *CM_MLPERF_CPP*: `yes`
        - *CM_MLPERF_IMPLEMENTATION*: `ctuning_cpp_tflite`
        - *CM_IMAGENET_ACCURACY_DTYPE*: `float32`
      - Workflow:
        1. ***Read "prehook_deps" on other CM scripts***
           * app,mlperf,tflite-cpp,inference
             * `if (CM_SKIP_RUN  != True)`
             * CM names: `--adr.['tflite-cpp-mlperf-inference', 'mlperf-inference-implementation']...`
             - CM script: [app-mlperf-inference-ctuning-cpp-tflite](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-ctuning-cpp-tflite)

    </details>


  * Group "**backend**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_deepsparse`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `deepsparse`
      - Workflow:
    * `_glow`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `glow`
      - Workflow:
    * `_ncnn`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `ncnn`
      - Workflow:
    * `_onnxruntime`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `onnxruntime`
      - Workflow:
    * `_pytorch`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `pytorch`
      - Workflow:
    * `_ray`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `ray`
      - Workflow:
    * `_tensorrt`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tensorrt`
      - Workflow:
    * `_tf`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tf`
      - Workflow:
    * `_tflite`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tflite`
      - Workflow:
    * `_tvm-onnx`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tvm-onnx`
      - Workflow:
    * `_tvm-pytorch`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tvm-pytorch`
      - Workflow:
    * `_tvm-tflite`
      - Environment variables:
        - *CM_MLPERF_BACKEND*: `tvm-tflite`
      - Workflow:

    </details>


  * Group "**device**"
    <details>
    <summary>Click here to expand this section.</summary>

    * **`_cpu`** (default)
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `cpu`
      - Workflow:
    * `_cuda`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `gpu`
      - Workflow:
    * `_qaic`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `qaic`
      - Workflow:
    * `_rocm`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `rocm`
      - Workflow:
    * `_tpu`
      - Environment variables:
        - *CM_MLPERF_DEVICE*: `tpu`
      - Workflow:

    </details>


  * Group "**model**"
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
    * `_dlrm-v2-99`
      - Environment variables:
        - *CM_MODEL*: `dlrm-v2-99`
      - Workflow:
    * `_dlrm-v2-99.9`
      - Environment variables:
        - *CM_MODEL*: `dlrm-v2-99.9`
      - Workflow:
    * `_efficientnet`
      - Environment variables:
        - *CM_MODEL*: `efficientnet`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,dataset-aux,imagenet-aux
             - CM script: [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)
        1. ***Read "posthook_deps" on other CM scripts***
           * run,accuracy,mlperf,_imagenet
             * `if (CM_MLPERF_LOADGEN_MODE in ['accuracy', 'all'] AND CM_MLPERF_ACCURACY_RESULTS_DIR  == on)`
             * CM names: `--adr.['mlperf-accuracy-script', 'imagenet-accuracy-script']...`
             - CM script: [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)
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
    * `_mobilenet`
      - Environment variables:
        - *CM_MODEL*: `mobilenet`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,dataset-aux,imagenet-aux
             - CM script: [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)
        1. ***Read "posthook_deps" on other CM scripts***
           * run,accuracy,mlperf,_imagenet
             * `if (CM_MLPERF_LOADGEN_MODE in ['accuracy', 'all'] AND CM_MLPERF_ACCURACY_RESULTS_DIR  == on)`
             * CM names: `--adr.['mlperf-accuracy-script', 'imagenet-accuracy-script']...`
             - CM script: [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)
    * **`_resnet50`** (default)
      - Environment variables:
        - *CM_MODEL*: `resnet50`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,dataset-aux,imagenet-aux
             - CM script: [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)
        1. ***Read "posthook_deps" on other CM scripts***
           * run,accuracy,mlperf,_imagenet
             * `if (CM_MLPERF_LOADGEN_MODE in ['accuracy', 'all'] AND CM_MLPERF_ACCURACY_RESULTS_DIR  == on)`
             * CM names: `--adr.['mlperf-accuracy-script', 'imagenet-accuracy-script']...`
             - CM script: [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)
    * `_retinanet`
      - Environment variables:
        - *CM_MODEL*: `retinanet`
      - Workflow:
        1. ***Read "posthook_deps" on other CM scripts***
           * run,accuracy,mlperf,_openimages
             * `if (CM_MLPERF_LOADGEN_MODE in ['accuracy', 'all'] AND CM_MLPERF_ACCURACY_RESULTS_DIR  == on)`
             * CM names: `--adr.['mlperf-accuracy-script', 'openimages-accuracy-script']...`
             - CM script: [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)
    * `_rnnt`
      - Environment variables:
        - *CM_MODEL*: `rnnt`
      - Workflow:
        1. ***Read "posthook_deps" on other CM scripts***
           * run,accuracy,mlperf,_librispeech
             * `if (CM_MLPERF_LOADGEN_MODE in ['accuracy', 'all'] AND CM_MLPERF_ACCURACY_RESULTS_DIR  == on) AND (CM_MLPERF_IMPLEMENTATION  != nvidia)`
             * CM names: `--adr.['mlperf-accuracy-script', 'librispeech-accuracy-script']...`
             - CM script: [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)
    * `_sdxl`
      - Environment variables:
        - *CM_MODEL*: `stable-diffusion-xl`
      - Workflow:
        1. ***Read "posthook_deps" on other CM scripts***
           * run,accuracy,mlperf,_coco2014
             * `if (CM_MLPERF_LOADGEN_MODE in ['accuracy', 'all'] AND CM_MLPERF_ACCURACY_RESULTS_DIR  == on) AND (CM_MLPERF_IMPLEMENTATION  != nvidia)`
             * CM names: `--adr.['mlperf-accuracy-script', 'coco2014-accuracy-script']...`
             - CM script: [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)

    </details>


  * Group "**precision**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_bfloat16`
      - Environment variables:
        - *CM_MLPERF_QUANTIZATION*: `False`
        - *CM_MLPERF_MODEL_PRECISION*: `float32`
      - Workflow:
    * `_float16`
      - Environment variables:
        - *CM_MLPERF_QUANTIZATION*: `False`
        - *CM_MLPERF_MODEL_PRECISION*: `float32`
      - Workflow:
    * **`_float32`** (default)
      - Aliases: `_fp32`
      - Environment variables:
        - *CM_MLPERF_QUANTIZATION*: `False`
        - *CM_MLPERF_MODEL_PRECISION*: `float32`
      - Workflow:
    * `_int4`
      - Environment variables:
        - *CM_MLPERF_QUANTIZATION*: `True`
        - *CM_MLPERF_MODEL_PRECISION*: `int4`
      - Workflow:
    * `_int8`
      - Aliases: `_quantized`
      - Environment variables:
        - *CM_MLPERF_QUANTIZATION*: `True`
        - *CM_MLPERF_MODEL_PRECISION*: `int8`
      - Workflow:
    * `_uint8`
      - Environment variables:
        - *CM_MLPERF_QUANTIZATION*: `True`
        - *CM_MLPERF_MODEL_PRECISION*: `uint8`
      - Workflow:

    </details>


  * Group "**execution-mode**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_fast`
      - Environment variables:
        - *CM_FAST_FACTOR*: `5`
        - *CM_OUTPUT_FOLDER_NAME*: `fast_results`
        - *CM_MLPERF_RUN_STYLE*: `fast`
      - Workflow:
    * **`_test`** (default)
      - Environment variables:
        - *CM_OUTPUT_FOLDER_NAME*: `test_results`
        - *CM_MLPERF_RUN_STYLE*: `test`
      - Workflow:
    * `_valid`
      - Environment variables:
        - *CM_OUTPUT_FOLDER_NAME*: `valid_results`
        - *CM_MLPERF_RUN_STYLE*: `valid`
      - Workflow:

    </details>


  * Group "**reproducibility**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_r2.1_default`
      - Environment variables:
        - *CM_SKIP_SYS_UTILS*: `yes`
        - *CM_TEST_QUERY_COUNT*: `100`
      - Workflow:
    * `_r3.0_default`
      - Environment variables:
        - *CM_SKIP_SYS_UTILS*: `yes`
      - Workflow:
    * `_r3.1_default`
      - Workflow:
    * `_r4.0_default`
      - Workflow:

    </details>


  * *Internal group (variations should not be selected manually)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_3d-unet_`
      - Environment variables:
        - *CM_MLPERF_MODEL_EQUAL_ISSUE_MODE*: `yes`
      - Workflow:
        1. ***Read "posthook_deps" on other CM scripts***
           * run,accuracy,mlperf,_kits19,_int8
             * `if (CM_MLPERF_LOADGEN_MODE in ['accuracy', 'all'] AND CM_MLPERF_ACCURACY_RESULTS_DIR  == on) AND (CM_MLPERF_IMPLEMENTATION  != nvidia)`
             * CM names: `--adr.['mlperf-accuracy-script', '3d-unet-accuracy-script']...`
             - CM script: [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)
    * `_bert_`
      - Workflow:
        1. ***Read "deps" on other CM scripts***
           * get,dataset,squad,language-processing
             * `if (CM_DATASET_SQUAD_VAL_PATH not in on)`
             - CM script: [get-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad)
           * get,dataset-aux,squad-vocab
             * `if (CM_ML_MODEL_BERT_VOCAB_FILE_WITH_PATH not in on)`
             - CM script: [get-dataset-squad-vocab](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad-vocab)
        1. ***Read "posthook_deps" on other CM scripts***
           * run,accuracy,mlperf,_squad
             * `if (CM_MLPERF_LOADGEN_MODE in ['accuracy', 'all'] AND CM_MLPERF_ACCURACY_RESULTS_DIR  == on)`
             * CM names: `--adr.['squad-accuracy-script', 'mlperf-accuracy-script']...`
             - CM script: [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)
    * `_dlrm_`
      - Workflow:
        1. ***Read "posthook_deps" on other CM scripts***
           * run,accuracy,mlperf,_terabyte,_float32
             * `if (CM_MLPERF_LOADGEN_MODE in ['accuracy', 'all'] AND CM_MLPERF_ACCURACY_RESULTS_DIR  == on)`
             * CM names: `--adr.['terabyte-accuracy-script', 'mlperf-accuracy-script']...`
             - CM script: [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)
    * `_gptj_`
      - Aliases: `_gptj`
      - Environment variables:
        - *CM_MLPERF_MODEL_EQUAL_ISSUE_MODE*: `yes`
      - Workflow:
        1. ***Read "posthook_deps" on other CM scripts***
           * run,accuracy,mlperf,_cnndm
             * `if (CM_MLPERF_LOADGEN_MODE in ['accuracy', 'all'] AND CM_MLPERF_ACCURACY_RESULTS_DIR  == on) AND (CM_MLPERF_IMPLEMENTATION  != intel)`
             * CM names: `--adr.['cnndm-accuracy-script', 'mlperf-accuracy-script']...`
             - CM script: [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)
    * `_intel-original,gptj_`
      - Workflow:
    * `_llama2-70b_`
      - Environment variables:
        - *CM_MLPERF_MODEL_EQUAL_ISSUE_MODE*: `yes`
      - Workflow:
        1. ***Read "posthook_deps" on other CM scripts***
           * run,accuracy,mlperf,_open-orca,_int32
             * `if (CM_MLPERF_LOADGEN_MODE in ['accuracy', 'all'] AND CM_MLPERF_ACCURACY_RESULTS_DIR  == on) AND (CM_MLPERF_IMPLEMENTATION  != nvidia)`
             * CM names: `--adr.['mlperf-accuracy-script', 'open-orca-accuracy-script']...`
             - CM script: [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)
    * `_reference,bert_`
      - Workflow:
    * `_reference,dlrm-v2_`
      - Workflow:
    * `_reference,gptj_`
      - Workflow:
    * `_reference,llama2-70b_`
      - Workflow:
    * `_reference,sdxl_`
      - Workflow:

    </details>


  * *No group (any variation can be selected)*
    <details>
    <summary>Click here to expand this section.</summary>

    * `_intel-original,bert-99`
      - Workflow:
    * `_intel-original,bert-99.9`
      - Workflow:
    * `_intel-original,gptj-99`
      - Workflow:
    * `_intel-original,gptj-99.9`
      - Workflow:
    * `_intel-original,gptj_,build-harness`
      - Workflow:
    * `_intel-original,resnet50`
      - Workflow:
    * `_intel-original,retinanet`
      - Workflow:
    * `_kilt,qaic,bert-99`
      - Workflow:
    * `_kilt,qaic,bert-99.9`
      - Workflow:
    * `_kilt,qaic,resnet50`
      - Workflow:
    * `_kilt,qaic,retinanet`
      - Workflow:
    * `_power`
      - Environment variables:
        - *CM_MLPERF_POWER*: `yes`
        - *CM_SYSTEM_POWER*: `yes`
      - Workflow:
    * `_reference,resnet50`
      - Workflow:
    * `_reference,retinanet`
      - Workflow:
    * `_rnnt,reference`
      - Environment variables:
        - *CM_MLPERF_PRINT_SUMMARY*: `no`
      - Workflow:
    * `_valid,retinanet`
      - Workflow:

    </details>


  * Group "**batch_size**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_batch_size.#`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_MAX_BATCHSIZE*: `#`
      - Workflow:

    </details>


  * Group "**loadgen-scenario**"
    <details>
    <summary>Click here to expand this section.</summary>

    * `_multistream`
      - Environment variables:
        - *CM_MLPERF_LOADGEN_SCENARIO*: `MultiStream`
      - Workflow:
    * **`_offline`** (default)
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


#### Unsupported or invalid variation combinations



* `_resnet50,_pytorch`
* `_retinanet,_tf`
* `_nvidia-original,_tf`
* `_nvidia-original,_onnxruntime`
* `_nvidia-original,_pytorch`
* `_nvidia,_tf`
* `_nvidia,_onnxruntime`
* `_nvidia,_pytorch`
* `_gptj,_tf`

#### Default variations

`_cpu,_float32,_offline,_reference,_resnet50,_test`

#### Script flags mapped to environment
<details>
<summary>Click here to expand this section.</summary>

* `--clean=value`  &rarr;  `CM_MLPERF_CLEAN_SUBMISSION_DIR=value`
* `--count=value`  &rarr;  `CM_MLPERF_LOADGEN_QUERY_COUNT=value`
* `--debug=value`  &rarr;  `CM_DEBUG_SCRIPT_BENCHMARK_PROGRAM=value`
* `--docker=value`  &rarr;  `CM_RUN_DOCKER_CONTAINER=value`
* `--gpu_name=value`  &rarr;  `CM_NVIDIA_GPU_NAME=value`
* `--hw_name=value`  &rarr;  `CM_HW_NAME=value`
* `--imagenet_path=value`  &rarr;  `IMAGENET_PATH=value`
* `--max_amps=value`  &rarr;  `CM_MLPERF_POWER_MAX_AMPS=value`
* `--max_batchsize=value`  &rarr;  `CM_MLPERF_LOADGEN_MAX_BATCHSIZE=value`
* `--max_volts=value`  &rarr;  `CM_MLPERF_POWER_MAX_VOLTS=value`
* `--mode=value`  &rarr;  `CM_MLPERF_LOADGEN_MODE=value`
* `--multistream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY=value`
* `--ntp_server=value`  &rarr;  `CM_MLPERF_POWER_NTP_SERVER=value`
* `--num_threads=value`  &rarr;  `CM_NUM_THREADS=value`
* `--offline_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS=value`
* `--output_dir=value`  &rarr;  `OUTPUT_BASE_DIR=value`
* `--power=value`  &rarr;  `CM_MLPERF_POWER=value`
* `--power_server=value`  &rarr;  `CM_MLPERF_POWER_SERVER_ADDRESS=value`
* `--readme=value`  &rarr;  `CM_MLPERF_README=value`
* `--regenerate_files=value`  &rarr;  `CM_REGENERATE_MEASURE_FILES=value`
* `--rerun=value`  &rarr;  `CM_RERUN=value`
* `--scenario=value`  &rarr;  `CM_MLPERF_LOADGEN_SCENARIO=value`
* `--server_target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_SERVER_TARGET_QPS=value`
* `--singlestream_target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY=value`
* `--target_latency=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_LATENCY=value`
* `--target_qps=value`  &rarr;  `CM_MLPERF_LOADGEN_TARGET_QPS=value`
* `--test_query_count=value`  &rarr;  `CM_TEST_QUERY_COUNT=value`

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

</details>

___
### Dependencies on other CM scripts


  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference/_cm.yaml)***
     * detect,os
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
     * get,sys-utils-cm
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
     * get,python
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,mlcommons,inference,src
       * CM names: `--adr.['inference-src']...`
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
     * get,mlperf,inference,utils
       - CM script: [get-mlperf-inference-utils](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-utils)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference/_cm.yaml)
  1. ***Run native script if exists***
     * [run.sh](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference/run.sh)
  1. ***Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference/_cm.yaml)***
     * get,mlperf,sut,description
       - CM script: [get-mlperf-inference-sut-description](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference/customize.py)***
  1. Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference/_cm.yaml)

___
### Script output
`cmr "app vision language mlcommons mlperf inference generic [,variations]" [--input_flags] -j`
#### New environment keys (filter)

* `CM_MLPERF_*`
#### New environment keys auto-detected from customize

* `CM_MLPERF_LOADGEN_COMPLIANCE_TEST`