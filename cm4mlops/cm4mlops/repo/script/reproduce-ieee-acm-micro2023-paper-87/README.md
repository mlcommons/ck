# CM script to run and reproduce experiments

Archived artifact: https://zenodo.org/record/8218698

## Reusability using MLCommons CM automation language

Install MLCommmons CM using [this guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md).
Note that you need run the following command to install CM automation scripts:

```bash
cm pull repo mlcommons@ck
```

Install this repository with CM interface for reproduced experiments:

```bash
cm pull repo ctuning@cm4research
```

## Install deps

To install dependencies, run:

```bash
cmr "reproduce paper micro-2023 clockhands _install_deps"
```

## Run 

```bash
cmr "reproduce paper micro-2023 clockhands _build_compiler"
cmr "reproduce paper micro-2023 clockhands _create_binary"
cmr "reproduce paper micro-2023 clockhands _build_onikiri"
cmr "reproduce paper micro-2023 clockhands _experiment_setup"
cmr "reproduce paper micro-2023 clockhands _experiment"
cmr "reproduce paper micro-2023 clockhands _Preliminary_build_onikiri"
cmr "reproduce paper micro-2023 clockhands _Preliminary_create_binary"
cmr "reproduce paper micro-2023 clockhands _Preliminary_experiment_setup"
cmr "reproduce paper micro-2023 clockhands _Preliminary_experiment"
```

## Plot

To plot the results of the real experiments, run

```bash
cmr "reproduce paper micro-2023 clockhands _plot"
cmr "reproduce paper micro-2023 clockhands _Preliminary_plot"
```
