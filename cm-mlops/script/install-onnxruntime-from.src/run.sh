#!/bin/bash

export CC=${CM_GCC_BIN_WITH_PATH}
export CXX=${CM_GCC_INSTALLED_PATH}/g++

echo "cd ${CM_RUN_DIR}"
cd ${CM_RUN_DIR}
test $? -eq 0 || exit $?
rm -rf build

echo ${CM_RUN_CMD}
eval ${CM_RUN_CMD}
test $? -eq 0 || exit $?

exit 1
