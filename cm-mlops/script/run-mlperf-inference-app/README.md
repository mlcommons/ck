This CM script generates the CM commands to run all the required MLPerf scenarios for a given MLPerf inference model, runtime, device and language.

## Commands

To run the Python implementation of the MLPerf Reference Implementation we can do
``` 
cm run script --tags=run,mlperf,inference,reference,generate-run-cmds \
--model=resnet50 \
--device=cpu \
--backend=onnxruntime \
--lang=python \
--run_style=valid \
--output_dir=$HOME/results \
--add_deps.imagenet.tags=_full \
--imagenet_path=$HOME/datasets/imagenet-2012-val \
--hw_name=gcp-n2-standard-80
```

`CM_HW_NAME` is used to pick the runtime configuration value of the system as spefified for a given SUT [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-configs-sut-mlperf-inference)
 
