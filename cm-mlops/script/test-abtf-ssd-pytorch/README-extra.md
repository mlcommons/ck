# Test ABTF SSD PyTorch model via CM

Install CM automation language using this [guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)

# Pull main repository with CM DevOps and MLOps automations

```bash
cm pull repo mlcommons@ck
```

Clean CM cache if needed:

```bash
cm rm cache -f
```

Install python virtual environment to avoid messing up your original Python:

```bash
cmr "install python-venv" --name=abtf
```

Test pre-trained model (add computer_mouse.jpg or any other file to your current directory):
```bash
cmr "test abtf ssd-pytorch" --adr.python.name=abtf --input=computer_mouse.jpg --output=computer_mouse_ssd.jpg
```

# Misc CM commands


```bash
cmr "test abtf ssd-pytorch" --adr.ml-model.tags=_e01 --adr.python.name=abtf --input=computer_mouse.jpg --output=computer_mouse_ssd.jpg
```

```bash
cmr "test abtf ssd-pytorch" --adr.python.name=abtf --adr.torch.version=1.13.1 --adr.torchvision.version=0.14.1 --input=computer_mouse.jpg --output=computer_mouse_ssd.jpg
```

# Testing docker

```bash
cm docker script --tags=test,abtf,ssd-pytorch --docker_cm_repo=ctuning@mlcommons-ck --env.CM_GH_TOKEN=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 --input=computer_mouse.jpg --output=computer_mouse_ssd.jpg
```

```bash
cm docker script --tags=test,abtf,ssd-pytorch --docker_cm_repo=ctuning@mlcommons-ck --docker_os=ubuntu --docker_os_version=23.04 --input=computer_mouse.jpg --output=computer_mouse_ssd.jpg 
```

TBD: pass file to CM docker: [meta](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/build-mlperf-inference-server-nvidia/_cm.yaml#L197).
