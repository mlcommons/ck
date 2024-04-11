# About

This portable script converts raw results from the [MLPerf™ Inference benchmark]( https://github.com/mlcommons/inference )
to the [MLCommons CM format](https://github.com/mlcommons/ck) for the [Collective Knowledge Playground](https://x.cKnowledge.org).

The goal is to make it easier for the community to analyze MLPerf inference results, 
add derived metrics such as performance/Watt and constraints,
and link reproducibility reports as shown in these examples:
* [Power efficiency to compare Qualcomm, Nvidia and Sima.ai devices](https://cKnowledge.org/mlcommons-mlperf-inference-gui-derived-metrics-and-conditions)
* [Reproducibility report for Nvidia Orin](https://access.cknowledge.org/playground/?action=experiments&name=mlperf-inference--v3.0--edge--closed--image-classification--offline&result_uid=3751b230c800434a)

Aggreaged results are available in [this MLCommons repository](https://github.com/mlcommons/cm4mlperf-results).

You can see these results at [MLCommons CK playground](https://access.cknowledge.org/playground/?action=experiments&tags=mlperf-inference,all).

## Usage

We have tested this portable CM script on Ubuntu and Windows.

Install [MLCommons CM framework](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

Pull the MLCommons CK repository with automation recipes for interoperable MLOps:
```bash
cm pull repo mlcommons@ck
```

Pull already imported results (v2.0, v2.1, v3.0, v3.1) from this [mlcommons@cm4mlperf-results repo](https://github.com/mlcommons/cm4mlperf-results):

```bash
cm pull repo mlcommons@cm4mlperf-results --checkout=dev
```

Install repository with raw MLPerf inference benchmark results with {NEW VERSION}:
```bash
cmr "get git repo _repo.https://github.com/mlcommons/inference_results_v{NEW VERSION}" --extra_cache_tags=mlperf-inference-results,version-{NEW VERSION} --time --space

```

Use the following CM command if you want to analyze private MLPerf results under submission 
(you need to be a submitter or collaborate with cTuning.org and cKnowledge.org to have an access to such repository):

```bash
cm run script "get git repo _repo.https://github.com/mlcommons/submissions_inference_v4.0" --env.CM_GIT_CHECKOUT=main --extra_cache_tags=mlperf-inference-results,version-4.0-private --time --space
```

Convert all raw MLPerf results into CM experiment entries - it can take 5..15 minutes to run submission checker 
with raw MLPerf results before converting them to the fast CM format (skip target_repo if you want
to record results to the `local` CM repository):

```bash
cm run script "import mlperf inference to-experiment" --target_repo=mlcommons@cm4mlperf-results --time --space
```

or for a specific submitter:

```bash
cm run script "import mlperf inference to-experiment" --submitter=CTuning
```


If you already generated `summary.csv` in your current directory, you can skip submission checker as follows:

```bash
cm run script "import mlperf inference to-experiment _skip_checker"
```

Visualize results on your local machine via CK playground GUI:

```bash
cm run script "gui _playground"
```

These results are also available in the [public CK playground](https://access.cknowledge.org/playground/?action=experiments&tags=mlperf-inference,all).

## Further analysis of results

Please check this [README](https://github.com/mlcommons/cm4mlperf-results#how-to-update-this-repository-with-new-results).

# Contact us

This project is maintained by the [MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce).
Join our [Discord server](https://discord.gg/JjWNWXKxwT) to ask questions, provide your feedback and participate in further developments.
