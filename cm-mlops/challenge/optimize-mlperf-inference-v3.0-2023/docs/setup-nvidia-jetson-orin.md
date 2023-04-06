## Setup
We used Nvidia Jetson AGX Orin developer kit with 32GB RAM and 64GB eMMC. We also connected a 500GB SSD disk via USB and Wifi connection for internet connectivity.

We used the out of the box developer kit image which was running Ubuntu 20.04 and JetPack 5.0.1 Developer Preview with CUDA 11.4. 

[cuDNN 8.6.0](https://developer.nvidia.com/compute/cudnn/secure/8.6.0/local_installers/11.8/cudnn-local-repo-ubuntu2004-8.6.0.163_1.0-1_arm64.deb) and [TensorRT 8.5.2.2](https://developer.nvidia.com/downloads/compute/machine-learning/tensorrt/secure/8.5.3/local_repos/nv-tensorrt-local-repo-ubuntu2004-8.5.3-cuda-11.8_1.0-1_arm64.deb) were downloaded as Debian packages on a host machine, copied over to Nvidia Jetson Orin and installed.


We need to get imagenet full dataset to make image-classification submissions for MLPerf inference. Since this dataset is not publicly available via a URL please follow the instructions given [here](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-dataset-imagenet-val/README-extra.md) to download the dataset.

### Copy the needed files from a host machine

Copy the imagenet dataset to the created instance. For example,

```
rsync -avz  $HOME/imagenet-2012-val/ user@192.168.0.27:
```

Login to Orin and register the imagenet dataset as
```
cm run script --tags=get,imagenet,dataset,_2012,_full --input=$HOME/imagenet-2012-val
```

Once all the required files are copied over, follow the individual benchmark instructions from the README files given [here](./) All the required dependencies should be resolved by CM.
