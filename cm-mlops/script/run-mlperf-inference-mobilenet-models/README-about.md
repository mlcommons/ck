## Set up

We need to get imagenet full dataset to make image-classification submissions for MLPerf inference. Since this dataset is not publicly available via a URL please follow the instructions given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md) to download the dataset and register in CM.  

<details>
<summary>Click here to set up docker (Optional).</summary>

### Docker Setup

CM commands are expected to run natively but if you prefer not to modify the host system, you can do the below command to set up a docker container. 

```
cm docker script --tags=run,mobilenet-models,_tflite,_accuracy-only \
--adr.compiler.tags=gcc  \
--docker_cm_repo=mlcommons@ck \
--imagenet_path=$HOME/imagenet-2012-val \
--results_dir=$HOME/mobilenet_results \
--submission_dir=$HOME/inference_submission_3.1 \
--docker_skip_run_cmd
```

This command will build a docker container and give you an interactive shell from which you can execute the below CM run commands.
* `results_dir`, `submission_dir` and `imagenet_path` are mounted from the host system.
* `results_dir` and `submission_dir` are expected to be empty directories to be populated by the docker
* `imagenet_path` should point to the imagenet folder containing the 50000 validation images.

</details>

## Run Commands

Since the runs can take many hours, in case you are running remotely you can install screen as follows. You may omit "screen" from all commands if you are running on a host system.
```
cmr "get generic-sys-util _screen"
```
### Default tflite


#### Do a full accuracy run for all the models (can take almost a day)

```
screen cmr "run mobilenet-models _tflite _accuracy-only" \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results
```

#### Do a full performance run for all the models (can take almost a day)
```
screen cmr "run mobilenet-models _tflite _performance-only" \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results 
```

#### Generate README files for all the runs
```
cmr "run mobilenet-models _tflite _populate-readme" \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results
```

#### Generate actual submission tree

We should use the master branch of MLCommons inference repo for the submission checker. You can use `--hw_note_extra` option to add your name to the notes.
```
cmr "generate inference submission" \
--results_dir=$HOME/mobilenet_results/valid_results \
--submission_dir=$HOME/mobilenet_submission_tree \
--clean \
--infer_scenario_results=yes \
--adr.compiler.tags=gcc --adr.inference-src.version=master \
--run-checker \
--submitter=cTuning \
--hw_notes_extra="Result taken by NAME" 
```
* Use `--hw_name="My system name"` to give a meaningful system name. Examples can be seen [here](https://github.com/mlcommons/inference_results_v3.0/tree/main/open/cTuning/systems)

#### Push the results to GitHub repo

First, create a fork of [this repo](https://github.com/ctuning/mlperf_inference_submissions_v3.1/). Then run the following command after replacing `--repo_url` with your fork URL.
```
cmr "push github mlperf inference submission" \
--submission_dir=$HOME/mobilenet_submission_tree \
--repo_url=https://github.com/ctuning/mlperf_inference_submissions_v3.1/ \
--commit_message="Mobilenet results added"
```

Create a PR to [cTuning repo](https://github.com/ctuning/mlperf_inference_submissions_v3.1/)

### Using ARMNN with NEON

Follow the same procedure as above but for the first three experiment runs add `_armnn,_neon` to the tags. For example
```
cmr "run mobilenet-models _tflite _armnn _neon _accuracy-only" \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results
```

`results_dir` and `submission_dir` can be the same as before as results will be going to different subfolders. 

### Using ARMNN with OpenCL
Follow the same procedure as above but for the first three experiment runs add `_armnn,_opencl` to the tags. For example
```
cmr "run mobilenet-models _tflite _armnn _opencl _accuracy-only" \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results
```

`results_dir` and `submission_dir` can be the same as before as results will be going to different subfolders. 
