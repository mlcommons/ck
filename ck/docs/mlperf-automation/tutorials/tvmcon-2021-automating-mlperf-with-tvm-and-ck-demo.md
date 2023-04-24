# Reproducibility report: system setup

**Tags:** MLPerf inference v1.1; Image Classification; Resnet50; TVM; AWS m5zn.6xlarge; X64; datacenter; open division

## Install system dependencies

* https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/platform/x8664-ubuntu.md

## Check python version (3.7+)

```bash
python3 --version

> 3.7.10
```

## Install [CK automation framework](https://github.com/mlcommons/ck)

Tested with the version 2.5.8

```bash
python3 -m pip install ck -U
```

*You may need to restart your bash to initialize PATH to CK scripts.*

## Install CK repository with ML/MLPerf automations 

```bash
ck pull repo:mlcommons@ck-mlops
ck where repo:mlcommons@ck-mlops

```

## Prepare environment

```bash
ck setup kernel --var.install_to_env=yes

ck detect platform.os --platform_init_uoa=generic-linux-dummy

ck detect soft:compiler.python

ck detect soft:compiler.gcc --full_path=`which gcc`

ck detect soft:tool.cmake

ck show env


python3 -m pip install protobuf

ck install package --quiet --tags=mlperf,inference,src,r1.1-tvm-seed

ck install package --tags=lib,python-package,absl

ck install package --tags=lib,python-package,numpy

ck install package --tags=lib,python-package,scipy

ck install package --tags=lib,python-package,matplotlib

ck install package --tags=lib,python-package,cython

ck install package --tags=lib,python-package,opencv-python-headless

ck install package --tags=lib,python-package,mlperf,loadgen

ck install package --tags=tool,coco,api

ck show env

```

## Install CK components

```bash
ck install package --tags=lib,python-package,onnxruntime-cpu,1.8.1
ck install package --tags=lib,python-package,onnx,1.10.1

ck install package --tags=lib,python-package,pytorch,cpu,1.9.0
ck install package --tags=lib,python-package,torchvision,cpu,0.10.0

ck install package --tags=tool,cmake,prebuilt,v3.21.1
ck install package --tags=compiler,llvm,prebuilt,v12.0.0

ck install package --tags=lib,dnnl,v2.2.4 --dep_add_tags.compiler=llvm

ck install package --tags=compiler,tvm,src,dev-0.8-dnnl-int8-v2-mlperf-1.1 \
      --env.USE_DNNL_CODEGEN=ON --env.USE_OPENMP=gnu --j=16 --quiet
```

## Prepare image classification task

```bash
ck install package --tags=imagenet,2012,aux
```

### Plug local ImageNet into CK

Note that the ImageNet validation dataset is not available for public download. 
Please follow these [instructions](https://github.com/mlcommons/ck/blob/master/docs/mlperf-automation/datasets/imagenet2012.md) to obtain it.

Find the path with the ImageNet validation set (50,000 images) and plug it into CK as follows:

```bash
ck detect soft:dataset.imagenet.val --force_version=2012 --extra_tags=full \
      --search_dir={directory where the ImageNet val dataset is downloaded}
```

### Use reduced ImageNet to test the MLPerf workflow

```bash
ck install package --tags=imagenet,2012,val,min,non-resized
```




## Install PyTorch model (Resnet50; int8; quantized)

Install MLPerf model:

```bash
ck install package --tags=model,image-classification,mlperf,pytorch,v1.5-int8-quantized
```

More information about this model: 
[ [CK meta.json](https://github.com/mlcommons/ck-mlops/blob/main/package/ml-model-mlperf-resnet50-pytorch/.cm/meta.json) ]

### See all installed packages and detected components

```bash
ck show env
ck show env --tags=tvm
ck show env --tags=mlcommons,src
ck locate env --tags=tvm
```

## Install CK workflow Python dependencies

```bash
ck run program:mlperf-inference-bench-image-classification-tvm-pytorch-cpu \
     --cmd_key=install-python-requirements
```

## Run Offline scenario

### Accuracy

```bash
time ck benchmark program:mlperf-inference-bench-image-classification-tvm-pytorch-cpu \
     --repetitions=1 --skip_print_timers --skip_print_stats --skip_stat_analysis \
     --cmd_key=accuracy-offline \
     --env.MLPERF_BACKEND=tvm2 \
     --env.MLPERF_TVM_EXECUTOR=graph \
     --env.MLPERF_TVM_TARGET="llvm -mcpu=cascadelake" \
     --env.MLPERF_TVM_USE_DNNL=YES \
     --env.TVM_BATCH_SIZE=1 \
     --env.TVM_BIND_THREADS=0 \
     --env.OMP_NUM_THREADS=1 \
     --env.TVM_NUM_THREADS=1 \
     --env.EXTRA_OPS="" \
     --print_files=accuracy.txt
```

### Performance

```bash

time ck benchmark program:mlperf-inference-bench-image-classification-tvm-pytorch-cpu \
     --repetitions=1 --skip_print_timers --skip_print_stats --skip_stat_analysis \
     --cmd_key=performance-offline \
     --env.MLPERF_BACKEND=tvm2 \
     --env.MLPERF_TVM_EXECUTOR=graph \
     --env.MLPERF_TVM_TARGET="llvm -mcpu=cascadelake" \
     --env.MLPERF_TVM_USE_DNNL=YES \
     --env.TVM_BATCH_SIZE=1 \
     --env.TVM_BIND_THREADS=0 \
     --env.OMP_NUM_THREADS=1 \
     --env.TVM_NUM_THREADS=1 \
     --env.EXTRA_OPS="--qps 900 --time 610" \
     --print_files=mlperf_log_summary.txt

```


*Add --no_clean flag to avoid recompiling TVM model*





## Prepare your submission

One can use the [end-to-end MLPerf submission and visualization workflow](https://github.com/mlcommons/ck-mlops/tree/main/module/bench.mlperf.inference)
(collaboration between MLCommons, OctoML and the cTuning foundation) to prepare the above submission as follows:

```bash
ck pull repo:ck-mlperf-inference

ck install package --tags=mlperf,inference,results,dummy

ck set kernel --var.mlperf_inference_version=1.1
ck set kernel --var.mlperf_inference_submitter=OctoML
ck set kernel --var.mlperf_inference_division=open

ck add bench.mlperf.system:aws-m5zn.6xlarge-tvm --base=1-node-2s-clx-tf-int8
ck set kernel --var.mlperf_inference_system=aws-m5zn.6xlarge-tvm

ck run bench.mlperf.inference  --framework=tvm-pytorch --model=resnet50 --scenario=offline --mode=prereq

ck run bench.mlperf.inference  --framework=tvm-pytorch --model=resnet50 --scenario=offline --mode=accuracy \
     --skip_system_ext \
     --env.MLPERF_BACKEND=tvm2 \
     --env.MLPERF_TVM_EXECUTOR=graph \
     --env.MLPERF_TVM_TARGET="llvm -mcpu=cascadelake" \
     --env.MLPERF_TVM_USE_DNNL=YES \
     --env.TVM_BATCH_SIZE=1 \
     --env.TVM_BIND_THREADS=0 \
     --env.OMP_NUM_THREADS=1 \
     --env.TVM_NUM_THREADS=1 \
     --env.EXTRA_OPS=""

ck run bench.mlperf.inference  --framework=tvm-pytorch --model=resnet50 --scenario=offline --mode=performance \
     --clean \
     --skip_system_ext \
     --env.MLPERF_BACKEND=tvm2 \
     --env.MLPERF_TVM_EXECUTOR=graph \
     --env.MLPERF_TVM_TARGET="llvm -mcpu=cascadelake" \
     --env.MLPERF_TVM_USE_DNNL=YES \
     --env.TVM_BATCH_SIZE=1 \
     --env.TVM_BIND_THREADS=0 \
     --env.OMP_NUM_THREADS=1 \
     --env.TVM_NUM_THREADS=1 \
     --env.EXTRA_OPS="--qps 900 --time 610"
```

You should truncate your accuracy files before submitting results:
```bash
ck run program:mlperf-inference-submission --cmd_key=truncate_accuracy_log --env.CK_MLPERF_SUBMITTER=OctoML
```

Check the submission by the MLPerf submission checker:
```bash
ck run program:mlperf-inference-submission --cmd_key=check
```

Pack results:
```
ck zip bench.mlperf.system
```



# Visualize MLPerf results

## Convert MLPerf inference results into the CK database format

* Supported host OS to process results: Linux, Windows, MacOS

## Install CK automation for the Python virtual environment

Install CK as described [here](https://github.com/ctuning/ck#installation).

Prepare virtual CK environment:

```bash
ck pull repo:mlcommons@ck-venv

ck create venv:mlperf --template=generic

ck activate venv:mlperf
```

## Pull CK repo with MLOps automation recipes
```bash
ck pull repo:mlcommons@ck-mlops
```

## Pull already processed results
```bash
ck pull repo:ck-mlperf-inference
```

## Install CK packages with MLPerf inference results

```bash
ck install package --tags=mlperf,inference,results,v1.1
ck install package --tags=mlperf,inference,results,v1.0
ck install package --tags=mlperf,inference,results,v0.7
ck install package --tags=mlperf,inference,results,v0.5
```

*Note that you can skip the above step and register your own local directory with your results as follows:*
```bash
ck detect soft:mlperf.inference.results  --full_path={FULL PATH TO YOUR DIRECTORY WITH MLPERF RESULTS}/README.md --force_version={SOME VERSION}
```

## Import results into CK format

Create a scratch CK repository to record results (unless you want to record them to the shared "ck-mlperf-inference" repo:
```bash
ck add repo:ck-mlperf-inference-1.1-dse --quiet
```

Import results to this repository:

```bash
ck import bench.mlperf.inference --target_repo=ck-mlperf-inference-1.1-dse
```

Note that we do not yet have a smart way to update results in the repository and they will be appended each time you run the above command.
You may want to clean your results before running this command again:
```bash
ck rm ck-mlperf-inference-1.1-dse:result:* -f
```

## Display all results locally

```bash
ck display dashboard --template=result --cfg=mlperf.inference.all
```

You can customize URL to show results from a given repo (ck_repo) and for a given scenario as follows:

* http://localhost:3344/?template=result&cfg=mlperf.inference.all&cfg_id=mlperf-inference-all-image-classification-edge-singlestream&repo_uoa=ck-mlperf-inference-1.1-dse
* http://localhost:3344/?template=result&cfg=mlperf.inference.all&cfg_id=mlperf-inference-all-image-classification-edge-offline&repo_uoa=ck-mlperf-inference-1.1-dse

You can also specify a given MLPerf scenario and a repository with results from the command line with starting a dashboard (CK version > 2.5.8):

```bash
ck display dashboard --template=result --cfg=mlperf.inference.all --cfg_id=mlperf-inference-all-image-classification-edge-singlestream --repo_uoa=ck-mlperf-inference-1.1-dse
```
or
```bash
ck display dashboard --template=result --cfg=mlperf.inference.all --extra_url="cfg_id=mlperf-inference-all-image-classification-edge-singlestream&repo_uoa=ck-mlperf-inference-1.1-dse"
```

## Process results on a Pareto frontier

```bash
ck filter ck-mlperf-inference-1.1-dse:bench.mlperf.inference:mlperf-inference-all-image-classification-edge-singlestream-pareto 
ck filter ck-mlperf-inference-1.1-dse:bench.mlperf.inference:mlperf-inference-all-*-pareto 
```

You can remove "ck-mlperf-inference-1.1-dse:" from above commands to process results in all repositories.


## Display other reproduced results at cKnowledge.io

* [List dashboards](https://cknow.io/reproduced-results)






## Resources

Our on-going collaboration with MLCommons to make 
the MLPerf&trade; inference benchmark more customizable, portable and easy to use:

* [MLPerf Inference Benchmark article](https://arxiv.org/abs/1911.02549)
* [Motivation](https://www.youtube.com/watch?v=7zpeIVwICa4)
* [MLCommons working groups](https://mlcommons.org/en/groups)
* [Open-source CK framework](https://github.com/mlcommons/ck) and [MLCube](https://github.com/mlcommons/mlcube)
  * [ML/AI packages from the community, OctoML and the cTuning foundation](https://github.com/mlcommons/ck-mlops/tree/main/package)
  * [ML/AI workflows from the community, OctoML and the cTuning foundation](https://github.com/mlcommons/ck-mlops/tree/main/program)
* [Documentation for the CK-powered MLPerf automation suite](https://github.com/mlcommons/ck/tree/master/docs/mlperf-automation)
* [Prototype of the end-to-end submission workflow for the MLPerf inference benchmark](https://github.com/mlcommons/ck-mlops/tree/main/module/bench.mlperf.inference)
