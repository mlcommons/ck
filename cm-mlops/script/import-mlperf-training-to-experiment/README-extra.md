# About

This portable script converts raw results from the [MLPerf™ Training benchmark]( https://github.com/mlcommons/training )
to the [MLCommons CM format](https://github.com/mlcommons/ck) for the [Collective Knowledge Playground](https://x.cKnowledge.org).

The goal is to make it easier for the community to analyze MLPerf results, 
add derived metrics such as performance/Watt and constraints,
and link reproducibility reports.

Aggreaged results are available in [this MLCommons repository](https://github.com/mlcommons/cm4mlperf-results).

You can see these results at [MLCommons CK playground](https://access.cknowledge.org/playground/?action=experiments&tags=mlperf-training,all).

## Usage

We have tested this portable CM script on Ubuntu.

Install [MLCommons CM automation language](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

Pull the MLCommons CK repository with automation recipes for interoperable MLOps:
```bash
cm pull repo mlcommons@ck
```

Install repositories with raw MLPerf training benchmark results:
```bash
cmr "get git repo _repo.https://github.com/mlcommons/training_results_v1.0" --extra_cache_tags=mlperf-training-results,version-1.0 --branch=master --depth=""
cmr "get git repo _repo.https://github.com/mlcommons/training_results_v1.1" --extra_cache_tags=mlperf-training-results,version-1.1 --branch=main --depth=""
cmr "get git repo _repo.https://github.com/mlcommons/training_results_v2.0" --extra_cache_tags=mlperf-training-results,version-2.0 --branch=main --depth=""
cmr "get git repo _repo.https://github.com/mlcommons/training_results_v2.1" --extra_cache_tags=mlperf-training-results,version-2.1 --branch=main
cmr "get git repo _repo.https://github.com/mlcommons/training_results_v3.0" --extra_cache_tags=mlperf-training-results,version-3.0
```

You can install private submission repository as follows:
```bash
cm run script "get git repo _repo.https://github.com/mlcommons/submissions_training_v3.0" --extra_cache_tags=mlperf-training-results,version-3.0-private --branch=main --depth=4
```

Convert raw MLPerf training results into CM experiment entries:
```bash
cmr "import mlperf training to-experiment"
```

Visualize results on your local machine via CK playground GUI:
```bash
cmr "gui _playground"
```

These results are also available in the [public CK playground](https://access.cknowledge.org/playground/?action=experiments&tags=mlperf-training,all).

# Contact us

This project is maintained by the [MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce).
Join our [Discord server](https://discord.gg/JjWNWXKxwT) to ask questions, provide your feedback and participate in further developments.
