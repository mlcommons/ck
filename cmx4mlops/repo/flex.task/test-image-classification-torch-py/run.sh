#!/bin/bash

# ${CMX_PYTHON_WITH_PATH} -m pip install -r ${CMX_PATH_TO_FLEX_TASK}/requirements.txt
#test $? -eq 0 || exit $?

${CMX_PYTHON_WITH_PATH} ${CMX_PATH_TO_FLEX_TASK}/src/classify.py
test $? -eq 0 || exit $?
