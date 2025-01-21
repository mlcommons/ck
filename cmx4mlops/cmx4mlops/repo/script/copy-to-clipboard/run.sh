#!/bin/bash

${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/code.py
test $? -eq 0 || exit 1
