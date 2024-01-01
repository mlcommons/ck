#!/bin/bash

${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/filter.py ${CM_DATASET_OPENIMAGES_ANNOTATIONS_FILE_PATH} > ordered.txt
test $? -eq 0 || exit $?

head -n 400 ordered.txt >filtered.txt
