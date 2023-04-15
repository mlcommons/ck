**[ [TOC](../README.md) ]**

# Common workflow for MLPerf inference

## Prototype

We have developed the prototype of the automated submission system 
for the MLPerf inference benchmark:
* [CK module with Readme](https://github.com/mlcommons/ck-mlops/tree/main/module/bench.mlperf.inference)
* [API](https://github.com/mlcommons/ck-mlops/blob/main/module/bench.mlperf.inference/module.py#L1230)


## Required functionality


```
--submitter (module:mlperf.submitter)
--division (closed/open)

--task (image classification)
--backend (onnx/tvm/tensorflow/pytorch)
--target (cpu/gpu/tpu/dsp)
--sut
--model (resnet50)
--dataset (imagenet2017)

--dataset_size (500)

--dse.batch
--dse.thread

--env (extra params)

--version (1.1)

--record (record to mlperf.result)
--record_mlperf (record to MLPerf inference results GitHub package)

--mode=(performance/accuracy/audit)

```

This high-level workflow will install relevant CK packages ([ctuning@ai](https://github.com/mlcommons/ck-mlops/tree/main/package) / [mlcommons@ck-mlops](https://github.com/mlcommons/ck-mlops/tree/main/package))
and run low-level [CK program workflows for MLPerf](https://github.com/mlcommons/ck-mlops/tree/main/program).


## Tested configuration

We need to create a CK entry with a list of tested configurations and related CK workflows and packages
to test the user selection in the above workflow:

``` 
? module:mlperf.bench.inference.tested / available / conf ?
```

## Dashboard

We prepared a CK dashboard engine for MLPerf (module:mlperf.result). 

## Import all MLPerf inference results

Import results from all installed CK "MLPerf inference result" packages 
to the mlperf.result entries


```
ck import mlperf.bench.inference
```

## Export all MLPerf inference results

```
ck export mlperf.bench.inference
 or
ck export mlperf.result
```



# Coordinator

* [Grigori Fursin](https://cKnowledge.org/gfursin)
