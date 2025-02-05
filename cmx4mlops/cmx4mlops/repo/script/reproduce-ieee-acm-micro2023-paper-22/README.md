# CM script to run and reproduce experiments

Original repository: https://github.com/UofT-EcoSystem/Grape-MICRO56-Artifact/wiki#installation

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

### Install dependencies

```bash
cmr "reproduce project micro-2023 22 _install_deps"
cmr "reproduce project micro-2023 22 _install_deps_driver"
cmr "reproduce project micro-2023 22 _install_deps_cuda"
cmr "reproduce project micro-2023 22 _install_deps_pytorch"
cmr "reproduce project micro-2023 22 _install_deps_transformers"
```

Please reboot the machine after the above installation steps for the GPU driver installation to take effect. This can be verified from the message `NVRM: loading customized kernel module from Grape` when running the command `sudo dmesg`. If the message does not appear, please repeat the command

```bash
cmr "reproduce project micro-2023 22 _install_deps_driver"
```

### Run experiments

```bash
cmr "reproduce project micro-2023 22 _run_figure13"
cmr "reproduce project micro-2023 22 _run_figure11"
cmr "reproduce project micro-2023 22 _run_figure12"
```
