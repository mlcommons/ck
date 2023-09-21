# Introduction

This guide will help you run the reference implementation of the MLPerf inference benchmark v3.1 
with GPT-J 6B model and PyTorch on any Linux-based system with Nvidia GPU (24GB min memory required)
using the [MLCommons CM automation language](https://doi.org/10.5281/zenodo.8105339).

CM will help you to obtain performance and accuracy numbers for GPT-J 6B model on your system
for the SingleStream scenario and submit them to the official MLPerf v3.1 inference benchmarking round 
in open division and edge category 
(**deadline to send us results for v3.1 submission: August 3, 2023**).

You can read more about scenarios, divisions and categories of MLPerf inference benchmarks
in this [MLPerf inference benchmark paper](https://arxiv.org/abs/1911.02549) -
our goal is to help the community compare performance, accuracy and other metrics of popular models across diverse systems
in an automated, unified and reproducible way!

This benchmark will require ~30GB of disk space and can take ~1 day to run on one system 
to have a valid MLPerf result.



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


## Do the performance run

Now you can run MLPerf inference benchmark to measure performance of GPT-J using CM command as follows
(note that `cmr` is equivalent to `cm run script`):

```bash
cm run script --tags=generate-run-cmds,inference,_performance-only \
    --division=open \
    --category=edge \
    --model=gptj-99 \
    --precision=bfloat16 \
    --device=cuda \
    --implementation=reference \
    --backend=pytorch \
    --scenario=SingleStream \
    --env.GPTJ_BEAM_SIZE=1 \
    --execution-mode=valid \
    --results_dir=$HOME/results_dir \
    --quiet
```

Note that this command will need to automatically download the model (24GB) 
and [CNN Daily Mail dataset (relatively small)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-dataset-cnndm)!

The benchmark run is expected to finish within 10-100 minutes depending on the performance of your GPU.

In the end of the valid run, you should see [output](https://github.com/ctuning/mlperf_inference_submissions_v3.1/blob/main/open/cTuning/results/amd_zen4_workstation-reference-gpu-pytorch-v2.0.1-default_config/gptj-99/singlestream/performance/run_1/mlperf_log_summary.txt) similar to 

```txt
================================================
MLPerf Results Summary
================================================
SUT name : PySUT
Scenario : SingleStream
Mode     : PerformanceOnly
90th percentile latency (ns) : 4751920830
Result is : VALID
  Min duration satisfied : Yes
  Min queries satisfied : Yes
  Early stopping satisfied: Yes
Early Stopping Result:
 * Processed at least 64 queries (201).
 * Would discard 9 highest latency queries.
 * Early stopping 90th percentile estimate: 5387449249
 * Not enough queries processed for 99th percentile
 early stopping estimate (would need to process at
 least 662 total queries).

================================================
Additional Stats
================================================
QPS w/ loadgen overhead         : 0.33
QPS w/o loadgen overhead        : 0.33

Min latency (ns)                : 881803157
Max latency (ns)                : 5939081711
Mean latency (ns)               : 3008773902
50.00 percentile latency (ns)   : 2788885477
90.00 percentile latency (ns)   : 4751920830
95.00 percentile latency (ns)   : 5307244203
97.00 percentile latency (ns)   : 5677375096
99.00 percentile latency (ns)   : 5927209480
99.90 percentile latency (ns)   : 5939081711

================================================
Test Parameters Used
================================================
samples_per_query : 1
target_qps : 2000
target_latency (ns): 0
max_async_queries : 1
min_duration (ms): 600000
max_duration (ms): 620000
min_query_count : 100
max_query_count : 0
qsl_rng_seed : 148687905518835231
sample_index_rng_seed : 520418551913322573
schedule_rng_seed : 811580660758947900
accuracy_log_rng_seed : 0
accuracy_log_probability : 0
accuracy_log_sampling_target : 0
print_timestamps : 0
performance_issue_unique : 0
performance_issue_same : 0
performance_issue_same_index : 0
performance_sample_count : 13368

No warnings encountered during test.

No errors encountered during test.
```


## Do the accuracy run

```bash
cm run script --tags=generate-run-cmds,inference,_accuracy-only \
    --division=open \
    --category=edge \
    --model=gptj-99 \
    --precision=bfloat16 \
    --device=cuda \
    --implementation=reference \
    --backend=pytorch \
    --scenario=SingleStream \
    --env.GPTJ_BEAM_SIZE=1 \
    --execution-mode=valid \
    --results_dir=$HOME/results_dir \
    --quiet
```

This accuracy run can take many hours (typically 12..46 hours). You can estimate it using the QPS (queries per second) 
from the previous performance run as follows:

accuracy time = data set / QPS = 13368 / QPS .

For example, if your reported QPS is 0.1 (equivalent to 10000 ms latency), it will take 13368/0.1 ~ 37 hours.



## Populate the MLPerf README files describing your submission

Now you can use CM to automatically populate README files mandated by MLPerf to describe your submission
(we also show you a simpler syntax of `cmr` instead of `cm run script --tags=`):

```bash
cmr "generate-run-cmds inference _populate-readme" \
    --division=open \
    --category=edge \
    --model=gptj-99 \
    --precision=bfloat16 \
    --device=cuda \
    --implementation=reference \
    --backend=pytorch \
    --scenario=SingleStream \
    --env.GPTJ_BEAM_SIZE=1 \
    --execution-mode=valid \
    --results_dir=$HOME/results_dir \
    --quiet
```


## Generate MLPerf submission

Unless your organization is an official member of MLCommons, you will be able to participate in the official MLPerf inference community submission
via the cTuning foundation (founding member of MLCommons).

You should update the following flags in the below CM command:
* Use `--hw_notes_extra` option to add your name to the submission such as `--hw_notes_extra="Result taken by NAME" `.
* Use `--hw_name="My system name"` to give a meaningful system name describing your GPU. 
  Examples can be seen [here](https://github.com/mlcommons/inference_results_v3.0/tree/main/open/cTuning/systems).
* Use `--submitter=<Your name>` if your organization is an official MLCommons member and you would like to submit under your organization.

You should use the master branch of MLCommons inference repo for the submission checker:

```bash
cmr "generate inference submission" \
    --clean \
    --submitter=cTuning \
    --results_dir=$HOME/results_dir/valid_results \
    --submission_dir=$HOME/inference_submission_tree \
    --preprocess_submission=yes \
    --adr.compiler.tags=gcc \
    --adr.inference-src.version=master \
    --run-checker 
```

## Push the results to GitHub repo

1. Create a fork of [this cTuning repo with the community results](https://github.com/ctuning/mlperf_inference_submissions_v3.1). 

2. Run the following command after replacing `--repo_url` with your fork URL.

  ```
  cmr "push github mlperf inference submission" \
      --submission_dir=$HOME/inference_submission_tree \
      --repo_url=https://github.com/ctuning/mlperf_inference_submissions_v3.1/ \
      --commit_message="GPTJ results on <HW name> added by <Name>"
  ```

3. Create a PR to the [cTuning repo with the community results](https://github.com/ctuning/mlperf_inference_submissions_v3.1)









## Additional performance optimization challenge for interested enthusiasts

The MLPerf GPT-J inference benchmark is implemented in this [backend.py](https://github.com/mlcommons/inference/blob/master/language/gpt-j/backend.py).

It is automatically installed and cached by CM. You can find it on your system using this command:
```bash
cd `cm find cache --tags=inference,src,_branch.master`/language/gpt-j
ls backend.py
```

The original model is available at the [Hugging Face Zoo](https://huggingface.co/EleutherAI/gpt-j-6b). It was fine-tuned by Intel for this benchmark
and is available at the MLCommons cloud. It is automatically downloaded by CM using [this script](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-ml-model-gptj/_cm.json).

You can try to improve the performance (QPS) on this code or fine-tune model and substitute the default one 
in [this line](https://github.com/mlcommons/inference/blob/master/language/gpt-j/backend.py#L27).

Some examples of fine-tuning can be seen [here](https://betterprogramming.pub/fine-tuning-gpt-j-6b-on-google-colab-or-equivalent-desktop-or-server-gpu-b6dc849cb205). 

Any better performance or accuracy result will be very valuable to the community.

After any modification, you can redo a quick performance run to see the performance difference. 
```
cm run script --tags=generate-run-cmds,inference,_performance-only \
    --division=open \
    --category=edge \
    --model=gptj-99 \
    --precision=bfloat16 \
    --device=cuda \
    --implementation=reference \
    --backend=pytorch \
    --scenario=SingleStream \
    --env.GPTJ_BEAM_SIZE=1 \
    --execution-mode=valid \
    --results_dir=$HOME/results_dir \
    --quiet
```



## Questions? Suggestions?

Don't hesitate to get in touch with the community and organizers 
via [public Discord server](https://discord.gg/JjWNWXKxwT).
