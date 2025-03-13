#!/bin/bash

${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/detect.py
test $? -eq 0 || exit $?
