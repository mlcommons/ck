**[ [TOC](../README.md) ]**

***Reproduced by [Grigori Fursin](https://cKnowledge.org/gfursin) on 20210428***

# MLPerf&trade; Inference v1.0 - Object Detection - TFLite 2.4.1 with RUY

### System packages

Install system packages for [x86 Ubuntu](../platform/amd-milan.md).

## Install Collective Knowledge (CK) and Virtual Environment

```
python3 -m pip install ck
ck pull repo:mlcommons@ck-venv
ck create venv:reproduce-mlperf
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

## Set up CK environment

```
ck detect platform.os --platform_init_uoa=generic-linux-dummy
ck detect soft:compiler.python --full_path=${CK_VENV_PYTHON_BIN}
ck detect soft:compiler.gcc --full_path=`which gcc`
```

## Install common CK packages
```
ck install package --tags=tool,cmake,prebuilt

ck install package --tags=lib,python-package,absl
ck install package --tags=lib,python-package,numpy
ck install package --tags=lib,python-package,matplotlib
ck install package --tags=lib,python-package,cython
ck install package --tags=lib,python-package,pillow

ck install package --tags=mlperf,inference,src,r1.0
ck install package --tags=lib,mlperf,loadgen,static
```

## Install COCO 2017 val dataset (5000 images)

```
ck install package --ask --tags=dataset,coco,val,2017
ck install package --tags=tool,coco,api
```

## Install framework TFLite 2.4.1 with RUY

```
ck install package --tags=lib,tflite,via-cmake,v2.4.1,with.ruy
ck install package --tags=api,model,tensorflow,r2.3.0
```

## Convert COCO to 300x300

```
ck install package --tags=dataset,object-detection,preprocessed,full,side.300,using-pillow
```

## Install models compatible with processed COCO 300x300

### TF SSD Mobilenet-v1 non-quantized

Install the non-quantized model directly
```
ck install package --tags=model,tflite,object-detection,ssd-mobilenet,non-quantized
```

### See CK environment

```
ck show env
```

### Benchmark

#### Performance

```
ck benchmark program:object-detection-tflite-loadgen \
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
     --tags=mlperf,division.closed,task.object-detection,platform.amd,inference_engine.tflite,inference_engine_version.v2.4.1,inference_engine_backend.ruy,scenario.singlestream,mode.performance,workload.ssd-mobilenet-non-quantized,preprocessed_using.pillow,target_latency.20
```

Print MLPerf&trade; compatible output:
```
cat `ck find program:object-detection-tflite-loadgen`/tmp/mlperf_log_summary.txt
```

List CK experiments database:
```
ck ls experiment
```

#### Accuracy

```
ck benchmark program:object-detection-tflite-loadgen \
     --env.CK_SILENT_MODE=YES \
     --skip_print_timers \
     --dep_add_tags.compiler=gcc \
     --dep_add_tags.python=v3 \
     --dep_add_tags.mlperf-inference-src=r1.0 \
     --dep_add_tags.weights=ssd-mobilenet \
     --dep_add_tags.dataset=dataset,object-detection,preprocessed,full,using-pillow \
     --dep_add_tags.library=tflite,v2.4.1,with.ruy \
     --env.CK_LOADGEN_DATASET_SIZE=5000 \
     --env.USE_NMS=regular \
     --env.CK_VERBOSE=1 \
     --env.CK_LOADGEN_SCENARIO=SingleStream \
     --env.CK_LOADGEN_MODE=AccuracyOnly \
     --skip_stat_analysis \
     --process_multi_keys \
     --repetitions=1 \
     --record \
     --record_repo=local \
     --record_uoa=mlperf-closed-amd-tflite-v2.4.1-ruy-ssd-mobilenet-non-quantized-singlestream-accuracy-target-latency-20 \
     --tags=mlperf,division.closed,task.object-detection,platform.amd,inference_engine.tflite,inference_engine_version.v2.4.1,inference_engine_backend.ruy,scenario.singlestream,mode.accuracy,workload.ssd-mobilenet-non-quantized,preprocessed_using.pillow,target_latency.20
```

Print MLPerf&trade; compatible output:
     
```
cat `ck find program:object-detection-tflite-loadgen`/tmp/accuracy.txt 
```

#### Compliance

* TEST04-A:

```
ck benchmark program:object-detection-tflite-loadgen \
      --env.CK_SILENT_MODE=YES \
      --skip_print_timers \
      --dep_add_tags.compiler=gcc \
      --dep_add_tags.python=v3 \
      --dep_add_tags.mlperf-inference-src=r1.0 \
      --dep_add_tags.weights=ssd-mobilenet \
      --dep_add_tags.dataset=dataset,object-detection,preprocessed,full,using-pillow \
      --dep_add_tags.library=tflite,v2.4.1,with.ruy \
      --env.CK_LOADGEN_DATASET_SIZE=1024 \
      --env.CK_VERBOSE=0 \
      --env.CK_LOADGEN_SCENARIO=SingleStream \
      --env.CK_LOADGEN_TARGET_LATENCY=20 \
      --env.CK_MLPERF_COMPLIANCE_TEST=TEST04-A \
      --env.CK_LOADGEN_MODE=PerformanceOnly \
      --skip_stat_analysis \
      --process_multi_keys \
      --repetitions=1 \
      --record \
      --record_repo=local \
      --record_uoa=mlperf-closed-amd-tflite-v2.4.1-ruy-ssd-mobilenet-non-quantized-singlestream-performance-compliance.TEST04-A \
      --tags=mlperf,division.closed,task.object-detection,platform.amd,inference_engine.tflite,inference_engine_version.v2.4.1,inference_engine_backend.ruy,scenario.singlestream,mode.performance,workload.ssd-mobilenet-non-quantized,preprocessed_using.pillow,target_latency.20,compliance.TEST04-A
```

Print MLPerf&trade; compatible output:
       
```
cat `ck find program:object-detection-tflite-loadgen`/tmp/mlperf_log_summary.txt
```

* TEST04-B
* TEST01
* TEST05
