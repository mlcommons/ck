#!/bin/bash

${CMX_PYTHON_WITH_PATH} ${CMX_PATH_TO_FLEX_TASK}/src/test.py
test $? -eq 0 || exit $?
