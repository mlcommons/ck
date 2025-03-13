#!/bin/bash
CUR=$PWD
cd ${CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH}
${CM_PYTHON_BIN_WITH_PATH} scripts/custom_systems/add_custom_system.py
test $? -eq 0 || exit $?
