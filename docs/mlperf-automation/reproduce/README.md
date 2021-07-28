**[ [TOC](../README.md) ]**

# Reproduce MLPerf&trade; benchmark

## Using ad-hoc MLCommons&trade; scripts

* [Dell EMC System inteference v0.7](https://infohub.delltechnologies.com/p/running-the-mlperf-inference-v0-7-benchmark-on-dell-emc-systems)
* [NVidia Jetson Xavier](reproduce/image-classification-nvidia-jetson-xavier-mlperf.md)

## Using CK workflows

* [Official MLCommons&trade; notes for image classification (a bit outdated - more automation exists)](https://github.com/mlcommons/inference/tree/master/vision/classification_and_detection/optional_harness_ck/classification)
* [Official MLCommons&trade; notes for object detection (a bit outdated - more automations exists)](https://github.com/mlcommons/inference/tree/master/vision/classification_and_detection/optional_harness_ck/detection)

## Using CK adaptive containers (to be tested!)

* [MLPerf&trade; workflows](https://cknowledge.io/?q=module_uoa%3A%22docker%22+AND+%22mlperf%22)

* [CK image classification](https://cknowledge.io/?q=module_uoa%3A%22docker%22+AND+%22image-classification%22)
* [CK object detection](https://cknowledge.io/?q=module_uoa%3A%22docker%22+AND+%22object-detection%22)


# Reproducibility studies

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
