#!/bin/bash

${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/filter.py ${CM_DATASET_CALIBRATION_ANNOTATIONS_FILE_PATH} > ordered.txt
test $? -eq 0 || exit $?
head -n ${CM_CALIBRATION_FILTER_SIZE} ordered.txt >filtered.txt
test $? -eq 0 || exit $?
