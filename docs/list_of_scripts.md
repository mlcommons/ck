[ [Back to index](README.md) ]

<!--
This file is generated automatically - don't edit!
-->

This is an automatically generated list of reusable CM scripts being developed
by the [open taskforce on education and reproducibility](https://github.com/mlcommons/ck/issues/536) 
to make MLOps and DevOps tools more interoperable, portable, deterministic and reproducible.
These scripts suppport the community effort to modularize ML Systems and automate their bechmarking, optimization,
design space exploration and deployment across continuously changing software and hardware. 

# List of CM scripts by categories

### Modular MLPerf benchmarks

* [app-loadgen-generic-python](#app-loadgen-generic-python)
* [app-mlperf-inference](#app-mlperf-inference)
* [app-mlperf-inference-cpp](#app-mlperf-inference-cpp)
* [app-mlperf-inference-nvidia-harness](#app-mlperf-inference-nvidia-harness)
* [app-mlperf-inference-reference](#app-mlperf-inference-reference)
* [generate-mlperf-inference-submission](#generate-mlperf-inference-submission)
* [generate-mlperf-tiny-submission](#generate-mlperf-tiny-submission)
* [get-mlperf-inference-loadgen](#get-mlperf-inference-loadgen)
* [get-mlperf-inference-results](#get-mlperf-inference-results)
* [get-mlperf-inference-src](#get-mlperf-inference-src)
* [get-mlperf-inference-sut-configs](#get-mlperf-inference-sut-configs)
* [get-mlperf-inference-sut-description](#get-mlperf-inference-sut-description)
* [get-mlperf-power-dev](#get-mlperf-power-dev)
* [get-mlperf-training-src](#get-mlperf-training-src)
* [get-spec-ptd](#get-spec-ptd)
* [process-mlperf-accuracy](#process-mlperf-accuracy)
* [reproduce-mlperf-octoml-tinyml-results](#reproduce-mlperf-octoml-tinyml-results)
* [run-mlperf-inference-app](#run-mlperf-inference-app)
* [run-mlperf-inference-submission-checker](#run-mlperf-inference-submission-checker)
* [run-mlperf-power-client](#run-mlperf-power-client)
* [run-mlperf-power-server](#run-mlperf-power-server)
* [truncate-mlperf-inference-accuracy-log](#truncate-mlperf-inference-accuracy-log)
* [wrapper-reproduce-octoml-tinyml-submission](#wrapper-reproduce-octoml-tinyml-submission)

### Modular ML/AI applications

* [app-image-classification-onnx-cpp](#app-image-classification-onnx-cpp)
* [app-image-classification-onnx-py](#app-image-classification-onnx-py)
* [app-image-classification-torch-py](#app-image-classification-torch-py)
* [app-image-classification-tvm-onnx-py](#app-image-classification-tvm-onnx-py)

### Modular applications

* [app-image-corner-detection](#app-image-corner-detection)

### ML/AI datasets

* [get-dataset-criteo](#get-dataset-criteo)
* [get-dataset-imagenet-aux](#get-dataset-imagenet-aux)
* [get-dataset-imagenet-helper](#get-dataset-imagenet-helper)
* [get-dataset-imagenet-val](#get-dataset-imagenet-val)
* [get-dataset-librispeech](#get-dataset-librispeech)
* [get-dataset-openimages](#get-dataset-openimages)
* [get-dataset-squad](#get-dataset-squad)
* [get-preprocessed-dataset-criteo](#get-preprocessed-dataset-criteo)
* [get-preprocessed-dataset-imagenet](#get-preprocessed-dataset-imagenet)
* [get-preprocessed-dataset-openimages](#get-preprocessed-dataset-openimages)
* [get-preprocesser-script-generic](#get-preprocesser-script-generic)

### ML/AI models

* [get-dlrm](#get-dlrm)
* [get-ml-model-bert-large-squad](#get-ml-model-bert-large-squad)
* [get-ml-model-mobilenet](#get-ml-model-mobilenet)
* [get-ml-model-resnet50](#get-ml-model-resnet50)
* [get-ml-model-resnet50-tvm](#get-ml-model-resnet50-tvm)
* [get-ml-model-retinanet](#get-ml-model-retinanet)
* [get-ml-model-retinanet-nvidia](#get-ml-model-retinanet-nvidia)

### ML/AI frameworks

* [get-onnxruntime-prebuilt](#get-onnxruntime-prebuilt)
* [get-tvm](#get-tvm)
* [install-tensorflow-for-c](#install-tensorflow-for-c)
* [install-tensorflow-from-src](#install-tensorflow-from-src)
* [install-tflite-from-src](#install-tflite-from-src)

### Platform information

* [detect-cpu](#detect-cpu)
* [detect-os](#detect-os)

### Compiler automation

* [get-cl](#get-cl) *(Microsoft C compiler)*
* [get-compiler-flags](#get-compiler-flags)
* [get-gcc](#get-gcc) *(GCC compiler)*
* [get-go](#get-go)
* [get-llvm](#get-llvm) *(LLVM compiler)*
* [install-gcc-src](#install-gcc-src)
* [install-llvm-prebuilt](#install-llvm-prebuilt) *(Install prebuilt LLVM compiler)*
* [install-llvm-src](#install-llvm-src) *(Build LLVM compiler from sources (can take >30 min))*

### Detection or installation of tools and artifacts

* [get-android-sdk](#get-android-sdk)
* [get-bazel](#get-bazel)
* [get-cmake](#get-cmake)
* [get-cmsis_5](#get-cmsis_5)
* [get-generic-sys-util](#get-generic-sys-util)
* [get-java](#get-java)
* [get-javac](#get-javac)
* [get-openssl](#get-openssl)
* [get-sys-utils-cm](#get-sys-utils-cm)
* [get-sys-utils-min](#get-sys-utils-min)
* [install-bazel](#install-bazel)
* [install-cmake-prebuilt](#install-cmake-prebuilt)
* [install-github-cli](#install-github-cli)
* [install-openssl](#install-openssl)
* [prototype-lib-dnnl](#prototype-lib-dnnl)

### Cloud automation

* [destroy-terraform](#destroy-terraform)
* [get-aws-cli](#get-aws-cli)
* [get-terraform](#get-terraform)
* [install-aws-cli](#install-aws-cli)
* [install-terraform-from-src](#install-terraform-from-src)
* [run-terraform](#run-terraform)

### TinyML automation

* [flash-tinyml-binary](#flash-tinyml-binary)
* [get-microtvm](#get-microtvm)
* [get-zephyr](#get-zephyr)
* [get-zephyr-sdk](#get-zephyr-sdk)

### CUDA automation

* [get-cuda](#get-cuda)
* [get-cuda-devices](#get-cuda-devices)
* [get-tensorrt](#get-tensorrt)
* [install-cuda-package-manager](#install-cuda-package-manager)
* [install-cuda-prebuilt](#install-cuda-prebuilt)

### Docker automation

* [build-docker-image](#build-docker-image)
* [build-dockerfile](#build-dockerfile)
* [run-docker-container](#run-docker-container)

### Remote automation

* [remote-run-commands](#remote-run-commands)

### Misc automation

* [get-github-cli](#get-github-cli)
* [set-echo-off-win](#set-echo-off-win)
* [tar-my-folder](#tar-my-folder)

### Application automation

* [benchmark-program](#benchmark-program)
* [compile-program](#compile-program)

### Dashboards

* [publish-results-to-dashboard](#publish-results-to-dashboard)

### Python automation

* [activate-python-venv](#activate-python-venv) *(Activate python virtual environment)*
* [get-generic-python-lib](#get-generic-python-lib)
* [get-python3](#get-python3)
* [install-generic-python-lib](#install-generic-python-lib)
* [install-python-src](#install-python-src)
* [install-python-venv](#install-python-venv)

### Legacy CK support

* [get-ck](#get-ck)
* [get-ck-repo-mlops](#get-ck-repo-mlops)

### Tests

* [print-hello-world](#print-hello-world)
* [print-hello-world-java](#print-hello-world-java)
* [print-hello-world-json](#print-hello-world-json)
* [print-hello-world-py](#print-hello-world-py)
* [print-python-version](#print-python-version)
* [test-set-sys-user-cm](#test-set-sys-user-cm)


# List of all sorted CM scripts 

* [activate-python-venv](#activate-python-venv) *(Activate python virtual environment)*
* [app-image-classification-onnx-cpp](#app-image-classification-onnx-cpp)
* [app-image-classification-onnx-py](#app-image-classification-onnx-py)
* [app-image-classification-torch-py](#app-image-classification-torch-py)
* [app-image-classification-tvm-onnx-py](#app-image-classification-tvm-onnx-py)
* [app-image-corner-detection](#app-image-corner-detection)
* [app-loadgen-generic-python](#app-loadgen-generic-python)
* [app-mlperf-inference](#app-mlperf-inference)
* [app-mlperf-inference-cpp](#app-mlperf-inference-cpp)
* [app-mlperf-inference-nvidia-harness](#app-mlperf-inference-nvidia-harness)
* [app-mlperf-inference-reference](#app-mlperf-inference-reference)
* [benchmark-program](#benchmark-program)
* [build-docker-image](#build-docker-image)
* [build-dockerfile](#build-dockerfile)
* [compile-program](#compile-program)
* [destroy-terraform](#destroy-terraform)
* [detect-cpu](#detect-cpu)
* [detect-os](#detect-os)
* [flash-tinyml-binary](#flash-tinyml-binary)
* [generate-mlperf-inference-submission](#generate-mlperf-inference-submission)
* [generate-mlperf-tiny-submission](#generate-mlperf-tiny-submission)
* [get-android-sdk](#get-android-sdk)
* [get-aws-cli](#get-aws-cli)
* [get-bazel](#get-bazel)
* [get-ck](#get-ck)
* [get-ck-repo-mlops](#get-ck-repo-mlops)
* [get-cl](#get-cl) *(Microsoft C compiler)*
* [get-cmake](#get-cmake)
* [get-cmsis_5](#get-cmsis_5)
* [get-compiler-flags](#get-compiler-flags)
* [get-cuda](#get-cuda)
* [get-cuda-devices](#get-cuda-devices)
* [get-dataset-criteo](#get-dataset-criteo)
* [get-dataset-imagenet-aux](#get-dataset-imagenet-aux)
* [get-dataset-imagenet-helper](#get-dataset-imagenet-helper)
* [get-dataset-imagenet-val](#get-dataset-imagenet-val)
* [get-dataset-librispeech](#get-dataset-librispeech)
* [get-dataset-openimages](#get-dataset-openimages)
* [get-dataset-squad](#get-dataset-squad)
* [get-dlrm](#get-dlrm)
* [get-gcc](#get-gcc) *(GCC compiler)*
* [get-generic-python-lib](#get-generic-python-lib)
* [get-generic-sys-util](#get-generic-sys-util)
* [get-github-cli](#get-github-cli)
* [get-go](#get-go)
* [get-java](#get-java)
* [get-javac](#get-javac)
* [get-llvm](#get-llvm) *(LLVM compiler)*
* [get-microtvm](#get-microtvm)
* [get-ml-model-bert-large-squad](#get-ml-model-bert-large-squad)
* [get-ml-model-mobilenet](#get-ml-model-mobilenet)
* [get-ml-model-resnet50](#get-ml-model-resnet50)
* [get-ml-model-resnet50-tvm](#get-ml-model-resnet50-tvm)
* [get-ml-model-retinanet](#get-ml-model-retinanet)
* [get-ml-model-retinanet-nvidia](#get-ml-model-retinanet-nvidia)
* [get-mlperf-inference-loadgen](#get-mlperf-inference-loadgen)
* [get-mlperf-inference-nvidia-common-code](#get-mlperf-inference-nvidia-common-code)
* [get-mlperf-inference-results](#get-mlperf-inference-results)
* [get-mlperf-inference-src](#get-mlperf-inference-src)
* [get-mlperf-inference-sut-configs](#get-mlperf-inference-sut-configs)
* [get-mlperf-inference-sut-description](#get-mlperf-inference-sut-description)
* [get-mlperf-power-dev](#get-mlperf-power-dev)
* [get-mlperf-training-src](#get-mlperf-training-src)
* [get-onnxruntime-prebuilt](#get-onnxruntime-prebuilt)
* [get-openssl](#get-openssl)
* [get-preprocessed-dataset-criteo](#get-preprocessed-dataset-criteo)
* [get-preprocessed-dataset-imagenet](#get-preprocessed-dataset-imagenet)
* [get-preprocessed-dataset-openimages](#get-preprocessed-dataset-openimages)
* [get-preprocesser-script-generic](#get-preprocesser-script-generic)
* [get-python3](#get-python3)
* [get-spec-ptd](#get-spec-ptd)
* [get-sys-utils-cm](#get-sys-utils-cm)
* [get-sys-utils-min](#get-sys-utils-min)
* [get-tensorrt](#get-tensorrt)
* [get-terraform](#get-terraform)
* [get-tvm](#get-tvm)
* [get-zephyr](#get-zephyr)
* [get-zephyr-sdk](#get-zephyr-sdk)
* [install-aws-cli](#install-aws-cli)
* [install-bazel](#install-bazel)
* [install-cmake-prebuilt](#install-cmake-prebuilt)
* [install-cuda-package-manager](#install-cuda-package-manager)
* [install-cuda-prebuilt](#install-cuda-prebuilt)
* [install-gcc-src](#install-gcc-src)
* [install-generic-python-lib](#install-generic-python-lib)
* [install-github-cli](#install-github-cli)
* [install-llvm-prebuilt](#install-llvm-prebuilt) *(Install prebuilt LLVM compiler)*
* [install-llvm-src](#install-llvm-src) *(Build LLVM compiler from sources (can take >30 min))*
* [install-openssl](#install-openssl)
* [install-python-src](#install-python-src)
* [install-python-venv](#install-python-venv)
* [install-tensorflow-for-c](#install-tensorflow-for-c)
* [install-tensorflow-from-src](#install-tensorflow-from-src)
* [install-terraform-from-src](#install-terraform-from-src)
* [install-tflite-from-src](#install-tflite-from-src)
* [print-hello-world](#print-hello-world)
* [print-hello-world-java](#print-hello-world-java)
* [print-hello-world-json](#print-hello-world-json)
* [print-hello-world-py](#print-hello-world-py)
* [print-python-version](#print-python-version)
* [process-mlperf-accuracy](#process-mlperf-accuracy)
* [prototype-lib-dnnl](#prototype-lib-dnnl)
* [publish-results-to-dashboard](#publish-results-to-dashboard)
* [remote-run-commands](#remote-run-commands)
* [reproduce-mlperf-octoml-tinyml-results](#reproduce-mlperf-octoml-tinyml-results)
* [run-docker-container](#run-docker-container)
* [run-mlperf-inference-app](#run-mlperf-inference-app)
* [run-mlperf-inference-submission-checker](#run-mlperf-inference-submission-checker)
* [run-mlperf-power-client](#run-mlperf-power-client)
* [run-mlperf-power-server](#run-mlperf-power-server)
* [run-terraform](#run-terraform)
* [set-echo-off-win](#set-echo-off-win)
* [tar-my-folder](#tar-my-folder)
* [test-set-sys-user-cm](#test-set-sys-user-cm)
* [truncate-mlperf-inference-accuracy-log](#truncate-mlperf-inference-accuracy-log)
* [wrapper-reproduce-octoml-tinyml-submission](#wrapper-reproduce-octoml-tinyml-submission)


* **fp32** (default)
## get-ml-model-retinanet

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,ml-model,resnext50,retinanet,object-detection"`*
* CM CLI alternative: `cm run script "get ml-model resnext50 retinanet object-detection"`*
* Variations: *_fp32;&nbsp; _onnx;&nbsp; _onnx,fp32;&nbsp; _pytorch;&nbsp; _pytorch,fp32;&nbsp; _pytorch,fp32,weights;&nbsp; _weights*
* Default variation: *onnx-fp32*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet/README-extra.md)

## get-ml-model-retinanet-nvidia

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet-nvidia)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet-nvidia/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,ml-model,nvidia-retinanet,nvidia"`*
* CM CLI alternative: `cm run script "get ml-model nvidia-retinanet nvidia"`*
* Variations: *_efficient-nms*

## get-mlperf-inference-loadgen

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,loadgen,inference,inference-loadgen,mlperf,mlcommons"`*
* CM CLI alternative: `cm run script "get loadgen inference inference-loadgen mlperf mlcommons"`*
* Versions: *custom;&nbsp; master;&nbsp; r2.1*
* Default version: *master*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen/README-extra.md)

## get-mlperf-inference-nvidia-common-code

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-common-code)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-common-code/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,nvidia,mlperf,inference,common-code"`*
* CM CLI alternative: `cm run script "get nvidia mlperf inference common-code"`*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-common-code/README-extra.md)

## get-mlperf-inference-results

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-results)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-results/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,results,inference,inference-results,mlcommons,mlperf"`*
* CM CLI alternative: `cm run script "get results inference inference-results mlcommons mlperf"`*
* Versions: *v2.1*
* Default version: *v2.1*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-results/README-extra.md)

## get-mlperf-inference-src

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,src,source,inference,inference-src,inference-source,mlperf,mlcommons"`*
* CM CLI alternative: `cm run script "get src source inference inference-src inference-source mlperf mlcommons"`*
* Variations: *_3d-unet;&nbsp; _deeplearningexamples;&nbsp; _default;&nbsp; _full-history;&nbsp; _gn;&nbsp; _no-recurse-submodules;&nbsp; _nvidia-pycocotools;&nbsp; _octoml;&nbsp; _patch;&nbsp; _power-dev;&nbsp; _pybind;&nbsp; _recurse-submodules;&nbsp; _short-history*
* Default variation: *default*
* Versions: *custom;&nbsp; master;&nbsp; r2.1;&nbsp; tvm*
* Default version: *master*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/README-extra.md)

## get-mlperf-inference-sut-configs

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,mlperf,sut,configs,sut-configs"`*
* CM CLI alternative: `cm run script "get mlperf sut configs sut-configs"`*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs/README-extra.md)

## get-mlperf-inference-sut-description

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,mlperf,sut,description,system-under-test,system-description"`*
* CM CLI alternative: `cm run script "get mlperf sut description system-under-test system-description"`*

## get-mlperf-power-dev

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-power-dev)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-power-dev/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,src,source,power,power-dev,mlperf,mlcommons"`*
* CM CLI alternative: `cm run script "get src source power power-dev mlperf mlcommons"`*
* Variations: *_default;&nbsp; _full-history;&nbsp; _patch;&nbsp; _short-history*
* Default variation: *default*
* Versions: *custom;&nbsp; master*
* Default version: *master*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-power-dev/README-extra.md)

## get-mlperf-training-src

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-src)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-src/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,src,source,training,training-src,training-source,mlperf,mlcommons"`*
* CM CLI alternative: `cm run script "get src source training training-src training-source mlperf mlcommons"`*
* Variations: *_default;&nbsp; _full-history;&nbsp; _no-recurse-submodules;&nbsp; _nvidia-retinanet;&nbsp; _patch;&nbsp; _short-history*
* Default variation: *default*
* Versions: *custom;&nbsp; master*
* Default version: *master*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-src/README-extra.md)

## get-onnxruntime-prebuilt

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="install,onnxruntime,get,prebuilt,lib,lang-c,lang-cpp"`*
* CM CLI alternative: `cm run script "install onnxruntime get prebuilt lib lang-c lang-cpp"`*
* Variations: *_cpu;&nbsp; _cuda*
* Default variation: *cpu*
* Default version: *1.12.1*

## get-openssl

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-openssl)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-openssl/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,openssl,lib-openssl"`*
* CM CLI alternative: `cm run script "get openssl lib-openssl"`*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-openssl/README-extra.md)

## get-preprocessed-dataset-criteo

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-criteo)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-criteo/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,dataset,criteo,recommendation,dlrm,preprocessed"`*
* CM CLI alternative: `cm run script "get dataset criteo recommendation dlrm preprocessed"`*
* Variations: *_1;&nbsp; _50;&nbsp; _full;&nbsp; _validation*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-criteo/README-extra.md)

## get-preprocessed-dataset-imagenet

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,dataset,imagenet,ILSVRC,image-classification,preprocessed"`*
* CM CLI alternative: `cm run script "get dataset imagenet ILSVRC image-classification preprocessed"`*
* Variations: *_1;&nbsp; _500;&nbsp; _NCHW;&nbsp; _NHWC;&nbsp; _for.mobilenet;&nbsp; _for.mobilenet-quantized;&nbsp; _for.resnet50;&nbsp; _for.resnet50-quantized;&nbsp; _full*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/README-extra.md)

## get-preprocessed-dataset-openimages

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,dataset,openimages,open-images,object-detection,preprocessed"`*
* CM CLI alternative: `cm run script "get dataset openimages open-images object-detection preprocessed"`*
* Variations: *_1;&nbsp; _5;&nbsp; _50;&nbsp; _500;&nbsp; _NCHW;&nbsp; _NHWC;&nbsp; _calibration;&nbsp; _fp32;&nbsp; _full;&nbsp; _int8;&nbsp; _nvidia;&nbsp; _validation*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/README-extra.md)

## get-preprocesser-script-generic

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocesser-script-generic)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocesser-script-generic/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,preprocessor,generic,image-preprocessor,script"`*
* CM CLI alternative: `cm run script "get preprocessor generic image-preprocessor script"`*

## get-python3

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,python,python3,get-python,get-python3"`*
* CM CLI alternative: `cm run script "get python python3 get-python get-python3"`*
* Variations: *_shared;&nbsp; _with-ssl*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3/README-extra.md)

## get-spec-ptd

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-spec-ptd)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-spec-ptd/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,spec,ptd,ptdaemon,power,daemon,power-daemon,mlperf,mlcommons"`*
* CM CLI alternative: `cm run script "get spec ptd ptdaemon power daemon power-daemon mlperf mlcommons"`*
* Versions: *custom;&nbsp; main*
* Default version: *main*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-spec-ptd/README-extra.md)

## get-sys-utils-cm

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,sys-utils-cm"`*
* CM CLI alternative: `cm run script "get sys-utils-cm"`*
* Variations: *_user*

## get-sys-utils-min

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-min)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-min/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,sys-utils-min"`*
* CM CLI alternative: `cm run script "get sys-utils-min"`*

## get-tensorrt

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tensorrt)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tensorrt/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,tensorrt,nvidia"`*
* CM CLI alternative: `cm run script "get tensorrt nvidia"`*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tensorrt/README-extra.md)

## get-terraform

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-terraform)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-terraform/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,terraform,get-terraform"`*
* CM CLI alternative: `cm run script "get terraform get-terraform"`*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-terraform/README-extra.md)

## get-tvm

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,tvm,get-tvm"`*
* CM CLI alternative: `cm run script "get tvm get-tvm"`*
* Variations: *_cuda;&nbsp; _llvm;&nbsp; _openmp;&nbsp; _pip-install*
* Versions: *main;&nbsp; v0.10.0;&nbsp; v0.7.0;&nbsp; v0.8.0;&nbsp; v0.9.0*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm/README-extra.md)

## get-zephyr

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,zephyr"`*
* CM CLI alternative: `cm run script "get zephyr"`*
* Versions: *v2.7*
* Default version: *v2.7*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr/README-extra.md)

## get-zephyr-sdk

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr-sdk)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr-sdk/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,zephyr-sdk"`*
* CM CLI alternative: `cm run script "get zephyr-sdk"`*
* Versions: *0.13.1;&nbsp; 0.13.2;&nbsp; 0.15.0*
* Default version: *0.13.2*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr-sdk/README-extra.md)

## install-aws-cli

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-aws-cli)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-aws-cli/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="install,script,aws-cli,aws,cli"`*
* CM CLI alternative: `cm run script "install script aws-cli aws cli"`*

## install-bazel

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-bazel)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-bazel/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="install,script,bazel"`*
* CM CLI alternative: `cm run script "install script bazel"`*
* Default version: *5.2.0*

## install-cmake-prebuilt

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cmake-prebuilt)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cmake-prebuilt/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="install,prebuilt,cmake,prebuilt-cmake,install-prebuilt-cmake"`*
* CM CLI alternative: `cm run script "install prebuilt cmake prebuilt-cmake install-prebuilt-cmake"`*
* Default version: *3.21.1*

## install-cuda-package-manager

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-package-manager)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-package-manager/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="install,package-manager,cuda,package-manager-cuda,install-pm-cuda"`*
* CM CLI alternative: `cm run script "install package-manager cuda package-manager-cuda install-pm-cuda"`*

## install-cuda-prebuilt

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="install,prebuilt,cuda,prebuilt-cuda,install-prebuilt-cuda"`*
* CM CLI alternative: `cm run script "install prebuilt cuda prebuilt-cuda install-prebuilt-cuda"`*
* Versions: *11.7.0;&nbsp; 11.8.0*
* Default version: *11.7.0*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt/README-extra.md)

## install-gcc-src

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-gcc-src)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-gcc-src/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="install,src,gcc,src-gcc"`*
* CM CLI alternative: `cm run script "install src gcc src-gcc"`*
* Versions: *master*
* Default version: *12*

## install-generic-python-lib

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-python-lib)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-python-lib/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="install,generic,generic-python-lib"`*
* CM CLI alternative: `cm run script "install generic generic-python-lib"`*
* Variations: *_apache-tvm;&nbsp; _attrs;&nbsp; _boto3;&nbsp; _colored;&nbsp; _decorator;&nbsp; _jax;&nbsp; _jax_cuda;&nbsp; _mlperf_logging;&nbsp; _numpy;&nbsp; _nvidia-pycocotools;&nbsp; _nvidia-pyindex;&nbsp; _nvidia-tensorrt;&nbsp; _onnx;&nbsp; _onnxruntime;&nbsp; _onnxruntime_gpu;&nbsp; _opencv-python;&nbsp; _pandas;&nbsp; _pillow;&nbsp; _pip;&nbsp; _polygraphy;&nbsp; _protobuf;&nbsp; _psutil;&nbsp; _pycocotools;&nbsp; _pycuda;&nbsp; _scipy;&nbsp; _setuptools;&nbsp; _sklearn;&nbsp; _tensorflow;&nbsp; _tokenization;&nbsp; _torch;&nbsp; _torch_cuda;&nbsp; _torchaudio;&nbsp; _torchaudio_cuda;&nbsp; _torchvision;&nbsp; _torchvision_cuda;&nbsp; _tqdm;&nbsp; _transformers;&nbsp; _typing_extensions;&nbsp; _ujson;&nbsp; _wandb*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-python-lib/README-extra.md)

## install-github-cli

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-github-cli)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-github-cli/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="install,gh,github,cli,github-cli"`*
* CM CLI alternative: `cm run script "install gh github cli github-cli"`*

## install-llvm-prebuilt

*Install prebuilt LLVM compiler.*

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="install,prebuilt,llvm,prebuilt-llvm,install-prebuilt-llvm"`*
* CM CLI alternative: `cm run script "install prebuilt llvm prebuilt-llvm install-prebuilt-llvm"`*
* Default version: *14.0.0*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt/README-extra.md)

## install-llvm-src

*Build LLVM compiler from sources (can take >30 min).*

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-src)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-src/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="install,src,llvm,src-llvm"`*
* CM CLI alternative: `cm run script "install src llvm src-llvm"`*

## install-openssl

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-openssl)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-openssl/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="install,src,openssl,openssl-lib"`*
* CM CLI alternative: `cm run script "install src openssl openssl-lib"`*
* Versions: *1.1.1*
* Default version: *1.1.1*

## install-python-src

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-src)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-src/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="install,src,python,python3,src-python3,src-python"`*
* CM CLI alternative: `cm run script "install src python python3 src-python3 src-python"`*
* Variations: *_shared;&nbsp; _with-ssl*
* Default version: *3.10.5*

## install-python-venv

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-venv)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-venv/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="install,python,get-python-venv,python-venv"`*
* CM CLI alternative: `cm run script "install python get-python-venv python-venv"`*

## install-tensorflow-for-c

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-for-c)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-for-c/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="install,tensorflow,lib,lang-c"`*
* CM CLI alternative: `cm run script "install tensorflow lib lang-c"`*
* Default version: *2.8.0*

## install-tensorflow-from-src

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-from-src)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-from-src/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,install,tensorflow,lib,source,from-source,from-src"`*
* CM CLI alternative: `cm run script "get install tensorflow lib source from-source from-src"`*
* Variations: *_tflite*
* Versions: *master;&nbsp; v1.15.0;&nbsp; v2.0.0;&nbsp; v2.1.0;&nbsp; v2.2.0;&nbsp; v2.3.0;&nbsp; v2.4.0;&nbsp; v2.5.0;&nbsp; v2.6.0;&nbsp; v2.7.0;&nbsp; v2.8.0;&nbsp; v2.9.0*
* Default version: *master*

## install-terraform-from-src

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-terraform-from-src)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-terraform-from-src/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="install,terraform,from-src"`*
* CM CLI alternative: `cm run script "install terraform from-src"`*
* Versions: *main*
* Default version: *main*

## install-tflite-from-src

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tflite-from-src)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tflite-from-src/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,install,tflite-cmake,tensorflow-lite-cmake,from-src"`*
* CM CLI alternative: `cm run script "get install tflite-cmake tensorflow-lite-cmake from-src"`*
* Versions: *master*
* Default version: *master*

## print-hello-world

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="print,hello-world,hello world,hello,world,script"`*
* CM CLI alternative: `cm run script "print hello-world hello world hello world script"`*

## print-hello-world-java

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-java)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-java/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="print,hello world,hello-world,hello,world,java"`*
* CM CLI alternative: `cm run script "print hello world hello-world hello world java"`*

## print-hello-world-json

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-json)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-json/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="print,hello world,hello-world,hello,world,java"`*
* CM CLI alternative: `cm run script "print hello world hello-world hello world java"`*

## print-hello-world-py

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-py)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-py/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="print,hello world,hello-world,hello,world,python"`*
* CM CLI alternative: `cm run script "print hello world hello-world hello world python"`*

## print-python-version

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-python-version)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-python-version/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="print,python,version,python-version"`*
* CM CLI alternative: `cm run script "print python version python-version"`*

## process-mlperf-accuracy

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="run,mlperf,mlcommons,accuracy,mlc,process-accuracy"`*
* CM CLI alternative: `cm run script "run mlperf mlcommons accuracy mlc process-accuracy"`*
* Variations: *_float16;&nbsp; _float32;&nbsp; _float64;&nbsp; _imagenet;&nbsp; _int16;&nbsp; _int32;&nbsp; _int64;&nbsp; _int8;&nbsp; _openimages;&nbsp; _squad*

## prototype-lib-dnnl

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prototype-lib-dnnl)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prototype-lib-dnnl/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="get,lib-dnnl,lib,dnnl"`*
* CM CLI alternative: `cm run script "get lib-dnnl lib dnnl"`*
* Versions: *2.2.4;&nbsp; dev*
* Default version: *dev*

## publish-results-to-dashboard

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/publish-results-to-dashboard)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/publish-results-to-dashboard/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="publish-results,dashboard"`*
* CM CLI alternative: `cm run script "publish-results dashboard"`*

## remote-run-commands

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="remote,run,cmds,remote-run,remote-run-cmds,ssh-run,ssh"`*
* CM CLI alternative: `cm run script "remote run cmds remote-run remote-run-cmds ssh-run ssh"`*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/README-extra.md)

## reproduce-mlperf-octoml-tinyml-results

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="reproduce,tiny,results,mlperf,octoml,mlcommons"`*
* CM CLI alternative: `cm run script "reproduce tiny results mlperf octoml mlcommons"`*
* Variations: *_NRF;&nbsp; _NUCLEO;&nbsp; _ad;&nbsp; _cmsis_nn;&nbsp; _ic;&nbsp; _kws;&nbsp; _native;&nbsp; _vww*
* Versions: *r1.0*
* Default version: *r1.0*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/README-extra.md)

## run-docker-container

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="run,docker,container"`*
* CM CLI alternative: `cm run script "run docker container"`*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container/README-extra.md)

## run-mlperf-inference-app

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="run,generate-run-cmds,run-mlperf,vision,mlcommons,mlperf,inference,reference"`*
* CM CLI alternative: `cm run script "run generate-run-cmds run-mlperf vision mlcommons mlperf inference reference"`*
* Variations: *_all-modes;&nbsp; _all-scenarios;&nbsp; _compliance;&nbsp; _dashboard;&nbsp; _fast;&nbsp; _short;&nbsp; _submission;&nbsp; _valid*
* Versions: *master;&nbsp; r2.1*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app/README-extra.md)

## run-mlperf-inference-submission-checker

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="run,mlc,mlcommons,mlperf,inference,mlperf-inference,submission,checker,submission-checker,mlc-submission-checker"`*
* CM CLI alternative: `cm run script "run mlc mlcommons mlperf inference mlperf-inference submission checker submission-checker mlc-submission-checker"`*
* Variations: *_short-run*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker/README-extra.md)

## run-mlperf-power-client

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="run,mlc,mlcommons,mlperf,power,client,power-client"`*
* CM CLI alternative: `cm run script "run mlc mlcommons mlperf power client power-client"`*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client/README-extra.md)

## run-mlperf-power-server

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="run,mlc,mlcommons,mlperf,power,server,power-server"`*
* CM CLI alternative: `cm run script "run mlc mlcommons mlperf power server power-server"`*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server/README-extra.md)

## run-terraform

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="run,terraform"`*
* CM CLI alternative: `cm run script "run terraform"`*
* Variations: *_aws;&nbsp; _c5.12xlarge;&nbsp; _c5.4xlarge;&nbsp; _c5d.9xlarge;&nbsp; _g4dn.xlarge;&nbsp; _t2.micro*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/README-extra.md)

## set-echo-off-win

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-echo-off-win)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-echo-off-win/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="set,echo,off,win,echo-off-win,echo-off"`*
* CM CLI alternative: `cm run script "set echo off win echo-off-win echo-off"`*

## tar-my-folder

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/tar-my-folder)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/tar-my-folder/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="run,tar"`*
* CM CLI alternative: `cm run script "run tar"`*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/tar-my-folder/README-extra.md)

## test-set-sys-user-cm

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-set-sys-user-cm)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-set-sys-user-cm/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="demo,set,sys-user,cm,sys-user-cm"`*
* CM CLI alternative: `cm run script "demo set sys-user cm sys-user-cm"`*

## truncate-mlperf-inference-accuracy-log

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/truncate-mlperf-inference-accuracy-log)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/truncate-mlperf-inference-accuracy-log/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="run,mlc,mlcommons,mlperf,inference,mlperf-inference,truncation,truncator,truncate,accuracy,accuracy-log,accuracy-log-trancation,accuracy-log-truncator,mlc-accuracy-log-trancation,mlc-accuracy-log-truncator"`*
* CM CLI alternative: `cm run script "run mlc mlcommons mlperf inference mlperf-inference truncation truncator truncate accuracy accuracy-log accuracy-log-trancation accuracy-log-truncator mlc-accuracy-log-trancation mlc-accuracy-log-truncator"`*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/truncate-mlperf-inference-accuracy-log/README-extra.md)

## wrapper-reproduce-octoml-tinyml-submission

* GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission)*
* Meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM CLI with all tags: `cm run script --tags="run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml"`*
* CM CLI alternative: `cm run script "run generate-tiny generate submission tiny generate-tiny-submission results mlcommons mlperf octoml"`*
* Default version: *r1.0*
* Extra README: [*GitHub*](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/README-extra.md)


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
