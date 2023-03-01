## Run Commands

We need to get imagenet full dataset to make image-classification submissions for MLPerf inference. Since this dataset is not publicly available via a URL please follow the instructions given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md) to download the dataset and register in CM.

On edge category ResNet50 has Offline, SingleStream and MultiStream scenarios and in datacenter category it has Offline and Server scenarios. The below commands are assuming an edge category system. 

### Onnxruntime backend

#### Do a test run to detect and record the system performance

```
cm run script --tags=generate-run-cmds,inference,_find-performance,_full,_all-scenarios --model=resnet50 \
--device=cpu --backend=onnxruntime --quiet
```
* Use `--device=cuda` to run the inference on Nvidia GPU
* Use `--division=closed` to run all scenarios for a closed division including the compliance tests
* Use `--category=datacenter` to run datacenter scenarios

#### Do a full accuracy run for all the scenarios

```
cm run script --tags=generate-run-cmds,inference,_accuracy-only,_all-scenarios --model=resnet50 --device=cpu \
--implementation=reference --backend=onnxruntime --execution-mode=valid --results_dir=$HOME/inference_3.0_results --quiet
```

#### Do a full performance run for all the scenarios
```
cm run script --tags=generate-run-cmds,inference,_performance-only,_all-scenarios --model=resnet50 --device=cpu \
--implementation=reference --backend=onnxruntime --execution-mode=valid --results_dir=$HOME/inference_3.0_results --quiet
```

#### Populate the README files
```
cm run script --tags=generate-run-cmds,inference,_populate-readme,_all-scenarios --model=resnet50 --device=cpu \
--implementation=reference --backend=onnxruntime --execution-mode=valid --results_dir=$HOME/inference_3.0_results --quiet
```

#### Generate actual submission tree

We should use the master branch of MLCommons inference repo for the submission checker. You can use `--hw_note_extra` option to add your name to the notes.
```
cm run script --tags=generate,inference,submission --results_dir=$HOME/inference_3.0_results/valid_results \
--submission_dir=$HOME/inference_submission_tree --clean  \
--run-checker --submitter=cTuning --adr.inference-src.version=master --hw_notes_extra="Result taken by NAME" --quiet
```

#### Push the results to GitHub repo

First create a fork of [this repo](https://github.com/ctuning/mlperf_inference_submissions_v3.0/). Then run the following command after replacing `--repo_url` with your fork URL.
```
cm run script --tags=push,github,mlperf,inference,submission --submission_dir=$HOME/inference_submission_tree \
--repo_url=https://github.com/ctuning/mlperf_inference_submissions_v3.0/ \
--commit_message="ResNet50 results added"
```

Create a PR to [cTuning repo](https://github.com/ctuning/mlperf_inference_submissions_v3.0/)

## Tensorflow backend

Same commands as for `onnxruntime` should work by replacing `backend=onnxruntime` with `--backend=tf`. For example,

```
cm run script --tags=generate-run-cmds,inference,_accuracy-only,_all-scenarios --model=resnet50 --device=cpu \
--implementation=reference --backend=tf --execution-mode=valid --results_dir=$HOME/inference_3.0_results --quiet
```

## TVM backend

Same commands as for `onnxruntime` should work by replacing `backend=onnxruntime` with `--backend=tvm-onnx`. (Only `--device=cpu` is currently supported for TVM) For example,

```
cm run script --tags=generate-run-cmds,inference,_accuracy-only,_all-scenarios --model=resnet50 --device=cpu \
--implementation=reference --backend=tvm-onnx --execution-mode=valid --results_dir=$HOME/inference_3.0_results --quiet
```
