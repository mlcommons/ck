# Automating ML&systems R&D

After releasing CK we started working with the community to [gradually automate](introduction.md#how-ck-supports-collaborative-and-reproducible-mlsystems-research) 
the most common and repetitive tasks for ML&systems R&D (see the [journal article](https://arxiv.org/pdf/2011.01149.pdf) 
and [FastPath'20 presentation](https://doi.org/10.5281/zenodo.4005773)).

We started adding the following CK modules and actions with a unified API and I/O.

## Platform and environment detection

These CK modules automate and unify the detection of different properties of user platforms and environments.

* *module:os* [[API](https://cknow.io/c/module/platform/#api)] [[components](https://cknow.io/c/os)]
* *module:platform* [[API](https://cknow.io/c/module/platform/#api)]
* *module:platform.os* [[API](https://cknow.io/c/module/platform.os/#api)]
* *module:platform.cpu* [[API](https://cknow.io/c/module/platform.cpu/#api)]
* *module:platform.gpu* [[API](https://cknow.io/c/module/platform.gpu/#api)]
* *module:platform.gpgpu* [[API](https://cknow.io/c/module/platform.gpgpu/#api)]
* *module:platform.nn* [[API](https://cknow.io/c/module/platform.nn/#api)]

Examples:
```bash
ck pull repo:mlcommons@ck-mlops

ck detect platform
ck detect platform.gpgpu --cuda
```

## Software detection

This CK module automates the detection of a given software or files (datasets, models, libraries, compilers, frameworks, tools, scripts)
on a given platform using CK names, UIDs, and tags:

* *module:soft* [[API](https://cknow.io/c/module/soft/#api)] [[components](https://cknow.io/c/soft)]

It helps to understand a user platform and environment to prepare portable workflows.

Examples:
```bash
ck detect soft:compiler.python
ck detect soft --tags=compiler,python
ck detect soft:compiler.llvm
ck detect soft:compiler.llvm --target_os=android23-arm64
```


## Virtual environment

* *module:env* [[API](https://cknow.io/c/module/env/#api)]

Whenever a given software or files are found using software detection plugins, 
CK creates a new "env" component in the local CK repository
with an env.sh (Linux/MacOS) or env.bat (Windows). 

This environment file contains multiple environment variables 
with unique names usually starting from *CK_* with automatically
detected information about a given soft such as versions and paths
to sources, binaries, include files, libraries, etc.

This allows you to detect and use multiple versions of different software
that can easily co-exist on your system in parallel.

Examples:
```bash
ck detect soft:compiler.python
ck detect soft --tags=compiler,python
ck detect soft:compiler.llvm

ck show env 
ck show env --tags=compiler
ck show env --tags=compiler,llvm
ck show env --tags=compiler,llvm --target_os=android23-arm64

ck virtual env --tags=compiler,python

```



## Meta packages

When a given software is not detected on our system, we usually want to install related packages with different versions.

That's why we have developed the following CK module that can automate installation of missing packages (models, datasets, tools, frameworks, compilers, etc):

* *module:package* [[API](https://cknow.io/c/module/package/#api)] [[components](https://cknow.io/c/package)]

This is a meta package manager that provides a unified API to automatically download, build, and install
packages for a given target (including mobile and edge devices)
using existing building tools and package managers.

All above modules can now support portable workflows that can automatically adapt to a given environment
based on [soft dependencies](https://cknow.io/solution/demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows/#dependencies).


Examples:

```bash
ck install package --tags=lib,tflite,v2.1.1
ck install package --tags=tensorflowmodel,tflite,edgetpu
```

See an example of variations to customize a given package: [lib-tflite](https://github.com/ctuning/ck-tensorflow/tree/master/package/lib-tflite).


## Scripts

We also provided an abstraction for ad-hoc scripts:

* *module:script* [[API](https://cknow.io/c/module/script/#api)] [[components](https://cknow.io/c/script)]

See an example of the CK component with a script used for MLPerf&trade; benchmark submissions: [GitHub](https://github.com/ctuning/ck-mlperf/tree/master/script/mlperf-inference-v0.7.image-classification)



## Portable program pipeline (workflow)

Next we have implemented a CK module to provide a common API to compile, run, and validate programs while automatically adapting to any platform and environment:

* *module:program* [[API](https://cknow.io/c/module/program/#api)] [[components](https://cknow.io/c/program)]

A user describes dependencies on CK packages in the CK program meta as well as commands to build, pre-process, run, post-process, and validate a given program.

Examples:
```bash
ck pull repo:mlcommons@ck-mlops

ck compile program:image-corner-detection --speed
ck run program:image-corner-detection --repeat=1 --env.OMP_NUM_THREADS=4

```

## Reproducible experiments

We have developed an abstraction to record and reply experiments using the following CK module:

* *module:experiment* [[API](https://cknow.io/c/module/experiment/#api)] [[components](https://cknow.io/c/experiment)]

This module records all resolved dependencies, inputs and outputs when running above CK programs
thus allowing to preserve experiments with all the provenance and replay them later on the same or different machine:

```bash
ck benchmark program:image-corner-detection --record --record_uoa=my_experiment

ck find experiment:my_experiment

ck replay experiment:my_experiment

ck zip experiment:my_experiment
```

## Dashboards

Since we can record all experiments in a unified way, we can also visualize them in a unified way.
That's why we have developed a simple web server that can help to create customizable dashboards:

* *module:web* [[API](https://cknow.io/c/module/web/#api)]

See examples of such dashboards:
* [view online at cknow.io platform](https://cknow.io/reproduced-results)
* [view locally (with or without Docker)](https://github.com/ctuning/ck-mlperf/tree/master/docker/image-classification-tflite.dashboard.ubuntu-18.04)




## Interactive articles

One of our goals for CK was to automate the (re-)generation of reproducible articles. 
We have validated this possibility in [this proof-of-concept project](https://cKnowledge.org/rpi-crowd-tuning) 
with the Raspberry Pi foundation. 

We plan to develop a GUI to make the process of generating such papers more user friendly!




## Jupyter notebooks

It is possible to use CK from Jupyter and Colab notebooks. We provided an abstraction to share Jupyter notebooks in CK repositories:

* *module:jnotebook* [[API](https://cknow.io/c/module/jnotebook/#api)] [[components](https://cknow.io/c/jnotebook)]

You can see an example of a Jupyter notebook with CK commands to process MLPerf&trade; benchmark results
[here](https://nbviewer.jupyter.org/urls/dl.dropbox.com/s/5yqb6fy1nbywi7x/medium-object-detection.20190923.ipynb).



## Docker

We provided an abstraction to build, pull, and run Docker images:

* *module:docker* [[API](https://cknow.io/c/module/docker/#api)] [[components](https://cknow.io/c/docker)]

You can see examples of Docker images with unified CK commands to automate the MLPerf&trade; benchmark 
[here](https://github.com/ctuning/ck-mlperf/tree/master/docker).



# Further info

During the past few years we converted all the workflows and components from our past ML&systems R&D
including the [MILEPOST and cTuning.org project](https://github.com/ctuning/reproduce-milepost-project) to the CK format.

There are now [150+ CK modules](https://cknow.io/modules) with actions automating and abstracting 
many tedious and repetitive tasks in ML&systems R&D including model training and prediction, 
universal autotuning, ML/SW/HW co-design, model testing and deployment, paper generation and so on:

* [A high level overview of portable CK workflows](https://cknowledge.org/high-level-overview.pdf)
* [A Collective Knowledge workflow for collaborative research into multi-objective autotuning and machine learning techniques (collaboration with the Raspberry Pi foundation)]( https://cKnowledge.org/report/rpi3-crowd-tuning-2017-interactive )
* [A summary of main CK-based projects with academic and industrial partners]( https://cKnowledge.org/partners.html )
* [cKnowledge.io platform documentation]( https://cknow.io/docs )

Don't hesitate to [contact us](https://cKnowledge.org/contacts.html) if you have a feedback or want to know more about our plans!
