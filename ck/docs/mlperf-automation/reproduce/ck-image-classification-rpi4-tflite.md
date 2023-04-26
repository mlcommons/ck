**[ [TOC](../README.md) ]**

***Reproduced by [Grigori Fursin](https://cKnowledge.org/gfursin) on 20210505***

* Platform: Raspberry Pi 4
* OS: Ubuntu 20.04 64-bit

# MLPerf&trade; Inference v1.0 - Image Classification - TFLite 2.4.1

## System packages

Install system packages for [RPi4 Ubuntu](../platform/rpi4-ubuntu.md).

## Install Collective Knowledge (CK) and Virtual Environment

Note that you need Python 3.7+! If you do not have it installed, don't worry - 
CK can rebuilt a required version when creating a virtual environment.

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

You will need cmake to build MLPerf&trade; loadgen. First, attempt to detect if you already have it installed:
```
ck detect soft --tags=tool,cmake
```

Note that you need version >= 3.16

CK will register your version if it manages to detect it:
```
ck show env

Env UID:         Target OS: Bits: Name: Version: Tags:

2aa2c857e2be84a4   linux-64    64 cmake 3.16.3   64bits,cmake,host-os-linux-64,target-os-linux-64,tool,v3,v3.16,v3.16.3
`````

If you do not have cmake installed or CK did not manage to detect it, you can use a CK package to build it for your system:
```
ck install package --tags=tool,cmake,src
```

You can now install other dependencies via CK:

```
ck install package --tags=lib,python-package,absl
ck install package --tags=lib,python-package,numpy
ck install package --tags=lib,python-package,matplotlib
ck install package --tags=lib,python-package,cython
ck install package --tags=lib,python-package,pillow
ck install package --tags=lib,python-package,opencv-python-headless

ck install package --tags=mlperf,inference,src,r1.0
ck install package --tags=lib,mlperf,loadgen,static
```

## Install (detect) full ImageNet 2012 val dataset with 50000 images

ImageNet 2012 validation set is no longer publicly available
and this CK meta-package cannot automatically download it!

If you already have it installed on your machine, you can detect
and register it to work with CK workflows using this command:

```
ck detect soft:dataset.imagenet.val --force_version=2012 \
            --extra_tags=full --search_dir={directory where the dataset is installed}
ck install package --tags=imagenet,2012,aux,from.berkeley
```

You can also download it via [Academic Torrents](https://academictorrents.com/details/5d6d0df7ed81efd49ca99ea4737e0ae5e3a5f2e5)
and then register in the CK using the above command.


### Preprocess using OpenCV (better accuracy but may fail on some machines)

```
time ck install package --dep_add_tags.dataset-source=full \
          --tags=dataset,imagenet,val,full,preprocessed,using-opencv,side.224 \
          --version=2012
```

Processing time: ~30 min.

### Preprocess using pillow (slightly worse accuracy but works most of the time)

```
time ck install package --dep_add_tags.dataset-source=full \
          --tags=dataset,imagenet,val,full,preprocessed,using-pillow,side.224 \
          --version=2012
```

Processing time: ~26 min.





## Install reduced ImageNet 2012 val dataset with the first 500 images

If you do not have the full ImagNet val dataset, you can install its reduced version via CK
with the first 500 images just for a test:
```
ck install package --tags=imagenet,2012,val,min,non-resized
ck install package --tags=imagenet,2012,aux,from.berkeley
```

### Preprocess using OpenCV (better accuracy but may fail on some machines)

```
time ck install package --dep_add_tags.dataset-source=min \
         --tags=dataset,imagenet,val,preprocessed,using-opencv,side.224,first.500 \
         --version=2012
```

### Preprocess using pillow (slightly worse accuracy but works most of the time)

```
time ck install package --dep_add_tags.dataset-source=min \
         --tags=dataset,imagenet,val,preprocessed,using-pillow,side.224,first.500 \
         --version=2012
```

## Install framework TFLite 2.4.1 with RUY

Note that TFLite will only use CPU on Nvidia Jetson cards

```
time ck install package --tags=lib,tflite,via-cmake,v2.4.1,with.ruy --env.CK_HOST_CPU_NUMBER_OF_PROCESSORS=2
```

Building time: ~15 min.



## Install model(s)

### ResNet-50 (no-argmax)

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
     --dep_add_tags.weights=resnet50 \
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
     --env.CK_LOADGEN_DATASET_SIZE=50000 \
     --dep_add_tags.weights=resnet50 \
     --dep_add_tags.images=preprocessed,using-opencv \
     --env.CK_LOADGEN_BUFFER_SIZE=1024 \
     --repetitions=1 \
     --skip_print_timers \
     --skip_print_stats \
     --print_files=accuracy.txt
```

### Accuracy: Offline (500 samples)

```
time ck benchmark program:image-classification-tflite-loadgen \
     --env.CK_LOADGEN_MODE=AccuracyOnly \
     --env.CK_LOADGEN_SCENARIO=Offline \
     --env.CK_LOADGEN_DATASET_SIZE=500 \
     --dep_add_tags.weights=resnet50 \
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
     --env.CK_LOADGEN_DATASET_SIZE=500 \
     --dep_add_tags.weights=resnet50 \
     --dep_add_tags.images=preprocessed,using-opencv \
     --env.CK_LOADGEN_TARGET_LATENCY=600 \
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
     --dep_add_tags.weights=resnet50 \
     --dep_add_tags.images=preprocessed,using-opencv \
     --env.CK_LOADGEN_MODE=PerformanceOnly \
     --env.CK_LOADGEN_SCENARIO=Offline \
     --env.CK_LOADGEN_TARGET_QPS=2 \
     --env.CK_LOADGEN_DATASET_SIZE=500 \
     --env.CK_LOADGEN_BUFFER_SIZE=1024 \
     --repetitions=1 \
     --skip_print_timers \
     --skip_print_stats \
     --print_files=mlperf_log_summary.txt,mlperf_log_detail.txt
```
