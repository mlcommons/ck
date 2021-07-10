**[ [TOC](../README.md) ]**

# Common workflow for MLPerf inference

## Brainstorming workflow interface

We plan to add module:mlperf.bench.inference with the following flags:

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

This high-level workflow will install relevant CK packages ([ctuning@ai](https://github.com/ctuning/ck-mlops/tree/main/package) / [octoml@mlops](https://github.com/octoml/mlops/tree/main/package))
and run low-level [CK program workflows for MLPerf](https://github.com/octoml/mlops/tree/main/program).


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

* [Grigori Fursin](https://cKnowledge.io/@gfursin)
