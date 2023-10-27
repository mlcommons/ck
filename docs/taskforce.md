[ [Back to index](README.md) ]

# MLCommons Task force on Automation and Reproducibility

## Mission

The Task Force on Automation and Reproducibility was established by [MLCommons]( https://mlcommons.org ) and the [cTuning foundation](https://cTuning.org) in 2022
to develop an open-source automation technology that can help everyone [co-design, benchmark and optimize AI & ML Systems](mlperf/README.md) 
across diverse models, data sets, software and hardware from any vendor using the [MLPerf methodology](https://arxiv.org/abs/1911.02549).

As an outcome of this community effort, we have developed the [MLCommons CM automation language](https://doi.org/10.5281/zenodo.8105339), 
[MLCommons C++ Modular Inference Library (MIL)](../cm-mlops/script/app-mlperf-inference-cpp/README-extra.md) 
and the [MLCommons CK playground](https://access.cKnowledge.org).
This open-source technology was successfully validated during the [1st mass-scale community MLPerf inference submission](https://www.linkedin.com/feed/update/urn:li:activity:7112057645603119104/) 
of 12000+ benchmarking results (representing > 90% of all v3.1 submissions)
across diverse models, data sets, software and hardware from different vendors.

We also use CM/CK/MIL to support reproducibility initiatives at [ML and Systems conferences](https://cTuning.org/ae)
and organize [reproducibility, replicability and optimization challenges](https://access.cknowledge.org/playground/?action=challenges)
to reproduce results from research papers and MLPerf submissions, 
improve/optimize them in terms of accuracy, performance, power consumption, size, costs and other metrics, 
and [validate them in the real-world applications](https://www.youtube.com/watch?v=7zpeIVwICa4).

We continue collaborating with the community to extend the CM automation language, CK playground and MIL
to automatically generate the most efficient, reproducible and deployable applications from the most suitable 
combination of software, hardware and models based on their requirements,
constraints and [MLPerf results](https://access.cknowledge.org/playground/?action=experiments).
Our ultimate mission is to help all AI developers and users focus on innovation while
slashing their benchmarking, development, optimization and operational costs.

## Discussions

* Join our [public Discord server](https://discord.gg/JjWNWXKxwT).
* Check our upcoming [reproducibility, replicability and optimization challenges](https://access.cknowledge.org/playground/?action=challenges).
* See the notes from our [weekly public conf-calls](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw).
* Check our [news](news.md).

## Chairs and Tech Leads

* [Grigori Fursin](https://cKnowledge.org/gfursin)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) 

## Development plan

### 2023

- [x] DONE: Stable CM automation language (aka CK2) to let the community submit MLPerf inference v3.0 results across any software and hardware stack 
      (our technology powered 4K+ results (!) across diverse cloud and edge platforms with different versions of PyTorch, ONNX, TFLite, TF, TVM targeting diverse CPUs and GPUs 
      that will be announced at the beginning of April)!
- [x] DONE: Prototype an [open-source on-prem CK platform](https://github.com/mlcommons/ck/tree/master/docs#collective-knowledge-playground-ck) 
      with a public API to automate SW/HW co-design for AI, ML and other emerging workloads based on user requirements and constraints.
- [x] DONE: [Collaborative CK challenge](https://access.cknowledge.org/playground/?action=challenges&name=optimize-mlperf-inference-v3.0-2023) 
      for the community to reproduce, optimize and submit results to MLPerf inference v3.0
      - 98% of all results were automated by the MLCommons CK technology!
- [x] [New CK challenge](https://access.cknowledge.org/playground/?action=challenges&name=optimize-mlperf-inference-v3.1-2023) 
      to help MLCommons organizations and the community use our platform to prepare, optimize and compare their MLPerf inference v3.1 submissions on any SW/HW stack
- [ ] In progress: Enhance the MLCommons CK2/CM automation meta-framework to support our platform across any SW/HW stacks from MLCommons members and the community.
- [ ] In progress: Enhance the [MLPerf C++ inference template library (MIL)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp) 
      to run and optimize MLPerf inference across any AI/ML/SW/HW stack.
- [ ] In progress: Enhance our platform and automation framework to support [reproducibility initiatives and studies](https://cTuning.org/ae) at conferences and journals 
      across rapidly evolving software, hardware and data (collaboration with the [cTuning foundation](https://cTuning.org), ACM, IEEE and NeurIPS).
- [ ] In progress: Connect CM and MLCube


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
