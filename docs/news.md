[ [Back to index](README.md) ]

## MLCommons CK and CM news

### 202306

We were honored to give a [keynote](https://doi.org/10.5281/zenodo.8105338) about our MLCommons automation and reproducibility language
to faciliate reproducible experiments and bridge the growing gap between research and production
at the [1st ACM conference for Reproducibility and Replicability](https://acm-rep.github.io/2023/keynotes).

### 202305

Following the successful validation of our [CK/CM technology](https://github.com/mlcommons/ck) by the community
to automate MLPerf inference v3.0 submissions, the [MLCommons Task Force on automation and reproducibilty](taskforce.md) 
have prepared a [presentation](https://doi.org/10.5281/zenodo.7871070) 
about our development plans for the [MLCommons CK playground](../platform) 
and [MLCommons CM scripting language](../cm) for Q3 2023.

Our current mission is to prepare [new optimization challenges](../cm-mlops/challenge) 
to help companies, students, researchers and practitioners reproduce and optimize MLPerf
inference v3.0 results and/or submit new/better results to MLPerf
inference v3.1 across diverse models, software and hardware 
as a community effort.

### 202304

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


### 202304

We pre-released a free, open-source and technology-agnostic [Collective Knowledge Playground (MLCommon CK)](https://x.cKnowledge.org)
to automate benchmarking, optimization and reproducibility of MLperf inference benchmark via collaborative challenges!

### 202302

New GUI to visualize all MLPerf results is available [here](https://cknowledge.org/cm-gui-graph).

### 202301

New GUI to run MLPerf inference is available [here](https://cknowledge.org/mlperf-inference-gui).

### 202212

We have added GitHub actions to the MLPerf inference repo to automatically
test MLPerf inference benchmark with different models, data sets and
frameworks using our customizable MLCommons CM-MLPerf workflows:

* [Test LoadGen](https://github.com/mlcommons/inference/blob/master/.github/workflows/test-loadgen.yml)
* [Test RetinaNet](https://github.com/mlcommons/inference/blob/master/.github/workflows/test-retinanet.yml)
* [Test ResNet50](https://github.com/mlcommons/inference/blob/master/.github/workflows/test-resnet50.yml)

### 202211

Our new [scriping language (MLCommons CM)](https://github.com/mlcommons/ck/tree/master/cm) 
was successfully validated at the [Student Cluster Competition at SuperComputing'22](https://studentclustercompetition.us/2022/index.html).
It was used to make it easier to prepare and run the MLPerf inference benchmark just under 1 hour!
Please test it using [this CM tutorial](https://github.com/mlcommons/ck/blob/master/docs/tutorials/sc22-scc-mlperf.md).


### 202210

We have prototyped [modular CM-MLPerf containers](../docker) 
using our portable MLCommons CM scripting language.

### 202209

We have prepared a [presentation](https://doi.org/10.5281/zenodo.7143424) 
about the mission of the MLCommons Task Force on automation and reproducibility.

### 202308

We have prototyped [universal MLPerf inference workflows](../cm-mlops/script/app-mlperf-inference)
using the MLCommons CM scripting language.

### 202307

[Grigori Fursin](https://cKnowledge.org/gfursin) 
and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) have established an 
[MLCommons Task Force on automation and reproducibility](taskforce.md)
to continue developing MLCommons CK/CM as a community effort.

### 202306     

We have pre-released [stable and portable automation CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) 
to unify MLOps and DevOps across diverse software, hardware, models and data.

### 202305

We have prepared an example of [portable and modular image classification using the MLCommons CM scriping language](tutorials/modular-image-classification.md).

### 202203

Following positive feedback from the community about our [Collective Knowledge concept](https://www.youtube.com/watch?v=7zpeIVwICa4) 
to facilitate reproducible research and technology transfer across rapidly evolving models, software, hardware and data,
we have started developing its simplified version as a common scripting language to connect academia and industry:
[Collective Mind framework (MLCommons CM aka CK2)](https://github.com/mlcommons/ck/tree/master/cm).
