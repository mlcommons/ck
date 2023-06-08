# CM "experiment" automation

*We suggest you to check [CM introduction](https://github.com/mlcommons/ck/blob/master/docs/introduction-cm.md), 
 [CM CLI/API](https://github.com/mlcommons/ck/blob/master/docs/interface.md) 
 and [CM scripts](../script/README-extra.md) to understand CM motivation and concepts.
 You can also try [CM tutorials](https://github.com/mlcommons/ck/blob/master/docs/tutorials/README.md) 
 to run some applications and benchmarks on your platform using CM scripts.*

## Introducing CM experiment automation

Researchers and practitioners need to experiment a lot with different settings of
applications, compilers, software and hardware before finding the optimal combination
suitable for real use cases.

Based on the feedback from researchers, engineers and students, our [MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md) 
started developing a CM automation called "experiment".
The goal is to provide a common interface to run, record, share, visualize and reproduce experiments
on any platform with any software, hardware and data.

For example, this automation is used to record results in a unified CM format from [several MLPerf benchmarks](https://github.com/mlcommons/cm_inference_results)
including [MLPerf inference](https://github.com/mlcommons/inference) and [MLPerf Tiny](https://github.com/mlcommons/tiny),
visualize them at the [MLCommons CM platform](https://access.cknowledge.org/playground/?action=experiments&tags=all),
and improve them by the community via [public reproducibility and optimization challenges](https://access.cknowledge.org/playground/?action=challenges).

## Installing CM with ResearchOps/DevOps/MLOps automations

This CM automation is available in the most commonly used `mlcommons@ck` repository. 

First, install CM automation language as described [here](https://github.com/mlcommons/ck/blob/master/docs/installation.md).
Then, install or update this repository as follows:
```bash
cm pull repo mlcommons@ck
```

You can now test that CM experiment automation is available as follows:
```bash
cm run experiment --help
```
or using `cme` shortcut in CM V1.4.1+
```bash
cme --help
```

## Understanding CM experiments




## Visualizing

cm run script "gui _playground"



## The next steps
