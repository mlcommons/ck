#!/bin/bash

CM_TMP_CURRENT_SCRIPT_PATH=${CM_TMP_CURRENT_SCRIPT_PATH:-$PWD}

${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/detect-version.py > tmp-ver.out 2> tmp-ver.err

echo "********************************"
cat tmp-ver.out
cat tmp-ver.err
echo "********************************"
