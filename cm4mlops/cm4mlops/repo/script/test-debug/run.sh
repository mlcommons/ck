#!/bin/bash

echo "========================================================"

${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/python/main.py
test $? -eq 0 || exit 1

echo ========================================================
