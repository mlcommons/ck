# CM script to run and reproduce experiments

Original repository: https://github.com/CMU-SAFARI/Victima


### Reusability using MLCommons CM automation language

Install MLCommmons CM using [this guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

Install reusable MLCommons automations: 

```bash
cm pull repo mlcommons@ck
```

Install this repository with CM interface for reproduced experiments:
```bash
cm pull repo ctuning@cm4research
```

### Run Victima via CM interface

Perform the following steps to evaluate Victima with MLCommons CM automation language:

1) This command will install system dependencies for Docker and require sudo (skip it if you have Docker installed):
```bash
cmr "reproduce project m 2023 victima _install_deps"
```

2) This command will prepare and run all experiments via Docker:

```bash
cmr "reproduce project m 2023 victima _run" 
```

You can specify --job_manager and --container if needed:
```bash
cmr "reproduce project m 2023 victima _run" --job_manager=native|slurm --contianer=docker|podman
```

3) In case of successful execution of a previous command, this command will generate plots to help you validate results from the article:

```bash
cmr "reproduce project m 2023 victima _plot"
```
