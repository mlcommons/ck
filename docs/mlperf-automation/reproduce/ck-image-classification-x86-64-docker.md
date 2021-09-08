**[ [TOC](../README.md) ]**

# Adaptive CK container for MLPerf&trade; Inference v1.0 - Image Classification - TFLite 2.4.1 with RUY

## Install Collective Knowledge (CK) with CK MLOps repo

```
python3 -m pip install ck
ck pull repo:mlcommons@ck-mlops
```

## Build Docker container with CK components and a small ImageNet (500 images) to test MLPerf&trade; workflows

```
ck build docker:ck-mlperf-inference-v1.0-image-classification-small-imagenet-fcbc9a7708491791 --tag=ubuntu-20.04
```

## Run this container interactively

```
ck run docker:ck-mlperf-inference-v1.0-image-classification-small-imagenet-fcbc9a7708491791 --tag=ubuntu-20.04
```

You can now issue standard CK commands from [here](ck-image-classification-x86-64-tflite.md#install-models) to install ResNet-50 and benchmark it via loadgen.



## Issue a CK command to this container

### Linux
```
docker run --rm mlcommons/ck-mlperf-inference-v1.0-image-classification-small-imagenet-fcbc9a7708491791:ubuntu-20.04 \
    "ck install package --tags=model,tflite,resnet50,no-argmax && ck benchmark program:image-classification-tflite-loadgen \
     --env.CK_LOADGEN_MODE=AccuracyOnly \
     --env.CK_LOADGEN_SCENARIO=SingleStream \
     --env.CK_LOADGEN_DATASET_SIZE=500 \
     --dep_add_tags.weights=resnet50 \
     --dep_add_tags.images=preprocessed,using-opencv \
     --env.CK_LOADGEN_BUFFER_SIZE=1024 \
     --repetitions=1 \
     --skip_print_timers \
     --skip_print_stats \
     --print_files=accuracy.txt \
     --record \
     --record_repo=local \
     --record_uoa=mlperf-closed-image-classification-amd-tflite-v2.4.1-ruy-resnet-50-singlestream-performance-target-latency-75 \
     --tags=mlperf,division.closed,task.image-classification,platform.amd,inference_engine.tflite,inference_engine_version.v2.4.1,inference_engine_backend.ruy,scenario.singlestream,mode.performance,workload"
```

## Run a container and record experiments locally

You can run adaptive CK containers while recording experiments to local CK repositories to perform further analysis and visualization on yout host machine.

Let's create a dummy repository 'ck-experiment':
```
ck add repo:ck-experiment --quiet
```

You can then run the script "ck-object-detection-x86-64-docker-start.sh" from this directory
to pass the path to this repo to the container, run it, benchmark MLPerf&trade; model, and record 
experiments to the above ck-experiment repository:

```
./ck-image-classification-x86-64-docker-start.sh
```

Here is the content of this script:
```
export CK_HOST_REPO_EXPERIMENTS=`ck where repo:ck-experiments`

echo ${CK_HOST_REPO_EXPERIMENTS}

export CK_LOCAL_DOCKER_SCRIPT=ck-image-classification-x86-64-docker-helper.sh
export CK_HOST_RUN_SCRIPT=$PWD/${CK_LOCAL_DOCKER_SCRIPT}
export CK_HOST_DATASETS=~/datasets

docker run \
       --volume ${CK_HOST_REPO_EXPERIMENTS}:/home/ckuser/ck-experiments \
       --volume ${CK_HOST_RUN_SCRIPT}:/home/ckuser/${CK_LOCAL_DOCKER_SCRIPT} \
       -it mlcommons/ck-mlperf-inference-v1.0-image-classification-small-imagenet-fcbc9a7708491791:ubuntu-20.04 \
       "./${CK_LOCAL_DOCKER_SCRIPT}"
```

It also passes a helper script "ck-object-detection-x86-64-docker-helper.sh" to the container:
```
echo "======================================================================="
echo "Fixing access to datasets and ck-experiments ..."
echo ""
time sudo chmod -R 777 datasets
time sudo chmod -R 777 ck-experiments

echo "====================================================================="
echo "Adding external ck-experiments repository ..."
echo ""

ck add repo:ck-experiments --path=/home/ckuser/ck-experiments --quiet

ck ls repo

pwd

ls

ck install package --tags=model,tflite,resnet50,no-argmax 

ck benchmark program:image-classification-tflite-loadgen \
     --env.CK_LOADGEN_MODE=AccuracyOnly \
     --env.CK_LOADGEN_SCENARIO=SingleStream \
     --env.CK_LOADGEN_DATASET_SIZE=500 \
     --dep_add_tags.weights=resnet50 \
     --dep_add_tags.images=preprocessed,using-opencv \
     --env.CK_LOADGEN_BUFFER_SIZE=1024 \
     --repetitions=1 \
     --skip_print_timers \
     --skip_print_stats \
     --record \
     --record_repo=local \
     --record_uoa=mlperf-closed-image-classification-amd-tflite-v2.4.1-ruy-resnet-50-singlestream-performance-target-latency-75 \
     --tags=mlperf,division.closed,task.image-classification,platform.amd,inference_engine.tflite,inference_engine_version.v2.4.1,inference_engine_backend.ruy,scenario.singlestream,mode.performance,workload \
     --print_files=accuracy.txt

```

You can see the results in the ck-experiments from your host machine as follows:
```
ck ls experiment
```
or
```
ck ls ck-experiments:experiment:*
```

You can pack this repository.
```
ck zip repo:ck-experiments
```

CK will create "ckr-ck-experiments.zip" file that can be shared with other colleagues or workgroups.

Anyone else can now add these experiments in their own CK repositories for further analysis as follows:
```
ck unzip repo --zip=ckr-ck-experiments.zip
```

You can also visualize this data using [CK dashboards](../results/ck-dashboard.md).

## Run a container with external ImageNet


Run the following examples for Windows and Linux:
* [ck-image-classification-x86-64-docker-external-imagenet-start.sh](ck-image-classification-x86-64-docker-external-imagenet-start.sh)
* [ck-image-classification-x86-64-docker-external-imagenet-start.bat](ck-image-classification-x86-64-docker-external-imagenet-start.bat)

and a helper file:
* [ck-image-classification-x86-64-docker-external-imagenet-helper.sh](ck-image-classification-x86-64-docker-external-imagenet-helper.sh)
