#!/bin/bash

CUR_DIR=$PWD

echo "***********************************************************"
CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_CPU_TOTAL_CORES}}
CM_MAKE_CORES=${CM_MAKE_CORES:-2}
CM_WGET_URL=https://github.com/gflags/gflags/archive/refs/tags/v${CM_VERSION}.tar.gz
wget -nc ${CM_WGET_URL}
test $? -eq 0 || exit 1
tar -xzf "v${CM_VERSION}.tar.gz" && cd gflags-${CM_VERSION}
test $? -eq 0 || exit 1
rm -rf build
mkdir build && cd build
cmake ..
make -j${CM_MAKE_CORES}
test $? -eq 0 || exit 1
sudo make install
