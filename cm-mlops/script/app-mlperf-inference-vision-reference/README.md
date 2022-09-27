## Commands
To run the Python implementation of the MLPerf Reference Implementation we can do
``` 
cm run script --tags=app,mlperf,inference,reference,python,_resnet50,_tf,_cpu \
--output_dir=$HOME/results \
--add_deps.imagenet.tags=_full \
--env.IMAGENET_PATH=$HOME/datasets/imagenet-2012-val \
--env.CM_LOADGEN_MODE=performance \
--env.CM_LOADGEN_SCENARIO=Offline \
--env.CM_HW_NAME=gcp-n2-standard-80
```

Full set of tags for the script can be seen [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference/_cm.json#L191)
and the full set of dependencies can be seen [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference/_cm.json#L5).
`CM_HW_NAME` is used to pick the runtime configuration value of the system as spefified for a given SUT [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sut-mlc-configs)
 
We can control run other variants using the following commands

### Important options
1. `--env.CM_LOADGEN_MODE`. Valid values: {performance, accuracy}
2. `--env.CM_LOADGEN_SCENARIO`. Valid values: {Offline, Server, SingleStream, MultiStream}
3. `--env.CM_HW_NAME`. Valid value - any system description which has a config file (under same name) defined [here](https://github.com/arjunsuresh/ck/tree/master/cm-mlops/script/get-sutCM_LOADGEN_MAX_BATCHSIZE-mlc-configs/configs)
4. `--env.IMAGENET_PATH`. Location of directory containing Imagenet which cannot be downloaded from a public URL
5. `--env.OUTPUT_DIR`. Location where the outputs are produced.
6. `--env.CM_NUM_THREADS` - Number of CPU threads to launch the application with
7. `--env.CM_LOADGEN_MAX_BATCHSIZE` - Maximum batchsize to be used

Full set of options and how they are being used can be seen [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference/customize.py#L6)

## Resnet50 

``` 
cm run script --tags=mlperf,inference,reference,python,_resnet50,_onnxruntime,_cpu \
--add_deps.imagenet.tags=_full \
--env.IMAGENET_PATH=$HOME/datasets/imagenet-2012-val \
--env.CM_LOADGEN_MODE=performance \
--env.CM_LOADGEN_SCENARIO=Offline
```
Here, `_onnxruntime` can be replaced by `_tf` also for tensorflow backend. 

## Retinanet 

``` 
cm run script --tags=mlperf,inference,reference,python,_retinanet,_onnxruntime,_cpu \
--env.CM_LOADGEN_MODE=performance \
--env.CM_LOADGEN_SCENARIO=Offline
```
Tensorflow backend is currently not supported by the reference implementation for retinanet.
