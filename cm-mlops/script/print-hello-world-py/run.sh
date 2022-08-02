#!/bin/bash

CM_TMP_CURRENT_SCRIPT_PATH=${CM_TMP_CURRENT_SCRIPT_PATH:-$PWD}

which ${CM_PYTHON_BIN}
${CM_PYTHON_BIN} --version

${CM_PYTHON_BIN} ${CM_TMP_CURRENT_SCRIPT_PATH}/code.py
test $? -eq 0 || exit $?

echo "CM_NEW_VAR_FROM_RUN=$MLPERF_XYZ" > tmp-run-env.out
