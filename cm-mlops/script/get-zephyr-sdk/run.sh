#!/bin/bash
env
CM_TMP_CURRENT_SCRIPT_PATH=${CM_TMP_CURRENT_SCRIPT_PATH:-$PWD}
echo $PWD
version=${CM_ZEPHYR_SDK_VERSION}
os=${CM_HOST_OS_TYPE}
if [ $os == "darwin" ]; then
  os=${CM_HOST_OS_FLAVOR}
fi
platform=${CM_HOST_OS_MACHINE}
if [ $platform == "arm64" ]; then
  platform=aarch64
fi

file=zephyr-sdk-${version}-${os}-${platform}-setup.run
url=https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v${version}/$file
wget "${url}"
if [ "${?}" != "0" ]; then exit 1; fi
chmod +x $file
./file -- -d $CUR/zephyr-sdk-$version

if [ "${?}" != "0" ]; then exit 1; fi

