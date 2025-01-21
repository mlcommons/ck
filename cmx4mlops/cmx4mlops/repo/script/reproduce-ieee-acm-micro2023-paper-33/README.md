# CM script to run and reproduce experiments

Original repository: https://github.com/filipmazurek/spa-artifact

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

### Set up and start Docker container

```bash
cmr "reproduce project m 2023 33 _install_deps"
```

You should be within the Docker container now.

The next step is not yet fully automated by CM and you need to do it manually to set up Conda environment:

### Set up Conda

```bash
cd /shared/
bash ./in-docker-bash-scripts/set-up-conda.sh

# Use conda with the bash shell
eval "$(/root/miniconda3/bin/conda shell.bash hook)"

conda activate spa
```

### Install CM inside Conda to continue using CM interface

```bash
python3 -m pip install cmind
cm pull repo mlcommons@ck
cm pull repo ctuning@cm4research
```

### Download Ubuntu Image and Kernel

```bash
cmr "reproduce project m 2023 33 _install_deps_kernel"
```

### Copy gem5 PARSEC Binaries

```bash
cmr "reproduce project m 2023 33 _install_deps_gem5"
```

### Run experiments Using gem5

```bash
cmr "reproduce project m 2023 33 _run"
```

### Collect data and reproduce results

```bash
cmr "reproduce project m 2023 33 _plot"
```

All figures should be available in `/shared/paper-figures/`.
