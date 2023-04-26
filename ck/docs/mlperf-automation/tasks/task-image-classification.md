**[ [TOC](../README.md) ]**

# MLPerf&trade; Inference v1.0: image classification

## Official models

| model | reference app | framework | dataset |
| ---- | ---- | ---- | ---- |
| resnet50-v1.5 | [vision/classification_and_detection](https://github.com/mlperf/inference/tree/r1.0/vision/classification_and_detection) | tensorflow, pytorch, onnx | imagenet2012 [[**CK automation**](../datasets/imagenet2012.md)] |

## All supported models

| model | framework | accuracy | dataset | model link | model source | precision | notes | CK dataset | CK model | CK model package tags |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| resnet50-v1.5 | tensorflow | 76.456% | imagenet2012 validation | [from zenodo](https://zenodo.org/record/2535873/files/resnet50_v1.pb) | [mlperf](https://github.com/mlperf/training/tree/master/image_classification), [tensorflow](https://github.com/tensorflow/models/tree/master/official/resnet) | fp32 | NHWC. More information on resnet50 v1.5 can be found [here](https://github.com/tensorflow/models/tree/master/official/resnet).||   |   |   |
| resnet50-v1.5 | onnx | 76.456% | imagenet2012 validation | from zenodo: [opset-8](https://zenodo.org/record/2592612/files/resnet50_v1.onnx), [opset-11](https://zenodo.org/record/4735647/files/resnet50_v1.onnx) | [from zenodo](https://zenodo.org/record/2535873/files/resnet50_v1.pb) converted with [this script](https://github.com/mlcommons/inference/blob/master/vision/classification_and_detection/tools/convert-to-onnx.sh) | fp32 | NCHW, tested on pytorch and onnxruntime |   | [link](https://github.com/mlcommons/ck-mlops/tree/main/package/ml-model-mlperf-resnet50-v1.5-onnx)  | *model,image-classification,mlperf,onnx,resnet50*  |
| resnet50-v1.5 | pytorch | 76.014% | imagenet2012 validation | [from zenodo](https://zenodo.org/record/4588417/files/resnet50-19c8e357.pth) | [from TorchVision](https://github.com/pytorch/vision/blob/v0.8.2/torchvision/models/resnet.py) | fp32 | NCHW |   |   |   | 
| resnet50-v1.5 | pytorch | 75.790% | imagenet2012 validation | [from zenodo](https://zenodo.org/record/4589637/files/resnet50_INT8bit_quantized.pt) | Edgecortix [quantization script](https://github.com/mlcommons/inference/blob/master/vision/classification_and_detection/tools/calibrate_torchvision_model.py) | A: int8, W: uint8 | NCHW |   |   |   |



## Common CK setup

```
python3 -m pip install ck
```

We suggest you to create a virtual CK environment using MLPerf&trade; inference v1.1 template 
(with the TVM backend from OctoML) as follows:

```
ck pull repo:mlcommons@ck-venv

ck create venv:mlperf-inference --template=mlperf-inference-1.1-tvm

ck activate venv:mlperf-inference
```

Note that you need Python 3.6+ for the MLPerf inference benchmark.

Alternatively, use the following commands if you want to use your native environment:

```
ck pull repo:mlcommons@ck-mlops

ck setup kernel --var.install_to_env=yes

ck detect platform.os --platform_init_uoa=generic-linux-dummy

ck detect soft:compiler.python --full_path=${CK_VENV_PYTHON_BIN}
ck detect soft:compiler.gcc --full_path=`which gcc`

ck install package --quiet --tags=tool,cmake,src

ck install package --quiet --tags=mlperf,inference,src,r1.1-tvm

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

## CK setup for the ImageNet 2012 dataset

You can install a reduced ImageNet 2012 data set with the first 500 images to test MLPerf&trade; workflows as follows :

```
ck install package --tags=imagenet,2012,val,min,non-resized
ck install package --tags=imagenet,2012,aux,from.berkeley
```

Feel free to check the [CK JSON meta](https://github.com/mlcommons/ck-mlops/blob/main/package/imagenet-2012-val-min/.cm/meta.json)
and CK installation scripts for [Linux](https://github.com/mlcommons/ck-mlops/blob/main/package/imagenet-2012-val-min/install.sh) 
and [Windows](https://github.com/mlcommons/ck-mlops/blob/main/package/imagenet-2012-val-min/install.bat)
for the CK ImageNet val min package.

ImageNet 2012 validation set is no longer publicly available.
If you already have it installed on your machine, you can detect
and register it to work with CK workflows using this command:

```
ck detect soft:dataset.imagenet.val --force_version=2012 \
            --extra_tags=full --search_dir={directory where the dataset is installed}
```

You can also download it via [Academic Torrents](https://academictorrents.com/details/5d6d0df7ed81efd49ca99ea4737e0ae5e3a5f2e5)
and then register in the CK using the above command.

Please check [this doc](../datasets/imagenet2012.md) to see how you can preprocess the ImageNet 
in multiple ways with the help of CK.

Feel free to check the [CK JSON meta](https://github.com/mlcommons/ck-mlops/blob/main/soft/dataset.imagenet.val/.cm/meta.json)
and [CK Python customization script](https://github.com/mlcommons/ck-mlops/blob/main/soft/dataset.imagenet.val/customize.py)
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

#### Install ResNet50 v1.5 fp32 for ONNX opset-8

```
ck install package --tags=model,image-classification,mlperf,onnx,resnet50,v1.5-opset-8
```

Feel free to check [CK JSON meta](https://github.com/mlcommons/ck-mlops/blob/main/package/ml-model-mlperf-resnet50-v1.5-onnx/.cm/meta.json) of this package.

#### Install ResNet50 v1.5 fp32 for ONNX opset-11

```
ck install package --tags=model,image-classification,mlperf,onnx,resnet50,v1.5-opset-11
```

Feel free to check [CK JSON meta](https://github.com/mlcommons/ck-mlops/blob/main/package/ml-model-mlperf-resnet50-v1.5-onnx/.cm/meta.json) of this package.




#### Benchmark

First, check LOADGEN parameters for image classification [here](https://github.com/mlcommons/inference/tree/master/vision/classification_and_detection#usage).

```
ck run program:mlperf-inference-bench-image-classification-onnx-cpu --env.EXTRA_OPS="OPTIONS FOR LOADGEN"
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

You can test accuracy in Offline mode for 500 images as follows:
```
ck run program:mlperf-inference-bench-image-classification-onnx-cpu --cmd_key=accuracy-offline --env.EXTRA_OPS="--count 500"
```

You can test performance in SingleStream mode for 500 images as follows:
```
ck run program:mlperf-inference-bench-image-classification-onnx-cpu --cmd_key=performance-singlestream --env.EXTRA_OPS="--count 500 --time 60 --qps 200 --max-latency 0.1"
```

Feel free to check the [CK JSON meta](https://github.com/mlcommons/ck-mlops/blob/main/program/mlperf-inference-bench-image-classification-onnx-cpu/.cm/meta.json) 
and [CK dependencies](https://github.com/mlcommons/ck-mlops/blob/main/program/mlperf-inference-bench-image-classification-onnx-cpu/.cm/meta.json#L99) for this benchmark!

Note that you can obtain help about any CK module such as "program" and action such as "run" as follows:
```
ck run program --help
```

You can then customize your CMD using JSON keys as follows:
```
ck run program:my-program --key1=value1 --key2=value2
```

#### Record results to the CK repository

You can record results to the CK repository for further analysis (for example, using [CK dashboards](../results/ck-dashboard.md)) as follows:

```
ck benchmark program:mlperf-inference-bench-image-classification-onnx-cpu \
     --cmd_key=performance-singlestream \
     --env.EXTRA_OPS="--count 500 --time 60 --qps 200 --max-latency 0.1" \
     --repetitions=1 --skip_print_timers --skip_print_stats \
     --record \
     --record_repo=local \
     --record_uoa=mlperf-inference-bench-image-classification-onnx-cpu-resnet50-v1.5-result1 \
     --tags=mlperf-v1.0,inference,image-classification,onnx,resnet50-v1.5,cpu \
     --print_files=mlperf_log_summary.txt,results.json

```

Note that you can create a new CK repository to group your experimental results as follows:
```
ck add repo:my-cool-experiments --quiet
```
and then substitute 'local' with 'my-cool-experiments' in the above CMD to run the MLPerf&trade; benchmark.




### PyTorch-based models for CPU

Note: seems that PyTorch implementation in MLPerf inference v1.0 benchmark is not working with the latest ONNX

```
ck install package --tags=lib,python-package,onnx,1.8.1
ck install package --tags=lib,python-package,torch
```

#### Install ResNet50 v1.5 fp32 for ONNX opset-8

```
ck install package --tags=model,image-classification,mlperf,onnx,resnet50,v1.5-opset-8
```

#### Install ResNet50 v1.5 fp32 for ONNX opset-11

Note: ONNX opset-11 doesn't work with PyTorch in MLPerf inference v1.0




#### Benchmark

First, check LOADGEN parameters for image classification [here](https://github.com/mlcommons/inference/tree/master/vision/classification_and_detection#usage).

```
ck run program:mlperf-inference-bench-image-classification-pytorch-cpu --env.EXTRA_OPS="OPTIONS FOR LOADGEN"
```

You can test it as follows:
```
ck run program:mlperf-inference-bench-image-classification-pytorch-cpu --cmd_key=performance-singlestream --env.EXTRA_OPS="--count 500 --time 60 --qps 200 --max-latency 0.1"
```





## Analyze experimental results

You can find and check the CK entry with the results (based on [FAIR principles](https://www.go-fair.org/fair-principles/) 
to make sure that results are reproducible) as follows:
```
cd `ck find experiment --tags=mlperf-v1.0,inference,image-classification,onnx,resnet50-v1.5,cpu`
```
or 

```
cd `ck find experiment:mlperf-inference-bench-image-classification-onnx-cpu-resnet50-v1.5-result1`
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


## Integration with web services and CI platforms

All CK modules, automation actions and workflows are accessible as a micro-service with a unified JSON I/O API
to make it easier to integrate them with web services and CI platforms as described [here](../tools/continuous-integration.md).


# Questions and feedback

* Contact: grigori@octoml.ai
