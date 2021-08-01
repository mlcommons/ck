**[ [TOC](../README.md) ]**

# Rapsberry Pi 4 with a standard port of Debian

* OS release: 2021-03-04 (32-but)
* Memory: 4GB

## Notes: 

* [20210422] Grigori tested ck venv to prepare CK virtual environment 
  and build several python versions - it worked fine.

* [20210423] Grigori attempted to build loadgen 
  from [MLCommons&trade; inference](https://github.com/mlcommons/inference/tree/master/loadgen)
  but it fails during C++ compliation. 

  The earlier revision of loadgen (r0.5?) works - this means that it's possible 
  to fix the latest version if needed.

  [Ubuntu 20.04 64-bit]() seems to work fine.

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

