**[ [TOC](../README.md) ]**

# CK workflows for image classification with TFLite

* [Old CK workflow](https://github.com/mlcommons/ck-mlops/tree/main/program/image-classification-tflite-loadgen)

# Supported ML models

* EfficientNet (quantized/non-quantized): [TensorFlow and TFLite](https://github.com/mlcommons/ck-mlops/tree/main/package/model-tflite-mlperf-efficientnet-lite/.cm/meta.json)
* MobileNet-v3 (quantized/non-quantized): [TensorFlow and TFLite](https://github.com/mlcommons/ck-mlops/tree/main/package/model-tf-and-tflite-mlperf-mobilenet-v3/.cm/meta.json)
* MobileNet-v2 (quantized): [TensorFlow and TFLite](https://github.com/mlcommons/ck-mlops/tree/main/package/model-tf-and-tflite-mlperf-mobilenet-v2-quant/.cm/meta.json)
* MobileNet-v2 (non-quantized): [TensorFlow and TFLite](https://github.com/mlcommons/ck-mlops/tree/main/package/model-tf-and-tflite-mlperf-mobilenet-v2/.cm/meta.json)
* MobileNet-v1 (quantized/non-quantized): [TensorFlow and TFLite](https://github.com/mlcommons/ck-mlops/tree/main/package/model-tf-and-tflite-mlperf-mobilenet-v1-20180802/.cm/meta.json)

# Reproducibility studies

* [x8664](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/reproduce/ck-image-classification-x86-64-tflite2.md)
* [RPi4](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/reproduce/ck-image-classification-rpi4-tflite.md)
* [Jetson Nano](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/reproduce/ck-image-classification-jetson-nano-tflite.md)

# Future work

We plan to update above workflow to be compatible with our 
[new end-to-end MLPerf submission workflow](https://github.com/mlcommons/ck-mlops/tree/main/module/bench.mlperf.inference).
