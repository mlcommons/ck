#!/bin/bash
if [ ! -z ${CM_IMAGENET_PREPROCESSED_PATH+x} ]; then
    exit 0
fi
${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/preprocess.py
test $? -eq 0 || exit 1
