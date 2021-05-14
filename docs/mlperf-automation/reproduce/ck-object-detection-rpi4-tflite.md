***Reproduced by [Grigori Fursin](https://cKnowledge.io/@gfursin) on 20210428***

# MLPerf&trade; Inference v1.0 - Object Detection - TFLite

* Platform: RPi4
* OS: Ubuntu 20.04 64-but

## Prerequisites

### System packages

Install system packages for [RPi4 Ubuntu](../platform/rpi4-ubuntu.md).

### Install Collective Knowledge (CK)

Please follow the [installation instructions](https://github.com/ctuning/ck#installation) for your system e.g.:

```bash
$ python3 -m pip install ck --user
$ echo "export PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc
$ source ~/.bashrc && ck version
```

Note that you need GCC 9+!

### Pull [CK-ML repository](https://github.com/ctuning/ck-ml)

```bash
$ ck pull repo:octoml@mlops
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

## Setup for RPi4 CPU

### Install CK packages explicitly

~30 min to build

```
ck install package --tags=dataset,object-detection,preprocessed,full,side.300
ck install package --tags=model,tflite,object-detection,ssd-mobilenet,non-quantized

ck install package --tags=api,model,tensorflow,r2.3.0

ck install package --tags=lib,tflite,via-cmake,v2.4.1,with.ruy --env.CK_HOST_CPU_NUMBER_OF_PROCESSORS=2
```

### Run experiments

#### Performance

```
ck run cmdgen:benchmark.object-detection.tflite-loadgen --verbose \
   --library=tflite-v2.4.1-ruy \
   --model=non-quantized \
   --scenario=singlestream \
   --mode=performance \
   --target_latency=170 \
   --sut=rpi4coral

```

#### Accuracy
```
ck run cmdgen:benchmark.object-detection.tflite-loadgen --verbose \
   --library=tflite-v2.4.1-ruy \
   --model=non-quantized \
   --scenario=singlestream \
   --mode=accuracy \
   --dataset_size=5000 \
   --sut=rpi4coral

```

Sample result:
```
***************************************************************************************
Some statistics:

* Failed: no

* Binary size: 0
* Object size: 0

* Kernel repeat: 0

* Normalized time in sec. (min .. max): 0 .. 0

* Total time in us (min .. max): 0 .. 0

loading annotations into memory...
Done (t=2.39s)
creating index...
index created!
Loading and preparing results...
DONE (t=0.68s)
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=52.64s).
Accumulating evaluation results...
DONE (t=8.79s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.224
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.341
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.247
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.015
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.160
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.515
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.203
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.255
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.255
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.019
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.182
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.593
mAP=22.350%
==========================================================================================

```

#### Compliance

```
ck run cmdgen:benchmark.object-detection.tflite-loadgen --verbose \
   --library=tflite-v2.4.1-ruy \
   --model=non-quantized \
   --scenario=singlestream \
   --target_latency=170 \
   --compliance,=TEST04-A,TEST04-B,TEST01,TEST05 \
   --sut=rpi4coral

```

## Notes

* https://github.com/mlcommons/inference_results_v0.7/tree/master/closed/Dividiti/measurements/rpi4coral-tflite-v2.2.0-ruy/ssd-mobilenet-non-quantized/singlestream
* https://github.com/ctuning/ck-mlperf/blob/master/program/object-detection-tflite-loadgen/README.singlestream.md
* https://mlcommons.org/en/inference-edge-07/
* https://mlcommons.org/en/inference-edge-10/
* https://github.com/mlcommons/inference_results_v1.0/blob/master/open/Krai/measurements/rpi4coral-fan.on-tflite-v2.4.1-ruy/efficientnet-lite0-non-quantized/singlestream/README.md#mobilenet_v3


