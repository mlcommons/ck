### Introduction

The goal of this MLPerf@home challenge is to help the community find 
the most efficient Nvidia GPUs for GPT-J 6B model and BERT-99 in terms of 
latency, throughput, accuracy, number of cores, frequency, memory size, cost, and other metrics.

We would like to ask you to run a few [MLPerf inference benchmarks](https://arxiv.org/abs/1911.02549) 
with GPT-J and BERT-99 models on one or more systems with different Nvidia GPUs 
that you have an access to: laptops, servers, cloud instances...

You will be able to run benchmarks, collect all metrics and submit results in an automated way 
in a native environment or Docker container using the portable and technology-agnostic 
[MLCommons Collective Mind automation language (CM)](https://doi.org/10.5281/zenodo.8105339).

Your name and benchmark submissions will be published in the official MLCommons inference v3.1 results
on September 1, 2023 (submission deadline: August 4, 2023), 
will be published in the [official leaderboard](https://access.cknowledge.org/playground/?action=contributors),
will be included to the prize draw, and will be presented in our upcoming ACM/HiPEAC events 
and joint white paper about crowd-benchmarking AI/ML systems similar to SETI@home.

If you have questions or would like to discuss this challenge with the community and organizers, 
please don't hesitate to join our [public Discord server](https://discord.gg/JjWNWXKxwT)
and [weekly conf-calls](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw/edit).

Please report encountered problems using [GitHub issues](https://github.com/mlcommons/ck)
to help the community improve CM automation workflows to run MLPerf benchmarks on any system with any software/hardware stack.

Thank you in advance for helping the community find Pareto-efficient AI/ML Systems!

### Minimal requirements

* GPU: Nvidia
* GPU memory:
  * GPT-J 6B: min 24GB
  * BERT-99: min 8..16GB
* OS: any Linux (tested on Ubuntu 22.04)
* Disk space: ~30GB per model/data set
* Time to run:
  * GPT-J 6B: ~ 1 day
  * BERT-99: ~ 2 hours

### Instructions to run benchmarks and submit results

You can run any of these benchmarks or all depending on available time:

* [GPT-J 6B model; Reference MLPerf implementation; native environment or Docker; PyTorch+CUDA](https://github.com/mlcommons/ck/blob/master/cm-mlops/challenge/run-mlperf%40home-v3.1-gpu/run-nvidia-gpu-gpt-j-6b-ref-pytorch.md)
* [BERT-99 model; Nvidia MLPerf implementation; Docker; TensorRT](https://github.com/mlcommons/ck/blob/master/cm-mlops/challenge/run-mlperf%40home-v3.1-gpu/run-nvidia-gpu-bert-99-nvidia-docker-tensorrt.md)
* [BERT-99 model; Reference MLPerf implementation; native environment; PyTorch/ONNX/TensorFlow](https://github.com/mlcommons/ck/blob/master/cm-mlops/challenge/run-mlperf%40home-v3.1-gpu/run-nvidia-gpu-bert-99-ref-native-onnx-pytorch-tf.md)
* [BERT-99 model; Nvidia MLPerf implementation; native environment; TensorRT](https://github.com/mlcommons/ck/blob/master/cm-mlops/challenge/run-mlperf%40home-v3.1-gpu/run-nvidia-gpu-bert-99-nvidia-native-tensorrt.md)

### Organizers

* [MLCommons Task Force on Automation and Reproducibility](https://cKnowledge.org/mlcommons-taskforce) 
  led by [Grigori Fursin](https://cKnowledge.org/gfursin) and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)
* [cTuning.org](https://www.linkedin.com/company/ctuning-foundation)
* [cKnowledge.org](https://www.linkedin.com/company/cknowledge)

### Advanced challenges

If you feel that running these benchmarks was relatively easy, 
please try [more advanced challenges](https://access.cknowledge.org/playground/?action=challenges)!
