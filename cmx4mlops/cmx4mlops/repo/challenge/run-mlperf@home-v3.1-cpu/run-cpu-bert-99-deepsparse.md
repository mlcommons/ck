# Introduction

This guide will help you automatically run the MLPerf inference benchmark v3.1 with BERT-99 model and DeepSparse engine
on any Linux-based system with Intel, AMD or Arm CPU.

This benchmark is automated by the MLCommons CM language and you should be able to submit official MLPerf v3.1 inference results
for offline scenario in open division and edge category.

It will require ~20GB of disk space and can take ~2 hours to run on 1 system.




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




### Do a test run to detect and record the system performance

```bash
cm run script --tags=generate-run-cmds,inference,_find-performance \
--model=bert-99 --implementation=reference --device=cpu --backend=deepsparse \
--category=edge --division=open --quiet --scenario=Offline
```

### Do full accuracy and performance run

```
cm run script --tags=generate-run-cmds,inference,_submission --model=bert-99 \
--device=cpu --implementation=reference --backend=deepsparse \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet --scenario=Offline
```
### Generate and upload MLPerf submission

Follow [this guide](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/Submission.md) to generate the submission tree and upload your results.


