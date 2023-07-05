This script is a CM wrapper to the official [Nvidia submission code](https://github.com/mlcommons/inference_results_v3.0/tree/master/closed/NVIDIA) used for MLPerf inference submissions. 


Nvidia working directory is given by `CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH` variable which can be seen by running 
```bash
cm run script --tags=get,nvidia,common-code,_nvidia-only  --out=json
```
* Use `--custom_system=yes` input if the above command fails to recognize your system.


## Requirements
You need to have CUDA, cuDNN and TensorRT installed on your system.

### Download the needed files
For x86 machines, please download the latest install tar files from the below sites
1. [cuDNN](https://developer.nvidia.com/cudnn) (for cuda 11)
2. [TensorRT](https://developer.nvidia.com/tensorrt)

<details>

<summary>
    
### Using Docker (Recommended on x86 systems)

</summary>

1. Copy the downloaded tar files of `cuDNN` and `TensorRT` to a folder say `$HOME/install_data`
2. Download the CUDA installation file to the same folder
```
cmr --tags=download,file,_url.https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run --download_path=$HOME/install_data
```
3. Build the docker container and mount the folder with the downloaded files
```
cm docker script --tags=build,nvidia,inference,server --docker_mounts,=$HOME/install_data:/data/ --adr.install-cuda-prebuilt.local_run_file_path=/data/cuda_11.8.0_520.61.05_linux.run  --adr.tensorrt.tar_file=/data/TensorRT-8.6.1.6.Linux.x86_64-gnu.cuda-11.8.tar.gz --adr.cudnn.tar_file=/data/cudnn-linux-x86_64-8.9.2.26_cuda11-archive.tar.xz --docker_cm_repo=mlcommons@ck  --adr.compiler.tags=gcc
```


Now you'll be inside the CM Nvidia docker container and can run further scripts. You can try the below command to make sure things are working as expected. 
```
nvidia-smi
```

4. Run the CM build command inside the docker. This step is necessary because the build needs Nvidia drivers which are available only after the container launch.
```
cm run script --tags=build,nvidia,inference,server --adr.install-cuda-prebuilt.local_run_file_path=/data/cuda_11.8.0_520.61.05_linux.run --adr.tensorrt.tar_file=/data/TensorRT-8.6.1.6.Linux.x86_64-gnu.cuda-11.8.tar.gz --adr.cudnn.tar_file=/data/cudnn-linux-x86_64-8.9.2.26_cuda11-archive.tar.xz --adr.compiler.tags=gcc
```

5. Once the build is complete, you can proceed with any further CM scripts like for MLPerf inference. You can also save the container at this stage using [docker commit](https://docs.docker.com/engine/reference/commandline/commit/) so that it can be launched later without having to go through the previous steps.

</details>

<details>

<summary>

### Without Docker
</summary>

### Install CUDA
If CUDA is not detected, CM should download and install it automatically when you run the workflow. 
** Nvidia drivers are expected to be installed on the system **


### Install cuDNN
For x86 machines, you can [download the tar files for cuDNN](https://developer.nvidia.com/cudnn) (for cuda 11) and [TensorRT](https://developer.nvidia.com/tensorrt) and install them using the following commands
```bash
cm run script --tags=get,cudnn --input=<PATH_TO_CUDNN_TAR_FILE>
```

### Install TensorRT
```bash
cm run script --tags=get,tensorrt,_dev --input=<PATH_TO_TENSORRT_TAR_FILE>
```

On other systems, you can do a package manager install and then CM should pick up the installation automatically during the workflow run.

</details>



