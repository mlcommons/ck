## Setup

We used Nvidia Jetson AGX Orin developer kit with 32GB RAM and 64GB eMMC. We also connected a 500GB SSD disk via USB and Wifi connection for internet connectivity.

We used the out of the box developer kit image which was running Ubuntu 20.04 and JetPack 5.0.1 Developer Preview (L4T 34.1.1) with CUDA 11.4. We were also using the default 4k page size (Nvidia recommends 64k for MLPerf inference).

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

### Power Measurement Setup

We were measuring power in the peak performance mode (MaxN) except for one SUT where the energy efficiency mode was changed to Max15. Our aim was to showcase the out of the box performance of Nvidia Jetson AGX Orin including the power usage. 

## Reproducing the Nvidia Jetson AGX Orin Submission

After our submission we followed the instructions from Nvidia in the inference v3.0 repository and tried to reproduce the numbers from Nvidia. For MaxN mode we were able to match the numbers by Nvidia using same versions of CUDA, cuDNN and TensorRT but outside of docker. For MaxQ mode, we could get the same performance as Nvidia but our power usage was about 5W higher.

### Performance results MaxN

The below table shows the performance comparison of our results under different settings and the Nvidia submission for MLPerf inference 3.0. We'll be updating our instructions for easier reproducibility of these numbers including CM scripts for flashing the L4T image and rebuilding the kernel for 64k pagesize.


| Workload  | Results | L4T   | PAGESIZE | Power Mode | FAN Dynamic Speed control | Offline Accuracy | Offline Performance | SingleStream Accuracy | SingleStream Performance | MultiStream Accuracy | MultiStream Performance |
| --------- | --------------------------------- | ----- | -------- | ---------- | ------------------------- | ---------------- | ------------------- | --------------------- | ------------------------ | -------------------- | ----------------------- |
| ResNet50  |  Nvidia Submitted (docker)                        | r35.3 | 64k      | MaxN       | active                    | 75.934           | 6438.1              | 76.032                | 0.633479                 | 76.032               | 2.187731                |
| ResNet50  |  cTuning Submitted                         | r34.1.1 | 4k      | MaxN       | active                    | 75.934           | 4697              | 76.032                | 0.72                 | 76.032               | 2.57                |
| ResNet50  | MLCommons taskforce on reproducibility              | r35.2.1    | 4k       | MaxN          | active                    | 75.85            | 6172                | 76.056                | 0.644                    | 76.056               | 2.074                   |
| ResNet50  | MLCommons taskforce on reproducibility              | r35.3     | 64k       | MaxN         | active                    | 75.85            | 6430                | 76.056               | 0.659                    | 76.056              | 2.20                   |
| RetinaNet |  Nvidia Submitted (docker)                         | r35.3 | x        | MaxN       | active                    | 37.372           | 92.4048             | 37.403                | 13.924457                | 37.519               | 104.680313              |
| RetinaNet | MLCommons taskforce on reproducibility             | r35.2.1     | 4k       | MaxN          | active                    | 37.346                | 80.0854 (no DLA)                   | 37.350                     | 14,19                        | 37.409 | 105.344828              |
| RetinaNet | MLCommons taskforce on reproducibility             | r35.3     | 64k       | MaxN          | active                    | 37.345               | 94.6886                    | 37.340                     | 14.073                       | 37.488                    | 103.8                     |
| BERT      | Nvidia Submitted (docker)                     | r35.3 | x        | MaxN       | active                    | 90.552           | 544.243             | 90.344                | 5.635431                 | NA                   | NA                      |
| BERT      | cTuning Submitted                         | r34.1.1 | 4k        | MaxN       | active                    | 90.552           | 449.96             | 90.344                | 7.8                 | NA                   | NA                      |
| BERT      | MLCommons taskforce on reproducibility             | r35.2.1     | 4k       | MaxN          | active                    | 90.562           | 527 (128 batchsize)                 | 90.311                | 6.636                    | NA                   | NA                      |
| BERT      | MLCommons taskforce on reproducibility            | r35.3     | 64k       | MaxN          | active                    | 90.552          | 539                 | 90.344                | 6.31                    | NA                   | NA                      |


