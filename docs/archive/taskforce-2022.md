[ [Back to index](README.md) ]

# MLCommons Taskforce on Education and Reproducibility

## Mission

* help you automate and validate your MLPerf inference benchmark submissions to the v3.0 round for any hardware target (deadline: March 3, 2023) - 
  join the related [Discord channel](https://discord.com/channels/1055858598779027636/1055858599664046172/1070286455634677811);
* enable faster innovation while adapting to the world of rapidly evolving software, hardware, 
  and data by encoding everyone’s knowledge in a form of 
  [portable, iteroperable and customizable automation recipes](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) 
  reusable across the community;
* modularize AI and ML Systems by decomposing them into [above automation recipes](list_of_scripts.md)
  using the [MLCommons CK2 automation meta-framework (aka CM)](https://github.com/mlcommons/ck);
* automate benchmarking, design space exploration and optimization of AI and ML Systems across diverse software and hardware stacks;
* help the community reproduce MLPerf benchmarks, prepare their own submissions and deploy Pareto-optimal ML/AI systems in the real world;
* support student competitions, reproducibility initiatives and artifact evaluation at ML and Systems conferences using the rigorous MLPerf methodology and the MLCommons automation meta-framework.

## Co-chairs and tech leads

* [Grigori Fursin](https://cKnowledge.org/gfursin) (CM project coordinator)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)

## Discord server

* [Invite link](https://discord.gg/JjWNWXKxwT)

## Meeting notes and news

* [Shared doc]( https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw/edit?usp=sharing )

## Conf-calls

Following our successful community submission to MLPerf inference v3.0, 
we will set up new weekly conf-calls shortly - <a href="https://discord.gg/JjWNWXKxwT">please stay tuned for more details</a>!

Please add your topics for discussion in the [meeting notes](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw/edit?usp=sharing)
or via [GitHub tickets](https://github.com/mlcommons/ck).

## Mailing list

Please join our mailing list [here](https://groups.google.com/g/collective-knowledge).


## GUI for MLPerf inference

* [Run MLPerf inference ](https://cknowledge.org/mlperf-inference-gui)
* [Prepare submission](https://cknowledge.org/mlperf-inference-submission-gui)
* [Visualize past and on-going results](https://cKnowledge.org/cm-gui-graph)

## On-going projects

See our [R&D roadmap for Q4 2022 and Q1 2023](https://github.com/mlcommons/ck/issues/536)

* Modularize MLPerf benchmarks and make it easier to run, optimize, customize and reproduce them across rapidly evolving software, hardware and data. 
  * Implement and enhance [cross-platform CM scripts](list_of_scripts.md) to make MLOps and DevOps more interoperable, reusable, portable, deterministic and reproducible. 
  * Lower the barrier of entry for new MLPerf submitters and reduce their associated costs. 
  * Develop universal, modular and portable benchmarking workflow that can run on any software/hardware stack from the cloud to embedded devices.
* Automate design space exploration and optimization of the whole ML/SW/HW stack to trade off performance, accuracy, energy, size and costs.
  * Automate submission of Pareto-efficient configurations to MLPerf.
* Help end-users of ML Systems visualize all MLPerf results, reproduce them and deploy Pareto-optimal ML/SW/HW stacks in production.


## Purpose

MLCommons is a non-profit consortium of 50+ companies that was originally created 
to develop a common, reproducible and fair benchmarking methodology for new AI and ML hardware.

MLCommons has developed an open-source reusable module called [loadgen](https://github.com/mlcommons/inference/tree/master/loadgen)
that efficiently and fairly measures the performance of inference systems.
It generates traffic for scenarios that were formulated by a diverse set of experts from MLCommons
to emulate the workloads seen in mobile devices, autonomous vehicles, robotics, and cloud-based setups.

MLCommons has also prepared several reference ML tasks, models and datasets 
for vision, recommendation, language processing and speech recognition
to let companies benchmark and compare their new hardware in terms of accuracy, latency, throughput and energy
in a reproducible way twice a year.

The first goal of this open automation and reproducibility taskforce is to 
develop a light-weight and open-source automation meta-framework
that can make MLOps and DevOps more interoperable, reusable, portable,
deterministic and reproducible. 

We then use this automation meta-framework to develop plug&play workflows
for the MLPerf benchmarks to make it easier for the newcomers to run them 
across diverse hardware, software and data and automatically plug in 
their own ML tasks, models, data sets, engines, libraries and tools.

Another goal is to use these portable MLPerf workflows to help students, researchers and
engineers participate in crowd-benchmarking and exploration of the design space tradeoffs 
(accuracy, latency, throughput, energy, size, etc.) of their ML Systems from the cloud to the
edge using the mature MLPerf methodology while automating the submission
of their Pareto-efficient configurations to the open division of the MLPerf
inference benchmark.

The final goal is to help end-users reproduce MLPerf results 
and deploy the most suitable ML/SW/HW stacks in production 
based on their requirements and constraints.


## Technology

This MLCommons taskforce is developing an open-source and technology-neutral 
[Collective Mind meta-framework (CM)](https://github.com/mlcommons/ck)
to modularize ML Systems and automate their benchmarking, optimization 
and design space exploration across continuously changing software, hardware and data.

CM is the second generation of the [MLCommons CK workflow automation framework](https://arxiv.org/pdf/2011.01149.pdf) 
that was originally developed to make it easier to [reproduce research papers and validate them in the real world](https://learning.acm.org/techtalks/reproducibility).

As a proof-of-concept, this technology was successfully used to automate 
[MLPerf benchmarking and submissions](https://github.com/mlcommons/ck/tree/master/docs/mlperf-automation)
from Qualcomm, HPE, Dell, Lenovo, dividiti, Krai, the cTuning foundation and OctoML.
For example, it was used and extended by [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) 
with several other engineers to automate the record-breaking MLPerf inference benchmark submission for Qualcomm AI 100 devices.

The goal of this group is to help users automate all the steps to prepare and run MLPerf benchmarks
across any ML models, data sets, frameworks, compilers and hardware
using the MLCommons CM framework.

Here is an example of current manual and error-prone MLPerf benchmark preparation steps:

![](https://raw.githubusercontent.com/ctuning/ck-guide-images/master/cm-mlperf-edu-repro-wg1.png)

Here is the concept of CM-based automated workflows:

![](https://raw.githubusercontent.com/ctuning/ck-guide-images/master/cm-mlperf-edu-repro-wg2.png)


We have finished prototyping the new CM framework in summer 2022 based on the feedback of CK users
and successfully used it to modularize MLPerf and automate the submission of benchmarking results to the MLPerf inference v2.1.
See this [tutorial](tutorials/list_of_scripts.md) for more details.

We continue developing CM as an open-source educational toolkit 
to help the community learn how to modularize, crowd-benchmark, optimize and deploy 
Pareto-efficient ML Systems based on the mature MLPerf methodology and [portable CM scripts](list_of_scripts.md) - 
please check the [deliverables section](#deliverables) to keep track of our community developments
and do not hesitate to [join this community effort](https://forms.gle/i5gCDtBC8gMtcvRw6)!


## Agenda

See our [R&D roadmap for Q4 2022 and Q1 2023](https://github.com/mlcommons/ck/issues/536)

### 2022

* Prototype the new CM toolkit to modularize AI&ML systems based on the original CK concepts: 
  * **DONE - [GitHub](https://github.com/mlcommons/ck/tree/master/cm)** .
* Decompose MLPerf inference benchmark into portable, reusable and plug&play CM components:
  * **DONE for image classification and object detection - [GitHub](https://github.com/mlcommons/ck/tree/master/cm-mlops)**.
* Demonstrate CM-based automation to submit results to MLPerf inference:
  * **DONE - [showcased CM automation concept for MLPerf inference v2.1 submission](https://github.com/mlcommons/ck/blob/master/docs/mlperf-cm-automation-demo.md)**.
* Prepare CM-based MLPerf modularization and automation tutorial:
  * **DONE - [link](mlperf-cm-automation-demo.md)**
* Add tests to cover critical functionality of portable CM scripts for MLPerf:
  * **DONE - [link](https://github.com/mlcommons/ck/issues/275)**
* Improve CM workflow/script automaton to modularize ML Systems:
  * **DONE - [link](tutorials/sc22-scc-mlperf.md)**
* Prototype CM-based modularization of the MLPerf inference benchmark with C++ back-end and loadgen 
  to automatically plug in different ML models, data sets, frameworks, SDKs, compilers and tools 
  and automatically run it across different hardware and run-times:
  * [Ongoing internship of Thomas Zhu from Oxford University](https://github.com/mlcommons/ck/issues/265)
* Prototype CM-based automation for TinyMLPerf:
  * [Ongoing](https://github.com/mlcommons/ck/issues/268)
* Add basic TVM back-end to the latest MLPerf inference repo:
  * [Ongoing](https://github.com/mlcommons/ck/issues/267)
* Convert [outdated CK components for MLPerf and MLOps](https://github.com/mlcommons/ck-mlops) into the new CM format
  * Ongoing
* Develop a methodology to create modular containers and [MLCommons MLCubes](https://github.com/mlcommons/mlcube) that contain CM components to run the MLPerf inference benchmarks out of the box:
  * [Ongoing](https://github.com/mlcommons/ck/tree/master/docker)
* Prototype CM integration with power infrastructure (power WG) and logging infrastructure (infra WG):
  * TBD
* Process feedback from the community about CM-based modularization and crowd-benchmarking of MLPerf:
  * TBD

### 2023 

* Upload all stable CM components for MLPerf to Zenodo or any other permanent archive to ensure the stability of all CM workflows for MLPerf and modular ML Systems.
* Develop CM automation for community crowd-benchmarking of the MLPerf benchmarks across different models, data sets, frameworks, compilers, run-times and platforms.
* Develop a customizable dashboard to visualize and analyze all MLPerf crowd-benchmarking results based on these examples from the legacy CK prototype: 
  [1](https://cknow.io/c/result/mlperf-inference-all-image-classification-edge-singlestream), 
  [2](https://cknow.io/result/crowd-benchmarking-mlperf-inference-classification-mobilenets-all).
* Share MLPerf benchmarking results in a database compatible with FAIR principles (mandated by the funding agencies in the USA and Europe) -- 
  ideally, eventually, the MLCommons general datastore.
* Connect CM-based MLPerf inference submission system with our [reproducibility initiatives at ML and Systems conferences](https://cTuning.org/ae). 
  Organize open ML/SW/HW optimization and co-design tournaments using CM and the MLPerf methodology 
  based on our [ACM ASPLOS-REQUEST'18 proof-of-concept](https://cknow.io/c/event/repro-request-asplos2018/).
* Enable automatic submission of the Pareto-efficient crowd-benchmarking results (performance/accuracy/energy/size trade-off - 
  see [this example from the legacy CK prototype](https://cknow.io/c/result/mlperf-inference-all-image-classification-edge-singlestream-pareto))
  to MLPerf on behalf of MLCommons.
* Share deployable MLPerf inference containers with Pareto-efficient ML/SW/HW stacks.


## Resources

* Motivation:
  * [MLPerf Inference Benchmark (ArXiv paper)](https://arxiv.org/abs/1911.02549)
  * [ACM TechTalk with CK/CM intro moderated by Peter Mattson (MLCommons president)](https://www.youtube.com/watch?v=7zpeIVwICa4)
  * [Journal article with CK/CM concepts and our long-term vision](https://arxiv.org/pdf/2011.01149.pdf)
  * [HPCA'22 presentation "MLPerf design space exploration and production deployment"](https://doi.org/10.5281/zenodo.6475385)

* Tools:
  * [MLCommons CM toolkit to modularize ML&AI Systems (Apache 2.0 license)](https://github.com/mlcommons/ck)
  * [Portable, reusable and customizable CM components to modularize ML and AI Systems (Apache 2.0 license)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
  * [Legacy CK automation for MLPerf](https://github.com/mlcommons/ck/tree/master/docs/mlperf-automation)

* [Google Drive](https://drive.google.com/drive/folders/1CKewftoZ2VpBWheMCSxFG-pcIBgCu4Au?usp=sharing) (public access)





## Acknowledgments

This project is supported by [MLCommons](https://mlcommons.org), [OctoML](https://octoml.ai) 
and many great [contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).

