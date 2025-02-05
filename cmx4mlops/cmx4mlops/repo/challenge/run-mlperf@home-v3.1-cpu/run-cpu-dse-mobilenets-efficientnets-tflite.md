# Introduction

This guide will help you automatically run the MLPerf inference benchmark v3.1 with multiple variations of MobileNets and EfficientNets 
and TFLite on any Linux-based system with Intel, AMD or Arm CPU.

This benchmark is automated by the MLCommons CM language and you should be able to submit official MLPerf v3.1 inference results
for singlestream scenario in open division and edge category.

It will require ~140GB of disk space and can take ~2 days to run on 1 system producing 243 MLPerf results 
during automatic design space exploration to trade off accuracy vs performance.



## Install CM automation language

Install the [MLCommons CM automation language](https://doi.org/10.5281/zenodo.8105339) as described in this [guide](../../../docs/installation.md). 
It is a small Python library with `cm` and `cmr` command line front-ends and minimal dependencies including Python 3+, Git and wget.

If you encounter problems, please report them at [GitHub](https://github.com/mlcommons/ck/issues).


## Install repository with CM automations

Install the MLCommons repository with [reusable and portable automation recipes (CM scripts)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) via CM.
These scripts are being developed and shared by the community and MLCommons under Apache 2.0 license 
to enable portable, modular, and technology-agnostic benchmarks and applications 
that can automatically run with any software, hardware, models and data sets.

```bash
cm pull repo mlcommons@ck
```

You can run it again at any time to pick up the latest updates.

Note that CM will store all such repositories and downloaded/installed data sets, models and tools
in your `$HOME/CM` directory. 

Since MLPerf benchmarks require lots of space (somethings hundreds of Gigabytes), 
you can change the above location to some large scratch disk using `CM_REPOS` 
environment variable as follows:

```bash
export CM_REPOS={new path to CM repositories and data}
echo "CM_REPOS=${CM_REPOS} >> $HOME/.bashrc"
cm pull repo mlcommons@ck
```



## Setup virtual environment

We suggest you to setup a Python virtual environment via CM to avoid contaminating your existing Python installation:

```bash
cm run script "install python-venv" --name=mlperf --version_min=3.8
export CM_SCRIPT_EXTRA_CMD="--adr.python.name=mlperf"
```

CM will install a new Python virtual environment in CM cache and will install all Python dependencies there:
```bash
cm show cache --tags=python-venv
```

Note that CM downloads and/or installs models, data sets, packages, libraries and tools in this cache.

You can clean it at any time and start from scratch using the following command:
```bash
cm rm cache -f
```

Alternatively, you can remove specific entries using tags:
```bash
cm show cache
cm rm cache --tags=tag1,tag2,...
```


