## Setup
Please follow the MLCommons CK [installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md) to install CM.
Download the ck repo to get the CM script for MLPerf submission
```
cm pull repo mlcommons@ck
```
## Run Commands

Bert has two variants - `bert-99` and `bert-99.9` where the `99` and `99.9` specifies the required accuracy constraint with respect to the reference floating point model. `bert-99.9` model is applicable only on a datacenter system.

On edge category `bert-99` has Offline and SingleStream scenarios and in datacenter category both `bert-99` and `bert-99.9` have Offline and Server scenarios. The below commands are assuming an edge category system. 

### Onnxruntime backend

#### Do a test run to detect and record the system performance

```
cm run script --tags=generate-run-cmds,inference,_find-performance,_all-scenarios \
--model=bert-99 --implementation=reference --device=cpu --backend=onnxruntime --quiet
```
* Use `--device=cuda` to run the inference on Nvidia GPU
* Use `--division=closed` to run all scenarios for a closed division including the compliance tests
* Use `--category=datacenter` to run datacenter scenarios

#### Do a full accuracy run for all the scenarios

```
cm run script --tags=generate-run-cmds,inference,_accuracy-only,_all-scenarios \
--model=bert-99 --device=cpu --implementation=reference --backend=onnxruntime \
--execution-mode=valid --results_dir=$HOME/inference_3.0_results --quiet
```

#### Do a full performance run for all the scenarios
```
cm run script --tags=generate-run-cmds,inference,_performance-only,_all-scenarios \
--model=bert-99 --device=cpu --implementation=reference --backend=onnxruntime \
--execution-mode=valid --results_dir=$HOME/inference_3.0_results --quiet
```

#### Populate the README files
```
cm run script --tags=generate-run-cmds,inference,_populate-readme,_all-scenarios \
--model=bert-99 --device=cpu --implementation=reference --backend=onnxruntime \
--execution-mode=valid --results_dir=$HOME/inference_3.0_results --quiet
```

#### Generate actual submission tree

We should use the master branch of MLCommons inference repo for the submission checker. You can use `--hw_note_extra` option to add your name to the notes.
```
cm run script --tags=generate,inference,submission --results_dir=$HOME/inference_3.0_results/valid_results \
--device=cpu --submission_dir=$HOME/inference_submission_tree --clean --run-checker --submitter=cTuning 
--adr.inference-src.version=master --hw_notes_extra="Result taken by NAME" --quiet
```

#### Push the results to GitHub repo

First create a fork of [this repo](https://github.com/ctuning/mlperf_inference_submissions_v3.0/). Then run the following command after replacing `--repo_url` with your fork URL.
```
cm run script --tags=push,github,mlperf,inference,submission \
--submission_dir=$HOME/inference_submission_tree \
--repo_url=https://github.com/ctuning/mlperf_inference_submissions_v3.0/ \
--commit_message="Bert results added"
```

Create a PR to [cTuning repo](https://github.com/ctuning/mlperf_inference_submissions_v3.0/)

## Tensorflow backend

Same commands as for `onnxruntime` should work by replacing `backend=onnxruntime` with `--backend=tf`. For example,

```
cm run script --tags=generate-run-cmds,inference,_accuracy-only,_all-scenarios \
--model=bert-99 --device=cpu --implementation=reference --backend=tf --execution-mode=valid \
--results_dir=$HOME/inference_3.0_results --quiet
```

## Pytorch backend

Same commands as for `onnxruntime` should work by replacing `backend=onnxruntime` with `--backend=pytorch`. For example,

```
cm run script --tags=generate-run-cmds,inference,_accuracy-only,_all-scenarios \
--model=bert-99 --device=cpu --implementation=reference --backend=pytorch \
--execution-mode=valid --results_dir=$HOME/inference_3.0_results --quiet
```

