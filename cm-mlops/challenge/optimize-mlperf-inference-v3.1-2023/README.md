### Introduction

Our goal is to help the community benchmark and optimize various AI/ML applications 
across diverse software and hardware provided by volunteers similar to SETI@home!

Open-source [MLPerf inference benchmarks](https://arxiv.org/abs/1911.02549) 
were developed by a [consortium of 50+ companies and universities (MLCommons)](https://mlcommons.org)
to enable trustable and reproducible comparison of AI/ML systems 
in terms of latency, throughput, power consumption, accuracy and other metrics
across diverse software/hardware stacks from different vendors.

However, running MLPerf inference benchmarks and submitting results [turned out to be a challenge](https://doi.org/10.5281/zenodo.8144274) 
even for experts and could easily take many weeks to prepare. That's why [MLCommons](https://mlcommons.org), 
[cTuning.org](https://www.linkedin.com/company/ctuning-foundation)
and [cKnowledge.org](https://www.linkedin.com/company/cknowledge) 
decided to develop an open-source, technology-agnostic 
and non-intrusive [Collective Mind automation language (CM)](https://github.com/mlcommons/ck)
and [Collective Knowledge Playground (CK)](https://access.cknowledge.org/playground/?action=experiments) 
to help anyone run, reproduce, optimize and compare MLPerf inference benchmarks out-of-the-box 
across diverse software, hardware, models and data sets.

You can read more about our vision, open-source technology and future plans 
in this [presentation](https://doi.org/10.5281/zenodo.8105339).



### Advanced challenge

We would like to ask volunteers run various MLPerf inference benchmarks 
on diverse CPUs (Intel, AMD, Arm) and Nvidia GPUs similar to SETI@home 
across different framework (ONNX, PyTorch, TF, TFLite) 
either natively or in a cloud (AWS, Azure, GCP, Alibaba, Oracle, OVHcloud, ...) 
and submit results to MLPerf inference v3.1.

However, since some benchmarks may take 1..2 days to run, we suggest to start in the following order (these links describe CM commands to run benchmarks and submit results):
* [CPU: Reference implementation of Image Classification with ResNet50 (open and then closed division)](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/resnet50/README_reference.md)
* [CPU: TFLite C++ implementation of Image classification with variations of MobileNets and EfficientNets (open division)](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/run-mlperf-inference-mobilenet-models/README-about.md)
* [Nvidia GPU: Nvidia optimized implementation of Image Classification with ResNet50 (open and then closed division)](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/resnet50/README_nvidia.md)
* [Nvidia GPU: Nvidia optimized implementation of Language processing with BERT large (open and then closed division)](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/bert/README_nvidia.md)
* [Nvidia GPU: Reference implementation of Image Classification with ResNet50 (open and then closed division)](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/bert/README_nvidia.md)
* [Nvidia GPU: Reference implementation of Language processing with BERT large (open and then closed division)](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/resnet50/README_reference.md)
* [Nvidia GPU (24GB of memory min): Reference implementation of Language processing with GPT-J 6B (open)](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/gpt-j/README_reference.md)
* [Nvidia GPU: Nvidia optimized implementation of all other models (open and closed division)](https://github.com/ctuning/mlcommons-ck/blob/master/docs/mlperf/inference/README.md#run-benchmarks-and-submit-results)

Please read [this documentation](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/README.md)
to set up and run above benchmarks using CM.

You can register your participation for the [Collective Knowledge leaderboard]( https://access.cKnowledge.org/playground/?action=contributors )
using this [guide](https://github.com/mlcommons/ck/blob/master/platform/register.md).

Please report encountered problems using [GitHub issues](https://github.com/mlcommons/ck/issues)
and the public [Discord server](https://discord.gg/JjWNWXKxwT) to help the community
improve the portability of the CM automation for MLPerf and other benchmarks and projects.

You can also talk to organizers at any time using above [Discord server](https://discord.gg/JjWNWXKxwT) or 
during our [weekly conf-calls](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw/edit).

Looking forward to your submissions and happy hacking!



### Prizes

* *All submitters will participate in writing a common white paper about running and comparing MLPerf inference benchmarks out-of-the-box.*
* *All submitters will receive 1 point for submitting valid results for 1 complete benchmark on one system.*
* *All submitters will receive an official MLCommons Collective Knowledge contributor award (see [this example](https://ctuning.org/awards/ck-award-202307-zhu.pdf)).*
* *The top contributors will receive cash prizes from [MLCommons organizations](https://mlcommons.org) and [cKnowledge.org](https://www.linkedin.com/company/cknowledge)*.


### Organizers

* [MLCommons](https://cKnowledge.org/mlcommons-taskforce)
* [cTuning.org](https://www.linkedin.com/company/ctuning-foundation)
* [cKnowledge.org](https://www.linkedin.com/company/cknowledge)


### Status

You can see shared results in [this repostiory](https://github.com/ctuning/mlperf_inference_submissions_v3.1) 
with PRs from participants [here](https://github.com/ctuning/mlperf_inference_submissions_v3.1/pulls).

### Results

All accepted results will be publicly available in the CM format with derived metrics 
in this [MLCommons repository](https://github.com/mlcommons/cm4mlperf-results),
in [MLCommons Collective Knowledge explorer](https://access.cknowledge.org/playground/?action=experiments) 
and at official [MLCommons website](https://mlcommons.org).
