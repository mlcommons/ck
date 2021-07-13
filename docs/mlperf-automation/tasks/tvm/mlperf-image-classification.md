# MLPerf task: image classification

* [Install general MLPerf dependencies](README.md)

## Install task dependencies

```bash
ck install package --tags=imagenet,2012,val,min,non-resized
ck install package --tags=imagenet,2012,aux,from.berkeley

ck install package --tags=model,image-classification,mlperf,onnx,resnet50,v1.5-opset-8
ck install package --tags=model,image-classification,mlperf,onnx,resnet50,v1.5-opset-11

ck run program:mlperf-inference-bench-image-classification-tvm-cpu --cmd_key=install-python-requirements

```

## Scenario: Accuracy; Offline

All items are enqued from the start and then scheduled across threads.

### Use TVM

Run with default parameters:
```bash
ck run program:mlperf-inference-bench-image-classification-tvm-cpu \
        --cmd_key=accuracy-offline
```

Customize it:
```
ck run program:mlperf-inference-bench-image-classification-tvm-cpu \
        --cmd_key=accuracy-offline \
        --env.MLPERF_TVM_EXECUTOR=graph \
        --env.MLPERF_TVM_TARGET="llvm -mcpu=znver2" \
        --env.EXTRA_OPS="--count=100 --thread 1 --max-batchsize 1"

```

Record results in a local CK repository for further analysis and visualization:
```
ck benchmark program:mlperf-inference-bench-image-classification-tvm-cpu \
     --cmd_key=accuracy-singlestream \
     --repetitions=1 \
     --skip_print_timers --skip_print_stats \
     --skip_stat_analysis --process_multi_keys=dummy \
     --record --record_repo=local \
     --record_uoa=mlperf-closed-image-classification-accuracy-single-stream \
     --tags=mlperf,division.closed,task.image-classification,tvm \
     --print_files=accuracy.txt
```

Pack experiments:
```
ck zip local:experiment:*
```

This command will create *ckr-local.zip* file with all CK experiments form the local repository.
It can be shared with other colleagues and installed locally for analysis as follows:
```
ck unzip repo --zip=ckr-local.zip
```

Replay experiment (to be improved):
```
ck ls experiment
ck reply experiment:{CK alias from above list}
```



### Use ONNX


```bash
ck benchmark program:mlperf-inference-bench-image-classification-onnx-cpu \
     --cmd_key=accuracy-offline \
     --env.EXTRA_OPS="--count 5000 --max-batchsize 1 --threads 1" \
     --repetitions=1 \
     --skip_print_timers --skip_print_stats \
     --print_files=mlperf_log_summary.txt

```



## Scenario: Accuracy; Single Stream

Substitute "cmd_key" with accuracy-singlestream.

## Scenario: Accuracy; Server

Substitute "cmd_key" with accuracy-server.

Extra options:
```bash
 --env.EXTRA_OPS="--count 5000 --time 20 --qps 10 --max-batchsize 2 --threads 4" \
```


## Scenario: Accuracy; MultiStream

Note that MultiStream scenario is removed from MLPerf v1.1

samples-per-query are separated by max-batchsize.
                          Substitute "cmd_key" with "accuracy-multistream.

Extra options:
```bash
 --env.EXTRA_OPS="--count 5000 --time 20 --samples-per-query 4 --max-batchsize 2 --threads 8" \
```








## Scenario: Performance; Single Stream

### Use TVM

```bash
time ck run program:mlperf-inference-bench-image-classification-tvm-cpu \
     --cmd_key=performance-singlestream
```

Customize and record it:
```bash

time ck benchmark program:mlperf-inference-bench-image-classification-tvm-cpu \
     --cmd_key=performance-singlestream \
     --env.EXTRA_OPS="--count 500 --time 60 --qps 200 --max-latency 0.1 --threads 1 --max-batchsize 1" \
     --env.MLPERF_TVM_TARGET="llvm -mcpu=znver2" \
     --env.TVM_NUM_THREADS=1 \
     --env.MLPERF_TVM_EXECUTOR="graph" \
     --repetitions=1 \
     --skip_print_timers --skip_print_stats \
     --record --record_repo=local \
     --record_uoa=mlperf-closed-image-classification-accuracy-single-stream \
     --tags=mlperf,division.closed,task.image-classification,tvm
```

*Note that "--count" forces number of quieries and may not satisfy constraints.*


### Use ONNX

```bash
time ck benchmark program:mlperf-inference-bench-image-classification-onnx-cpu \
     --cmd_key=performance-singlestream \
     --env.EXTRA_OPS="--count 5000 --max-batchsize 1 --threads 1" \
     --repetitions=1 \
     --skip_print_timers --skip_print_stats \
     --print_files=mlperf_log_summary.txt
```



## Scenario: Performance; Single Stream

Substitute "cmd_key" with performance-singlestream.

## Scenario: Performance; Server

Substitute "cmd_key" with performance-server.

Extra options:
```bash
 --env.EXTRA_OPS="--count 5000 --time 20 --qps 10 --max-batchsize 2 --threads 4" \
```


## Scenario: Performance; MultiStream

Note that MultiStream scenario is removed from MLPerf v1.1

samples-per-query are separated by max-batchsize.
                          Substitute "cmd_key" with "performance-multistream.

Extra options:
```bash
 --env.EXTRA_OPS="--count 5000 --time 20 --samples-per-query 4 --max-batchsize 2 --threads 8" \
```









## Run TVM-based MLPerf inference benchmark with an Octomized model

We have a preliminary support to run MLPerf inference (image classification)
with models from Octomizer wheels shared as CK packages 
([see this guide how to create them](../octomizer-wheels/test-tune-and-produce-a-wheel.md)):



```bash

time ck benchmark program:mlperf-inference-bench-image-classification-octomizer-cpu \
     --cmd_key=accuracy-offline \
     --env.EXTRA_OPS="--count 10 --max-batchsize 1 --threads 1" \
     --env.CK_USE_OCTOMIZER=yes \
     --repetitions=1 \
     --skip_print_timers --skip_print_stats \
     --print_files=mlperf_log_summary.txt

```




## Use Docker 


Build adaptive CK container with [TVM-based MLPerf inference benchmark](https://github.com/octoml/mlops/blob/main/docker/ck-mlperf-inference-dev-image-classification-onnx-tvm/Dockerfile.ubuntu-20.04):
```bash
ck build docker:ck-mlperf-inference-dev-image-classification-onnx-tvm --tag=ubuntu-20.04
```

Check installed CK packages:
```bash
ck run docker:ck-mlperf-inference-dev-image-classification-onnx-tvm --tag=ubuntu-20.04 \
    --command="ck show env"
```

Run this container with the default test:
```bash
ck run docker:ck-mlperf-inference-dev-image-classification-onnx-tvm --tag=ubuntu-20.04
```

Run this container with the customized CK API command:
```bash
ck run docker:ck-mlperf-inference-dev-image-classification-onnx-tvm --tag=ubuntu-20.04  \
     --command="ck run program:mlperf-inference-bench-image-classification-tvm-cpu \
     --cmd_key=accuracy-offline \
     --env.EXTRA_OPS=\"--thread 1 --max-batchsize 1\""
```

Run this container in bash mode:
```bash
ck run docker:ck-mlperf-inference-dev-image-classification-onnx-tvm --tag=ubuntu-20.04 --bash
```

