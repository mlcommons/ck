#!/bin/bash

cmd="${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/process.py"

echo $cmd

eval $cmd
