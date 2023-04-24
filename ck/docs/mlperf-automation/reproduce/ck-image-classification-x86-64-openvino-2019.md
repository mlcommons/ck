**[ [TOC](../README.md) ]**

***Reproduced by [Grigori Fursin](https://cKnowledge.org/gfursin) on 20210808***

* Platform: x8664
* OS: Ubuntu 18.04 64-bit

# MLPerf&trade; Inference v0.5 - Image Classification - OpenVino 2019 R3

## System packages

Install system packages for [x86](../platform/amd-milan.md).

## Install Collective Knowledge (CK) and Virtual Environment

Note that you need Python 3.7+! If you do not have it installed, don't worry - 
CK can rebuilt a required version when creating a virtual environment.

```
python3 -m pip install ck
ck pull repo:mlcommons@ck-venv
ck create venv:reproduce-mlperf --template=mlperf-inference-1.1
```
CK will attempt to detect existing python versions and will ask you which one to use for your virtual environment.

## Activate created virtual environment

```
ck activate venv:reproduce-mlperf
```

## Pull [CK MLOps repository]( https://github.com/mlcommons/ck-mlops )

```bash
ck pull repo:mlcommons@ck-mlops
```

## Remove new MLPerf

Remove the latest MLPerf (automatically installed by the venv template) to install the old one:
```bash
ck rm env:* --tags=mlperf -f
ck install package --tags=mlperf,inference,source,dividiti.v0.5-intel
```

## Add CPATH for Boost (to be automated in the future)

Substitute python3.7m with the version you use (check this directory):
```bash
export CPATH=${CK_ENV_COMPILER_PYTHON}/include/python3.7m:${CPATH}
```

## Install CK packages

```bash
ck install package --tags=lib,python-package,tensorflow --force_version=1.15.2 --quiet

ck install package --tags=lib,python-package,networkx --force_version=2.3.0

ck install package --tags=lib,python-package,defusedxml

ck install package --tags=lib,python-package,test-generator

ck install package --tags=lib,opencv,v3.4.3

ck install package --tags=lib,boost,v1.67.0,from-sourceforge --no_tags=min-for-caffe

ck install package --tags=lib,loadgen,static
```

## Install OpenVino 2019 R3

```bash
ck install package --tags=lib,intel,open-model-zoo,2019_R3

ck install package --tags=lib,openvino,2019_R3
```

## Install datasets and calibrate model

```bash
ck install package --tags=dataset,imagenet,aux
ck install package --tags=dataset,imagenet,cal,all.500

python3 -m pip install scikit_learn==0.20.2
python3 -m pip install nibabel pillow progress py-cpuinfo pyyaml shapely tqdm xmltodict yamlloader

ck install package --tags=model,tf,mlperf,resnet,from-zenodo --no_tags=ssd

ck install package --tags=model,openvino,resnet50
```

## Copy val_map.txt to the dataset directory

```bash
head -n 500 `ck locate env --tags=aux`/val.txt > `ck locate env --tags=raw,val`/val_map.txt
```

*If want to use full dataset and detect it - need to copy val_map.txt to new env!*

## Check offline accuracy

```bash
export NPROCS=`grep -c processor /proc/cpuinfo`

ck run program:mlperf-inference-v0.5 --skip_print_timers \
     --cmd_key=image-classification --env.CK_OPENVINO_MODEL_NAME=resnet50 \
    --env.CK_LOADGEN_SCENARIO=Offline --env.CK_LOADGEN_MODE=Accuracy --env.CK_LOADGEN_DATASET_SIZE=500 \
    --env.CK_OPENVINO_NTHREADS=$NPROCS --env.CK_OPENVINO_NSTREAMS=$NPROCS --env.CK_OPENVINO_NIREQ=$NPROCS

cat `ck find program:mlperf-inference-v0.5`/tmp/accuracy.txt
```

## Check offline performance

```bash
ck run program:mlperf-inference-v0.5 --skip_print_timers \
     --cmd_key=image-classification --env.CK_OPENVINO_MODEL_NAME=resnet50 \
    --env.CK_LOADGEN_SCENARIO=Offline --env.CK_LOADGEN_MODE=Performance --env.CK_LOADGEN_DATASET_SIZE=500 \
    --env.CK_OPENVINO_NTHREADS=$NPROCS --env.CK_OPENVINO_NSTREAMS=$NPROCS --env.CK_OPENVINO_NIREQ=$NPROCS \
    --env.CK_OPENVINO_NWARMUP_ITERS=1000

cat `ck find program:mlperf-inference-v0.5`/tmp/mlperf_log_summary.txt
```

## Check server performance

```bash
ck run program:mlperf-inference-v0.5 --skip_print_timers \
    --cmd_key=image-classification --env.CK_OPENVINO_MODEL_NAME=resnet50 \
    --env.CK_LOADGEN_SCENARIO=Server --env.CK_LOADGEN_MODE=Performance --env.CK_LOADGEN_DATASET_SIZE=500 \
    --env.CK_OPENVINO_NTHREADS=60 --env.CK_OPENVINO_NSTREAMS=6 --env.CK_OPENVINO_NIREQ=6 \
    --env.CK_OPENVINO_NWARMUP_ITERS=1000 \
    --env.CK_LOADGEN_TARGET_LATENCY=15 \
    --env.CK_LOADGEN_MAX_QUERY_COUNT=1000  \
    --env.CK_LOADGEN_TARGET_QPS=500
```

Extra flags to play with:

* --env.CK_LOADGEN_SAMPLES_PER_QUERY=100  \
* --env.CK_LOADGEN_BUFFER_SIZE=10       \
* --env.CK_LOADGEN_MIN_QUERY_COUNT=1 \
* --env.CK_LOADGEN_MAX_QUERY_COUNT=1  \
* --env.CK_LOADGEN_BUFFER_SIZE=1       \
* --env.CK_LOADGEN_SAMPLES_PER_QUERY=10  \
* --env.CK_LOADGEN_TARGET_QPS=1          \
* --env.CK_LOADGEN_TARGET_LATENCY=1

