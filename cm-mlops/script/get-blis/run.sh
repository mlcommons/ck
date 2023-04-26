#!/bin/bash
CUR=$PWD
mkdir -p install
test $? -eq 0 || exit $?
INSTALL_DIR=$PWD/install
cd ${CM_BLIS_SRC_PATH}
./configure --prefix=$INSTALL_DIR auto
test $? -eq 0 || exit $?
make -j${CM_HOST_CPU_TOTAL_PHYSICAL_CORES}
test $? -eq 0 || exit $?
make install
test $? -eq 0 || exit $?
