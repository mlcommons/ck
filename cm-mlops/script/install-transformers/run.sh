#!/bin/bash

${CM_PYTHON_BIN_WITH_PATH} -m pip install transformers${CM_TMP_PIP_VERSION_STRING}
test $? -eq 0 || exit 1
