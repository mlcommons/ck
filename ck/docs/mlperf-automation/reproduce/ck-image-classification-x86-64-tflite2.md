**[ [TOC](../README.md) ]**

***Reproduced by [Grigori Fursin](https://cKnowledge.org/gfursin) on 20210808***

* Platform: x8664
* OS: Ubuntu 18.04 64-bit
* Python 3.7.10

# MLPerf&trade; Inference v1.0 - Image Classification - TFLite 2.5.0 RUY (x86)

## System packages

Install system packages for [x86](../platform/amd-milan.md).

## Install Collective Knowledge (CK) and Virtual Environment

Note that you need Python 3.7+! If you do not have it installed, don't worry - 
CK can rebuilt a required version when creating a virtual environment.

```bash
python3 -m pip install ck -U
ck pull repo:mlcommons@ck-venv
ck create venv:mlperf-tflite --template=mlperf-inference-1.1
```
CK will attempt to detect existing python versions and will ask you which one to use for your virtual environment.

## Activate created virtual environment

```bash
ck activate venv:mlperf-tflite
```

## Pull [CK MLOps repository]( https://github.com/mlcommons/ck-mlops )

```bash
ck pull repo:mlcommons@ck-mlops
```

## Build static LoadGen 

You can now install other dependencies via CK:

```bash
ck install package --tags=lib,mlperf,loadgen,static
```

## Install ImageNet 2012 aux files

```bash
ck install package --tags=imagenet,2012,aux
```

## Plug full ImageNet 2012 val dataset with 50000 images into CK

ImageNet 2012 validation set is no longer publicly available
and this CK meta-package cannot automatically download it!

If you already have it installed on your machine, you can detect
and register it to work with CK workflows using this command:

```
ck detect soft:dataset.imagenet.val --force_version=2012 \
            --extra_tags=full --search_dir={directory where the dataset is installed}
```

You can also download it via [Academic Torrents](https://academictorrents.com/details/5d6d0df7ed81efd49ca99ea4737e0ae5e3a5f2e5)
and then register in the CK using the above command.


### Preprocess using OpenCV (better accuracy but may fail on some machines)

```
time ck install package --dep_add_tags.dataset-source=full \
          --tags=dataset,imagenet,val,full,preprocessed,using-opencv,side.224 \
          --version=2012
```

Processing time: ~6 min.



## Optional: install reduced ImageNet 2012 val dataset with the first 500 images

If you do not have the full ImagNet val dataset, you can install its reduced version via CK
with the first 500 images just for a test:
```
ck install package --tags=imagenet,2012,val,min,non-resized
ck install package --tags=imagenet,2012,aux,from.berkeley
```

You can now preprocess it using OpenCV (better accuracy but may fail on some machines)

```
time ck install package --dep_add_tags.dataset-source=min \
         --tags=dataset,imagenet,val,preprocessed,using-opencv,side.224,first.500 \
         --version=2012
```

## Build TFLite 2.5.0 with RUY via CK

Note that TFLite will only use CPU on Nvidia Jetson cards

```
time ck install package --tags=lib,tflite,via-cmake,v2.5.0,with.ruy --j=2
```



## Install model: ResNet-50 (no-argmax)

Install ResNet model via CK:
```
ck install package --tags=model,tflite,resnet50,no-argmax
```

Test that it works with the installed TFLite version:

```
time ck benchmark program:image-classification-tflite \
      --speed --repetitions=1 --skip_print_timers \
      --dep_add_tags.images=preprocessed,using-opencv \
      --dep_add_tags.weights=resnet \
      --env.CK_BATCH_SIZE=1 --env.CK_BATCH_COUNT=10 \
      --skip_print_stats

```

## Run MLPerf&trade; benchmark

### Accuracy: Single Stream (50 samples)

```
time ck benchmark program:image-classification-tflite-loadgen \
     --env.CK_LOADGEN_MODE=AccuracyOnly \
     --env.CK_LOADGEN_SCENARIO=SingleStream \
     --env.CK_LOADGEN_DATASET_SIZE=50 \
     --dep_add_tags.images=preprocessed,using-opencv \
     --env.CK_LOADGEN_BUFFER_SIZE=1024 \
     --repetitions=1 \
     --skip_print_timers \
     --skip_print_stats \
     --print_files=accuracy.txt
```

### Accuracy: Single Stream (50000 samples)

```
time ck benchmark program:image-classification-tflite-loadgen \
     --env.CK_LOADGEN_MODE=AccuracyOnly \
     --env.CK_LOADGEN_SCENARIO=SingleStream \
     --env.CK_LOADGEN_DATASET_SIZE=100 \
     --dep_add_tags.images=preprocessed,using-opencv \
     --env.CK_LOADGEN_BUFFER_SIZE=1024 \
     --repetitions=1 \
     --skip_print_timers \
     --skip_print_stats \
     --print_files=accuracy.txt
```

It took around 95 minutes to complete this test on AMD Milan.

```
accuracy=76.442%, good=38221, total=50000
```

### Accuracy: Offline (500 samples)

```
time ck benchmark program:image-classification-tflite-loadgen \
     --env.CK_LOADGEN_MODE=AccuracyOnly \
     --env.CK_LOADGEN_SCENARIO=Offline \
     --env.CK_LOADGEN_DATASET_SIZE=500 \
     --dep_add_tags.images=preprocessed,using-opencv \
     --env.CK_LOADGEN_BUFFER_SIZE=1024 \
     --repetitions=1 \
     --skip_print_timers \
     --skip_print_stats \
     --print_files=accuracy.txt
```

### Performance: Single Stream (500 samples)

**A note from the community:**
A valid SingleStream performance run [must reach](https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc#3-scenarios) 
a) the minimum duration of 60 seconds (NB: increased to 600 seconds for v1.0), and 
b) the minimum of 1,024 queries. Increasing the expected SingleStream target latency
in user.conf from 10 milliseconds to above ~60 milliseconds decreases the
number of queries that LoadGen issues from 6,000 (actually, 12,000
to account for variability) to 1,024. Note that it does not matter whether
the expected latency is, say, 100 ms or 1000 ms, as long as it is above ~60 ms.

```
time ck benchmark program:image-classification-tflite-loadgen \
     --env.CK_LOADGEN_MODE=PerformanceOnly \
     --env.CK_LOADGEN_SCENARIO=SingleStream \
     --env.CK_LOADGEN_DATASET_SIZE=100 \
     --dep_add_tags.images=preprocessed,using-opencv \
     --env.CK_LOADGEN_TARGET_LATENCY=45 \
     --env.CK_LOADGEN_BUFFER_SIZE=1024 \
     --repetitions=1 \
     --skip_print_timers \
     --skip_print_stats \
     --print_files=mlperf_log_summary.txt
```

### Performance: Offline (500 samples)

**A note from the community:**
A valid Offline performance run [must reach](https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc#3-scenarios) 
the minimum duration of 60 seconds (NB: increased to 600 seconds for v1.0), and b) the minimum of 24,576 samples.

```
time ck benchmark program:image-classification-tflite-loadgen \
     --env.CK_LOADGEN_MODE=PerformanceOnly \
     --env.CK_LOADGEN_SCENARIO=Offline \
     --dep_add_tags.images=preprocessed,using-opencv \
     --env.CK_LOADGEN_TARGET_QPS=8 \
     --env.CK_LOADGEN_DATASET_SIZE=500 \
     --env.CK_LOADGEN_BUFFER_SIZE=1024 \
     --repetitions=1 \
     --skip_print_timers \
     --skip_print_stats \
     --print_files=mlperf_log_summary.txt,mlperf_log_detail.txt
```

## Check C++ LoadGen front-ends
* [TFLite](https://github.com/mlcommons/ck-mlops/blob/main/program/image-classification-tflite-loadgen/classification.cpp) *synchronous*
* [QAIC](https://github.com/cknowledge/ck-qaic/blob/main/program/image-classification-qaic-loadgen/harness.cpp#L219) *parallel*

## Check other models

See [CK-ML repo docs](https://github.com/mlcommons/ck-ml/blob/main/program/image-classification-tflite-loadgen/README.md)

You can list available CK MLPerf&trade; model packages as follows:
```
ck ls ck-ml:package:model-*mlperf* | sort
```

For example, install MobileNet v3 Large 224 1.0 Float:

```
ck install package --tags=model,image-classification,tflite,nhwc,mobilenet-v3,v3-large_224_1.0_uint8
```

You can then run above commands without changes!
