[ [Back to index](README.md) ]

# MLCommons Taskforce on Automation and Reproducibility

*Note that this is on-going and heavily evolving project - please join our public
 [Discord server](https://discord.gg/JjWNWXKxwT) 
 or contact [Grigori Fursin and Arjun Suresh](mailto:gfursin@cKnowledge.org;asuresh@cTuning.org)
 to prepare the 1st open MLPerf inference optimization tournament in spring/summer 2023,
 brainstorm ideas,  request new features, add support for your software and hardware,
 and participate in developments and collaborative 
 benchmarking and optimization of AI/ML Systems.*


## Mission

This public taskforce is developing a free, open-source and technology-agnostic on-prem platform 
[*(Collective Knowledge Playground aka MLCommons CK)*](https://github.com/mlcommons/ck/tree/master/platform)
powered by the portable [*MLCommons Collective Mind automation framework (MLCommons CM)*](https://github.com/mlcommons/ck/tree/master/cm).

Our goal is to help the community and MLCommons members 
benchmark, optimize and compare AI, ML and other emerging applications
across diverse and rapidly evolving models, software, hardware and data from different vendors
in terms of cost, performance, power consumption, accuracy, size 
and other metrics in a collaborative, automated and reproducible way.

We thank [the community](https://access.cknowledge.org/playground/?action=contributors) for helping us to validate the CK technology 
during the [1st collaborative challenge to run MLPerf inference v3.0 benchmark](https://access.cknowledge.org/playground/?action=challenges&name=optimize-mlperf-inference-v3.0-2023)
across diverse models, software and hardware from Neural Magic, Qualcomm, Nvidia, Intel, AMD, Microsoft, Amazon, Google,
Krai, cKnowledge, cTuning foundation, OctoML, Deelvin, DELL, HPE, Lenovo, Hugging Face and Apple - 
CK has helped automate more than 80% of all recent MLPerf inference benchmark submissions 
(and 98% of all power results), make them more reproducible and reusable,
and obtain record inference performance on the latest Qualcomm and Nvidia devices.

Our ultimate motivation for our CK technology is to help researchers, engineers and entrepreneurs 
accelerate innovation by automatically generating the most efficient, reproducible and deployable 
full-stack AI/ML applications using the most suitable software/hardware stack 
at any given time (model, framework, inference engine and any other related dependency) 
based on their requirements and constraints including costs, throughput, latency, power consumption, accuracy, target devices (cloud/edge/mobile/tiny), 
environment and data while slashing their development and operational costs by 10..100 times.

See this [ACM tech talk](https://www.youtube.com/watch?v=7zpeIVwICa4) 
and [journal article](https://arxiv.org/abs/2011.01149) to learn more about our motivation.

## Discussions

Join our [Discord server](https://discord.gg/JjWNWXKxwT) 
or contact [Grigori Fursin and Arjun Suresh](mailto:gfursin@cKnowledge.org;asuresh@cTuning.org)
to learn more about our platform, participate in public developments and discussions,
and request platform features and support for your technology.

## Chairs and Tech Leads

* [Grigori Fursin](https://cKnowledge.org/gfursin)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) 

## Development plan

### 2023

- [x] DONE: prototype the CM (CK2) automation to let the community submit MLPerf inference v3.0 results across any software and hardware stack 
      (our technology powered 4K+ results (!) across diverse cloud and edge platforms with different versions of PyTorch, ONNX, TFLite, TF, TVM targeting diverse CPUs and GPUs 
      that will be announced at the beginning of April)!
- [x] Prototype an [open-source on-prem CK platform](https://github.com/mlcommons/ck/tree/master/platform) 
      with a public API to automate SW/HW co-design for AI, ML and other emerging workloads based on user requirements and constraints.
- [x] [Collaborative CK challenge](https://access.cknowledge.org/playground/?action=challenges&name=optimize-mlperf-inference-v3.0-2023) 
      for the community to reproduce, optimize and submit results to MLPerf inference v3.0
      - 98% of all results were automated by the MLCommons CK technology!
- [ ] [New CK challenge](https://access.cknowledge.org/playground/?action=challenges&name=optimize-mlperf-inference-v3.1-2023) 
      to help MLCommons organizations and the community use our platform to prepare, optimize and compare their MLPerf inference v3.1 submissions on any SW/HW stack
- [ ] Enhance the MLCommons CK2/CM automation meta-framework to support our platform across any SW/HW stacks from MLCommons members and the community.
- [ ] Enhance the [MLPerf C++ inference template library (MITL)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp) 
      to run and optimize MLPerf inference across any AI/ML/SW/HW stack.
- [ ] Enhance the [light MLPerf inference application](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp) 
      to benchmark any ML model on any SW/HW stack without data sets and accuracy.
- [ ] Enhance our platform and automation framework to support [reproducibility initiatives and studies](https://cTuning.org/ae) at conferences and journals 
      across rapidly evolving software, hardware and data (collaboration with the [cTuning foundation](https://cTuning.org), ACM, IEEE and NeurIPS).


### 2022

- [x] DONE: [Prototype of the 2nd version of the MLCommons CK framework to solve the dependency hell and run any application on any hardware/software stack](https://github.com/mlcommons/ck).
- [x] DONE: [GUI prototype to run MLPerf inference benchmarks on any software and hardware](https://cknowledge.org/mlperf-inference-gui).
- [x] DONE: [GUI prototype to prepare MLPerf inference submission](https://cknowledge.org/mlperf-inference-submission-gui).
- [x] DONE: [GUI prototype to visualize AI/ML benchmarking results](https://cKnowledge.org/cm-gui-graph).

[*Archive of 2022 tasks*](archive/taskforce-2022.md).


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

### Acknowledgments

This project is supported by [MLCommons](https://mlcommons.org), [cTuning foundation](https://cTuning.org),
[cKnowledge](https://cKnowledge.org) and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
