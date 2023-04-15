**[ [TOC](../README.md) ]**

# Reproducibility reports: MLPerf&trade; inference benchmark v1.1

* Official results: [Datacenter](https://mlcommons.org/en/inference-datacenter-11), [Edge](https://mlcommons.org/en/inference-edge-11)
* Raw results: [GitHub](https://github.com/mlcommons/inference_results_v1.1)
* News: [MLCommons press-release](https://mlcommons.org/en/news/mlperf-inference-v11)

### Image Classification

***Powered by the [MLCommons CK automation suite v2.5.8](https://github.com/mlcommons/ck-mlops/tree/main/module/bench.mlperf.inference):***

* [Resnet50; TVM; AWS m5zn.6xlarge; X64; datacenter; open division](ck-94cc7bdd1f23cce3.md)
* [Resnet50; TVM; GCP n2-standard-80; X64; datacenter; open division](ck-c3d81b4b869e8e07.md)
* [Resnet50; TVM; AWS c6gd.xlarge; ARM64; edge; closed division](ck-1b165548d8adbe4d.md)
* [Resnet50; TVM; Raspberry Pi 4; ARM64; edge; closed division](ck-3c77b273b4c7d878.md)
* [Design Space Exploration (Pareto frontier): efficientnet-lite0-non-quantized; TFLite; AWS c6gd.xlarge; Neoverse-N1; edge; open division](ck-6582273dd3646e28.md)
* [Design Space Exploration (Pareto frontier): mobilenet-v1-0.25-224-quantized; TFLite; AWS c6gd.xlarge; Neoverse-N1; edge; open division](ck-ae88dc4516a7084e.md)
* [Design Space Exploration (Pareto frontier): mobilenet-v3-large-minimalistic_224_1.0_uint8; TFLite; AWS c6gd.xlarge; Neoverse-N1; edge; open division](ck-b14c70816eca59c6.md)
* [Resnet50; ONNX (out of the box); AWS m5zn.6xlarge; X64; datacenter; open division](ck-3e0ad4b09998375d.md)
* [Resnet50; TensorFlow (out of the box); AWS m5zn.6xlarge; X64; datacenter; open division](ck-a399f837b48b0d1b.md)
* [Resnet50; ONNX (out of the box); GCP n2-standard-80; X64; datacenter; open division](ck-4f1a470a8a034bc3.md)
* [Resnet50; TensorFlow (out of the box); GCP n2-standard-80; X64; datacenter; open division](ck-9fb65e57d8c61db4.md)


Further developments of [CK workflows](../README.md) for other ML benchmarks, models and data sets 
are supported by [MLCommons&trade;](https://mlcommons.org) within the *Design Space Exploration workgroup*. 
Please contact [Grigori Fursin](mailto:grigori@octoml.ai) (workgroup co-chair) 
if you are interested to join this community effort!


# Reproducing MLPerf&trade; inference benchmarks (v0.7 and v1.0)

## Using native MLCommons&trade; scripts

* [Dell EMC System inteference v0.7](https://infohub.delltechnologies.com/p/running-the-mlperf-inference-v0-7-benchmark-on-dell-emc-systems)
* [NVidia Jetson Xavier](reproduce/image-classification-nvidia-jetson-xavier-mlperf.md)

## Using CK workflows

* [Official MLCommons&trade; notes for image classification (outdated - more automation exists)](https://github.com/mlcommons/inference/tree/master/vision/classification_and_detection/optional_harness_ck/classification)
* [Official MLCommons&trade; notes for object detection (outdated - more automations exists)](https://github.com/mlcommons/inference/tree/master/vision/classification_and_detection/optional_harness_ck/detection)

## Using CK adaptive containers (to be tested!)

* [MLPerf&trade; workflows](https://cknow.io/?q=module_uoa%3A%22docker%22+AND+%22mlperf%22)

* [CK image classification](https://cknow.io/?q=module_uoa%3A%22docker%22+AND+%22image-classification%22)
* [CK object detection](https://cknow.io/?q=module_uoa%3A%22docker%22+AND+%22object-detection%22)


# Other reproducibility studies

## Image Classification

* [**Example of adaptive CK container:** AMD (x8664) with TFlite](ck-image-classification-x86-64-docker.md)
* [x86 TFLite ImageNet](ck-image-classification-x86-64-tflite.md)
* [RPi4 TFLite ImageNet](ck-image-classification-rpi4-tflite.md)
* [Nvidia Jetson Nano (CPU) TFLite ImageNet](ck-image-classification-jetson-nano-tflite.md)

## Object detection

* [**Example of adaptive CK container:** AMD (x8664) with TFlite](ck-object-detection-x86-64-docker.md)
* [AMD (x8664) with TFlite](ck-object-detection-x86-64.md)
* [Coral EdgeTPU on RPi4 with TFlite](ck-object-detection-rpi4-coral-tflite.md)
* [RPi4 with TFlite](ck-object-detection-rpi4-tflite.md)
