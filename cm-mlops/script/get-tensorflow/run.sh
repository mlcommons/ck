#!/bin/bash

CM_TMP_CURRENT_SCRIPT_PATH=${CM_TMP_CURRENT_SCRIPT_PATH:-$PWD}

${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/detect-version.py > tmp-ver.out
TF_INC=`${CM_PYTHON_BIN_WITH_PATH} -c 'import tensorflow as tf; print(tf.sysconfig.get_include())'`
TF_LIB=`${CM_PYTHON_BIN_WITH_PATH} -c 'import tensorflow as tf; print(tf.sysconfig.get_lib())'`
test $? -eq 0 || exit 1

echo "TF_INC=$TF_INC" >> tmp-run-env.out
echo "TF_LIB=$TF_LIB" >> tmp-run-env.out
