#!/bin/bash

CUR=$PWD

if [[ ${CM_CRITEO_FAKE} == "yes" ]]; then
  exit 0
fi
#${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/preprocess.py
