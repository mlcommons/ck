#!/bin/bash

CUR_DIR=$PWD

echo "***********************************************************"
CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_CPU_TOTAL_CORES}}
CM_MAKE_CORES=${CM_MAKE_CORES:-2}
CM_WGET_URL=https://www.openssl.org/source/openssl-${CM_VERSION}g.tar.gz
wget -nc ${CM_WGET_URL}
test $? -eq 0 || exit 1
tar -xzf openssl-${CM_VERSION}g.tar.gz && cd openssl-${CM_VERSION}g
test $? -eq 0 || exit 1
mkdir -p install
./config --prefix=`pwd`/install
make -j${CM_MAKE_CORES}
test $? -eq 0 || exit 1
make install
