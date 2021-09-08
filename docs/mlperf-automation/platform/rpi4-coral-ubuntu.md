**[ [TOC](../README.md) ]**

# Rapsberry Pi 4 with Ubuntu Server 20.04.2 LTS 64-bit with Coral Edge TPU

First install the board and the dependencies as described [here](rpi4-ubuntu.md).

## Coral Edge TPU setup

You can find extended notes [here](https://coral.ai/docs/accelerator/get-started/#1-install-the-edge-tpu-runtime).

1. Add Debian package to the system:

```
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt-get update
```

2. Install Edge TPU run-time:
```
sudo apt-get install libedgetpu1-std
```

3. Disconnect and connect again Coral Edge TPU.

4. To get maximum performance for MLPerf&trade;, install a package with maximum operational frequency:
```
sudo apt-get install libedgetpu1-max

```

5. Add current user to plugdev group (otherwise need to run inference with sudo)!

```
sudo usermod -aG plugdev $USER
```

## Notes

* [20210428] Grigori tested basic Edge TPU setup with Python 3.7.10:

```
ck pull repo:mlcommons@ck-venv
ck create venv:test
ck activate venv:test

ck pull repo:mlcommons@ck-mlops

ck detect platform.os --platform_init_uoa=generic-linux-dummy
ck detect soft:compiler.python --full_path=$CK_VENV_PYTHON_BIN

ck run program:test-coral-edge-tpu-installation
```

* [20210428] Grigori tested MLPerf&trade; inference with libedgetpu1-max v15.0:


## Misc

* https://wiki.st.com/stm32mpu/wiki/How_to_compile_model_and_run_inference_on_Coral_Edge_TPU_using_STM32MP1
* https://github.com/google-coral/edgetpu/issues/201
