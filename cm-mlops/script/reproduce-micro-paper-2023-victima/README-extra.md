# CM script to run and reproduce experiments

Original repository: https://github.com/CMU-SAFARI/Victima


### Reusability using MLCommons CM automation language

Install MLCommmons CM using [this guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

Install reusable MLCommons automations: 

```bash
cm pull repo mlcommons@ck
```

### Run Victima via CM interface

The core CM script for Victima will be available under ```/CM/repos/mlcommons@ck/script/reproduce-micro-2023-paper-victima```

It is described by `_cm.yaml` and several native scripts.

Perform the following steps to evaluate Victima with MLCommons CM automation language:

1) This command will install system dependencies for Docker and require sudo (skip it if you have Docker installed):
```bash
cmr "reproduce paper micro 2023 victima _install_deps"
```

2) This command will prepare and run all experiments via Docker:

```bash
cmr "reproduce paper micro 2023 victima _run" 
```

You can specify --job_manager and --container if needed:
```bash
cmr "reproduce paper micro 2023 victima _run" --job_manager=native|slurm --contianer=docker|podman
```

3) In case of successful execution of a previous command, this command will generate plots to help you validate results from the article:

```bash
cmr "reproduce paper micro 2023 victima _plot"
```
