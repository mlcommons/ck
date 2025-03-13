# CM script to run and reproduce experiments

Original repository: [https://github.com/FPSG-UIUC/micro23-teaal-artifact](https://github.com/FPSG-UIUC/micro23-teaal-artifact)

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

## Run TeAAL via the CM interface

To install dependencies, run:

```bash
cmr "reproduce paper m 2023 8 _install_deps"
```

Note that the install script makes its best guess for the correct UID and GID
for the container to be using (the current user's UID and GID).  If you would
like to change the UID and/or GID of the container, you can do so in the
artifact repository `/path/to/<some hash>/repo/docker-compose.yaml`.
Instructions for finding this repository are below.

To check that the environment is correctly set up and evaluate each accelerator
configuration on a small example, run:

```bash
cmr "reproduce paper m 2023 8 _check"
```

To run the real experiments, run:

```bash
cmr "reproduce paper m 2023 8 _run"
```

To plot the results of the real experiments, run
```bash
cmr "reproduce paper m 2023 8 _plot"
```

The plots will be stored in the artifact repository at `/path/to/<some
hash>/repo/data/plots`. Instructions for finding this repository are below.

To plot pregenerated results (e.g., if you don't want to run the experiments
yourself), run:

```bash
cmr "reproduce paper m 2023 8 _plot_pregenerated"
```

### Finding the Artifact Repository

You can also find this directory via CM as follows:
```bash
cm show cache --tags=git,artifact,fpsg,teaal
```
or
```bash
cm find cache --tags=git,artifact,fpsg,teaal
```

