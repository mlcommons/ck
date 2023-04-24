**[ [TOC](../README.md) ]**

# MLPerf&trade; Inference v1.0: object detection

## Official models

| model | reference app | framework | dataset |
| ---- | ---- | ---- | ---- |
| ssd-mobilenet 300x300 | [vision/classification_and_detection](https://github.com/mlperf/inference/tree/r1.0/vision/classification_and_detection) | tensorflow, pytorch, onnx| coco resized to 300x300 [[**CK automation**](../datasets/coco2017.md)]| 
| ssd-resnet34 1200x1200 | [vision/classification_and_detection](https://github.com/mlperf/inference/tree/r1.0/vision/classification_and_detection) | tensorflow, pytorch, onnx | coco resized to 1200x1200 [[**CK automation**](../datasets/coco2017.md)] |

## All supported models

| model | framework | accuracy | dataset | model link | model source | precision | notes | CK dataset | CK model | CK model package tags |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| ssd-mobilenet 300x300 | tensorflow | mAP 0.23 | coco resized to 300x300 | [from tensorflow](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2018_01_28.tar.gz) | [from tensorflow](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2018_01_28.tar.gz) | fp32 | NHWC |   |   |   |
| ssd-mobilenet 300x300 quantized finetuned | tensorflow | mAP 0.23594 | coco resized to 300x300 | [from zenodo](https://zenodo.org/record/3252084/files/mobilenet_v1_ssd_8bit_finetuned.tar.gz) | Habana | int8 | ??? |   |   |   |
| ssd-mobilenet 300x300 symmetrically quantized finetuned | tensorflow | mAP 0.234 | coco resized to 300x300 | [from zenodo](https://zenodo.org/record/3401714/files/ssd_mobilenet_v1_quant_ft_no_zero_point_frozen_inference_graph.pb) | Habana | int8 | ??? |   |   |   |
| ssd-mobilenet 300x300 | pytorch | mAP 0.23 | coco resized to 300x300 | [from zenodo](https://zenodo.org/record/3239977/files/ssd_mobilenet_v1.pytorch) | [from tensorflow](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2018_01_28.tar.gz) | fp32 | NHWC |   |   |   |
| ssd-mobilenet 300x300 | onnx | mAP 0.23 | coco resized to 300x300 | from zenodo [opset-8](https://zenodo.org/record/3163026/files/ssd_mobilenet_v1_coco_2018_01_28.onnx), [opset-11](https://zenodo.org/record/4735652/files/ssd_mobilenet_v1_coco_2018_01_28.onnx) | [from tensorflow](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2018_01_28.tar.gz) converted using [this script](https://github.com/mlcommons/inference/blob/master/vision/classification_and_detection/tools/convert-to-onnx.sh) | fp32 | NHWC, tested on onnxruntime, some runtime warnings |   | [link](https://github.com/mlcommons/ck-mlops/tree/main/package/ml-model-mlperf-ssd-mobilenet-300-onnx) | *model,object-detection,mlperf,onnx,ssd-mobilenet,side.300,non-quantized*  |
| ssd-mobilenet 300x300 | onnx, pytorch | mAP 0.23 | coco resized to 300x300  | [from zenodo](https://zenodo.org/record/3252084/files/mobilenet_v1_ssd_8bit_finetuned.tar.gz) | ??? | int8 | ??? |   |   |   |
| ssd-resnet34 1200x1200 | tensorflow | mAP 0.20 | coco resized to 1200x1200| [from zenodo](https://zenodo.org/record/3345892/files/tf_ssd_resnet34_22.1.zip?download=1) | [from mlperf](https://github.com/mlperf/inference/tree/master/others/cloud/single_stage_detector/tensorflow), [training model](https://github.com/lji72/inference/tree/tf_ssd_resent34_align_onnx/others/cloud/single_stage_detector/tensorflow) | fp32 | NCHW |   |   |   |
| ssd-resnet34 1200x1200 | pytorch | mAP 0.20 | coco resized to 1200x1200 | [from zenodo](https://zenodo.org/record/3236545/files/resnet34-ssd1200.pytorch) | [from mlperf](https://github.com/mlperf/inference/tree/master/others/cloud/single_stage_detector/pytorch) | fp32 | NCHW |   |   |   |
| ssd-resnet34 1200x1200 | onnx | mAP 0.20 | coco resized to 1200x1200 | from zenodo [opset-8](https://zenodo.org/record/3228411/files/resnet34-ssd1200.onnx) | [from mlperf](https://github.com/mlperf/inference/tree/master/others/cloud/single_stage_detector) converted using the these [instructions](https://github.com/BowenBao/inference/tree/master/cloud/single_stage_detector/pytorch#6-onnx) | fp32 | Converted from pytorch model. |   | [link](https://github.com/mlcommons/ck-mlops/tree/main/package/ml-model-mlperf-ssd-resnet34-1200-onnx)  | *model,object-detection,mlperf,onnx,ssd-resnet34,side.1200,non-quantized,opset-8*  |
| ssd-resnet34 1200x1200 | onnx | mAP 0.20 | coco resized to 1200x1200 | from zenodo [opset-11](https://zenodo.org/record/4735664/files/ssd_resnet34_mAP_20.2.onnx) | [from zenodo](https://zenodo.org/record/3345892/files/tf_ssd_resnet34_22.1.zip) converted using [this script](https://github.com/mlcommons/inference/blob/master/vision/classification_and_detection/tools/convert-to-onnx.sh) | fp32 | Converted from the tensorflow model and uses the same interface as the tensorflow model. |   |   |   |

## Common CK setup

```
python3 -m pip install ck
```

We suggest you to create a virtual CK environment using MLPerf&trade; inference dev template as follows:

```
ck pull repo:mlcommons@ck-venv

ck create venv:mlperf-inference --template=mlperf-inference-dev

ck activate venv:mlperf-inference
```

Alternatively, use the following commands if you want to use your native environment:

```
ck pull repo:mlcommons@ck-mlops

ck setup kernel --var.install_to_env=yes

ck detect platform.os --platform_init_uoa=generic-linux-dummy

ck detect soft:compiler.python --full_path=${CK_VENV_PYTHON_BIN}
ck detect soft:compiler.gcc --full_path=`which gcc`

ck install package --quiet --tags=tool,cmake,src

ck install package --quiet --tags=mlperf,inference,src,dev

ck install package --tags=lib,python-package,absl
ck install package --tags=lib,python-package,numpy

ck install package --tags=lib,python-package,mlperf,loadgen

ck install package --tags=lib,python-package,matplotlib
ck install package --tags=lib,python-package,cython
ck install package --tags=lib,python-package,opencv-python-headless
ck install package --tags=tool,coco,api

ck show env

```

You can explore available packages in the [CK GitHub repo](https://github.com/mlcommons/ck-mlops/tree/main/package)
or using the [cKnowledge.io platform](https://cknow.io/c/package).

## Pull CK repo with the latest MLPerf&trade; automations from OctoML:
```
ck pull repo:mlcommons@ck-mlops
```

CK will pull and install GitHub repository from https://github.com/mlcommons/ck-mlops.
Note that you can pull any Git repository in the CK format as follows:
```
ck pull repo --url={URL}
```

## CK setup for the COCO 2017 val dataset (5000 images) converted to 300x300


You can install COCO 2017 val dataset as follows:

```
ck install package --tags=dataset,coco,val,2017,full
```

Feel free to check the [CK JSON meta](https://github.com/mlcommons/ck-mlops/tree/main/package/dataset-coco-2017-val/.cm/meta.json)
and CK installation scripts for [Linux](https://github.com/mlcommons/ck-mlops/tree/main/package/dataset-coco-2017-val/install.sh) 
and [Windows](https://github.com/mlcommons/ck-mlops/tree/main/package/dataset-coco-2017-val/install.bat)
for the CK COCO2017 val dataset package.

Please check [this doc](../datasets/coco2017.md) to see how you can preprocess this data set 
in multiple ways with the help of CK.

Feel free to check the [CK JSON meta](https://github.com/mlcommons/ck-mlops/tree/main/soft/dataset.coco.2017.val/.cm/meta.json)
and [CK Python customization script](https://github.com/mlcommons/ck-mlops/tree/main/soft/dataset.coco.2017.val/customize.py)
to detect this data set on your machine.

You can see other software detection plugins in the [CK repository](https://github.com/mlcommons/ck-mlops/tree/main/soft)
or using the [cKnowledge.io platform](https://cknow.io/c/soft).




## CK setup for different models and hardware

### ONNX-based models for CPU

```
ck install package --tags=lib,python-package,onnxruntime-cpu
```

You will be asked to select a specfic version or the latest one. You can install a specific version as follows:
```
ck install package --tags=lib,python-package,onnxruntime-cpu,1.6.0
```

#### Install SSD-Mobilenet 300x300 non-quantized fp32 for ONNX opset-8

```
ck install package --tags=model,object-detection,mlperf,onnx,ssd-mobilenet,side.300,non-quantized,opset-8
```

Feel free to check [CK JSON meta](https://github.com/mlcommons/ck-mlops/blob/main/package/ml-model-mlperf-ssd-mobilenet-300-onnx/.cm/meta.json) of this package.

#### Install SSD-Mobilenet 300x300 non-quantized fp32 for ONNX opset-11

```
ck install package --tags=model,object-detection,mlperf,onnx,ssd-mobilenet,side.300,non-quantized,opset-11
```

#### Install SSD-ResNet34 1200x1200 non-quantized fp32 for ONNX opset-8

```
ck install package --tags=model,object-detection,mlperf,onnx,ssd-resnet34,side.1200,non-quantized,opset-8
```



### Benchmark

First, check LOADGEN parameters for object detection [here](https://github.com/mlcommons/inference/tree/master/vision/classification_and_detection#usage).

```
ck run program:mlperf-inference-bench-object-detection-onnx-cpu --env.EXTRA_OPS="OPTIONS FOR LOADGEN"
```

CK will ask you to select a command line from:
```
More than one commmand line is found to run this program:

0) Accuracy-MultiStream (../run_local$#script_ext#$)
1) Accuracy-Offline (../run_local$#script_ext#$)
2) Accuracy-Server (../run_local$#script_ext#$)
3) Accuracy-SingleStream (../run_local$#script_ext#$)
4) Performance-MultiStream (../run_local$#script_ext#$)
5) Performance-Offline (../run_local$#script_ext#$)
6) Performance-Server (../run_local$#script_ext#$)
7) Performance-SingleStream (../run_local$#script_ext#$)

```

You can test accuracy in Offline mode while limiting time as follows:
```
ck run program:mlperf-inference-bench-object-detection-onnx-cpu --cmd_key=accuracy-offline --env.EXTRA_OPS="--time 60"
```

You can test performance in SingleStream mode while limiting time as follows:
```
ck run program:mlperf-inference-bench-object-detection-onnx-cpu --cmd_key=performance-singlestream --env.EXTRA_OPS="--time 60 --qps 200 --max-latency 0.1"
```

Feel free to check the [CK JSON meta](https://github.com/mlcommons/ck-mlops/blob/main/program/mlperf-inference-bench-object-detection-onnx-cpu/.cm/meta.json) 
and [CK dependencies](https://github.com/mlcommons/ck-mlops/blob/main/program/mlperf-inference-bench-object-detection-onnx-cpu/.cm/meta.json#L99) for this benchmark!

Note that you can obtain help about any CK module such as "program" and action such as "run" as follows:
```
ck run program --help
```

You can then customize your CMD using JSON keys as follows:
```
ck run program:my-program --key1=value1 --key2=value2
```

### Record benchmarking results to the CK repository

You can record results to the CK repository for further analysis (for example, using [CK dashboards](../results/ck-dashboard.md)) as follows:

```
ck benchmark program:mlperf-inference-bench-object-detection-onnx-cpu \
     --cmd_key=performance-singlestream \
     --env.EXTRA_OPS="--time 60 --qps 200 --max-latency 0.1" \
     --repetitions=1 --skip_print_timers --skip_print_stats \
     --record \
     --record_repo=local \
     --record_uoa=mlperf-inference-bench-object-detection-onnx-cpu-ssd-mobilenet-result1 \
     --tags=mlperf-v1.0,inference,object-detection,onnx,ssd-mobilenet,cpu \
     --print_files=mlperf_log_summary.txt,results.json

```

Note that you can create a new CK repository to group your experimental results as follows:
```
ck add repo:my-cool-experiments --quiet
```
and then substitute 'local' with 'my-cool-experiments' in the above CMD to run MLPerf&trade; benchmark.

## Analyze experimental results

You can find and check the CK entry with the results (based on [FAIR principles](https://www.go-fair.org/fair-principles/) 
to make sure that results are reproducible) as follows:
```
cd `ck find experiment --tags=mlperf-v1.0,inference,object-detection,onnx,ssd-mobilenet,cpu`
```
or 

```
cd `ck find experiment:mlperf-inference-bench-object-detection-onnx-cpu-ssd-mobilenet-result1`
```

You can see different experiments inside as follows:
```
ls -l
```

Note that you can process, analyze and visualize such CK results from multiple experiments using Python scripts, CK modules and Jupyter notebooks
as shown in this [Jupyter notebook example](https://nbviewer.jupyter.org/urls/dl.dropbox.com/s/f28u9epifr0nn09/ck-dse-demo-object-detection.ipynb) 
and [CK dashboard](https://cknow.io/result/crowd-benchmarking-mlperf-inference-classification-mobilenets-all/).



## Share experimental results

You can share experimental results publicly with the community or privately between different workgroups 
in the CK repositories or pack them to ZIP files:

```
ck zip experiment:*
```

This command will create ckr.zip with all CK experiment entries that you can share with your colleagues.
They can unzip this file into CK local repository as follows:
```
ck unzip repo
```

You can also pack and share the whole CK repository as follows:
```
ck zip repo:my-cool-experiments
```


## Delete unused virtual environments

You can delete an unused virtual CK environment as follows:
```
ck rm venv:mlperf-inference
```

You can delete all virtual CK environments as follows:
```
ck rm venv:*
```

## Use a Docker container

It is possible to automatically generate containers with the CK workflows inside 
while keeping the same CK interface across different projects. 

We've prepared a Docker container with pre-installed MLPerf&trade; inference benchmark v1.0 
with object detection that you can use interactively to benchmark models 
and record results in your local repository for further analysis.

Feel free to check the [CK entry](https://github.com/mlcommons/ck-mlops/tree/main/docker/ck-mlperf-inference-v1.0-object-detection-native) 
with this container. You can also check [adaptive CK containers shared by OctoML](https://github.com/mlcommons/ck-mlops/tree/main/docker)
and other [CK containers shared by the community](https://github.com/mlcommons/ck-mlops/tree/main/docker).


First, build a given Docker container using CK as follows:

```
ck build docker:ck-mlperf-inference-v1.0-object-detection-native --tag=ubuntu-20.04
```

Then, create a local CK repository where you would like to record benchmarking results:
```
ck add repo:ck-experiments --quiet
```

**Linux:** Start Docker while mounting CK repository with experiments:

```
export CK_HOST_REPO_EXPERIMENTS=`ck where repo:ck-experiments`

echo ${CK_HOST_REPO_EXPERIMENTS}

docker run --volume ${CK_HOST_REPO_EXPERIMENTS}:/home/ckuser/ck-experiments -it mlcommons/ck-mlperf-inference-v1.0-object-detection-native:ubuntu-20.04
```

Use this ugly hack to be able to record to your host CK repository:
```
sudo chmod -R 777 ck-experiments
ck add repo:ck-experiments --path=/home/ckuser/ck-experiments --quiet
```

Then try to run some experiments and record results:
```
ck benchmark program:mlperf-inference-bench-object-detection-onnx-cpu \
     --cmd_key=performance-singlestream \
     --env.EXTRA_OPS="--time 60 --qps 200 --max-latency 0.1" \
     --repetitions=1 --skip_print_timers --skip_print_stats \
     --record \
     --record_repo=ck-experiments \
     --record_uoa=mlperf-inference-bench-object-detection-onnx-cpu-ssd-mobilenet-result1 \
     --tags=mlperf-v1.0,inference,object-detection,onnx,ssd-mobilenet,cpu \
     --print_files=mlperf_log_summary.txt,results.json

```

After exiting this Docker container, you can see results in your local ck-experiment repo:
```
exit
ck ls ck-experiment:experiment:*
```


## Integration with web services and CI platforms

All CK modules, automation actions and workflows are accessible as a micro-service with a unified JSON I/O API
to make it easier to integrate them with web services and CI platforms as described [here](../tools/continuous-integration.md).




# Questions and feedback

* Contact: grigori@octoml.ai
