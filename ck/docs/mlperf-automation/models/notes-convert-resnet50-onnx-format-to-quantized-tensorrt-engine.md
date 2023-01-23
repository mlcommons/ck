**[ [TOC](../README.md) ]**

BeyondCloud commented:

Hi,
I am trying to reproduce the resnet50 benchmark result shows on [mlperf.org](https://mlperf.org/inference-results-0-7) (edged/closed division row 4). Currently I can achieve 2.4ms latency on Jetson Xavier AGX SingleStream scenario . However, I use [trtexec](https://github.com/NVIDIA/TensorRT/tree/master/samples/opensource/trtexec) to generate the int8 engine file from resnet50_v1.onnx and trtexec does not support calibration (it uses random weight instead). Could you tell me how did you convert resnet50_v1.onnx to int8 engine file (or plan file) you use in this [this repo](https://github.com/ctuning/ck-mlperf/tree/master/program/image-classification-tensorrt-loadgen-py/)? 

psyhtest commented:


To obtain the TensorRT plans, we followed NVIDIA's [instructions](https://github.com/mlcommons/inference_results_v0.5/tree/master/closed/NVIDIA) from their MLPerf&trade; Inference v0.5 submission. This happened between the v0.5 and v0.7 submission rounds, i.e. between October 2019 - September 2020. we submitted the results to v0.7 (without DLA support).

After v0.7, we [reproduced](https://github.com/ctuning/ck-ml/blob/master/jnotebook/mlperf-inference-v0.7-reproduce-xavier/) some of the results with JetPack 4.5, while [resolving](https://github.com/mlcommons/inference_results_v0.7/issues/15) a few issues along the way. We did not create CK packages for the new plans though.

When the v1.0 results are out on 21 April 2021, I'd encourage you to reproduce them in the same way and share your experience with the community!
