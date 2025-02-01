#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo ""

cd /shared/python-runners/

chmod 777 /shared/gem5/build/X86/gem5-mesi.fast
${CM_PYTHON_BIN_WITH_PATH} meta-runner.py

test $? -eq 0 || exit 1
