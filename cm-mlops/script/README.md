These portable and reusable CM scripts are being developed by the [MLCommons taskforce](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md) 
to make MLOps and DevOps more interoperable, reusable, portable, deterministic and reproducible.

## Catalog

### Compilers
* [detect/install GCC](script/get-gcc)
* [detect/install LLVM](script/get-llvm)
* [detect/install CUDA](script/get-cuda)

### ML models
* [install Bert-Large model (ONNX)](script/get-ml-model-bert-large-squad-onnx)
* [install Retinanet model (ONNX)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-retinanet)
* [install ResNet50 (ONNX, fp32)](script/get-ml-model-resnet50-onnx), [pytorch](script/get-ml-model-resnet50-pytorch) and [tensorflow](script/get-ml-model-resnet50-tf)
* [install RetinaNet (ONNX and PyTorch, fp32)](script/get-ml-model-retinanet)

### ML datasets
* [detect imageNet 2012 validation set](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-imagenet-val) (1,500,50000 images)
  * [Preprocess ImageNet](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-imagenet-preprocessed)
* [install Open Images](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-openimages-original)
* [install SQUAD dataset](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-squad)

### ML engines
* [detect/install tensorflow](script/get-tensorflow)
* [detect/install onnxruntime](script/get-onnxruntime)
* [detect/install pytorch](script/get-pytorch)
* [detect/install TVM](script/get-tvm)

### Apps
* [Run image classification onnx](script/app-image-classification-onnx-py), [onnx cpp](script/app-image-classification-onnx-cpp), [pytorch](script/app-image-classification-torch-py)
* [Run image corner detection]()
* [Run MLPerf inference vision run and submission generation from reference code](script/generate-mlc-inference-submission)
* [Run MLPerf image classification and submission generation from cpp code](script/app-mlperf-inference-cpp)

### Benchmarks
* [Run MLPerf inference image classification, object detection](script/app-mlperf-inference-vision-reference)

### Aux tools
* [detect/install bazel](script/get-bazel)
* [detect/install DNNLl](script/get-lib-dnnl)
* [detect/install zephyr](script/get-zephyr)
* [detect/install zephyr-sdk](script/get-zephyr-sdk)

### Containers
* [Build modular Docker container (Ubuntu 18.04, 20.04, 22.04 and RHEL9)](script/build-dockerfile/dockerfiles)



(C)opyright 2022 [MLCommons](https://mlcommons.org)
