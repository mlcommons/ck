**[ [TOC](../README.md) ]**

# Rapsberry Pi 4 with Ubuntu Server 20.04.2 LTS 64-bit

* OS release: 2021-02-04 (64-bit)
* Card: 128GB
* Memory: 4GB


## Notes

* [20210422] Grigori tested ck venv to prepare CK virtual environment 
  and build several python versions - it worked fine.

* [20210423] Grigori managed to build the latest loadgen 
  from [MLCommons&trade; inference](https://github.com/mlcommons/inference/tree/master/loadgen)
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
