## Setup
Please follow the MLCommons CK [installation guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md) to install CM.

Install MLCommons CK repository with automation workflows for MLPerf.
```
cm pull repo mlcommons@ck
```

## Run Commands

We need to get imagenet full dataset to make image-classification submissions for MLPerf inference. Since this dataset is not publicly available via a URL please follow the instructions given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md) to download the dataset and register in CM.  



### Default tflite


#### Do a full accuracy run for all the models (can take almost a day)

```
cm docker script --tags=run,mobilenet-models,_tflite,_accuracy-only --results_dir=$HOME/mobilenet_results \
--submission_dir=$HOME/inference_submission_3.1  --adr.compiler.tags=gcc  --cm_repo=mlcommons@ck --imagenet_path=$HOME/imagenet-2012-val
```

The above command will build a docker container, mounts the `results_dir`, `submission_dir`, and `imagenet_path` from the host machine, and then runs the cm command inside the launched container. The remaining `cm docker` commands below will be reusing this docker container. 

#### Do a full performance run for all the models (can take almost a day)
```
cm docker script --tags=run,mobilenet-models,_tflite,_accuracy-only --results_dir=$HOME/mobilenet_results \
--submission_dir=$HOME/inference_submission_3.1  --adr.compiler.tags=gcc  --cm_repo=mlcommons@ck --imagenet_path=$HOME/imagenet-2012-val
```

#### Generate README files for all the runs
```
cm docker script --tags=run,mobilenet-models,_tflite,_populate-readme --results_dir=$HOME/mobilenet_results \
--submission_dir=$HOME/inference_submission_3.1  --adr.compiler.tags=gcc  --cm_repo=mlcommons@ck --imagenet_path=$HOME/imagenet-2012-val
```

#### Generate actual submission tree

We should use the master branch of MLCommons inference repo for the submission checker. You can use `--hw_note_extra` option to add your name to the notes.
```
cm run script --tags=generate,inference,submission --results_dir=$HOME/mobilenet_results/valid_results \
--submission_dir=$HOME/mobilenet_submission_tree --clean --infer_scenario_results=yes --adr.compiler.tags=gcc \
--run-checker --submitter=cTuning --adr.inference-src.version=master --hw_notes_extra="Result taken by NAME" 
```
** This CM command is run in the host **

#### Push the results to GitHub repo

First, create a fork of [this repo](https://github.com/ctuning/mlperf_inference_submissions_v3.1/). Then run the following command after replacing `--repo_url` with your fork URL.
```
cm run script --tags=push,github,mlperf,inference,submission --submission_dir=$HOME/mobilenet_submission_tree \
--repo_url=https://github.com/ctuning/mlperf_inference_submissions_v3.1/ \
--commit_message="Mobilenet results added"
```
** This CM command is run in the host **

Create a PR to [cTuning repo](https://github.com/ctuning/mlperf_inference_submissions_v3.1/)

### Using ARMNN with NEON

Follow the same procedure as above but for the first three experiment runs add `_armnn,_neon` to the tags. For example
```
cm docker script --tags=run,mobilenet-models,_tflite,_armnn,_neon,_accuracy-only --results_dir=$HOME/mobilenet_results \
--submission_dir=$HOME/inference_submission_3.1  --adr.compiler.tags=gcc  --cm_repo=mlcommons@ck --imagenet_path=$HOME/imagenet-2012-val
```

`results_dir` and `submission_dir` can be the same as before as results will be going to different subfolders. 

### Using ARMNN with OpenCL
Follow the same procedure as above but for the first three experiment runs add `_armnn,_opencl` to the tags. For example
```
cm docker script --tags=run,mobilenet-models,_tflite,_armnn,_opencl,_accuracy-only --results_dir=$HOME/mobilenet_results \
--submission_dir=$HOME/inference_submission_3.1  --adr.compiler.tags=gcc  --cm_repo=mlcommons@ck --imagenet_path=$HOME/imagenet-2012-val

```

`results_dir` and `submission_dir` can be the same as before as results will be going to different subfolders. 
