# Nvidia Jetson Nano board

* SDK downloaded on 2021-04-20
* Ubuntu 18.04
* Card: 128GB
* CPU: Quad-core ARM® A57 CPU
  * ARMv8 Processor rev 1 (v8l) x 4
* GPU: NVIDIA Tegra X1 (nvgpu)/integrated
  * 128-core NVIDIA Maxwell™ GPU
* Memory: 4 GB 64-bit LPDDR4

## Notes

* [20210420] Grigori tested ck venv to prepare CK virtual environment 
  and build several python versions - it worked fine.

* [20210420] Grigori managed to build the latest loadgen 
  from [MLCommons inference](https://github.com/mlcommons/inference/tree/master/loadgen)
  (both python version and static library).


## Prerequisites

```
sudo apt install \
           git wget zip bzip2 libz-dev libbz2-dev cmake curl \
           openssh-client vim mc tree \
           gcc g++ autoconf autogen libtool make libc6-dev \
           libssl-dev libbz2-dev libffi-dev \
           python3 python3-pip python3-dev

pip3 install virtualenv
```

## Test CK automation (platform detection)

```
ck pull repo:octoml@mlops

ck detect platform.gpgpu --cuda
```
