### Introduction

Open-source [MLPerf inference benchmarks](https://arxiv.org/abs/1911.02549) 
were developed by a [consortium of 50+ companies and universities (MLCommons)](https://mlcommons.org)
to enable trustable and reproducible comparison of AI/ML systems 
in terms of latency, throughput, power consumption, accuracy and other metrics
across diverse software/hardware stacks from different vendors.

However, it is difficult to customize and run MLPerf benchmarks with non-reference models.

That's why the MLCommons Task Force on automation and reproducibility has developed
a [Collective Mind automation language](https://doi.org/10.5281/zenodo.8144274)
to modularize this benchmark and make it easier to run with different models and data sets.


### Challenge

Implement a CM workflow to connect any Hugging Face model
to MLPerf loadgen and run it with random inputs to obtain a preliminary latency and througput
without accuracy.

Resources:
* [CM script to get ML model from Hugging Face zoo](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-ml-model-huggingface-zoo)
* [CM script to convert Hugging Face model to ONNX](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/convert-ml-model-huggingface-to-onnx)
* [CM script to build MLPerf loadgen](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-mlperf-inference-loadgen)
* [CM script to run Python Loadgen with any ONNX model](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-loadgen-generic-python/README-extra.md)
* [MLPerf BERT FP32 model is available at Hugging Face](https://huggingface.co/ctuning/mlperf-inference-bert-onnx-fp32-squad-v1.1)

Some results showcases CK workflow to benchmark Hugging Face models with MLPerf from v3.0 (BERT):
* https://access.cknowledge.org/playground/?action=experiments&name=2f1f70d8b2594149
* https://access.cknowledge.org/playground/?action=experiments&name=mlperf-inference--v3.0--edge--open-power--language-processing--offline&result_uid=9d2594448bbb4b45

Join our public [Discord server](https://discord.gg/JjWNWXKxwT) and/or
our [weekly conf-calls](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw/edit)
to discuss this challenge with the organizers.

Read [this documentation](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/README.md) 
to run reference implementations of MLPerf inference benchmarks 
using the CM automation language and use them as a base for your developments.

Check [this ACM REP'23 keynote](https://doi.org/10.5281/zenodo.8105339) to learn more about our open-source project and long-term vision.

### Prizes

* *All contributors will participate in writing a common white paper about running and comparing MLPerf inference benchmarks out-of-the-box.*
* *All contributors will receive 1 point for submitting valid results for 1 complete benchmark on one system.*
* *All contributors will receive an official MLCommons Collective Knowledge contributor award (see [this example](https://ctuning.org/awards/ck-award-202307-zhu.pdf)).*
* *The top contributors will receive cash prizes from [MLCommons organizations](https://mlcommons.org) and [cKnowledge.org](https://www.linkedin.com/company/cknowledge)*.


### Organizers

* [MLCommons](https://cKnowledge.org/mlcommons-taskforce)
* [cTuning.org](https://www.linkedin.com/company/ctuning-foundation)
* [cKnowledge.org](https://www.linkedin.com/company/cknowledge)


