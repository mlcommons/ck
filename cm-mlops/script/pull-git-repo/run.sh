#!/bin/bash

CUR_DIR=$PWD
SCRIPT_DIR=${CM_TMP_CURRENT_SCRIPT_PATH}

path=${CM_GIT_CHECKOUT_PATH}
echo "cd $path"

cd $path
test $? -eq 0 || exit 1

echo ${CM_GIT_PULL_CMD}
eval ${CM_GIT_PULL_CMD}
test $? -eq 0 || exit 1

cd $CUR_DIR
