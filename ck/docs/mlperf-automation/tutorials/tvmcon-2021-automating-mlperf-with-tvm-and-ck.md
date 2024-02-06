## TVMCon'21 tutorial
**["Automating and simplifying MLPerf inference benchmark submissions with TVM and CK"](https://www.tvmcon.org/schedule/)**

*Shortcut: https://bit.ly/tvmcon21-mlperf*

## Authors
* Grigori Fursin, OctoML
* Thomas Zhu, Oxford University
* Alexander Peskov, Deelvin
* Thierry Moreau, OctoML

## Brief description

[MLPerf](https://mlcommons.org) is a community effort to develop a common Machine Learning (ML)
benchmark that provides consistent, reproducible, and fair measurements
of accuracy, speed, and efficiency across diverse ML models, datasets,
hardware, and software. While MLPerf popularity
is steadily growing, the barrier of entry to MLPerf remains high due to
a complex benchmarking and submission pipeline and rapidly evolving
hardware and software stacks. In this tutorial, we will demonstrate how
[Apache TVM](https://tvm.apache.org) 
and the [Collective Knowledge framework (CK)](https://github.com/mlcommons/ck) 
can simplify and automate MLPerf inference benchmarking based on our own MLPerf v1.1
submission. The goal is to explain how our flexible open-source stack can
lower the barrier of entry for future hardware participants by providing
a powerful framework that is both hardware and ML framework agnostic and
can optimize almost any deep learning model on almost any deployment
hardware.

## Agenda

* Introduction
  * [MLPerf and MLCommons](https://mlcommons.org/en)
  * MLPerf inference benchmark: [intro](https://arxiv.org/pdf/1911.02549.pdf), [GitHub](https://github.com/mlcommons/inference)
  * Regular submissions: [v1.1 results](https://mlcommons.org/en/news/mlperf-inference-v11)
  * Current problems: the high barrier of entry due to a complex submission pipeline and rapidly evolving ML/SW/HW stacks
  * [OctoML](https://octoml.ai) have joined MLCommons to help the community solve these problems with TVM and CK
    * [Apache TVM](https://tvm.apache.org)
    * CK "plug&play" automation framework: [GitHub](https://github.com/ctuning/ck), 
      [Motivation](https://www.youtube.com/watch?v=7zpeIVwICa4), 
      [journal paper](https://doi.org/10.1098/rsta.2020.0211),
      [automation actions](https://github.com/mlcommons/ck/tree/master/ck/repo/module),
      [MLOps components](https://github.com/mlcommons/ck-mlops)
    * [ACM REQUEST-ASPLOS'18: the 1st Reproducible Tournament on Pareto-efficient Image Classification](https://cknow.io/c/event/repro-request-asplos2018)
      * [Live scoreboard](https://cknow.io/c/result/pareto-efficient-ai-co-design-tournament-request-acm-asplos-2018)
    * [CK-based MLPerf automation](https://github.com/mlcommons/ck/tree/master/docs/mlperf-automation)

    ![](https://raw.githubusercontent.com/ctuning/ck-guide-images/master/mlperf-ck-automation.png)

    ![](https://raw.githubusercontent.com/ctuning/ck-guide-images/master/mlperf-ck-dse.png)
    ![](https://raw.githubusercontent.com/ctuning/ck-guide-images/master/mlperf-ck-dse-pareto.png)

    * [cKnowledge.io dashboard with reproducible results](https://cknow.io/result/crowd-benchmarking-mlperf-inference-classification-mobilenets-all)

* OctoML's MLPerf inference submission v1.1:

  * [TVM backend for MLPerf inference (vision)](https://github.com/octoml/mlcommons-inference/blob/r1.1-seed/vision/classification_and_detection/python/backend_tvm.py)
  * TVM extension to support MLPerf inference *(should be in the mainline TVM in Q1 2022)*
  * [CK packages for MLPerf](https://github.com/octoml/mlops/tree/main/package)
  * [CK workflows for MLPerf](https://github.com/octoml/mlops/tree/main/program)
  
  * [All Data Center results](https://mlcommons.org/en/inference-datacenter-11)
  * [OctoML's demo submission (open division)](https://www.datocms-assets.com/45680/1632440591-mlcommons.png?auto=format&w=1675)
  * [GitHub](https://github.com/mlcommons/inference_results_v1.1/tree/main/open/OctoML)

* Tutorial to reproduce our MLPerf TVM results using the CK framework

  *The same CK steps and APIs are used across different hardware, ML frameworks, libraries, compilers, models and data sets!*

  * [MLPerf inference v1.1; Image Classification; Resnet50; TVM; AWS m5zn.6xlarge; X64; datacenter; open division](tvmcon-2021-automating-mlperf-with-tvm-and-ck-demo.md)

  * [Automating MLPerf submission](https://github.com/mlcommons/inference_results_v1.1/tree/main/open/OctoML/measurements/aws-m5zn.6xlarge-tvm/resnet50/offline#prepare-your-submission)
    * [Using reduced ImageNet for testing](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/datasets/imagenet2012.md#install-reduced-imagenet-2012-val-dataset-with-the-first-500-images)
  
  * [Adaptive containers with the CK API](https://github.com/mlcommons/ck-mlops/tree/main/docker)
    * [Example: MLPerf object detection ONNX and TVM](https://github.com/mlcommons/ck-mlops/blob/main/docker/ck-mlperf-inference-dev-object-detection-onnx-tvm/Dockerfile.ubuntu-20.04)

* Tutorial to extend MLPerf benchmarks 
  * Can support any framework, model, compiler, hardware

* Future work: 

  *This is an on-going community effort - please get in touch!*

  * Preparing MLCommons WG on CK-based design space exploration of ML/SW/HW stacks
  * Adding TVM support to all MLPerf inference and training benchmarks
  * Developing CK and CK2 within MLCommons to make it easier to benchmark, optimize and deploy ML Systems across continuously changing ML/SW/HW stacks
  * Adding more ML models, data sets, frameworks, libraries and compilers as plug&play CK packages
  * Collaborating with other MLSys and MLOps projects

* Contact:
  * [Grigori Fursin](mailto:grigori@octoml.ai) and [Thierry Moreau](mailto:tmoreau@octoml.ai)
