[ [Back to index](README.md) ]

# Run MLPerf inference benchmarks out-of-the-box

This documentation will help you run, reproduce and compare MLPerf inference benchmarks out-of-the-box 
across any software, hardware, models and data sets from any vendor
using the open-source and technology-agnostic [MLCommons Collective Mind automation language (CM)](https://doi.org/10.5281/zenodo.8105339)
and [MLCommons Collective Knowledge Playground (CK)](https://access.cknowledge.org/playground/?action=experiments).

This project is supported by the [MLCommons Task Force on Automation and Reproducibility](../taskforce.md),
[cTuning foundation](https://cTuning.org) and [cKnowledge Ltd](https://cKnowledge.org).

Don't hesitate to get in touch with us using this [public Discord server](https://discord.gg/JjWNWXKxwT) 
to provide your feedback, ask questions, add new benchmark implementations, models, data sets and hardware backends,
and prepare and optimize your MLPerf submissions.


## Install CM automation language

Install MLCommons CM automation language as described [here](../../installation.md). 
It is a very small Python library with `cm` and `cmr` command line front-ends and minimal dependencies including Python 3+, Git and wget.

If you encounter problems, please report them at [GitHub](https://github.com/mlcommons/ck/issues).


## Install repository with CM automations

Install the MLCommons repository with [reusable automation recipes (CM scripts)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
that are being developed and shared by the community to enable portable, modular, and technology-agnostic benchmarks and applications 
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
```


