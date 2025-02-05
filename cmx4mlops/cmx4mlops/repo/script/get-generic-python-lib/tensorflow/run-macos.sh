#!/bin/bash

CM_PYTHON_BIN=${CM_PYTHON_BIN:-python3}

${CM_PYTHON_BIN} -m pip install tensorflow-macos${CM_TMP_PIP_VERSION_STRING}
test $? -eq 0 || exit 1
echo "CM_GENERIC_PYTHON_PACKAGE_NAME=tensorflow-macos" >> $PWD/tmp-run-env.out
