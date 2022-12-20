**[ [TOC](../README.md) ]**

# x8664-based generic platforms with Ubuntu

* Ubuntu 18.04 or 20.04
* Sample platform: Lenovo T470p with Intel Core i5-7300HQ


## Notes

* [20210813] Grigori successfully tested this setup with the 
  [MLPerf end-to-end submission system](https://github.com/mlcommons/ck-mlops/tree/main/module/bench.mlperf.inference)
  for TVM, ONNX, PyTorch, TF and TFLite
  across Azure, AWS and GCP nodes.

* [20210421] Grigori tested ck venv to prepare CK virtual environment 
  and build several python versions - it worked fine.

* [20210421] Grigori managed to build the latest loadgen 
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
