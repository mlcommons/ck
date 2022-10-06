These portable and reusable scripts are being developed by the [open workgroup](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md) 
to unify benchmarking, optimization and deployment of ML and AI systems across different SW/HW stacks - please join this community effort!

## Catalog

### Compilers
* [detect/install GCC](script/get-gcc)
* [detect/install LLVM](script/get-llvm)
* [detect/install CUDA](script/get-cuda)

### ML models
* [install resnet50 (ONNX, fp32)](script/get-ml-model-resnet50-onnx), [pytorch](script/get-ml-model-resnet50-pytorch) and [tensorflow](script/get-ml-model-resnet50-tf)
* [install retinanet (ONNX and PyTorch, fp32)](script/get-ml-model-retinanet)

### ML datasets
* [detect imagenet 2012 validation set](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-imagenet-val) (1,500,50000 images)
* [install imagenet preprocessed](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-imagenet-preprocessed)
* [install openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-openimages-original)

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
* [detect/install zephyr](script/get-zephyr)
* [detect/install zephyr-sdk](script/get-zephyr-sdk)
* [detect/install bazel](script/get-bazel)
* [detect/install DNNLl](script/get-lib-dnnl)

### Containers
* [Build modular Docker container (Ubuntu 18.04, 20.04, 22.04 and RHEL9)](script/build-dockerfile/dockerfiles)



(C)opyright 2022 [MLCommons](https://mlcommons.org)
