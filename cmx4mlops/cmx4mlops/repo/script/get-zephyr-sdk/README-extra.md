# GET-ZEPHYR-SDK
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) installs the [Zephyr-SDK](https://github.com/zephyrproject-rtos/sdk-ng/releases) from a prebuilt binary. 

## Install
```bash
cm run script --tags=get,zephyr-sdk --version=0.13.2
```
## Exported Variables
1. [ZEPHYR_SDK_INSTALL_DIR](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-zephyr-sdk/customize.py#L13): Location in CM cache where Zephyr SDK is installed. 
2. [ZEPHYR_TOOLCHAIN_VARIANT](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-zephyr-sdk/customize.py#L12)

## Supported Versions
1. 0.13.1
2. 0.13.2
3. 0.15.0

## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
2. RHEL 9
