# About

This portable CM script run submission checker and generates summary report for all Tiny MLPerf results
using [these native scripts](https://github.com/mlcommons/submissions_tiny_v1.1/pull/51).

## Usage

We have tested this portable CM script on Ubuntu and Windows.

Install [MLCommons CM framework](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

Pull the MLCommons CK repository with automation recipes for interoperable MLOps:
```bash
cm pull repo mlcommons@ck
```

Install repositories with raw MLPerf inference benchmark results:
```bash
cmr "get git repo _repo.https://github.com/mlcommons/tiny_results_v0.7" --extra_cache_tags=mlperf-tiny-results,version-0.7
cmr "get git repo _repo.https://github.com/mlcommons/tiny_results_v1.0" --extra_cache_tags=mlperf-tiny-results,version-1.0
```

You can also add private results to compare submissions locally before they become public:
```bash
cmr "get git repo _repo.https://github.com/mlcommons/submissions_tiny_v1.1" --extra_cache_tags=mlperf-tiny-results,version-1.1-private
```

You can use a specific checkout/branch as follows:
```bash
cm run script "get git repo _repo.https://github.com/mlcommons/submissions_tiny_v1.1" \
   --extra_cache_tags=mlperf-tiny-results,version-1.1-private,generate_final_report \
   --depth="" \
   --branch=generate_final_report
```


Now run this script:
```bash
cmr "generate mlperf-tiny report"
```

It will create `summary-{TinyMLPerf version}.csv' report in your current directory.

You can also specify a version of a repository here:

```bash
cmr "generate mlperf-tiny report" --repo_tags=1.1-private
```

These results are also available in the [public CK playground](https://access.cknowledge.org/playground/?action=experiments&tags=mlperf-tiny,all).

# Contact us

This project is maintained by the [MLCommons taskforce on automation and reproducibility](https://cKnowledge.org/mlcommons-taskforce).
Join our [Discord server](https://discord.gg/JjWNWXKxwT) to ask questions, provide your feedback and participate in further developments.
