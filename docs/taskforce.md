[ [Back to index](README.md) ]

# MLCommons Task force on Automation and Reproducibility

## Goals

* Provide free help for all [MLCommons]( https://mlcommons.org ) and the community 
  to prepare, run, optimize and compare MLPerf benchmarks (training, inference and tiny) and submit Pareto-optimal results
  with the help of the [MLCommons CM workflow automation language](README.md) and 
  [MLCommons CK playground (benchmarking, optimization and reproducibility challenges)](https://access.cKnowledge.org)
  to reduce benchmarking, optimization and reproducibility costs.
  ***We are very glad to see that more than 80% of all recent MLPerf inference benchmark submissions were automated using our open-source technology -
  don't hesitate to get in touch with the task force via our public [Discord server](https://discord.gg/JjWNWXKxwT).***
* Automatically run any MLPerf benchmark out-of-the-box with any software, hardware, model and data from any vendor: 
  *[prototype is available and validated during MLPerf inf v3.0 submission](../cm-mlops/challenge/optimize-mlperf-inference-v3.1-2023/README.md)*.
* Automate optimization experiments and visualization of results with derived metrics: *[prototype](https://cknowledge.org/mlcommons-inference-gui)*.
* Generate Pareto-optimal end-to-end applications based on reproducible MLPerf results: *under development*.
* Organize reproducibility, replicability and optimization challenges to improve MLPerf results across diverse software, hardware, models and data: 
  *[on-going](https://github.com/mlcommons/ck/tree/master/cm-mlops/challenge) 
  (see adopted terminology [here](artifact-evaluation/faq.md#what-is-the-difference-between-repeatability-reproducibility-and-replicability))*.
* Bridge the [growing gap between research and production](https://acm-rep.github.io/2023/author/grigori-fursin).


## Mission

This task force was established by [MLCommons]( https://mlcommons.org ) and the [cTuning foundation](https://cTuning.org) in 2022 to apply 
the [established automation and reproducibility methodology and open-source tools from ACM, IEEE and the cTuning foundation](https://learning.acm.org/techtalks/reproducibility)
to run MLPerf benchmarks out-of-the-box across any software, hardware, models and data from any vendor
with the help of the [MLCommons CM automation language](README.md) and the [MLCommons CK playground](https://access.cKnowledge.org).

We use this open-source technology to organize [reproducibility, replicability and optimization challenges](https://access.cknowledge.org/playground/?action=challenges)
to reproduce results from research papers and MLPerf submissions, 
improve/optimize them in terms of accuracy, performance, power consumption, size, costs and other metrics, 
and validate them in the real-world applications.

We successfully validated the latest version of open-technology during the [1st collaborative challenge to run MLPerf inference v3.0 benchmark](https://access.cknowledge.org/playground/?action=challenges&name=optimize-mlperf-inference-v3.0-2023)
across diverse models, software and hardware from Neural Magic, Qualcomm, Nvidia, Intel, AMD, Microsoft, Amazon, Google,
Krai, cKnowledge, cTuning foundation, OctoML, Deelvin, DELL, HPE, Lenovo, Hugging Face and Apple - 
CK and CM has helped to automate more than 80% of all recent MLPerf inference benchmark submissions 
(and 98% of all power results), make them more reproducible and reusable,
and obtain record inference performance on the latest Qualcomm and Nvidia devices.

Our ultimate mission is to help all MLCommons members and the community
slash their benchmarking, development, optimization and operational costs and accelerate innovation.
They should be able to use the CK playground and CM language to automatically generate 
the most efficient, reproducible and deployable application from the most suitable 
combination of software, hardware and models based on their requirements,
constraints and [MLPerf results](https://access.cknowledge.org/playground/?action=experiments).

## Discussions

* Join our [public Discord server](https://discord.gg/JjWNWXKxwT) to discuss developments and challenges.
* Check our upcoming [reproducibility, replicability and optimization challenges](https://access.cknowledge.org/playground/?action=challenges)
* Join our [public conf-calls](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw).
* Check our [news](news.md).

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

* Reproducibility and replicability studies:
  * [Terminology (ACM/NISO): Repeatability, Reproducibility and Replicability](artifact-evaluation/faq.md#what-is-the-difference-between-repeatability-reproducibility-and-replicability)
  * [Artifact Evaluation at ML and systems conferences](https://cTuning.org/ae)

### Acknowledgments

This task force is supported by [MLCommons](https://mlcommons.org), [cTuning foundation](https://cTuning.org),
[cKnowledge](https://cKnowledge.org) and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
