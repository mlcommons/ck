# MLPerf task: object detection

* [Install general MLPerf dependencies](README.md)

## Install task dependencies

```bash
ck run program:mlperf-inference-bench-object-detection-tvm-cpu --cmd_key=install-python-requirements

ck install package --tags=dataset,coco,2017,full
ck install package --tags=model,mlperf,octoml,ssd-resnet34,side.1200,opset-8
ck install package --tags=model,mlperf,octoml,ssd-resnet34,side.1200,opset-11
```


## Scenario: Accuracy; Offline

All items are enqued from the start and then scheduled across threads.

### Use TVM

```bash
   ck run program:mlperf-inference-bench-object-detection-tvm-cpu \
        --cmd_key=accuracy-offline \
        --env.MLPERF_TVM_TARGET="llvm -mcpu=znver2" \
        --env.MLPERF_TVM_EXECUTOR=vm
```

Customize it and record results in local CK repo:
```bash
ck benchmark program:mlperf-inference-bench-object-detection-tvm-cpu \
     --cmd_key=accuracy-offline \
     --env.MLPERF_TVM_TARGET="llvm -mcpu=znver2" \
     --env.MLPERF_TVM_EXECUTOR=vm \
     --env.EXTRA_OPS="--count 100 --threads 1 --max-batchsize 1" \
     --repetitions=1 \
     --skip_stat_analysis --process_multi_keys=dummy \
     --skip_print_timers --skip_print_stats \
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
ck benchmark program:mlperf-inference-bench-object-detection-onnx-cpu \
     --cmd_key=accuracy-offline \
     --env.EXTRA_OPS="--count 100 --threads 1 --max-batchsize 1" \
     --repetitions=1 \
     --skip_stat_analysis --process_multi_keys=dummy \
     --skip_print_timers --skip_print_stats \
     --print_files=accuracy.txt
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







## Check model accuracy

### model,image-classification,mlperf,onnx,resnet50,v1.5-opset-8

TVM and ONNX produced the same results (~35 min on AMD Milan):

```
* File: accuracy.txt

loading annotations into memory...
Done (t=0.38s)
creating index...
index created!
Loading and preparing results...
DONE (t=0.05s)
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=6.35s).
Accumulating evaluation results...
DONE (t=1.16s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.136
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.235
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.139
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.047
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.174
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.175
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.127
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.161
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.162
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.048
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.198
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.215
mAP=13.583%
```

### model,image-classification,mlperf,onnx,resnet50,v1.5-opset-11

TVM and ONNX produced the same results (~35 min on AMD Milan):

```
* File: accuracy.txt

loading annotations into memory...
Done (t=0.33s)
creating index...
index created!
Loading and preparing results...
DONE (t=4.89s)
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=39.34s).
Accumulating evaluation results...
DONE (t=9.06s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.223
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.407
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.217
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.144
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.298
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.249
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.214
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.348
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.369
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.196
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.460
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.434
mAP=22.317%
```




## Scenario: Performance; Single Stream

### Use TVM

```bash
   ck run program:mlperf-inference-bench-object-detection-tvm-cpu \
        --cmd_key=performance-singlestream \
        --env.MLPERF_TVM_TARGET="llvm -mcpu=znver2" \
        --env.MLPERF_TVM_EXECUTOR=vm
```


### Use ONNX

```bash
time ck benchmark program:mlperf-inference-bench-object-detection-onnx-cpu \
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



