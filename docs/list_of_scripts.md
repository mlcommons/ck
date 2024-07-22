[ [Back to index](README.md) ]

<!--
This file is generated automatically - don't edit!
-->

This is an automatically generated list of portable and reusable automation recipes (CM scripts)
with a [human-friendly interface (CM)](https://github.com/mlcommons/ck) 
to run a growing number of ad-hoc MLPerf, MLOps, and DevOps scripts
from [MLCommons projects](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
and [research papers](https://www.youtube.com/watch?v=7zpeIVwICa4) 
in a unified way on any operating system with any software and hardware
natively or inside containers.

Click on any automation recipe below to learn how to run and reuse it 
via CM command line, Python API or GUI.

CM scripts can easily chained together into automation workflows using `deps` and `tags` keys
while automatically updating all environment variables and paths 
for a given task and platform [using simple JSON or YAML](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.yaml).


*Note that CM is a community project being developed and extended by [MLCommons members and individual contributors](../CONTRIBUTING.md) -
 you can find source code of CM scripts maintained by MLCommons [here](../cm-mlops/script).
 Please join [Discord server](https://discord.gg/JjWNWXKxwT) to participate in collaborative developments or provide your feedback.*


# License

[Apache 2.0](LICENSE.md)


# Copyright

2022-2024 [MLCommons](https://mlcommons.org)





# List of CM scripts by categories

* [AI/ML datasets](#aiml-datasets)
* [AI/ML frameworks](#aiml-frameworks)
* [AI/ML models](#aiml-models)
* [AI/ML optimization](#aiml-optimization)
* [CM interface prototyping](#cm-interface-prototyping)
* [CUDA automation](#cuda-automation)
* [Cloud automation](#cloud-automation)
* [Collective benchmarking](#collective-benchmarking)
* [Compiler automation](#compiler-automation)
* [Dashboard automation](#dashboard-automation)
* [Detection or installation of tools and artifacts](#detection-or-installation-of-tools-and-artifacts)
* [DevOps automation](#devops-automation)
* [Docker automation](#docker-automation)
* [GUI](#gui)
* [Legacy CK support](#legacy-ck-support)
* [MLPerf benchmark support](#mlperf-benchmark-support)
* [Modular AI/ML application pipeline](#modular-aiml-application-pipeline)
* [Modular MLPerf benchmarks](#modular-mlperf-benchmarks)
* [Modular MLPerf inference benchmark pipeline](#modular-mlperf-inference-benchmark-pipeline)
* [Modular MLPerf training benchmark pipeline](#modular-mlperf-training-benchmark-pipeline)
* [Modular application pipeline](#modular-application-pipeline)
* [Platform information](#platform-information)
* [Python automation](#python-automation)
* [Remote automation](#remote-automation)
* [Reproduce MLPerf benchmarks](#reproduce-mlperf-benchmarks)
* [Reproducibility and artifact evaluation](#reproducibility-and-artifact-evaluation)
* [Tests](#tests)
* [TinyML automation](#tinyml-automation)


### AI/ML datasets

* [get-croissant](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-croissant)
* [get-dataset-cifar10](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cifar10)
* [get-dataset-cnndm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cnndm)
* [get-dataset-coco](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco)
* [get-dataset-coco2014](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco2014)
* [get-dataset-criteo](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-criteo)
* [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-aux)
* [get-dataset-imagenet-calibration](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-calibration)
* [get-dataset-imagenet-helper](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-helper)
* [get-dataset-imagenet-train](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-train)
* [get-dataset-imagenet-val](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-val)
* [get-dataset-kits19](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-kits19)
* [get-dataset-librispeech](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-librispeech)
* [get-dataset-openimages](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages)
* [get-dataset-openimages-annotations](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages-annotations)
* [get-dataset-openimages-calibration](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages-calibration)
* [get-dataset-openorca](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openorca)
* [get-dataset-squad](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-squad)
* [get-dataset-squad-vocab](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-squad-vocab)
* [get-preprocessed-dataset-criteo](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-criteo)
* [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-imagenet)
* [get-preprocessed-dataset-kits19](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-kits19)
* [get-preprocessed-dataset-librispeech](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-librispeech)
* [get-preprocessed-dataset-openimages](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-openimages)
* [get-preprocessed-dataset-openorca](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-openorca)
* [get-preprocessed-dataset-squad](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-squad)
* [get-preprocesser-script-generic](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocesser-script-generic)

### AI/ML frameworks

* [get-google-saxml](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-google-saxml)
* [get-onnxruntime-prebuilt](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-onnxruntime-prebuilt)
* [get-qaic-apps-sdk](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-qaic-apps-sdk)
* [get-qaic-platform-sdk](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-qaic-platform-sdk)
* [get-qaic-software-kit](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-qaic-software-kit)
* [get-rocm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-rocm)
* [get-tvm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tvm)
* [install-qaic-compute-sdk-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-qaic-compute-sdk-from-src)
* [install-rocm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-rocm)
* [install-tensorflow-for-c](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-tensorflow-for-c)
* [install-tensorflow-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-tensorflow-from-src)
* [install-tflite-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-tflite-from-src)

### AI/ML models

* [convert-ml-model-huggingface-to-onnx](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-ml-model-huggingface-to-onnx)
* [get-bert-squad-vocab](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-bert-squad-vocab)
* [get-dlrm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dlrm)
* [get-ml-model-3d-unet-kits19](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-3d-unet-kits19)
* [get-ml-model-bert-base-squad](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-base-squad)
* [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-large-squad)
* [get-ml-model-dlrm-terabyte](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-dlrm-terabyte)
* [get-ml-model-efficientnet-lite](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-efficientnet-lite)
* [get-ml-model-gptj](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-gptj)
* [get-ml-model-huggingface-zoo](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-huggingface-zoo)
* [get-ml-model-llama2](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-llama2)
* [get-ml-model-mobilenet](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-mobilenet)
* [get-ml-model-neuralmagic-zoo](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-neuralmagic-zoo)
* [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-resnet50)
* [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-retinanet)
* [get-ml-model-retinanet-nvidia](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-retinanet-nvidia)
* [get-ml-model-rnnt](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-rnnt)
* [get-ml-model-stable-diffusion](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-stable-diffusion)
* [get-ml-model-tiny-resnet](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-tiny-resnet)
* [get-ml-model-using-imagenet-from-model-zoo](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-using-imagenet-from-model-zoo)
* [get-tvm-model](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tvm-model)

### AI/ML optimization

* [calibrate-model-for.qaic](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/calibrate-model-for.qaic)
* [compile-model-for.qaic](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/compile-model-for.qaic)
* [prune-bert-models](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prune-bert-models)

### CM interface prototyping

* [test-mlperf-inference-retinanet](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-mlperf-inference-retinanet)

### CUDA automation

* [get-cuda](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cuda)
* [get-cuda-devices](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cuda-devices)
* [get-cudnn](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cudnn)
* [get-tensorrt](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tensorrt)
* [install-cuda-package-manager](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cuda-package-manager)
* [install-cuda-prebuilt](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cuda-prebuilt)

### Cloud automation

* [destroy-terraform](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/destroy-terraform)
* [get-aws-cli](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aws-cli)
* [get-terraform](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-terraform)
* [install-aws-cli](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-aws-cli)
* [install-terraform-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-terraform-from-src)
* [run-terraform](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-terraform)

### Collective benchmarking

* [launch-benchmark](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/launch-benchmark)

### Compiler automation

* [get-aocl](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aocl)
* [get-cl](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cl) *(Detect or install Microsoft C compiler)*
* [get-compiler-flags](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-compiler-flags)
* [get-compiler-rust](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-compiler-rust)
* [get-gcc](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-gcc) *(Detect or install GCC compiler)*
* [get-go](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-go)
* [get-llvm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-llvm) *(Detect or install LLVM compiler)*
* [install-gcc-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-gcc-src)
* [install-ipex-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-ipex-from-src) *(Build IPEX from sources)*
* [install-llvm-prebuilt](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-prebuilt) *(Install prebuilt LLVM compiler)*
* [install-llvm-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-src) *(Build LLVM compiler from sources (can take >30 min))*
* [install-onednn-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-onednn-from-src) *(Build oneDNN from sources)*
* [install-onnxruntime-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-onnxruntime-from-src) *(Build onnxruntime from sources)*
* [install-pytorch-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-pytorch-from-src) *(Build pytorch from sources)*
* [install-pytorch-kineto-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-pytorch-kineto-from-src) *(Build pytorch kineto from sources)*
* [install-torchvision-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-torchvision-from-src) *(Build pytorchvision from sources)*
* [install-tpp-pytorch-extension](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-tpp-pytorch-extension) *(Build TPP-PEX from sources)*
* [install-transformers-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-transformers-from-src) *(Build transformers from sources)*

### Dashboard automation

* [publish-results-to-dashboard](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/publish-results-to-dashboard)

### Detection or installation of tools and artifacts

* [get-android-sdk](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-android-sdk)
* [get-aria2](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aria2)
* [get-bazel](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-bazel)
* [get-blis](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-blis)
* [get-brew](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-brew)
* [get-cmake](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cmake)
* [get-cmsis_5](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cmsis_5)
* [get-docker](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-docker)
* [get-generic-sys-util](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-sys-util)
* [get-google-test](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-google-test)
* [get-java](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-java)
* [get-javac](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-javac)
* [get-lib-armnn](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-armnn)
* [get-lib-dnnl](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-dnnl)
* [get-lib-protobuf](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-protobuf)
* [get-lib-qaic-api](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-qaic-api)
* [get-nvidia-docker](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-nvidia-docker)
* [get-openssl](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-openssl)
* [get-rclone](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-rclone)
* [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-sys-utils-cm)
* [get-sys-utils-min](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-sys-utils-min)
* [get-xilinx-sdk](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-xilinx-sdk)
* [get-zendnn](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-zendnn)
* [install-bazel](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-bazel)
* [install-cmake-prebuilt](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cmake-prebuilt)
* [install-gflags](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-gflags)
* [install-github-cli](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-github-cli)
* [install-numactl-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-numactl-from-src) *(Build numactl from sources)*
* [install-openssl](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-openssl)

### DevOps automation

* [benchmark-program](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program)
* [compile-program](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/compile-program)
* [convert-csv-to-md](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-csv-to-md)
* [copy-to-clipboard](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/copy-to-clipboard)
* [create-conda-env](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-conda-env)
* [create-patch](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-patch)
* [detect-sudo](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-sudo)
* [download-and-extract](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-and-extract)
* [download-file](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-file)
* [download-torrent](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-torrent)
* [extract-file](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/extract-file)
* [fail](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/fail)
* [get-conda](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-conda)
* [get-git-repo](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-git-repo)
* [get-github-cli](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-github-cli)
* [pull-git-repo](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/pull-git-repo)
* [push-csv-to-spreadsheet](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-csv-to-spreadsheet)
* [set-device-settings-qaic](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-device-settings-qaic)
* [set-echo-off-win](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-echo-off-win)
* [set-performance-mode](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-performance-mode)
* [set-sqlite-dir](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-sqlite-dir)
* [tar-my-folder](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/tar-my-folder)

### Docker automation

* [build-docker-image](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-docker-image)
* [build-dockerfile](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-dockerfile)
* [prune-docker](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prune-docker)
* [run-docker-container](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-docker-container)

### GUI

* [gui](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/gui)

### Legacy CK support

* [get-ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ck)
* [get-ck-repo-mlops](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ck-repo-mlops)

### MLPerf benchmark support

* [add-custom-nvidia-system](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/add-custom-nvidia-system)
* [benchmark-any-mlperf-inference-implementation](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-any-mlperf-inference-implementation)
* [build-mlperf-inference-server-nvidia](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-mlperf-inference-server-nvidia)
* [generate-mlperf-inference-submission](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-submission)
* [generate-mlperf-inference-user-conf](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-user-conf)
* [generate-mlperf-tiny-report](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-tiny-report)
* [generate-mlperf-tiny-submission](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-tiny-submission)
* [generate-nvidia-engine](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-nvidia-engine)
* [get-mlperf-inference-intel-scratch-space](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-intel-scratch-space)
* [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-loadgen)
* [get-mlperf-inference-nvidia-common-code](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-nvidia-common-code)
* [get-mlperf-inference-nvidia-scratch-space](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-nvidia-scratch-space)
* [get-mlperf-inference-results](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-results)
* [get-mlperf-inference-results-dir](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-results-dir)
* [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-src)
* [get-mlperf-inference-submission-dir](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-submission-dir)
* [get-mlperf-inference-sut-configs](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-configs)
* [get-mlperf-inference-sut-description](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-description)
* [get-mlperf-logging](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-logging)
* [get-mlperf-power-dev](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-power-dev)
* [get-mlperf-tiny-eembc-energy-runner-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-tiny-eembc-energy-runner-src)
* [get-mlperf-tiny-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-tiny-src)
* [get-mlperf-training-nvidia-code](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-nvidia-code)
* [get-mlperf-training-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-src)
* [get-nvidia-mitten](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-nvidia-mitten)
* [get-spec-ptd](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-spec-ptd)
* [import-mlperf-inference-to-experiment](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/import-mlperf-inference-to-experiment)
* [import-mlperf-tiny-to-experiment](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/import-mlperf-tiny-to-experiment)
* [import-mlperf-training-to-experiment](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/import-mlperf-training-to-experiment)
* [install-mlperf-logging-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-mlperf-logging-from-src)
* [prepare-training-data-bert](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-bert)
* [prepare-training-data-resnet](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-resnet)
* [preprocess-mlperf-inference-submission](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/preprocess-mlperf-inference-submission)
* [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/process-mlperf-accuracy)
* [push-mlperf-inference-results-to-github](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-mlperf-inference-results-to-github)
* [run-mlperf-inference-mobilenet-models](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-mobilenet-models)
* [run-mlperf-inference-submission-checker](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-submission-checker)
* [run-mlperf-power-client](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-client)
* [run-mlperf-power-server](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-server)
* [run-mlperf-training-submission-checker](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-training-submission-checker)
* [truncate-mlperf-inference-accuracy-log](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/truncate-mlperf-inference-accuracy-log)

### Modular AI/ML application pipeline

* [app-image-classification-onnx-py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-onnx-py)
* [app-image-classification-tf-onnx-cpp](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-tf-onnx-cpp)
* [app-image-classification-torch-py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-torch-py)
* [app-image-classification-tvm-onnx-py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-tvm-onnx-py)
* [app-stable-diffusion-onnx-py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-stable-diffusion-onnx-py)

### Modular MLPerf benchmarks

* [app-mlperf-inference-dummy](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-dummy)
* [app-mlperf-inference-intel](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-intel)
* [app-mlperf-inference-qualcomm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-qualcomm)

### Modular MLPerf inference benchmark pipeline

* [app-loadgen-generic-python](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-loadgen-generic-python)
* [app-mlperf-inference](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference)
* [app-mlperf-inference-ctuning-cpp-tflite](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-ctuning-cpp-tflite)
* [app-mlperf-inference-mlcommons-cpp](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-mlcommons-cpp)
* [app-mlperf-inference-mlcommons-python](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-mlcommons-python)
* [benchmark-program-mlperf](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program-mlperf)
* [run-mlperf-inference-app](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-app)

### Modular MLPerf training benchmark pipeline

* [app-mlperf-training-nvidia](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-training-nvidia)
* [app-mlperf-training-reference](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-training-reference)

### Modular application pipeline

* [app-image-corner-detection](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-corner-detection)

### Platform information

* [detect-cpu](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-cpu)
* [detect-os](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-os)

### Python automation

* [activate-python-venv](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/activate-python-venv) *(Activate virtual Python environment)*
* [get-generic-python-lib](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-python-lib)
* [get-python3](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-python3)
* [install-generic-conda-package](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-generic-conda-package)
* [install-python-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-src)
* [install-python-venv](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-venv)

### Remote automation

* [remote-run-commands](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/remote-run-commands)

### Reproduce MLPerf benchmarks

* [app-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-nvidia)
* [reproduce-mlperf-octoml-tinyml-results](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results)
* [reproduce-mlperf-training-nvidia](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-training-nvidia)
* [wrapper-reproduce-octoml-tinyml-submission](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission)

### Reproducibility and artifact evaluation

* [get-ipol-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ipol-src)
* [process-ae-users](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/process-ae-users)
* [reproduce-ipol-paper-2022-439](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-ipol-paper-2022-439)

### Tests

* [print-croissant-desc](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-croissant-desc)
* [print-hello-world](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world)
* [print-hello-world-java](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world-java)
* [print-hello-world-javac](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world-javac)
* [print-hello-world-py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world-py)
* [print-python-version](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-python-version)
* [run-python](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-python)
* [test-download-and-extract-artifacts](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-download-and-extract-artifacts)
* [test-set-sys-user-cm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-set-sys-user-cm)
* [upgrade-python-pip](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/upgrade-python-pip)

### TinyML automation

* [create-fpgaconvnet-app-tinyml](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-app-tinyml)
* [create-fpgaconvnet-config-tinyml](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-config-tinyml)
* [flash-tinyml-binary](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/flash-tinyml-binary)
* [get-microtvm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-microtvm)
* [get-zephyr](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-zephyr)
* [get-zephyr-sdk](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-zephyr-sdk)


# List of all sorted CM scripts 

* [activate-python-venv](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/activate-python-venv) *(Activate virtual Python environment.)*
* [add-custom-nvidia-system](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/add-custom-nvidia-system)
* [app-image-classification-onnx-py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-onnx-py)
* [app-image-classification-tf-onnx-cpp](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-tf-onnx-cpp)
* [app-image-classification-torch-py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-torch-py)
* [app-image-classification-tvm-onnx-py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-classification-tvm-onnx-py)
* [app-image-corner-detection](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-image-corner-detection)
* [app-loadgen-generic-python](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-loadgen-generic-python)
* [app-mlperf-inference](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference)
* [app-mlperf-inference-ctuning-cpp-tflite](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-ctuning-cpp-tflite)
* [app-mlperf-inference-dummy](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-dummy)
* [app-mlperf-inference-intel](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-intel)
* [app-mlperf-inference-mlcommons-cpp](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-mlcommons-cpp)
* [app-mlperf-inference-mlcommons-python](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-mlcommons-python)
* [app-mlperf-inference-nvidia](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-nvidia)
* [app-mlperf-inference-qualcomm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-inference-qualcomm)
* [app-mlperf-training-nvidia](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-training-nvidia)
* [app-mlperf-training-reference](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-mlperf-training-reference)
* [app-stable-diffusion-onnx-py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/app-stable-diffusion-onnx-py)
* [benchmark-any-mlperf-inference-implementation](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-any-mlperf-inference-implementation)
* [benchmark-program](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program)
* [benchmark-program-mlperf](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/benchmark-program-mlperf)
* [build-docker-image](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-docker-image)
* [build-dockerfile](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-dockerfile)
* [build-mlperf-inference-server-nvidia](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/build-mlperf-inference-server-nvidia)
* [calibrate-model-for.qaic](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/calibrate-model-for.qaic)
* [compile-model-for.qaic](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/compile-model-for.qaic)
* [compile-program](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/compile-program)
* [convert-csv-to-md](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-csv-to-md)
* [convert-ml-model-huggingface-to-onnx](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/convert-ml-model-huggingface-to-onnx)
* [copy-to-clipboard](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/copy-to-clipboard)
* [create-conda-env](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-conda-env)
* [create-fpgaconvnet-app-tinyml](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-app-tinyml)
* [create-fpgaconvnet-config-tinyml](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-fpgaconvnet-config-tinyml)
* [create-patch](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/create-patch)
* [destroy-terraform](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/destroy-terraform)
* [detect-cpu](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-cpu)
* [detect-os](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-os)
* [detect-sudo](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/detect-sudo)
* [download-and-extract](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-and-extract)
* [download-file](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-file)
* [download-torrent](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/download-torrent)
* [dump-pip-freeze](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/dump-pip-freeze)
* [extract-file](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/extract-file)
* [fail](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/fail)
* [flash-tinyml-binary](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/flash-tinyml-binary)
* [generate-mlperf-inference-submission](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-submission)
* [generate-mlperf-inference-user-conf](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-inference-user-conf)
* [generate-mlperf-tiny-report](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-tiny-report)
* [generate-mlperf-tiny-submission](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-mlperf-tiny-submission)
* [generate-nvidia-engine](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/generate-nvidia-engine)
* [get-android-sdk](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-android-sdk)
* [get-aocl](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aocl)
* [get-aria2](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aria2)
* [get-aws-cli](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-aws-cli)
* [get-bazel](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-bazel)
* [get-bert-squad-vocab](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-bert-squad-vocab)
* [get-blis](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-blis)
* [get-brew](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-brew)
* [get-ck](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ck)
* [get-ck-repo-mlops](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ck-repo-mlops)
* [get-cl](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cl) *(Detect or install Microsoft C compiler.)*
* [get-cmake](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cmake)
* [get-cmsis_5](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cmsis_5)
* [get-compiler-flags](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-compiler-flags)
* [get-compiler-rust](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-compiler-rust)
* [get-conda](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-conda)
* [get-croissant](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-croissant)
* [get-cuda](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cuda)
* [get-cuda-devices](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cuda-devices)
* [get-cudnn](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-cudnn)
* [get-dataset-cifar10](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cifar10)
* [get-dataset-cnndm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-cnndm)
* [get-dataset-coco](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco)
* [get-dataset-coco2014](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-coco2014)
* [get-dataset-criteo](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-criteo)
* [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-aux)
* [get-dataset-imagenet-calibration](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-calibration)
* [get-dataset-imagenet-helper](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-helper)
* [get-dataset-imagenet-train](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-train)
* [get-dataset-imagenet-val](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-imagenet-val)
* [get-dataset-kits19](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-kits19)
* [get-dataset-librispeech](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-librispeech)
* [get-dataset-openimages](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages)
* [get-dataset-openimages-annotations](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages-annotations)
* [get-dataset-openimages-calibration](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openimages-calibration)
* [get-dataset-openorca](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-openorca)
* [get-dataset-squad](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-squad)
* [get-dataset-squad-vocab](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dataset-squad-vocab)
* [get-dlrm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dlrm)
* [get-dlrm-data-mlperf-inference](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-dlrm-data-mlperf-inference)
* [get-docker](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-docker)
* [get-gcc](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-gcc) *(Detect or install GCC compiler.)*
* [get-generic-python-lib](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-python-lib)
* [get-generic-sys-util](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-generic-sys-util)
* [get-git-repo](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-git-repo)
* [get-github-cli](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-github-cli)
* [get-go](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-go)
* [get-google-saxml](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-google-saxml)
* [get-google-test](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-google-test)
* [get-ipol-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ipol-src)
* [get-java](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-java)
* [get-javac](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-javac)
* [get-lib-armnn](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-armnn)
* [get-lib-dnnl](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-dnnl)
* [get-lib-protobuf](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-protobuf)
* [get-lib-qaic-api](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-lib-qaic-api)
* [get-llvm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-llvm) *(Detect or install LLVM compiler.)*
* [get-microtvm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-microtvm)
* [get-ml-model-3d-unet-kits19](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-3d-unet-kits19)
* [get-ml-model-bert-base-squad](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-base-squad)
* [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-bert-large-squad)
* [get-ml-model-dlrm-terabyte](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-dlrm-terabyte)
* [get-ml-model-efficientnet-lite](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-efficientnet-lite)
* [get-ml-model-gptj](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-gptj)
* [get-ml-model-huggingface-zoo](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-huggingface-zoo)
* [get-ml-model-llama2](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-llama2)
* [get-ml-model-mobilenet](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-mobilenet)
* [get-ml-model-neuralmagic-zoo](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-neuralmagic-zoo)
* [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-resnet50)
* [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-retinanet)
* [get-ml-model-retinanet-nvidia](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-retinanet-nvidia)
* [get-ml-model-rnnt](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-rnnt)
* [get-ml-model-stable-diffusion](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-stable-diffusion)
* [get-ml-model-tiny-resnet](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-tiny-resnet)
* [get-ml-model-using-imagenet-from-model-zoo](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-ml-model-using-imagenet-from-model-zoo)
* [get-mlperf-inference-intel-scratch-space](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-intel-scratch-space)
* [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-loadgen)
* [get-mlperf-inference-nvidia-common-code](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-nvidia-common-code)
* [get-mlperf-inference-nvidia-scratch-space](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-nvidia-scratch-space)
* [get-mlperf-inference-results](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-results)
* [get-mlperf-inference-results-dir](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-results-dir)
* [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-src)
* [get-mlperf-inference-submission-dir](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-submission-dir)
* [get-mlperf-inference-sut-configs](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-configs)
* [get-mlperf-inference-sut-description](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-sut-description)
* [get-mlperf-inference-utils](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-inference-utils)
* [get-mlperf-logging](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-logging)
* [get-mlperf-power-dev](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-power-dev)
* [get-mlperf-tiny-eembc-energy-runner-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-tiny-eembc-energy-runner-src)
* [get-mlperf-tiny-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-tiny-src)
* [get-mlperf-training-nvidia-code](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-nvidia-code)
* [get-mlperf-training-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-mlperf-training-src)
* [get-nvidia-docker](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-nvidia-docker)
* [get-nvidia-mitten](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-nvidia-mitten)
* [get-onnxruntime-prebuilt](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-onnxruntime-prebuilt)
* [get-openssl](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-openssl)
* [get-preprocessed-dataset-criteo](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-criteo)
* [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-imagenet)
* [get-preprocessed-dataset-kits19](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-kits19)
* [get-preprocessed-dataset-librispeech](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-librispeech)
* [get-preprocessed-dataset-openimages](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-openimages)
* [get-preprocessed-dataset-openorca](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-openorca)
* [get-preprocessed-dataset-squad](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocessed-dataset-squad)
* [get-preprocesser-script-generic](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-preprocesser-script-generic)
* [get-python3](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-python3)
* [get-qaic-apps-sdk](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-qaic-apps-sdk)
* [get-qaic-platform-sdk](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-qaic-platform-sdk)
* [get-qaic-software-kit](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-qaic-software-kit)
* [get-rclone](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-rclone)
* [get-rocm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-rocm)
* [get-spec-ptd](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-spec-ptd)
* [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-sys-utils-cm)
* [get-sys-utils-min](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-sys-utils-min)
* [get-tensorrt](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tensorrt)
* [get-terraform](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-terraform)
* [get-tvm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tvm)
* [get-tvm-model](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-tvm-model)
* [get-xilinx-sdk](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-xilinx-sdk)
* [get-zendnn](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-zendnn)
* [get-zephyr](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-zephyr)
* [get-zephyr-sdk](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/get-zephyr-sdk)
* [gui](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/gui)
* [import-mlperf-inference-to-experiment](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/import-mlperf-inference-to-experiment)
* [import-mlperf-tiny-to-experiment](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/import-mlperf-tiny-to-experiment)
* [import-mlperf-training-to-experiment](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/import-mlperf-training-to-experiment)
* [install-aws-cli](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-aws-cli)
* [install-bazel](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-bazel)
* [install-cmake-prebuilt](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cmake-prebuilt)
* [install-cuda-package-manager](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cuda-package-manager)
* [install-cuda-prebuilt](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-cuda-prebuilt)
* [install-gcc-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-gcc-src)
* [install-generic-conda-package](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-generic-conda-package)
* [install-gflags](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-gflags)
* [install-github-cli](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-github-cli)
* [install-ipex-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-ipex-from-src) *(Build IPEX from sources.)*
* [install-llvm-prebuilt](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-prebuilt) *(Install prebuilt LLVM compiler.)*
* [install-llvm-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-llvm-src) *(Build LLVM compiler from sources (can take >30 min).)*
* [install-mlperf-logging-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-mlperf-logging-from-src)
* [install-nccl-libs](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-nccl-libs)
* [install-numactl-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-numactl-from-src) *(Build numactl from sources.)*
* [install-onednn-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-onednn-from-src) *(Build oneDNN from sources.)*
* [install-onnxruntime-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-onnxruntime-from-src) *(Build onnxruntime from sources.)*
* [install-openssl](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-openssl)
* [install-pip-package-for-cmind-python](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-pip-package-for-cmind-python)
* [install-python-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-src)
* [install-python-venv](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-python-venv)
* [install-pytorch-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-pytorch-from-src) *(Build pytorch from sources.)*
* [install-pytorch-kineto-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-pytorch-kineto-from-src) *(Build pytorch kineto from sources.)*
* [install-qaic-compute-sdk-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-qaic-compute-sdk-from-src)
* [install-rocm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-rocm)
* [install-tensorflow-for-c](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-tensorflow-for-c)
* [install-tensorflow-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-tensorflow-from-src)
* [install-terraform-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-terraform-from-src)
* [install-tflite-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-tflite-from-src)
* [install-torchvision-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-torchvision-from-src) *(Build pytorchvision from sources.)*
* [install-tpp-pytorch-extension](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-tpp-pytorch-extension) *(Build TPP-PEX from sources.)*
* [install-transformers-from-src](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/install-transformers-from-src) *(Build transformers from sources.)*
* [launch-benchmark](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/launch-benchmark)
* [prepare-training-data-bert](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-bert)
* [prepare-training-data-resnet](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prepare-training-data-resnet)
* [preprocess-mlperf-inference-submission](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/preprocess-mlperf-inference-submission)
* [print-croissant-desc](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-croissant-desc)
* [print-hello-world](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world)
* [print-hello-world-java](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world-java)
* [print-hello-world-javac](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world-javac)
* [print-hello-world-py](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-hello-world-py)
* [print-python-version](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/print-python-version)
* [process-ae-users](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/process-ae-users)
* [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/process-mlperf-accuracy)
* [prune-bert-models](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prune-bert-models)
* [prune-docker](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/prune-docker)
* [publish-results-to-dashboard](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/publish-results-to-dashboard)
* [pull-git-repo](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/pull-git-repo)
* [push-csv-to-spreadsheet](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-csv-to-spreadsheet)
* [push-mlperf-inference-results-to-github](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/push-mlperf-inference-results-to-github)
* [remote-run-commands](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/remote-run-commands)
* [reproduce-ipol-paper-2022-439](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-ipol-paper-2022-439)
* [reproduce-mlperf-octoml-tinyml-results](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results)
* [reproduce-mlperf-training-nvidia](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/reproduce-mlperf-training-nvidia)
* [run-docker-container](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-docker-container)
* [run-mlperf-inference-app](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-app)
* [run-mlperf-inference-mobilenet-models](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-mobilenet-models)
* [run-mlperf-inference-submission-checker](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-inference-submission-checker)
* [run-mlperf-power-client](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-client)
* [run-mlperf-power-server](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-power-server)
* [run-mlperf-training-submission-checker](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-mlperf-training-submission-checker)
* [run-python](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-python)
* [run-terraform](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/run-terraform)
* [save-mlperf-inference-implementation-state](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/save-mlperf-inference-implementation-state)
* [set-device-settings-qaic](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-device-settings-qaic)
* [set-echo-off-win](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-echo-off-win)
* [set-performance-mode](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-performance-mode)
* [set-sqlite-dir](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-sqlite-dir)
* [set-venv](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/set-venv)
* [tar-my-folder](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/tar-my-folder)
* [test-download-and-extract-artifacts](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-download-and-extract-artifacts)
* [test-mlperf-inference-retinanet](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-mlperf-inference-retinanet)
* [test-set-sys-user-cm](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/test-set-sys-user-cm)
* [truncate-mlperf-inference-accuracy-log](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/truncate-mlperf-inference-accuracy-log)
* [upgrade-python-pip](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/upgrade-python-pip)
* [wrapper-reproduce-octoml-tinyml-submission](https://github.com/mlcommons/ck/tree/dev/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission)



