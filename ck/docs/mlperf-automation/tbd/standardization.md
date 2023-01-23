**[ [TOC](../README.md) ]**

# Standardization

## CK packages with ML models

Examples of JSON meta for CK packages with ML models:
* [SSD ResNet34 1200x1200 ONNX](https://github.com/mlcommons/ck-mlops/blob/main/package/ml-model-mlperf-ssd-resnet34-1200-onnx/.cm/meta.json#L6)
* [MobileNet v1.0 224x224 TensorFlow](https://github.com/mlcommons/ck-mlops/blob/main/package/ml-model-mlperf-ssd-resnet34-1200-onnx/.cm/meta.json#L6)
* [MobileNet v3.0 224x224 TFLite]( https://github.com/mlcommons/ck-mlops/blob/main/package/model-tf-and-tflite-mlperf-mobilenet-v3/.cm/meta.json )

## CK workflows for MLPerf

Examples:
* [MLPerf inference, object detection, ONNX, CPU](https://github.com/mlcommons/ck-mlops/blob/main/program/mlperf-inference-bench-object-detection-onnx-cpu/.cm/meta.json)

## TBD

We need to standardize:
* CK package meta and env for models
* CK package meta and env for datasets
* CK package meta and env for frameworks and libraries
* platform description
* CK program API for MLPerf&trade; tasks
* Power measurements
* Visualization of all results on multi-dimensional Pareto-frontier
