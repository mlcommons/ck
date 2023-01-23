**[ [TOC](../README.md) ]**

# Adaptive CK container for MLPerf&trade; Inference v1.0 - Object Detection - TFLite 2.4.1 with RUY

## Install Collective Knowledge (CK) with CK MLOps repo

```
python3 -m pip install ck
ck pull repo:mlcommons@ck-mlops
```

## Build Docker container with CK components and workflows for MLPerf&trade;

```
ck build docker:ck-mlperf-inference-v1.0-object-detection-4725481db87af8d0 --tag=ubuntu-20.04
```

## Run this container interactively

```
ck run docker:ck-mlperf-inference-v1.0-object-detection-4725481db87af8d0 --tag=ubuntu-20.04
```

You can now issue standard CK commands from [here](ck-object-detection-x86-64.md) to benchmark MLPerf&trade; model.

## Issue a CK command to this container

### Linux
```
docker run --rm mlcommons/ck-mlperf-inference-v1.0-object-detection-4725481db87af8d0:ubuntu-20.04 \
    "ck benchmark program:object-detection-tflite-loadgen \
     --env.CK_SILENT_MODE=YES \
     --skip_print_timers \
     --dep_add_tags.compiler=gcc \
     --dep_add_tags.python=v3 \
     --dep_add_tags.mlperf-inference-src=r1.0 \
     --dep_add_tags.weights=ssd-mobilenet \
     --dep_add_tags.library=tflite,v2.4.1,with.ruy \
     --env.CK_LOADGEN_DATASET_SIZE=1024 \
     --env.CK_VERBOSE=0 \
     --env.CK_LOADGEN_SCENARIO=SingleStream \
     --env.CK_LOADGEN_MODE=PerformanceOnly \
     --env.CK_LOADGEN_TARGET_LATENCY=20 \
     --skip_stat_analysis \
     --process_multi_keys \
     --repetitions=1 \
     --record \
     --record_repo=local \
     --record_uoa=mlperf-closed-amd-tflite-v2.4.1-ruy-ssd-mobilenet-non-quantized-singlestream-performance-target-latency-20 \
     --tags=mlperf,division.closed,task.object-detection,platform.amd,inference_engine.tflite,inference_engine_version.v2.4.1,inference_engine_backend.ruy,scenario.singlestream,mode.performance,workload.ssd-mobilenet-non-quantized,preprocessed_using.pillow,target_latency.20 \
    "
```

### Windows
```
docker run --rm mlcommons/ck-mlperf-inference-v1.0-object-detection-4725481db87af8d0:ubuntu-20.04 ^
    "ck benchmark program:object-detection-tflite-loadgen ^
     --env.CK_SILENT_MODE=YES ^
     --skip_print_timers ^
     --dep_add_tags.compiler=gcc ^
     --dep_add_tags.python=v3 ^
     --dep_add_tags.mlperf-inference-src=r1.0 ^
     --dep_add_tags.weights=ssd-mobilenet ^
     --dep_add_tags.library=tflite,v2.4.1,with.ruy ^
     --env.CK_LOADGEN_DATASET_SIZE=1024 ^
     --env.CK_VERBOSE=0 ^
     --env.CK_LOADGEN_SCENARIO=SingleStream ^
     --env.CK_LOADGEN_MODE=PerformanceOnly ^
     --env.CK_LOADGEN_TARGET_LATENCY=20 ^
     --skip_stat_analysis ^
     --process_multi_keys ^
     --repetitions=1 ^
     --record ^
     --record_repo=local ^
     --record_uoa=mlperf-closed-amd-tflite-v2.4.1-ruy-ssd-mobilenet-non-quantized-singlestream-performance-target-latency-20 ^
     --tags=mlperf,division.closed,task.object-detection,platform.amd,inference_engine.tflite,inference_engine_version.v2.4.1,inference_engine_backend.ruy,scenario.singlestream,mode.performance,workload.ssd-mobilenet-non-quantized,preprocessed_using.pillow,target_latency.20 ^
    "
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
./ck-object-detection-x86-64-docker-start.sh
```

Here is the content of this script:
```
export CK_HOST_REPO_EXPERIMENTS=`ck where repo:ck-experiments`

echo ${CK_HOST_REPO_EXPERIMENTS}

export CK_LOCAL_DOCKER_SCRIPT=ck-object-detection-x86-64-docker-helper.sh
export CK_HOST_RUN_SCRIPT=$PWD/${CK_LOCAL_DOCKER_SCRIPT}
export CK_HOST_DATASETS=~/datasets

docker run \
       --volume ${CK_HOST_REPO_EXPERIMENTS}:/home/ckuser/ck-experiments \
       --volume ${CK_HOST_RUN_SCRIPT}:/home/ckuser/${CK_LOCAL_DOCKER_SCRIPT} \
       -it mlcommons/ck-mlperf-inference-v1.0-object-detection-4725481db87af8d0:ubuntu-20.04 \
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

ck benchmark program:object-detection-tflite-loadgen \
     --env.CK_SILENT_MODE=YES \
     --skip_print_timers \
     --dep_add_tags.compiler=gcc \
     --dep_add_tags.python=v3 \
     --dep_add_tags.mlperf-inference-src=r1.0 \
     --dep_add_tags.weights=ssd-mobilenet \
     --dep_add_tags.dataset=dataset,object-detection,preprocessed,full,using-pillow \
     --dep_add_tags.library=tflite,v2.4.1,with.ruy \
     --env.CK_LOADGEN_DATASET_SIZE=50 \
     --env.USE_NMS=regular \
     --env.CK_VERBOSE=1 \
     --env.CK_LOADGEN_SCENARIO=SingleStream \
     --env.CK_LOADGEN_MODE=AccuracyOnly \
     --skip_stat_analysis \
     --process_multi_keys \
     --repetitions=1 \
     --record \
     --record_repo=ck-experiments \
     --record_uoa=mlperf-closed-amd-tflite-v2.4.1-ruy-ssd-mobilenet-non-quantized-singlestream-accuracy-target-latency-20 \
     --tags=mlperf,division.closed,task.object-detection,platform.amd,inference_engine.tflite,inference_engine_version.v2.4.1,inference_engine_backend.ruy,scenario.singlestream,mode.accuracy,workload.ssd-mobilenet-non-quantized,preprocessed_using.pillow,target_latency.20

echo "======================================================================="
cat `ck find program:object-detection-tflite-loadgen`/tmp/accuracy.txt 
echo "======================================================================="

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
