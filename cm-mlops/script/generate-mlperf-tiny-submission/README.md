*This README is automatically generated - don't edit! See [extra README](README-extra.md) for extra notes!*

<details>
<summary>Click here to see the table of contents.</summary>

* [About](#about)
* [Category](#category)
* [Origin](#origin)
* [Meta description](#meta-description)
* [Tags](#tags)
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
* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission)*
* CM automation "script": *[Docs](https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script)*

___
### Meta description
[_cm.json](_cm.json)

___
### Tags
generate,submission,mlperf,mlperf-tiny,tiny,mlcommons,tiny-submission,mlperf-tiny-submission,mlcommons-tiny-submission

___
### Default environment

___
### CM script workflow

  1. ***Read "deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission/_cm.json)***
     * get,python3
       * CM names: `--adr.['python', 'python3']...`
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
     * get,sut,system-description
       - CM script: [get-mlperf-inference-sut-description](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description)
  1. ***Run "preprocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission/customize.py)***
  1. Read "prehook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission/_cm.json)
  1. ***Run native script if exists***
  1. Read "posthook_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission/_cm.json)
  1. ***Run "postrocess" function from [customize.py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission/customize.py)***
  1. ***Read "post_deps" on other CM scripts from [meta](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission/_cm.json)***
     * 
       * `if (CM_MLPERF_RUN_STYLE  == valid)`
       - CM script: [get-android-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-android-sdk)
       - CM script: [get-go](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-go)
       - CM script: [run-mlperf-inference-app](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-app)
       - CM script: [get-llvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-llvm)
       - CM script: [install-llvm-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-prebuilt)
       - CM script: [get-ml-model-resnet50-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50-tvm)
       - CM script: [get-aws-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-aws-cli)
       - CM script: [get-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-openimages)
       - CM script: [get-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-python-lib)
       - CM script: [install-tflite-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tflite-from-src)
       - CM script: [run-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-terraform)
       - CM script: [get-mlperf-inference-results](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-results)
       - CM script: [destroy-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/destroy-terraform)
       - CM script: [app-mlperf-image-classification-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-image-classification-cpp)
       - CM script: [prototype-lib-dnnl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/prototype-lib-dnnl)
       - CM script: [get-cuda-devices](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda-devices)
       - CM script: [get-ml-model-rnnt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-rnnt)
       - CM script: [get-github-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-github-cli)
       - CM script: [get-tvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tvm)
       - CM script: [get-cudnn](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cudnn)
       - CM script: [run-mlperf-inference-submission-checker](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-inference-submission-checker)
       - CM script: [install-tensorflow-for-c](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-for-c)
       - CM script: [get-preprocessed-dataset-criteo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-criteo)
       - CM script: [print-hello-world-java](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-java)
       - CM script: [install-python-venv](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-venv)
       - CM script: [get-bazel](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-bazel)
       - CM script: [get-mlperf-inference-sut-description](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-description)
       - CM script: [activate-python-venv](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/activate-python-venv)
       - CM script: [get-cuda](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda)
       - CM script: [install-cmake-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cmake-prebuilt)
       - CM script: [get-ml-model-3d-unet-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-3d-unet-kits19)
       - CM script: [set-echo-off-win](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/set-echo-off-win)
       - CM script: [get-sys-utils-min](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-min)
       - CM script: [get-zephyr](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr)
       - CM script: [app-loadgen-generic-python](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-loadgen-generic-python)
       - CM script: [install-tensorflow-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-tensorflow-from-src)
       - CM script: [app-image-classification-tvm-onnx-py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-tvm-onnx-py)
       - CM script: [get-ml-model-retinanet-nvidia](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet-nvidia)
       - CM script: [install-generic-python-lib](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-generic-python-lib)
       - CM script: [print-hello-world-py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-py)
       - CM script: [generate-mlperf-inference-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-inference-submission)
       - CM script: [get-dlrm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dlrm)
       - CM script: [get-mlperf-inference-sut-configs](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-sut-configs)
       - CM script: [build-dockerfile](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-dockerfile)
       - CM script: [get-dataset-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad)
       - CM script: [get-dataset-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-kits19)
       - CM script: [get-terraform](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-terraform)
       - CM script: [process-mlperf-accuracy](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/process-mlperf-accuracy)
       - CM script: [get-ml-model-retinanet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
       - CM script: [get-dataset-imagenet-aux](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-aux)
       - CM script: [install-llvm-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-llvm-src)
       - CM script: [get-preprocessed-dataset-openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-openimages)
       - CM script: [test-set-sys-user-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/test-set-sys-user-cm)
       - CM script: [install-github-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-github-cli)
       - CM script: [remote-run-commands](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/remote-run-commands)
       - CM script: [get-mlperf-inference-nvidia-common-code](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-nvidia-common-code)
       - CM script: [install-cuda-package-manager](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-package-manager)
       - CM script: [app-mlperf-inference-reference](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference)
       - CM script: [install-gcc-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-gcc-src)
       - CM script: [get-dataset-criteo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-criteo)
       - CM script: [app-image-classification-onnx-py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-py)
       - CM script: [get-ml-model-dlrm-terabyte](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-dlrm-terabyte)
       - CM script: [app-image-classification-torch-py](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-torch-py)
       - CM script: [get-openssl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-openssl)
       - CM script: [get-microtvm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-microtvm)
       - CM script: [compile-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/compile-program)
       - CM script: [get-preprocesser-script-generic](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocesser-script-generic)
       - CM script: [get-tensorrt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-tensorrt)
       - CM script: [get-gcc](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-gcc)
       - CM script: [detect-os](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-os)
       - CM script: [get-onnxruntime-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-onnxruntime-prebuilt)
       - CM script: [install-openssl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-openssl)
       - CM script: [install-bazel](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-bazel)
       - CM script: [run-mlperf-power-server](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-server)
       - CM script: [build-docker-image](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image)
       - CM script: [get-dataset-imagenet-helper](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-helper)
       - CM script: [detect-cpu](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/detect-cpu)
       - CM script: [get-dataset-imagenet-val](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-imagenet-val)
       - CM script: [install-terraform-from-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-terraform-from-src)
       - CM script: [get-compiler-flags](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-compiler-flags)
       - CM script: [print-hello-world-json](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world-json)
       - CM script: [get-ml-model-resnet50](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-resnet50)
       - CM script: [install-cuda-prebuilt](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-cuda-prebuilt)
       - CM script: [app-image-classification-onnx-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-classification-onnx-cpp)
       - CM script: [get-sys-utils-cm](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sys-utils-cm)
       - CM script: [get-spec-ptd](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-spec-ptd)
       - CM script: [get-ck](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ck)
       - CM script: [get-cl](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cl)
       - CM script: [run-mlperf-power-client](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-mlperf-power-client)
       - CM script: [app-image-corner-detection](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-image-corner-detection)
       - CM script: [install-python-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-python-src)
       - CM script: [run-docker-container](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/run-docker-container)
       - CM script: [get-ck-repo-mlops](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ck-repo-mlops)
       - CM script: [generate-mlperf-tiny-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/generate-mlperf-tiny-submission)
       - CM script: [tar-my-folder](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/tar-my-folder)
       - CM script: [get-generic-sys-util](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-generic-sys-util)
       - CM script: [get-dataset-librispeech](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-librispeech)
       - CM script: [get-preprocessed-dataset-imagenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-imagenet)
       - CM script: [flash-tinyml-binary](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/flash-tinyml-binary)
       - CM script: [reproduce-mlperf-octoml-tinyml-results](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results)
       - CM script: [get-zephyr-sdk](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-zephyr-sdk)
       - CM script: [get-preprocessed-dataset-kits19](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-kits19)
       - CM script: [get-preprocessed-dataset-librispeech](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-preprocessed-dataset-librispeech)
       - CM script: [app-mlperf-inference](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference)
       - CM script: [wrapper-reproduce-octoml-tinyml-submission](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/wrapper-reproduce-octoml-tinyml-submission)
       - CM script: [get-ml-model-mobilenet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-mobilenet)
       - CM script: [get-javac](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-javac)
       - CM script: [get-python3](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-python3)
       - CM script: [truncate-mlperf-inference-accuracy-log](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/truncate-mlperf-inference-accuracy-log)
       - CM script: [app-mlperf-inference-nvidia-harness](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-nvidia-harness)
       - CM script: [print-python-version](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-python-version)
       - CM script: [benchmark-program](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-program)
       - CM script: [publish-results-to-dashboard](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/publish-results-to-dashboard)
       - CM script: [install-aws-cli](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/install-aws-cli)
       - CM script: [get-cmake](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmake)
       - CM script: [get-mlperf-inference-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-src)
       - CM script: [get-mlperf-inference-loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)
       - CM script: [get-java](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-java)
       - CM script: [get-cmsis_5](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cmsis_5)
       - CM script: [print-hello-world](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/print-hello-world)
       - CM script: [get-mlperf-power-dev](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-power-dev)
       - CM script: [app-mlperf-inference-cpp](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp)
       - CM script: [get-ml-model-bert-large-squad](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-bert-large-squad)
       - CM script: [get-mlperf-training-src](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-training-src)
___
### New environment export

___
### New environment detected from customize

* **CM_MLPERF_SUBMISSION_DIR**
* **CM_MLPERF_SUBMITTER**
___
### Usage

#### CM installation
[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

#### CM script automation help
```cm run script --help```

#### CM CLI
`cm run script --tags="generate,submission,mlperf,mlperf-tiny,tiny,mlcommons,tiny-submission,mlperf-tiny-submission,mlcommons-tiny-submission"`

*or*

`cm run script "generate submission mlperf mlperf-tiny tiny mlcommons tiny-submission mlperf-tiny-submission mlcommons-tiny-submission"`

*or*

`cm run script 04289b9fc07b42b6`

#### CM Python API

```python
import cmind

r = cmind.access({'action':'run'
                  'automation':'script',
                  'tags':'generate,submission,mlperf,mlperf-tiny,tiny,mlcommons,tiny-submission,mlperf-tiny-submission,mlcommons-tiny-submission'
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
___
### Maintainers

* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)