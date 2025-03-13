# CM script to run and reproduce experiments

## Reusability using MLCommons CM automation language

Install MLCommmons CM using [this guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

Install this repository with CM interface for reproduced experiments:

```bash
cm pull repo ctuning@cm4research
```

## Install Python virtual environment via CM

```bash
cm run script "install python-venv" --name=reproducibility
export CM_SCRIPT_EXTRA_CMD="--adr.python.name=reproducibility"
```

## Install dependencies

```bash
cmr "reproduce paper m2023 5 _install_deps"
```

## Run and create graphs

```bash
cmr "reproduce paper m2023 5"
```
