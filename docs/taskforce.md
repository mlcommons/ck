[ [Back to index](README.md) ]

# MLCommons Taskforce on Education and Reproducibility

## Mission

This public taskforce is developing a [free and open-source platform](https://github.com/mlcommons/ck/tree/master/platform) 
to automatically find the most efficient and reproducible way to run AI, ML and any other application 
with any data on any software/hardware stack from the cloud to the edge at any given time.

This platform will help users automatically generate the most suitable and deployable solution
(ML framework, math library, inference engine and any other related dependency) 
to run emerging applications based on their requirements and constraints 
including costs, throughput, latency, power consumption, accuracy, target devices (cloud/edge/mobile/tiny),
environment and data sets.

It is powered by the [rigorous MLPerf benchmark methodology](https://arxiv.org/abs/1911.02549) 
and the technology-agnostic [MLCommons CK/CM workflow automation framework](https://github.com/mlcommons/ck).
Our taskforce has developed this framework to solve the "dependency hell" 
and interconnect diverse and rapidly evolving software and hardware
from any company including Nvidia, Intel, Qualcomm, AMD, Microsoft, Amazon, Google, 
Neural Magic, Meta, OctoML, Krai, cKnowledge and Hugging Face in a transparent and non-intrusive way
using  [portable CM scripts  developed by the community](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md).

As a proof-of-concept, our technology helped the community and multiple companies 
including Qualcomm, Neural Magic, Krai, DELL, HPE and Lenovo
automate 98% of all MLPerf inference submissions, make them more reproducible and reusable,
and obtain record inference performance on the latest Qualcomm and Nvidia devices.

The ultimate goal of our taskforce is to help everyone accelerate innovation by automating 
all tedious and repetitive tasks and slashing research, development, benchmarking, 
optimization and deployment time and costs for novel technology by 10..100 times 
in the rapidly evolving world.

## Discussions

Join our [Discord server](https://discord.gg/JjWNWXKxwT) 
to learn more about our platform, participate in public developments and discussions,
and request platform features and support for your technology.

Don't hesitate to get in touch with [Grigori Fursin](https://fursin.net)
and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) 
(taskforce founders) if you have any questions and suggestions.

## Development plan


### 2022

- [x] DONE: [Prototype of the 2nd version of the MLCommons CK framework to solve the dependency hell and run any application on any hardware/software stack](https://github.com/mlcommons/ck).
- [x] DONE: [GUI prototype to run MLPerf inference benchmarks on any software and hardware](https://cknowledge.org/mlperf-inference-gui).
- [x] DONE: [GUI prototype to prepare MLPerf inference submission](https://cknowledge.org/mlperf-inference-submission-gui).
- [x] DONE: [GUI prototype to visualize AI/ML benchmarking results](https://cKnowledge.org/cm-gui-graph).

[*Archive of 2022 tasks*](archive/taskforce-2022.md).

### 2023

- [x] DONE: prototype the CM (CK2) automation to let the community submit MLPerf inference v3.0 results across any software and hardware stack 
      (our technology powered 4K+ results (!) across diverse cloud and edge platforms with different versions of PyTorch, ONNX, TFLite, TF, TVM targeting diverse CPUs and GPUs 
      that will be announced at the beginning of April)!
- [ ] Prototype an [open-source on-prem CK platform](https://github.com/mlcommons/ck/tree/master/platform) 
      with a public API to automate SW/HW co-design for AI, ML and other emerging workloads based on user requirements and constraints.
- [ ] Help MLCommons organizations and the community use our platform to prepare, optimize and compare their MLPerf inference v3.1 submissions on any SW/HW stack
- [ ] Enhance the MLCommons CK2/CM automation meta-framework to support our platform across diverse SW/HW stacks.
- [ ] Enhance the [MLCommons C++ inference template library](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp) 
      to run and optimize MLPerf inference across any AI/ML/SW/HW stack.
- [ ] Enhance the [light MLPerf inference application](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp) 
      to benchmark any ML model on any SW/HW stack without data sets and accuracy.
- [ ] Enhance our platform and automation framework to support [reproducibility initiatives and studies](https://cTuning.org/ae) at conferences and journals 
      across rapidly evolving software, hardware and data (collaboration with the [cTuning foundation](https://cTuning.org), ACM, IEEE and NeurIPS).



## Resources

* Motivation:
  * [MLPerf Inference Benchmark (ArXiv paper)](https://arxiv.org/abs/1911.02549)
  * [ACM TechTalk introducing technology-agnostic CK/CM workflow automation framework](https://www.youtube.com/watch?v=7zpeIVwICa4)
  * [Journal article with CK/CM concepts and our long-term vision](https://arxiv.org/pdf/2011.01149.pdf)
  * [HPCA'22 presentation "MLPerf design space exploration and production deployment"](https://doi.org/10.5281/zenodo.6475385)

* Tools:
  * [MLPerf loadgen](https://github.com/mlcommons/inference/tree/master/loadgen)
  * [MLCommons CM workflow automation meta-framework to modularize ML&AI Systems (Apache 2.0 license)](https://github.com/mlcommons/ck)
  * [MLPerf universal C++ inference template library](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp)
  * [Portable, reusable and customizable CM scripts for technology-agnostic AI/ML/SW/HW co-design  (Apache 2.0 license)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)



## Acknowledgments

This project is supported by [MLCommons](https://mlcommons.org), [cTuning foundation](https://cTuning.org),
[cKnowledge](https://cKnowledge.org) and our fantastic [contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
