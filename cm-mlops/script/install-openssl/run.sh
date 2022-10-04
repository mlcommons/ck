#!/bin/bash

CUR_DIR=$PWD

echo "***********************************************************"
CM_MAKE_CORES=${CM_MAKE_CORES:-${CM_HOST_CPU_TOTAL_CORES}}
CM_MAKE_CORES=${CM_MAKE_CORES:-2}
CM_WGET_URL=https://www.openssl.org/source/openssl-${CM_VERSION}g.tar.gz
wget ${CM_WGET_URL}
tar -xzf openssl-${CM_VERSION}g.tar.gz && cd openssl-${CM_VERSION}g
./config
make -j${CM_MAKE_CORES}
sudo make install
sudo ln -s /usr/local/bin/openssl /usr/bin/openssl

