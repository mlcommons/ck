## Run Commands

We need to get imagenet full dataset to make image-classification submissions for MLPerf inference. Since this dataset is not publicly available via a URL please follow the instructions given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md) to download the dataset and register in CM.  

### Default tflite

#### Do a test run to detect and record the system performance for each model (about an hour runtime)

```
cm run script --tags=run,mobilenet-models,_tflite,_find-performance --adr.compiler.tags=gcc
```

During the run, tflite library will be installed and you can give the following answers for the prompt questions

```
Please input the desired Python library path to use.  Default is [/home/ubuntu/CM/repos/local/cache/3795df3c20b44647/inference/tools/submission]

Do you wish to build TensorFlow with ROCm support? [y/N]: N
No ROCm support will be enabled for TensorFlow.

Do you wish to build TensorFlow with CUDA support? [y/N]: N
No CUDA support will be enabled for TensorFlow.

Do you wish to download a fresh release of clang? (Experimental) [y/N]: N
Clang will not be downloaded.

Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is -Wno-sign-compare]:


Would you like to interactively configure ./WORKSPACE for Android builds? [y/N]: N
```
#### Do a full accuracy run for all the models (can take almost a day)

```
cm run script --tags=run,mobilenet-models,_tflite,_accuracy-only --results_dir=$HOME/mobilenet_results --adr.compiler.tags=gcc
```
#### Do a full performance run for all the models (can take almost a day)
```
cm run script --tags=run,mobilenet-models,_tflite,_performance-only --results_dir=$HOME/mobilenet_results --adr.compiler.tags=gcc
```

#### Generate README files for all the runs
```
cm run script --tags=run,mobilenet-models,_tflite,_populate-readme --results_dir=$HOME/mobilenet_results --adr.compiler.tags=gcc
```

#### Generate actual submission tree

We should use the master branch of MLCommons inference repo for the submission checker. You can use `--hw_note_extra` option to add your name to the notes.
```
cm run script --tags=generate,inference,submission --results_dir=$HOME/mobilenet_results/valid_results \
--submission_dir=$HOME/mobilenet_submission_tree --clean --infer_scenario_results=yes \
--run-checker --submitter=cTuning --adr.inference-src.version=master --hw_notes_extra="Result taken by NAME" --adr.compiler.tags=gcc
```

#### Push the results to GitHub repo

First create a fork of [this repo](https://github.com/ctuning/mlperf_inference_submissions_v3.0/). Then run the following command after replacing `--repo_url` with your fork URL.
```
cm run script --tags=push,github,mlperf,inference,submission --submission_dir=$HOME/mobilenet_submission_tree \
--repo_url=https://github.com/ctuning/mlperf_inference_submissions_v3.0/ \
--commit_message="Mobilenet results added"
```

Create a PR to [cTuning repo](https://github.com/ctuning/mlperf_inference_submissions_v3.0/)

### Using ARMNN with NEON

Follow the same procedure as above but for the first 3 experiment runs add `_armnn,_neon` to the tags. For example
```
cm run script --tags=run,mobilenet-models,_tflite,_armnn,_neon,_find-performance --adr.compiler.tags=gcc
```

`results_dir` and `submission_dir` can be the same as before as results will be going to different sub folders. 

### Using ARMNN with OpenCL
Follow the same procedure as above but for the first 3 experiment runs add `_armnn,_opencl` to the tags. For example
```
cm run script --tags=run,mobilenet-models,_tflite,_armnn,_opencl,_find-performance --adr.compiler.tags=gcc
```

`results_dir` and `submission_dir` can be the same as before as results will be going to different sub folders. 
