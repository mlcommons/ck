#!/bin/bash

${CM_PYTHON_BIN} ${CM_TMP_CURRENT_SCRIPT_PATH}/process.py
test $? -eq 0 || exit 1
