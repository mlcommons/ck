## Commands
To run the Python implementation of the MLPerf Reference Implementation we can do
``` 
cm run script --tags=app,mlperf,inference,reference,python,_resnet50,_tf,_cpu \
--output_dir=$HOME/results \
--add_deps.imagenet.tags=_full \
--imagenet_path=$HOME/datasets/imagenet-2012-val \
--mode=performance \
--scenario=Offline \
--hw_name=gcp-n2-standard-80
```

Full set of tags for the script can be seen [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference/_cm.json#L191)
and the full set of dependencies can be seen [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference/_cm.json#L5).
`CM_HW_NAME` is used to pick the runtime configuration value of the system as spefified for a given SUT [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-sut-mlc-configs)
 
We can run other variants using the following commands

### Important options
* `--mode`. Valid values: {performance, accuracy}
* `--scenario`. Valid values: {Offline, Server, SingleStream, MultiStream}
* `--hw_name`. Valid value - any system description which has a config file (under same name) defined [here](https://github.com/arjunsuresh/ck/tree/master/cm-mlops/script/get-sutCM_LOADGEN_MAX_BATCHSIZE-mlc-configs/configs)
* `--imagenet_path`. Location of directory containing Imagenet which cannot be downloaded from a public URL
* `--output_dir`. Location where the outputs are produced.
* `--num_threads` - Number of CPU threads to launch the application with
* `--max_batchsize` - Maximum batchsize to be used
* `--rerun` - Redo the run even if previous run files exist
* `--regenerate_files` - Regenerates measurement files including accuracy.txt files even if a previous run exists. This option is redundant if `--rerun` is used
* `--test_query_count` - Specifies the number of samples to be processed during a test run

Full set of options and how they are being used can be seen [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference-vision-reference/customize.py#L6)

## Resnet50 

``` 
cm run script --tags=app,mlperf,inference,reference,python,_resnet50,_onnxruntime,_cpu \
--add_deps.imagenet.tags=_full \
--imagenet_path=$HOME/datasets/imagenet-2012-val \
--mode=performance \
--scenario=Offline
```
Here, `_onnxruntime` can be replaced by `_tf` also for tensorflow backend. 

## Retinanet 

``` 
cm run script --tags=app,mlperf,inference,reference,python,_retinanet,_onnxruntime,_cpu \
--mode=performance \
--scenario=Offline
```
Tensorflow backend is currently not supported by the reference implementation for retinanet.

## Bert

```
cm run script --tags=app,mlperf,inference,reference,python,_bert-99.9,_onnxruntime,_cpu \
--mode=performance \
--scenario=Offline
```
