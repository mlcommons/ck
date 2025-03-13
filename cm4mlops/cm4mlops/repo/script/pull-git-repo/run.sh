#!/bin/bash

CUR_DIR=$PWD
SCRIPT_DIR=${CM_TMP_CURRENT_SCRIPT_PATH}

path=${CM_GIT_CHECKOUT_PATH}
echo "cd $path"

cd $path
test $? -eq 0 || exit $?

echo ${CM_GIT_PULL_CMD}
eval ${CM_GIT_PULL_CMD}
#don't fail if there are local changes
#test $? -eq 0 || exit $?

cd $CUR_DIR
