# Getting Started Guide

## Reproducing and improving MLPerf inference results

The [Collective Knowledge platform](https://access.cKnowledge.org) 
is currently having experiment results from MLPerf Inference v2.0, v2.1 and v3.0 
in the [extensible CM format](https://github.com/mlcommons/cm_inference_results)
and with the possibility to add derived metrics such as power efficiency.

We are currently preparing the [optimization challenge for MLPerf Inference v3.1](https://github.com/ctuning/mlcommons-ck/blob/master/cm-mlops/challenge/optimize-mlperf-inference-v3.1-2023/README.md).

For MLPerf inference 3.1 we have the following benchmark tasks
1. [Image Classification](https://github.com/mlcommons/ck/blob/master/cm-mlops/challenge/optimize-mlperf-inference-v3.1-2023/docs/generate-resnet50-submission.md) using ResNet50 model and Imagenet-2012 dataset
2. [Object Detection](https://github.com/mlcommons/ck/blob/master/cm-mlops/challenge/optimize-mlperf-inference-v3.1-2023/docs/generate-retinanet-submission.md) using Retinanet model and OpenImages dataset
3. [Language processing](https://github.com/mlcommons/ck/blob/master/cm-mlops/challenge/optimize-mlperf-inference-v3.1-2023/docs/generate-bert-submission.md) using Bert-Large model and Squadv1.1 dataset
4. [Speech Recognition](https://github.com/mlcommons/ck/blob/master/cm-mlops/challenge/optimize-mlperf-inference-v3.1-2023/docs/generate-rnnt-submission.md) using RNNT model and LibriSpeech dataset
5. [Medical Imaging](https://github.com/mlcommons/ck/blob/master/cm-mlops/challenge/optimize-mlperf-inference-v3.1-2023/docs/generate-3d-unet-submission.md)  using 3d-unet model and KiTS19 dataset
6. Recommendation using DLRM model and Criteo dataset
7. Large Language Model (Pending)

The tasks are divided into 
1. Edge (SingleStream, MultiStream and Offline scenarios) and 
2. Datacenter (Offline and Server scenarios) categories. 

Results can be submitted under 
1. closed (requires compliance runs, strict accuracy requirement, no retraining and subject to audit) and 
2. open divisions (only dataset is fixed). 
 
Results can be just performance or performance with power. 

## Participating in other optimization challenges

Check our on-going optimization challenges [here](https://access.cknowledge.org/playground/?action=challenges) 
and join our [public Discord server](https://access.cknowledge.org/playground/?action=challenges) to discuss them.

## Further reading

* [Project documentation](../docs/README.md)
