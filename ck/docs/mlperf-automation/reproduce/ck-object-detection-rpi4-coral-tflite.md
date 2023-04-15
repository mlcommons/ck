**[ [TOC](../README.md) ]**

***Reproduced by [Grigori Fursin](https://cKnowledge.org/gfursin) on 20210501***

# MLPerf&trade; Inference v1.0 - Object Detection - TFLite (with Coral EdgeTPU support)

* Platform: RPi4 with Coral EdgeTPU
* OS: Ubuntu 20.04 64-but

## Prerequisites

### System packages

Install system packages for [RPi4 Coral Ubuntu](../platform/rpi4-coral-ubuntu.md).

### Install Collective Knowledge (CK)

Please follow the [installation instructions](https://github.com/mlcommons/ck#installation) for your system e.g.:

```bash
$ python3 -m pip install ck --user
$ echo "export PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc
$ source ~/.bashrc && ck version
```

Note that you need GCC 9+!

## Pull [CK MLOps repository]( https://github.com/mlcommons/ck-mlops )

```bash
ck pull repo:mlcommons@ck-mlops
```

### Set up CK environment

```
ck detect platform.os --platform_init_uoa=generic-linux-dummy
ck detect soft:compiler.python --full_path=`which ${PYTHON_EXE}`

ck detect soft:compiler.gcc --full_path=`which gcc`
```

### Install common CK packages
```
ck install package --tags=tool,cmake

ck install package --tags=lib,python-package,absl
ck install package --tags=lib,python-package,numpy

ck install package --tags=mlperf,inference,src,r1.0
ck install package --tags=lib,mlperf,loadgen,static
```

### Install COCO 2017 val dataset (5000 images) and 

```
ck install package --tags=tool,coco,api
ck install package --tags=lib,python-package,cv2,opencv-python-headless
ck install package --ask --tags=dataset,coco,val,2017
```

## Setup for EdgeTPU (Host: RPi 4)

### Install CK packages explicitly

Note that this will install TFLite 1.15.4 and compatible models:

```
ck install package --tags=dataset,object-detection,preprocessed,full,side.300
ck install package --tags=model,ssd-mobilenet,nhwc,quantized,v1 
ck install package --tags=model,ssd-mobilenet,nhwc,quantized,v2

ck install package --tags=api,model,tensorflow,r1.13.0

ck install package --tags=lib,tflite,for.coral,threads.2

```

### Run experiments

Performance:

```
ck run cmdgen:benchmark.object-detection.tflite-loadgen --verbose \
   --library=tflite-edgetpu \
   --model:=v1:v2 \
   --scenario=singlestream \
   --mode=performance \
   --target_latency=20 \
   --sut=rpi4coral
```

Accuracy:

```
ck run cmdgen:benchmark.object-detection.tflite-loadgen --verbose \
   --library=tflite-edgetpu \
   --model:=v1:v2 \
   --scenario=singlestream \
   --mode=accuracy \
   --dataset_size=5000 \
   --sut=rpi4coral
```


## Notes

* https://github.com/mlcommons/inference_results_v0.7/tree/master/closed/Dividiti/measurements/rpi4coral-tflite-v2.2.0-ruy/ssd-mobilenet-non-quantized/singlestream
* https://mlcommons.org/en/inference-edge-07/
* https://mlcommons.org/en/inference-edge-10/
* https://github.com/mlcommons/inference_results_v1.0/blob/master/open/Krai/measurements/rpi4coral-fan.on-tflite-v2.4.1-ruy/efficientnet-lite0-non-quantized/singlestream/README.md#mobilenet_v3


