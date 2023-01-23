**[ [TOC](../README.md) ]**

# Rapsberry Pi 4 with Ubuntu Server 20.04.2 LTS 64-bit

* OS release: 2021-02-04 (64-bit)
* Card: 128GB
* Memory: 4GB


## Notes

* [20210816] Grigori updated docs about the power supply and cooling.

* [20210812] Grigori updated docs to set up swap disk to run TVM with large models.

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
           python3 python3-pip python3-dev \
           libncurses5 libncurses5-dev

python3 -m pip install virtualenv
```

## Prepare large SWAP disk

```bash
sudo apt install dphys-swapfile
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile
```

Update the following lines (10GB swap):
* ```CONF_SWAPSIZE=10240```
* ```CONF_MAXSWAP=10240```

Initialize swap disk:

```bash
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
sudo reboot
```

## Check power supply and cooling 

You need to make sure that you have a native power supply (5.1V 2.5A) 
and cooling to have stable MLPerf results.

See our [power supply](images/rpi4-power-supply1.jpg) 
and [cooling](images/rpi4-cooling.jpg)
used to submit results to MLPerf v1.1.

## Set up CK scripts to set CPU frequency to max

```bash
ck detect platform.os --update_platform_init --platform_init_uoa=rpi4
```

Turn off scripts to handle frequency (use dummy linux scripts):
```bash
ck detect platform.os --update_platform_init --platform_init_uoa=generic-linux-dummy
```
