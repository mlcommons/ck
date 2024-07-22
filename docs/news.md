[ [Back to index](README.md) ]

### [News from the MLCommons Task Force on Automation and Reproducibility](taskforce.md)

#### 202406

* We published a white paper about the Collective Knowledge Playground, Collective Mind, MLPerf and CM4MLOps: https://arxiv.org/abs/2406.16791

#### 202403

* [cKnowledge](https://cKnowledge.org) has completed a collaborative engineering project with MLCommons 
  to enhance CM workflow automation to run MLPerf inference benchmarks
  across different models, software and hardware from different vendors in a unified way: [GUI](https://access.cknowledge.org/playground/?action=howtorun).
* [cTuning](https://cTuning.org) has validated the new [MLCommons CM workflow](https://github.com/mlcommons/ck) 
  to automate ~90% of all MLPerf inference v4.0 performance and power submissions
  while finding some top performance and cost-effective software/hardware configurations for AI systems: 
  [report](https://www.linkedin.com/pulse/new-cm-mlperf-automation-helps-benchmark-commodity-hardware-fursin-61noe).
* We presented a new project to ["Automatically Compose High-Performance and Cost-Efficient AI Systems with MLCommons' Collective Mind and MLPerf"](https://doi.org/10.5281/zenodo.10786893)
  at the [MLPerf-Bench workshop @HPCA'24](https://sites.google.com/g.harvard.edu/mlperf-bench-hpca24/home).


#### 202311

* [ACM/IEEE MICRO'23](https://ctuning.org/ae/micro2023.html) used CM 
  to [automate artifact evaluation](https://github.com/ctuning/cm4research/tree/main/script) 
  and make it easier for research to understand, prepare, run and reproduce research projects
  from published papers.

* The ACM YouTube channel has released the ACM REP'23 keynote about the MLCommons CM automation language and CK playground:
  [toward a common language to facilitate reproducible research and technology transfer](https://youtu.be/_1f9i_Bzjmg?si=7XoXRtcU0rglRJr0).

* [Grigori Fursin](https://cKnowledge.org/gfursin) and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)
  served as MLCommons liasons at the [Student Cluster Competition at SuperComputing'23](https://sc23.supercomputing.org/students/student-cluster-competition)
  helping the community run, optimize and enhance MLPerf inference benchmarks using the MLCommons CM workflow automation language
  and [CK playground](https://access.cKnowledge.org).

#### 202310

* [Grigori Fursin](https://cKnowledge.org/gfursin) gave an invited talk at [AVCC'23](https://avcc.org/avcc2023) about our MLCommons CM automation language and how it can help 
  to develop modular, portable and technology-agnostic benchmarks.

* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) and [Grigori Fursin](https://cKnowledge.org/gfursin) 
  gave an [IISWC'23 tutorial](https://iiswc.org/iiswc2023/#/program/) about our CM workflow automation language 
  and how it can make it easier for researchers to reproduce their projects and validate in the real world
  across rapidly evolving software and hardware.

#### 202309

* The Collective Knowledge Technology v3 with the open-source [MLCommons CM automation language](https://doi.org/10.5281/zenodo.8105338),
  [CK playground](https://access.cknowledge.org) 
  and [C++ Modular Inference Library](https://cknowledge.org/mil)
  helped the community automate > 90% of all [MLPerf inference v3.1 results](https://mlcommons.org/en/news/mlperf-inference-storage-q323/) 
  and cross 10000 submissions in one round for the first time (submitted via [cTuning foundation](https://cTuning.org))!
  Here is the [list of the new CM/CK capabilities](docs/news-mlperf-v3.1.md) available to everyone 
  to prepare and automate their future MLPerf submissions - please check this [HPC Wire article](https://www.hpcwire.com/2023/09/13/mlperf-releases-latest-inference-results-and-new-storage-benchmark)
  about cTuning's community submission and don't hesitate to reach us via [Discord server](https://discord.gg/JjWNWXKxwT) for more info!*

#### 202309

Our [CK playground](https://access.cKnowledge.org) was featured at the [AI hardware summit'23](https://aihwedgesummit.com/events/aihwedgesummit)

#### 202307

The overview of the MedPerf project was published in Nature: 
[Federated benchmarking of medical artificial intelligence with MedPerf](https://www.nature.com/articles/s42256-023-00652-2)!

#### 202306

We were honored to give a [keynote](https://doi.org/10.5281/zenodo.8105338) about our MLCommons automation and reproducibility language
to faciliate reproducible experiments and bridge the growing gap between research and production
at the [1st ACM conference for Reproducibility and Replicability](https://acm-rep.github.io/2023/keynotes).

#### 202305

Following the successful validation of our [CK/CM technology](https://github.com/mlcommons/ck) by the community
to automate MLPerf inference v3.0 submissions, the [MLCommons Task Force on automation and reproducibilty](taskforce.md) 
have prepared a [presentation](https://doi.org/10.5281/zenodo.7871070) 
about our development plans for the [MLCommons CK playground](https://access.cKnowledge.org) 
and [MLCommons CM scripting language](../cm) for Q3 2023.

Our current mission is to prepare [new optimization challenges](../cm-mlops/challenge) 
to help companies, students, researchers and practitioners reproduce and optimize MLPerf
inference v3.0 results and/or submit new/better results to MLPerf
inference v3.1 across diverse models, software and hardware 
as a community effort.

#### 202304

We have successfully validated the [MLCommons CK and CM technology](https://github.com/mlcommons/ck) 
to automate ~80% of MLPerf inference v3.0 submissions (98% of all power results).

MLCommons CK and CM has helped to automatically interconnect very diverse technology 
from Neural Magic, Qualcomm, Krai, cKnowledge, OctoML, Deelvin, DELL, HPE, Lenovo, Hugging Face, Nvidia and Apple 
and run it across diverse CPUs, GPUs and DSPs with PyTorch, 
ONNX, QAIC, TF/TFLite, TVM and TensorRT using popular cloud providers (GCP, AWS, Azure) and individual servers and edge devices 
via our recent [open optimization challenge](https://access.cknowledge.org/playground/?action=challenges&name=optimize-mlperf-inference-v3.0-2023).

* [Forbes article highlighting our MLCommons CK technology](https://www.forbes.com/sites/karlfreund/2023/04/05/nvidia-performance-trounces-all-competitors-who-have-the-guts-to-submit-to-mlperf-inference-30/?sh=3c38d2866676)
* [ZDNet article](https://www.zdnet.com/article/nvidia-dell-qualcomm-speed-up-ai-results-in-latest-benchmark-tests)
* [LinkedIn article from Grigori Fursin (MLCommons Task Force co-chair)](https://www.linkedin.com/pulse/announcing-my-new-project-reproducible-optimization-co-design-fursin)
* [Linkedin article from Arjun Suresh (MLCommons Task Force co-chair)](https://www.linkedin.com/posts/arjunsuresh_nvidia-performance-trounces-all-competitors-activity-7049500972275929088-nnnx?utm_source=share&utm_medium=member_desktop)


#### 202304

We pre-released a free, open-source and technology-agnostic [Collective Knowledge Playground (MLCommon CK)](https://x.cKnowledge.org)
to automate benchmarking, optimization and reproducibility of MLperf inference benchmark via collaborative challenges!

#### 202302

New GUI to visualize all MLPerf results is available [here](https://cknowledge.org/cm-gui-graph).

#### 202301

New GUI to run MLPerf inference is available [here](https://cknowledge.org/mlperf-inference-gui).

#### 202212

We have added GitHub actions to the MLPerf inference repo to automatically
test MLPerf inference benchmark with different models, data sets and
frameworks using our customizable MLCommons CM-MLPerf workflows:

* [Test LoadGen](https://github.com/mlcommons/inference/blob/master/.github/workflows/test-loadgen.yml)
* [Test RetinaNet](https://github.com/mlcommons/inference/blob/master/.github/workflows/test-retinanet.yml)
* [Test ResNet50](https://github.com/mlcommons/inference/blob/master/.github/workflows/test-resnet50.yml)

#### 202211

[Grigori Fursin](https://cKnowledge.org/gfursin) and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) 
successfully validated the prototype of  their new [workflow automation langugage (MLCommons CM)](https://github.com/mlcommons/ck/tree/master/cm) 
at the [Student Cluster Competition at SuperComputing'22](https://studentclustercompetition.us/2022/index.html).
It was used to make it easier to prepare and run the MLPerf inference benchmark just under 1 hour!
Please test it using this [CM tutorial](https://github.com/mlcommons/ck/blob/master/docs/tutorials/sc22-scc-mlperf.md).


#### 202210

We have prototyped [modular CM-MLPerf containers](../docker) 
using our portable MLCommons CM scripting language.

#### 202209

We have prepared a [presentation](https://doi.org/10.5281/zenodo.7143424) 
about the mission of the MLCommons Task Force on automation and reproducibility.

#### 202308

We have prototyped [universal MLPerf inference workflows](../cm-mlops/script/app-mlperf-inference)
using the MLCommons CM scripting language.

#### 202307

[Grigori Fursin](https://cKnowledge.org/gfursin) 
and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) have established an 
[MLCommons Task Force on automation and reproducibility](taskforce.md)
to continue developing MLCommons CK/CM as a community effort.

#### 202306     

We have pre-released [stable and portable automation CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) 
to unify MLOps and DevOps across diverse software, hardware, models and data.

#### 202305

We have prepared an example of [portable and modular image classification using the MLCommons CM scriping language](tutorials/modular-image-classification.md).

#### 202203

Following positive feedback from the community about our [Collective Knowledge concept](https://www.youtube.com/watch?v=7zpeIVwICa4) 
to facilitate reproducible research and technology transfer across rapidly evolving models, software, hardware and data,
we have started developing its simplified version as a common scripting language to connect academia and industry:
[Collective Mind framework (MLCommons CM aka CK2)](https://github.com/mlcommons/ck/tree/master/cm).
