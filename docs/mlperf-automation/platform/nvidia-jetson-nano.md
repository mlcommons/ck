**[ [TOC](../README.md) ]**

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
  from [MLCommons&trade; inference](https://github.com/mlcommons/inference/tree/master/loadgen)
  (both python version and static library).


## Prerequisites

```
sudo apt install \
           git wget zip bzip2 libz-dev libbz2-dev cmake curl \
           openssh-client vim mc tree \
           gcc g++ autoconf autogen libtool make libc6-dev \
           libssl-dev libbz2-dev libffi-dev \
           python3 python3-pip python3-dev \
           libncurses5 libncurses5-dev

python3 -m pip install virtualenv
```

## Test CK automation (platform detection)

```
ck pull repo:mlcommons@ck-mlops

ck detect platform.gpgpu --cuda
```

## Notes
* Prebuilt LLVM v12.0.0 doesn't work (requires newer libraries). One should use 11.0.1:
  * ```ck install package --tags=compiler,llvm,prebuilt,v11.0.1```

* Install TVM with CUDA:
  * ```ck install package --tags=tvm,src,dev-cuda```
