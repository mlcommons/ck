# Introduction

This guide will help you automatically run the reference implementation of the MLPerf inference benchmark v3.1 
with GPT-J 6B model and PyTorch on any Linux-based system with Nvidia GPU (24GB min memory required).

This benchmark is automated by the [MLCommons CM language](https://doi.org/10.5281/zenodo.8105339) 
and you should be able to submit official MLPerf v3.1 inference results
for singlestream scenario in open division and edge category 
(**deadline to send us results for v3.1 submission: August 3, 2023**).

It will require ~30GB of disk space and can take ~1 day to run on 1 system.



## Install CM automation language

Install the [MLCommons CM automation language](https://github.com/mlcommons/ck) as described in this [guide](../../../docs/installation.md). 
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

Note that CM will store all such repositories and downloaded/installed data sets, models, and tools
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



## Setup CUDA

1. We expect that CUDA driver 11+ is already installed on your system.
   However, even if it is not, any CM script with CUDA depedency should automatically
   download and install it using this [portable CM script](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-cuda).


2. Detect or install cuDNN (x86 host)

   Try to detect already installed cuDNN on your system via CM:
    
    ```bash
      cmr "get cudnn"
    ```

    If it is not available, you can download it from [here](https://developer.nvidia.com/cudnn) and install it via CM as follows:
    
    ```bash
      cmr "get cudnn" --input=<PATH_TO_CUDNN_TAR_FILE>
    ```


### Do the performance run

```
cm run script --tags=generate-run-cmds,inference,_performance-only --model=gptj-99 \
--device=cuda --implementation=reference --backend=pytorch \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet --precision=bfloat16 --env.GPTJ_BEAM_SIZE=1 \
--scenario=SingleStream --singlestream_target_latency=500
```

* `--singlestream_target_latency` is in milliseconds and just an approximate value is fine here as it is used just to determine the maximum number of queries to be generated.
* Run is expected to finish in 10-100 minutes depending on the performance of the GPU

### Do the accuracy run

```
cm run script --tags=generate-run-cmds,inference,_accuracy-only --model=gptj-99 \
--device=cuda --implementation=reference --backend=pytorch \
--execution-mode=valid --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet --precision=bfloat16 --env.GPTJ_BEAM_SIZE=1 \
--scenario=SingleStream
```

* Run can take many hours and if the queries per second of the system is 0.1 (latency in millisecond of 10000), it'll take 13368/0.1 seconds which is approximately 37 hours.  



### Populate the README files describing your submission

```
cmr "generate-run-cmds inference _populate-readme" \
--model=gptj-99 --device=cpu --implementation=reference --backend=pytorch \
--execution-mode=valid --scenario=SingleStream --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet --precision=bfloat16 --env.GPTJ_BEAM_SIZE=1
```

### Generate and upload MLPerf submission

Follow [this guide](https://github.com/ctuning/mlcommons-ck/blob/master/docs/mlperf/inference/Submission.md) to generate the submission tree and upload your results.

## Additional performance optimization challenge for interested enthusiasts

`cd` into the gpt-j code folder 
```
cd `cm find cache --tags=inference,src,_branch.master`
```

Here, `backend.py` is the code implementing the gpt-j inference. You can try to improve the performance of the code or to do better fine-tuning (some examples can be seen [here](https://betterprogramming.pub/fine-tuning-gpt-j-6b-on-google-colab-or-equivalent-desktop-or-server-gpu-b6dc849cb205). Any better performance or accuracy result will be very valuable to the community.

After any modification, you can redo a quick performance run to see the performance difference. 
```
cm run script --tags=generate-run-cmds,inference,_performance-only --model=gptj-99 \
--device=cuda --implementation=reference --backend=pytorch \
--execution-mode=fast --results_dir=$HOME/results_dir \
--category=edge --division=open --quiet --precision=bfloat16 --env.GPTJ_BEAM_SIZE=1 \
--scenario=SingleStream --singlestream_target_latency=500
```
