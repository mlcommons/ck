# Practical use cases and tutorials

We gradually update and improve this section with the help of our users.
Feel free to extend it via [GitHub pull-requests](https://github.com/ctuning/cbench).



## Share and reuse CK components similar to PyPI

[Collective Knowledge framework (CK)](https://github.com/ctuning/ck) was introduced in 2015 
to provide a common format for research artifacts and enable portable workflows.

The idea behind CK is to convert ad-hoc research projects into a file-based database 
of reusable components (code, data, models, pre-/post-processing scripts, experimental results, R&D
automation actions and best research practices to reproduce results, 
and live papers) with unified Python APIs, CLI-based actions, JSON meta
information and JSON input/output.

CK also features plugins to automatically detect required software, models and datasets 
on a user machine and install (cross-compile) the missing ones while supporting
different operating systems (Linux, Windows, MacOS, Android)
and hardware (Nvidia, Arm, Intel, AMD ...).

Unified CK API helps researchers to connect their artifacts into
automated workflows instead of some ad-hoc scripts while making them
[portable](https://cKnowledge.io/c/program) 
using the automatic [software detection plugins](https://cKnowledge.io/c/soft) and
[meta-packages](https://cKnowledge.io/c/soft).

While using CK to help researchers share their artifacts during [reproducibility initiatives at ML and systems conferences](https://cTuning.org/ae)
(see [15+ artifacts](https://cKnowledge.io/?q=%22reproduced-papers%22%20AND%20%22portable-workflow-ck%22) shared by researchers in the CK format) 
and companies to [automate ML benchmarking and move ML models to production](https://youtu.be/1ldgVZ64hEI) we noticed two major limitations: 
  
* The distributed nature of the CK technology, the lack of a centralized
  place to keep all CK components and the lack of convenient GUIs makes
  it very challenging to keep track of all contributions from the community,
  add new components, assemble workflows, automatically test them across
  diverse platforms, and connect them with legacy systems.

* The concept of backward compatibility of CK APIs and the lack
  of versioning similar to Java made it very challenging to keep stable and
  bug-free workflows in real life - a bug in a CK component from one GitHub
  project can easily break dependent ML workflows in another GitHub project.

These issues motivated us to develop cKnowledge.io portal
as an open web platform 
to aggregate, version and test all CK components and portable CK workflows 
necessary to benchmarking deep tech systems in a reproducible and collaborative way,
and to enable portable MLOps with the automated deployment of ML models 
in production across diverse systems from IoT to data centers in the most efficient way (MLSysOps).

You need to install [cBench](../getting-started/installation) 
and then follow [this guide](commands.html#cbench-ck-components)
to learn how to download or upload your CK components. 



## Create customizable dashboards for live papers and collaborative experiments

We created CK also to support [auto-generated and live papers](https://cKnowledge.io/?q=%22live-paper%22),
[collaborative experiments](https://cKnowledge.io/?q=%22reproduced-results%22),
[reproducible optimization tournaments](https://cKnowledge.org/request)
and [crowd-benchmarking](https://cKnowledge.io/result/sota-mlperf-object-detection-v0.5-crowd-benchmarking)

The users can now create customizable dashboards on cKnowledge platform
and push their results. Please follow [this guide](commands.html##cbench-dashboards) to learn
how to create such dashboards.

You can also check our [MLPerf demo](https://cKnowledge.io/c/solution/demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows/) 
with [crowd results](https://cKnowledge.io/result/sota-mlperf-object-detection-v0.5-crowd-benchmarking).




## Use cross-platform software detection plugins

*To be updated. Note that we plan to provide a GUI to add new CK components.*

See the list of [shared software detection plugins](https://cKnowledge.io/c/soft) with usage examples.

See examples of MLPerf inference benchmark automation using cKnowledge.io and cBench
for [Linux](https://cKnowledge.io/c/solution/demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows/#prereq),
[Raspberry Pi](https://cKnowledge.io/c/solution/demo-obj-detection-coco-tf-cpu-benchmark-rpi-portable-workflows/#prereq) 
and [Android](https://cKnowledge.io/c/solution/demo-obj-detection-coco-tflite-cpu-benchmark-android-portable-workflows/#prereq).



## Use cross-platform meta packages

*To be updated.*

See the list of [shared meta packages](https://cKnowledge.io/c/package) with usage examples.



## Use portable workflows

*To be updated.*

See the list of [shared program workflows](https://cKnowledge.io/c/program) with usage examples.



## Prepare portable cKnowledge solutions

*To be updated.*

See the list of [shared solutions](https://cKnowledge.io/c/program) and the [MLPerf automation demo](https://cKnowledge.io/c/solution/demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows).

Please follow [this guide](commands.html#cbench-solutions).
