# About

This portable CM script and C++ code was developed by [Thomas Zhu](https://www.linkedin.com/in/hanwen-zhu-483614189) 
to provide modular C++ implementations of the [MLPerf inference benchmark](https://github.com/mlcommons/inference) 
using the [MLCommons CM automation meta-framework](https://github.com/mlcommons/ck).

It is being extended by the [MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)
to make it easier to run, optimize and reproduce MLPerf benchmarks 
across diverse platforms with continuously changing software and hardware.

[![License](https://img.shields.io/badge/License-Apache%202.0-green)](https://github.com/mlcommons/ck/tree/master/cm)
[![CM repository](https://img.shields.io/badge/Collective%20Mind-compatible-blue)](https://github.com/mlcommons/ck)

&copy; 2021-2022 [MLCommons](https://mlcommons.org)<br>

# Developers

[Thomas Zhu](https://www.linkedin.com/in/hanwen-zhu-483614189), 
[Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)
and [Grigori Fursin]( https://cKnowledge.org/gfursin ).




## About

This is a modularized C++ implementation of an MLPerf Inference SUT. Each file corresponds to a different class that can be changed independently of other ones:
1. `Backend` runs the actual inference using a framework (ONNX Runtime, TF Lite, etc)
2. `Device` manages devices and memory (CPU, GPU, etc)
3. `Model` is a struct representing a model file (ResNet50, etc)
4. `SampleLibrary` is a dataset loader (ImageNet, COCO, etc)
5. `System` is the SUT interface to LoadGen which manages how input queries are issued

Data flow:
* Init
   1. All classes are initialized, e.g. `Backend` is initalized with selected `Model` and `Device`
* Loading samples to memory
   1. LoadGen calls `SampleLibrary->LoadSamplesFromRam()`
   2. `SampleLibrary` reads sample (e.g. from .npy file) and calls `Backend->LoadSampleFromRam()`
   3. `Backend` stores samples contiguously into each device memory, e.g. by `Device->Write()`
* Running the model
   1. LoadGen calls `System->IssueQuery()`
   2. `System` gathers a batch of samples, selects a device concurrency (e.g. the 3rd CPU core) and calls `Backend->IssueBatch()`
   3. `Backend` retrieves pointers to input data in device memory, and calls `RunInference()` implemented by a derived class, e.g. `OnnxRuntimeBackend->RunInference()`
   4. in this example, `OnnxRuntimeBackend->RunInference()` calls the ONNX Runtime API with the retrieved pointers as input, packs the raw ONNX Runtime output to LoadGen format via `Model->PostProcess()`, and sends the response to LoadGen
   5. LoadGen records the latency from 1 to 4

See comments in code for each class for details.

## Examples

### ResNet50, ONNX Runtime, CPU, Accuracy
```sh
cm run script "cpp mlperf _resnet50 _onnxruntime _cpu" \
   --output_dir=<OUTPUT_DIR> \
   --count=500 \
   --max_batchsize=32 \
   --mode=accuracy

python \
   /PATH/TO/inference/vision/classification_and_detection/tools/accuracy-imagenet.py \
   --mlperf-accuracy-file=<OUTPUT_DIR>/mlperf_log_accuracy.json \
   --imagenet-val-file `cm find cache --tags=imagenet-aux`/data/val.txt \
   --dtype int64
```

### RetinaNet, ONNX Runtime, GPU, Accuracy
Install dataset:
```sh
cm run script --tags=get,preprocessed,openimages,_500,_NCHW
```
Run benchmark:
```sh
cm run script "cpp mlperf _retinanet _onnxruntime _cuda" \
   --output_dir=<OUTPUT_DIR> \
   --count=500 \
   --max_batchsize=1 \
   --mode=accuracy

python /PATH/TO/inference/vision/classification_and_detection/tools/accuracy-openimages.py \
    --mlperf-accuracy-file <OUTPUT_DIR>/mlperf_log_accuracy.json \
    --openimages-dir `cm find cache --tags=openimages,original`/install
```
