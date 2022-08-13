## Commands
To run the Python implementation of the MLPerf Reference Implementation we can do
``` 
cm run script --tags=app,mlperf,inference,reference,python,_resnet50,_tf,_cpu \
--output_dir=$HOME/results \
--add_deps_tags.imagenet=_full \
--env.IMAGENET_PATH=$HOME/datasets/imagenet-2012-val \
--env.CM_LOADGEN_MODE=performance \
--env.CM_LOADGEN_SCENARIO=Offline \
--env.CM_SUT_NAME=gcp-n2-standard-80-tf
```

Full set of tags for the script can be seen [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference/_cm.json#L191)
and the full set of dependencies can be seen [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference/_cm.json#L5).
`CM_SUT_NAME` is used to pick the runtime configuration value of the system as spefified for a given SUT [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sut-mlc-configs)
By [default](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference/_cm.json#L161) the app runs the resnet50 model with Tensorflow backend on CPU device.
So, even if we omit the last 3 tags (`_resnet50,_tf,_cpu`) the behaviour remains the same. 
We can control run other variants using the following commands

### Important options
1. `--env.CM_LOADGEN_MODE`. Valid values: {performance, accuracy}
2. `--env.CM_LOADGEN_SCENARIO`. Valid values: {Offline, Server, SingleStream, MultiStream}
3. `--env.CM_SUT_NAME`. Valid value - any SUT which has a config file (under same name) defined [here](https://github.com/arjunsuresh/ck/tree/master/cm-mlops/script/get-sut-mlc-configs/configs)
4. `--env.IMAGENET_PATH`. Location of directory containing Imagenet which cannot be downloaded from a public URL
5. `--env.OUTPUT_DIR`. Location where the outputs are produced.
6. `--threads` - Number of CPU threads to launch the application with
7. `--max-batchsize` - Maximum batchsize to be used

Full set of options and how they are being used can be seen [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference/customize.py#L6)

## Resnet50 

``` 
cm run script --tags=mlperf,inference,reference,python,_resnet50,_onnxruntime,_cpu \
--add_deps_tags.imagenet=_full \
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
Tensorflow backend is currently not supported by the reference implementation.
