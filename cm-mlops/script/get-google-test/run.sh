#!/bin/bash
CUR=$PWD
mkdir -p install
INSTALL_DIR=$CUR/install
cd ${CM_GIT_REPO_CHECKOUT_PATH}
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=${INSTALL_DIR} ..
test $? -eq 0 || exit $?

CMD="make install"
echo ${CMD}
eval $CMD
test $? -eq 0 || exit $?
