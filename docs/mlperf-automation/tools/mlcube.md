**[ [TOC](../README.md) ]**

# MLCube&trade; project

* GitHub: https://github.com/mlcommons/mlcube

## Native CMD 

  
### Download SSD dataset (~20 GB, ~40 GB space required)
```
mlcube run --task download_data --platform docker
```

### Download ResNet34 feature extractor
```
mlcube run --task download_model --platform docker
```

### Run benchmark
```
mlcube run --task train --platform docker
```


## CK automation

### Common CK setup

Install the [CK framework](https://github.com/mlcommons/ck) as follows (check [this guide](https://github.com/mlcommons/ck#installation) in case of problems).

```
python3 -m pip install virtualenv
python3 -m pip install ck
```

We suggest you to create a virtual CK environment as follows:

```
ck pull repo:mlcommons@ck-venv

ck create venv:mlcube --template=generic

ck activate venv:mlcube
```

### Pull repo with CK MLOps, MLCube and MLPerf components:
```
ck pull repo:mlcommons@ck-mlops
```

### Install MLCube as a CK package
```
ck install package --tags=lib,mlcube
```

### List MLCube example

```
ck ls mlcube
```

### List target platforms
```
ck list target
```

### Add new target platform

```
ck add target:my-target --tags=mlcube,my-target
```

### TBD

```
ck run mlcube:demo --target=aws-demo
ck run mlcube:demo --target=my-target
```






## Notes 
* [Single Stage Detection with MLCube(tm)](https://github.com/mlcommons/training/pull/465)
