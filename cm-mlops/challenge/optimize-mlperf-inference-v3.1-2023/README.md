### Introduction

Open-source [MLPerf inference benchmarks](https://arxiv.org/abs/1911.02549) 
were developed by a [consortium of 50+ companies and universities (MLCommons)](https://mlcommons.org)
to enable trustable and reproducible comparison of popular AI tasks and models
across diverse software/hardware stacks from different vendors.

However, running MLPerf inference benchmarks and submitting results [turned out to be a challenge](https://arxiv.org/abs/1911.02549) 
even for experts and could easily take many weeks. That's why MLCommons partnered with 
[cTuning.org](https://www.linkedin.com/company/ctuning-foundation)
and [cKnowledge.org](https://www.linkedin.com/company/cknowledge) to develop an open-source, technology-agnostic 
and non-intrusive [Collective Mind automation language (CM)](https://github.com/mlcommons/ck)
and [Collective Knowledge Playground (CK)](https://access.cknowledge.org/playground/?action=experiments) 
to run, reproduce, optimize and compare MLPerf inference benchmarks out-of-the-box 
accross diverse software, hardware, models and data sets from any vendor.

You can read more about our vision, open-source technology and future plans 
in this [presentation](https://doi.org/10.5281/zenodo.8105339).



### Challenge

We would like you to run as many MLPerf inference benchmarks on as many CPUs and Nvidia GPUs 
as possible using CM and submit official results to MLPerf inference v3.1.

However, since some benchmarks may take 1 day to run, we suggest to start in the following order:
* 

Please read [this documentation](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/README.md)
to set up and run above benchmarks using CM.

* Submitting valid results for 1 complete benchmark on one system will give you 1 point.
* The first 3 top submitters will get a prize of 200$ each.
* All submitters will participate in writing a common white paper about running and comparing MLPerf inference benchmarks out-of-the-box.

You can register your participation for the [Collective Knowledge leaderboard](http://localhost:8501/?action=contributors)
using this [guide](https://github.com/mlcommons/ck/blob/master/platform/register.md).

Please report encountered problems using [GitHub issues](https://github.com/mlcommons/ck/issues)
and the public [Discord server](https://discord.gg/JjWNWXKxwT) to help the community
improve the portability of the CM interface for MLPerf.

You can also talk to organizers at any time using above [Discord server](https://discord.gg/JjWNWXKxwT) or 
during our [weekly conf-calls](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw/edit).

Looking forward to your submissions and happy hacking!



#### Organizers

* [MLCommons](https://cKnowledge.org/mlcommons-taskforce)
* [cTuning.org](https://cTuning.org)
* [cKnowledge.org](https://cKnowledge.org)

### Status

You can see shared results in [this repostiory](https://github.com/ctuning/mlperf_inference_submissions_v3.1) 
with PRs from participants [here](https://github.com/ctuning/mlperf_inference_submissions_v3.1/pulls).
