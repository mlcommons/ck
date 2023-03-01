## Run Commands

We need to get imagenet full dataset to make image-classification submissions for MLPerf inference. Since this dataset is not publicly available via a URL please follow the instructions given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md) to download the dataset and register in CM.


Requirements: You need to have CUDA, cuDNN and TensorRT installed on your system. 

If CUDA is not detected, CM should download and install it automatically when you run the workflow.

For x86 machines, you can download the tar files for cuDNN and TensorRT and install them using the following commands
```bash
cm run script --tags=get,cudnn --tar_file=<PATH_TO_CUDNN_TAR_FILE>
```

```bash
cm run script --tags=get,tensorrt --tar_file=<PATH_TO_TENSORRT_TAR_FILE>
```

On other systems you can do a package manager install and then CM should pick up the installation automatically during the workflow run.

Nvidia run configuration values for each model-sceraio for known systems are stored in `__init__.py` files under configs directory. For custom systems these are stored under `custom.py` files. When custom config files are generated they override the default config values with empty ones (not desirable). So, you'll probably need to open the custom config file and comment out the overrides. Typically `gpu_batch_size` and `offline_expected_qps` are enough for an offline scenario run on a typical single GPU system.


## Build Nvidia Inference Server
```
cm run script --tags=build,nvidia,inference,server
```

## Run ResNet50

### Find SUT performance

```
cm run script --tags=generate,run-cmds,inference,_find-performance --model=resnet50 --implementation=nvidia-original \
--device=cuda --adr.nvidia-harness.gpu_batch_size=64 --results_dir=$HOME/nvidia_original_results
```

### Do a complete submission run

```
cm run script --tags=generate,run-cmds,inference,_submission,_full --execution_mode=valid --model=resnet50 \
--implementation=nvidia-original --device=cuda --adr.nvidia-harness.gpu_batch_size=64 \
--adr.nvidia-harness.skip_preprocess=yes --adr.nvidia-harness.make_cmd=run_harness \
--results_dir=$HOME/nvidia_original_results --submission_dir=$HOME/nvidia_original_submissions \
--division=open --submitter=cTuning --category=edge
```

