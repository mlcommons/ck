#!/bin/bash

CUR_DIR=$PWD
rm -rf kineto
cp -r ${CM_PYTORCH_KINETO_SRC_REPO_PATH} kineto
cd kineto
rm -rf libkineto/build

mkdir -p libkneto/build && cd libkineto/build
cmake ..
test $? -eq 0 || exit $?
make
test $? -eq 0 || exit $?
sudo make install
test $? -eq 0 || exit $?
