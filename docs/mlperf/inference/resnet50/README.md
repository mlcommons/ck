[ [Back to MLPerf inference benchmarks index](../README.md) ]

# MLPerf inference benchmark

## Image classification with ResNet50

### Notes
 
In the edge category, ResNet50 has Offline, SingleStream, and MultiStream scenarios and in the datacenter category, it has Offline and Server scenarios. 

Please check [MLPerf inference GitHub](https://github.com/mlcommons/inference) for more details.

### Run using the [MLCommons CM framework](https://github.com/mlcommons/ck)

*From Feb 2024, we suggest you to use [this GUI](https://access.cknowledge.org/playground/?action=howtorun&bench_uid=39877bb63fb54725)
 to configure MLPerf inference benchmark, generate CM commands to run it across different implementations, models, data sets, software
 and hardware, and prepare your submissions.*

### Get Imagenet Dataset

We need to get full ImageNet dataset to make image-classification submissions for MLPerf inference. 
Since this dataset is not publicly available via a URL please follow the instructions 
given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md) 
to download the dataset and register in CM.

### A few ready-to-use CM commands

Install MLCommons CM automation framework with automation recipes for MLPerf as described [here](../../../installation.md).

The following guides explain how to run different implementations of this benchmark via CM:

* [MLCommons Reference implementation in Python](README_reference.md)
* [NVIDIA optimized implementation (GPU)](README_nvidia.md)
* [TFLite C++ implementation](README_tflite.md)

### Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
