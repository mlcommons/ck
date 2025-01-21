#!/bin/bash
cd ${CM_NVIDIA_MITTEN_SRC}
${CM_PYTHON_BIN_WITH_PATH} -m pip install .
test $? -eq 0 || exit $?
