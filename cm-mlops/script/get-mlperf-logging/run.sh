#!/bin/bash

echo ""

cd ${CM_MLPERF_LOGGING_SRC_PATH}

${CM_PYTHON_BIN_WITH_PATH} setup.py install
test $? -eq 0 || exit 1
