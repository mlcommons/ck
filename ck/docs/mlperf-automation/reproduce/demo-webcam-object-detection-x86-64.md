**[ [TOC](../README.md) ]**

MLPerf&trade; webcam demo: live object detection with a webcam using MLPerf&trade; models

## Install Collective Knowledge (CK) and Virtual Environment

```
python3 -m pip install ck
ck pull repo:mlcommons@ck-venv
ck create venv:mlperf-webcam-demo
```

CK will attempt to detect existing python versions and will ask you which one to use for your virtual environment.
Note, that this solution was tested with Python 3.6 and may not work with other versions!

## Activate created virtual environment

```
ck activate venv:mlperf-webcam-demo
```

## Install cBench client

```bash
python -m pip install cbench
```

## Initialize demo solution

This is a prototype of [CK-based ML solutions](https://cknow.io/docs/intro/introduction.html#portable-ck-solution)
to simplify ML deployment.


```
cb init demo-webcam-mlperf-obj-detection-coco-tf-cpu-linux

```

It may take ~5..10 minutes to install and build all CK components for MLPerf&trade; object detection 
SSD MobileNet non-quantized model (trained on COCO) with TensorFlow.

## Run CK workflow with MLPerf&trade; model in the background

```
cb run demo-webcam-mlperf-obj-detection-coco-tf-cpu-linux &
```

## Start cb client


```
cb start

```


## Go the cKnowledge.io webpage with camera

https://cknow.io/c/solution/demo-webcam-mlperf-obj-detection-coco-tf-cpu-linux

Click on "Start webcam"

Click on "Start AI workflow". The browser will send a command to the cBench client
to start the MLPerf&trade; model, will continuosly push images to this model and will
display inference results.

