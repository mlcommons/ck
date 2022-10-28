#!/bin/bash
if [ ! -z ${CM_IMAGENET_PREPROCESSED_PATH+x} ]; then
    exit 0
fi
${CM_PYTHON_BIN} -m pip install -r ${CM_TMP_CURRENT_SCRIPT_PATH}/requirements.txt
${CM_PYTHON_BIN} ${CM_TMP_CURRENT_SCRIPT_PATH}/preprocess.py
