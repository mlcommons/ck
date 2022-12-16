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


## activate-python-venv


*Activate python virtual environment.*


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/activate-python-venv)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/activate-python-venv/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="activate,python,activate-python-venv,python-venv"*


## app-image-classification-onnx-cpp


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-cpp)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-cpp/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="app,image-classification,onnx,cpp"*


## app-image-classification-onnx-py


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-py)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="app,image-classification,onnx,python"*
* CM script variations: *_cuda*


## app-image-classification-torch-py


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-torch-py)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-torch-py/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="app,image-classification,torch,python"*
* CM script variations: *_cuda*


## app-image-classification-tvm-onnx-py


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-tvm-onnx-py)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-tvm-onnx-py/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="app,image-classification,tvm-onnx,python"*
* CM script variations: *_cuda;&nbsp; _llvm;&nbsp; _tvm;&nbsp; _tvm-pip-install*
* CM script default variation: *tvm*


## app-image-corner-detection


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-corner-detection)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-corner-detection/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="app,image,corner-detection"*


## app-loadgen-generic-python


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-loadgen-generic-python)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-loadgen-generic-python/_cm.yaml)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="app,loadgen,generic,loadgen-generic,python"*
* CM script variations: *_cpu;&nbsp; _cuda;&nbsp; _onnxruntime;&nbsp; _resnet50;&nbsp; _retinanet*


## app-mlperf-inference


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference/_cm.yaml)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="app,vision,language,mlcommons,mlperf,inference,generic"*
* CM script variations: *_bert-99;&nbsp; _bert-99.9;&nbsp; _bert_;&nbsp; _cpp;&nbsp; _cpu;&nbsp; _cuda;&nbsp; _fast;&nbsp; _nvidia;&nbsp; _onnxruntime;&nbsp; _power;&nbsp; _python;&nbsp; _pytorch;&nbsp; _quantized;&nbsp; _r2.1_default;&nbsp; _reference;&nbsp; _resnet50;&nbsp; _retinanet;&nbsp; _test;&nbsp; _tf;&nbsp; _tflite;&nbsp; _tflite-cpp;&nbsp; _tvm-onnx;&nbsp; _tvm-pip-install-onnx;&nbsp; _tvm-pip-install-pytorch;&nbsp; _tvm-pytorch;&nbsp; _valid*


## app-mlperf-inference-cpp


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp/_cm.yaml)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="app,mlcommons,mlperf,inference,cpp"*
* CM script variations: *_cpu;&nbsp; _cuda;&nbsp; _onnxruntime;&nbsp; _pytorch;&nbsp; _resnet50;&nbsp; _retinanet;&nbsp; _tf;&nbsp; _tflite;&nbsp; _tvm-onnx*


## app-mlperf-inference-nvidia-harness


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-nvidia-harness)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-nvidia-harness/_cm.yaml)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="app,mlcommons,mlperf,inference,nvidia-harness,nvidia"*
* CM script variations: *_cpu;&nbsp; _cuda;&nbsp; _pytorch;&nbsp; _resnet50;&nbsp; _retinanet*


## app-mlperf-inference-reference


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference/_cm.yaml)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="app,vision,language,mlcommons,mlperf,inference,reference,ref"*
* CM script variations: *_bert;&nbsp; _bert-99;&nbsp; _bert-99.9;&nbsp; _cpu;&nbsp; _cuda;&nbsp; _fast;&nbsp; _onnxruntime;&nbsp; _python;&nbsp; _pytorch;&nbsp; _quantized;&nbsp; _r2.1_default;&nbsp; _resnet50;&nbsp; _retinanet;&nbsp; _tensorflow;&nbsp; _test;&nbsp; _tf;&nbsp; _tvm-onnx;&nbsp; _tvm-pytorch;&nbsp; _valid*


## benchmark-program


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="program,benchmark,benchmark-program"*
* CM script variations: *_mlperf-power;&nbsp; _numactl;&nbsp; _numactl-interleave;&nbsp; _profile*


## build-docker-image


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="build,docker,image,docker-image,dockerimage"*


## build-dockerfile


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-dockerfile)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-dockerfile/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="build,dockerfile"*
* CM script variations: *_slim*


## compile-program


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="compile,program,c-program,cpp-program,compile-program,compile-c-program,compile-cpp-program"*


## destroy-terraform


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/destroy-terraform)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/destroy-terraform/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="destroy,terraform,cmd"*


## detect-cpu


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="detect,cpu,detect-cpu,info"*


## detect-os


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="detect-os,detect,os,info"*


## flash-tinyml-binary


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="flash,tiny,mlperf,mlcommons"*
* CM script variations: *_NRF;&nbsp; _NUCLEO;&nbsp; _ad;&nbsp; _cmsis_nn;&nbsp; _ic;&nbsp; _kws;&nbsp; _native;&nbsp; _vww*
* CM script default version: *r1.0*


## generate-mlperf-inference-submission


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="generate,submission,mlperf,mlperf-inference,inference,mlcommons,inference-submission,mlperf-inference-submission,mlcommons-inference-submission"*


## generate-mlperf-tiny-submission


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="generate,submission,mlperf,mlperf-tiny,tiny,mlcommons,tiny-submission,mlperf-tiny-submission,mlcommons-tiny-submission"*


## get-android-sdk


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-android-sdk)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-android-sdk/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,android,sdk,android-sdk"*


## get-aws-cli


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-aws-cli)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-aws-cli/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,aws-cli,aws,cli"*


## get-bazel


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-bazel)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-bazel/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,bazel,get-bazel"*


## get-ck


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ck)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ck/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,ck,ck-framework"*


## get-ck-repo-mlops


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ck-repo-mlops)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ck-repo-mlops/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,ck-repo,mlops,ck-repo-mlops"*


## get-cl


*Microsoft C compiler.*


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,cl,compiler,c-compiler,cpp-compiler,get-cl"*


## get-cmake


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,cmake,get-cmake"*


## get-cmsis_5


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmsis_5)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmsis_5/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,cmsis,cmsis_5,arm-software"*
* CM script variations: *_recurse-submodules;&nbsp; _short-history*
* CM script versions: *custom;&nbsp; develop;&nbsp; master*
* CM script default version: *develop*


## get-compiler-flags


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-compiler-flags)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-compiler-flags/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,compiler-flags"*


## get-cuda


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,cuda,nvcc,get-nvcc,get-cuda"*
* CM script variations: *_compiler*


## get-cuda-devices


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-devices)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-devices/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,cuda-devices"*


## get-dataset-criteo


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-criteo)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-criteo/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,dataset,criteo,original"*
* CM script variations: *_backup*


## get-dataset-imagenet-aux


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,aux,dataset-aux,image-classification,imagenet-aux"*
* CM script variations: *_2012;&nbsp; _from.berkeleyvision;&nbsp; _from.dropbox*
* CM script default variation: *from.dropbox*


## get-dataset-imagenet-helper


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-helper)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-helper/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,imagenet,helper,imagenet-helper"*


## get-dataset-imagenet-val


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,dataset,imagenet,ILSVRC,image-classification,original"*
* CM script variations: *_2012-1;&nbsp; _2012-500;&nbsp; _2012-full;&nbsp; _full*
* CM script default variation: *2012-500*


## get-dataset-librispeech


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-librispeech)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-librispeech/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,dataset,speech,speech-recognition,librispeech,validation,audio,training,original"*
* CM script versions: *dev-clean;&nbsp; dev-other;&nbsp; test-clean;&nbsp; test-other;&nbsp; train-clean-100;&nbsp; train-clean-360;&nbsp; train-other-500*
* CM script default version: *dev-clean*


## get-dataset-openimages


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,dataset,openimages,open-images,object-detection,original"*
* CM script variations: *_1;&nbsp; _5;&nbsp; _50;&nbsp; _500;&nbsp; _calibration;&nbsp; _full;&nbsp; _validation*
* CM script default variation: *validation*


## get-dataset-squad


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,dataset,squad,language-processing,validation,training,original"*
* CM script versions: *1.1;&nbsp; 2.0*
* CM script default version: *1.1*


## get-dlrm


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dlrm)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dlrm/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,src,dlrm"*
* CM script variations: *_full-history*
* CM script versions: *main*
* CM script default version: *main*


## get-gcc


*GCC compiler.*


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,gcc,compiler,c-compiler,cpp-compiler,get-gcc"*


## get-generic-python-lib


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,generic,generic-python-lib"*
* CM script variations: *_apache-tvm;&nbsp; _attrs;&nbsp; _boto3;&nbsp; _colored;&nbsp; _decorator;&nbsp; _jax;&nbsp; _jax_cuda;&nbsp; _mlperf_logging;&nbsp; _numpy;&nbsp; _nvidia-pycocotools;&nbsp; _nvidia-pyindex;&nbsp; _nvidia-tensorrt;&nbsp; _onnx;&nbsp; _onnxruntime;&nbsp; _onnxruntime_gpu;&nbsp; _opencv-python;&nbsp; _pandas;&nbsp; _pillow;&nbsp; _pip;&nbsp; _polygraphy;&nbsp; _protobuf;&nbsp; _psutil;&nbsp; _pycocotools;&nbsp; _pycuda;&nbsp; _scipy;&nbsp; _setuptools;&nbsp; _sklearn;&nbsp; _tensorflow;&nbsp; _tokenization;&nbsp; _torch;&nbsp; _torch_cuda;&nbsp; _torchaudio;&nbsp; _torchaudio_cuda;&nbsp; _torchvision;&nbsp; _torchvision_cuda;&nbsp; _tqdm;&nbsp; _transformers;&nbsp; _typing_extensions;&nbsp; _ujson;&nbsp; _wandb*


## get-generic-sys-util


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,sys-util,generic,generic-sys-util"*
* CM script variations: *_gflags-dev;&nbsp; _glog-dev*


## get-github-cli


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-github-cli)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-github-cli/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,gh,github,cli,github-cli"*


## get-go


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-go)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-go/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,tool,go,get-go"*


## get-java


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,java"*
* CM script variations: *_install*


## get-javac


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-javac)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-javac/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,javac"*
* CM script variations: *_install*


## get-llvm


*LLVM compiler.*


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,llvm,compiler,c-compiler,cpp-compiler,get-llvm"*


## get-microtvm


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-microtvm)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-microtvm/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,src,source,microtvm,tiny"*
* CM script variations: *_default;&nbsp; _full-history;&nbsp; _short-history*
* CM script default variation: *default*
* CM script versions: *custom;&nbsp; main*
* CM script default version: *main*


## get-ml-model-bert-large-squad


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,ml-model,bert,bert-large,bert-squad,language,language-processing"*
* CM script variations: *_fp32;&nbsp; _int8;&nbsp; _onnx;&nbsp; _onnx,fp32;&nbsp; _onnx,int8;&nbsp; _onnxruntime;&nbsp; _pytorch;&nbsp; _pytorch,fp32;&nbsp; _pytorch,int8;&nbsp; _tensorflow;&nbsp; _tf*


## get-ml-model-mobilenet


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,ml-model,mobilenet,ml-model-mobilenet,image-classification"*
* CM script variations: *_fp32;&nbsp; _from.google;&nbsp; _from.zenodo;&nbsp; _int8;&nbsp; _onnx;&nbsp; _onnx,fp32;&nbsp; _onnx,int8;&nbsp; _onnx,opset-11,fp32;&nbsp; _onnx,opset-8,fp32;&nbsp; _opset-11;&nbsp; _opset-8;&nbsp; _tf;&nbsp; _tf,fp32;&nbsp; _tf,fp32,from.google;&nbsp; _tf,fp32,from.zenodo;&nbsp; _tf,int8;&nbsp; _tflite*
* CM script default variation: *onnx*


## get-ml-model-resnet50


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,raw,ml-model,resnet50,ml-model-resnet50,image-classification"*
* CM script variations: *_fp32;&nbsp; _int8;&nbsp; _onnx;&nbsp; _onnx,opset-11;&nbsp; _onnx,opset-8;&nbsp; _onnxruntime;&nbsp; _opset-11;&nbsp; _opset-8;&nbsp; _pytorch;&nbsp; _pytorch,fp32;&nbsp; _pytorch,int8;&nbsp; _tensorflow;&nbsp; _tf;&nbsp; _tflite;&nbsp; _uint8*
* CM script default variation: *onnx*


## get-ml-model-resnet50-tvm


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,ml-model,ml-model-tvm,tvm-model,resnet50,ml-model-resnet50,image-classification"*
* CM script variations: *_bs.1;&nbsp; _bs.16;&nbsp; _bs.2;&nbsp; _bs.32;&nbsp; _bs.4;&nbsp; _bs.64;&nbsp; _bs.8;&nbsp; _fp32;&nbsp; _int8;&nbsp; _onnx;&nbsp; _pytorch;&nbsp; _tensorflow;&nbsp; _tf;&nbsp; _tflite;&nbsp; _uint8*
* CM script default variation: *onnx*


## get-ml-model-retinanet


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,ml-model,resnext50,retinanet,object-detection"*
* CM script variations: *_fp32;&nbsp; _onnx;&nbsp; _onnx,fp32;&nbsp; _pytorch;&nbsp; _pytorch,fp32;&nbsp; _pytorch,fp32,weights;&nbsp; _weights*
* CM script default variation: *onnx-fp32*


## get-ml-model-retinanet-nvidia


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet-nvidia)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet-nvidia/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,ml-model,nvidia-retinanet,nvidia"*
* CM script variations: *_efficient-nms*


## get-mlperf-inference-loadgen


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,loadgen,inference,inference-loadgen,mlperf,mlcommons"*
* CM script versions: *custom;&nbsp; master;&nbsp; r2.1*
* CM script default version: *master*


## get-mlperf-inference-nvidia-common-code


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-common-code)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-common-code/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,nvidia,mlperf,inference,common-code"*


## get-mlperf-inference-results


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-results)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-results/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,results,inference,inference-results,mlcommons,mlperf"*
* CM script versions: *v2.1*
* CM script default version: *v2.1*


## get-mlperf-inference-src


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,src,source,inference,inference-src,inference-source,mlperf,mlcommons"*
* CM script variations: *_3d-unet;&nbsp; _deeplearningexamples;&nbsp; _default;&nbsp; _full-history;&nbsp; _gn;&nbsp; _no-recurse-submodules;&nbsp; _nvidia-pycocotools;&nbsp; _octoml;&nbsp; _patch;&nbsp; _power-dev;&nbsp; _pybind;&nbsp; _recurse-submodules;&nbsp; _short-history*
* CM script default variation: *default*
* CM script versions: *custom;&nbsp; master;&nbsp; r2.1;&nbsp; tvm*
* CM script default version: *master*


## get-mlperf-inference-sut-configs


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,mlperf,sut,configs,sut-configs"*


## get-mlperf-inference-sut-description


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,mlperf,sut,description,system-under-test,system-description"*


## get-mlperf-power-dev


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-power-dev)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-power-dev/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,src,source,power,power-dev,mlperf,mlcommons"*
* CM script variations: *_default;&nbsp; _full-history;&nbsp; _patch;&nbsp; _short-history*
* CM script default variation: *default*
* CM script versions: *custom;&nbsp; master*
* CM script default version: *master*


## get-mlperf-training-src


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-src)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-src/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,src,source,training,training-src,training-source,mlperf,mlcommons"*
* CM script variations: *_default;&nbsp; _full-history;&nbsp; _no-recurse-submodules;&nbsp; _nvidia-retinanet;&nbsp; _patch;&nbsp; _short-history*
* CM script default variation: *default*
* CM script versions: *custom;&nbsp; master*
* CM script default version: *master*


## get-onnxruntime-prebuilt


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="install,onnxruntime,get,prebuilt,lib,lang-c,lang-cpp"*
* CM script variations: *_cpu;&nbsp; _cuda*
* CM script default variation: *cpu*
* CM script default version: *1.12.1*


## get-openssl


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-openssl)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-openssl/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,openssl,lib-openssl"*


## get-preprocessed-dataset-criteo


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-criteo)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-criteo/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,dataset,criteo,recommendation,dlrm,preprocessed"*
* CM script variations: *_1;&nbsp; _50;&nbsp; _full;&nbsp; _validation*


## get-preprocessed-dataset-imagenet


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,dataset,imagenet,ILSVRC,image-classification,preprocessed"*
* CM script variations: *_1;&nbsp; _500;&nbsp; _NCHW;&nbsp; _NHWC;&nbsp; _for.mobilenet;&nbsp; _for.mobilenet-quantized;&nbsp; _for.resnet50;&nbsp; _for.resnet50-quantized;&nbsp; _full*


## get-preprocessed-dataset-openimages


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,dataset,openimages,open-images,object-detection,preprocessed"*
* CM script variations: *_1;&nbsp; _5;&nbsp; _50;&nbsp; _500;&nbsp; _NCHW;&nbsp; _NHWC;&nbsp; _calibration;&nbsp; _fp32;&nbsp; _full;&nbsp; _int8;&nbsp; _nvidia;&nbsp; _validation*


## get-preprocesser-script-generic


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocesser-script-generic)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocesser-script-generic/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,preprocessor,generic,image-preprocessor,script"*


## get-python3


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,python,python3,get-python,get-python3"*
* CM script variations: *_shared;&nbsp; _with-ssl*


## get-spec-ptd


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-spec-ptd)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-spec-ptd/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,spec,ptd,ptdaemon,power,daemon,power-daemon,mlperf,mlcommons"*
* CM script versions: *custom;&nbsp; main*
* CM script default version: *main*


## get-sys-utils-cm


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,sys-utils-cm"*
* CM script variations: *_user*


## get-sys-utils-min


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-min)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-min/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,sys-utils-min"*


## get-tensorrt


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tensorrt)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tensorrt/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,tensorrt,nvidia"*


## get-terraform


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-terraform)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-terraform/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,terraform,get-terraform"*


## get-tvm


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,tvm,get-tvm"*
* CM script variations: *_cuda;&nbsp; _llvm;&nbsp; _openmp;&nbsp; _pip-install*
* CM script versions: *main;&nbsp; v0.10.0;&nbsp; v0.7.0;&nbsp; v0.8.0;&nbsp; v0.9.0*


## get-zephyr


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,zephyr"*
* CM script versions: *v2.7*
* CM script default version: *v2.7*


## get-zephyr-sdk


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr-sdk)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr-sdk/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,zephyr-sdk"*
* CM script versions: *0.13.1;&nbsp; 0.13.2;&nbsp; 0.15.0*
* CM script default version: *0.13.2*


## install-aws-cli


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-aws-cli)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-aws-cli/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="install,script,aws-cli,aws,cli"*


## install-bazel


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-bazel)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-bazel/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="install,script,bazel"*
* CM script default version: *5.2.0*


## install-cmake-prebuilt


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cmake-prebuilt)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cmake-prebuilt/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="install,prebuilt,cmake,prebuilt-cmake,install-prebuilt-cmake"*
* CM script default version: *3.21.1*


## install-cuda-package-manager


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-package-manager)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-package-manager/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="install,package-manager,cuda,package-manager-cuda,install-pm-cuda"*


## install-cuda-prebuilt


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="install,prebuilt,cuda,prebuilt-cuda,install-prebuilt-cuda"*
* CM script versions: *11.7.0;&nbsp; 11.8.0*
* CM script default version: *11.7.0*


## install-gcc-src


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-gcc-src)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-gcc-src/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="install,src,gcc,src-gcc"*
* CM script versions: *master*
* CM script default version: *12*


## install-generic-python-lib


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-python-lib)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-python-lib/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="install,generic,generic-python-lib"*
* CM script variations: *_apache-tvm;&nbsp; _attrs;&nbsp; _boto3;&nbsp; _colored;&nbsp; _decorator;&nbsp; _jax;&nbsp; _jax_cuda;&nbsp; _mlperf_logging;&nbsp; _numpy;&nbsp; _nvidia-pycocotools;&nbsp; _nvidia-pyindex;&nbsp; _nvidia-tensorrt;&nbsp; _onnx;&nbsp; _onnxruntime;&nbsp; _onnxruntime_gpu;&nbsp; _opencv-python;&nbsp; _pandas;&nbsp; _pillow;&nbsp; _pip;&nbsp; _polygraphy;&nbsp; _protobuf;&nbsp; _psutil;&nbsp; _pycocotools;&nbsp; _pycuda;&nbsp; _scipy;&nbsp; _setuptools;&nbsp; _sklearn;&nbsp; _tensorflow;&nbsp; _tokenization;&nbsp; _torch;&nbsp; _torch_cuda;&nbsp; _torchaudio;&nbsp; _torchaudio_cuda;&nbsp; _torchvision;&nbsp; _torchvision_cuda;&nbsp; _tqdm;&nbsp; _transformers;&nbsp; _typing_extensions;&nbsp; _ujson;&nbsp; _wandb*


## install-github-cli


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-github-cli)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-github-cli/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="install,gh,github,cli,github-cli"*


## install-llvm-prebuilt


*Install prebuilt LLVM compiler.*


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="install,prebuilt,llvm,prebuilt-llvm,install-prebuilt-llvm"*
* CM script default version: *14.0.0*


## install-llvm-src


*Build LLVM compiler from sources (can take >30 min).*


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-src)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-src/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="install,src,llvm,src-llvm"*


## install-openssl


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-openssl)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-openssl/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="install,src,openssl,openssl-lib"*
* CM script versions: *1.1.1*
* CM script default version: *1.1.1*


## install-python-src


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-src)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-src/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="install,src,python,python3,src-python3,src-python"*
* CM script variations: *_shared;&nbsp; _with-ssl*
* CM script default version: *3.10.5*


## install-python-venv


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-venv)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-venv/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="install,python,get-python-venv,python-venv"*


## install-tensorflow-for-c


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-for-c)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-for-c/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="install,tensorflow,lib,lang-c"*
* CM script default version: *2.8.0*


## install-tensorflow-from-src


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-from-src)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-from-src/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,install,tensorflow,lib,source,from-source,from-src"*
* CM script variations: *_tflite*
* CM script versions: *master;&nbsp; v1.15.0;&nbsp; v2.0.0;&nbsp; v2.1.0;&nbsp; v2.2.0;&nbsp; v2.3.0;&nbsp; v2.4.0;&nbsp; v2.5.0;&nbsp; v2.6.0;&nbsp; v2.7.0;&nbsp; v2.8.0;&nbsp; v2.9.0*
* CM script default version: *master*


## install-terraform-from-src


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-terraform-from-src)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-terraform-from-src/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="install,terraform,from-src"*
* CM script versions: *main*
* CM script default version: *main*


## install-tflite-from-src


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tflite-from-src)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tflite-from-src/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,install,tflite-cmake,tensorflow-lite-cmake,from-src"*
* CM script versions: *master*
* CM script default version: *master*


## print-hello-world


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="print,hello-world,hello world,hello,world,script"*


## print-hello-world-java


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-java)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-java/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="print,hello world,hello-world,hello,world,java"*


## print-hello-world-json


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-json)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-json/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="print,hello world,hello-world,hello,world,java"*


## print-hello-world-py


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-py)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-py/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="print,hello world,hello-world,hello,world,python"*


## print-python-version


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-python-version)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-python-version/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="print,python,version,python-version"*


## process-mlperf-accuracy


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="run,mlperf,mlcommons,accuracy,mlc,process-accuracy"*
* CM script variations: *_float16;&nbsp; _float32;&nbsp; _float64;&nbsp; _imagenet;&nbsp; _int16;&nbsp; _int32;&nbsp; _int64;&nbsp; _int8;&nbsp; _openimages;&nbsp; _squad*


## prototype-lib-dnnl


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prototype-lib-dnnl)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prototype-lib-dnnl/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="get,lib-dnnl,lib,dnnl"*
* CM script versions: *2.2.4;&nbsp; dev*
* CM script default version: *dev*


## publish-results-to-dashboard


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/publish-results-to-dashboard)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/publish-results-to-dashboard/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="publish-results,dashboard"*


## remote-run-commands


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="remote,run,cmds,remote-run,remote-run-cmds,ssh-run,ssh"*


## reproduce-mlperf-octoml-tinyml-results


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="reproduce,tiny,results,mlperf,octoml,mlcommons"*
* CM script variations: *_NRF;&nbsp; _NUCLEO;&nbsp; _ad;&nbsp; _cmsis_nn;&nbsp; _ic;&nbsp; _kws;&nbsp; _native;&nbsp; _vww*
* CM script versions: *r1.0*
* CM script default version: *r1.0*


## run-docker-container


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="run,docker,container"*


## run-mlperf-inference-app


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="run,generate-run-cmds,run-mlperf,vision,mlcommons,mlperf,inference,reference"*
* CM script variations: *_all-modes;&nbsp; _all-scenarios;&nbsp; _compliance;&nbsp; _dashboard;&nbsp; _fast;&nbsp; _short;&nbsp; _submission;&nbsp; _valid*
* CM script versions: *master;&nbsp; r2.1*


## run-mlperf-inference-submission-checker


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="run,mlc,mlcommons,mlperf,inference,mlperf-inference,submission,checker,submission-checker,mlc-submission-checker"*
* CM script variations: *_short-run*


## run-mlperf-power-client


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="run,mlc,mlcommons,mlperf,power,client,power-client"*


## run-mlperf-power-server


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="run,mlc,mlcommons,mlperf,power,server,power-server"*


## run-terraform


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="run,terraform"*
* CM script variations: *_aws;&nbsp; _c5.12xlarge;&nbsp; _c5.4xlarge;&nbsp; _c5d.9xlarge;&nbsp; _g4dn.xlarge;&nbsp; _t2.micro*


## set-echo-off-win


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-echo-off-win)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-echo-off-win/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="set,echo,off,win,echo-off-win,echo-off"*


## tar-my-folder


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/tar-my-folder)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/tar-my-folder/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="run,tar"*


## test-set-sys-user-cm


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-set-sys-user-cm)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-set-sys-user-cm/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="demo,set,sys-user,cm,sys-user-cm"*


## truncate-mlperf-inference-accuracy-log


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/truncate-mlperf-inference-accuracy-log)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/truncate-mlperf-inference-accuracy-log/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="run,mlc,mlcommons,mlperf,inference,mlperf-inference,truncation,truncator,truncate,accuracy,accuracy-log,accuracy-log-trancation,accuracy-log-truncator,mlc-accuracy-log-trancation,mlc-accuracy-log-truncator"*


## wrapper-reproduce-octoml-tinyml-submission


* CM script GitHub repository: *[mlcommons@ck](https://github.com/mlcommons/ck/tree/master/cm-mlops)*
* CM script artifact (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission)*
* CM script meta description: *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission/_cm.json)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*
* CM script  tags: *cm run script --tags="run,generate-tiny,generate,submission,tiny,generate-tiny-submission,results,mlcommons,mlperf,octoml"*
* CM script default version: *r1.0*



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
