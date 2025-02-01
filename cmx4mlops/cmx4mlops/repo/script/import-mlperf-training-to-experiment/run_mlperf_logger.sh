#!/bin/bash

echo ""
${CM_PYTHON_BIN_WITH_PATH} -m mlperf_logging.result_summarizer "${CM_MLPERF_TRAINING_REPO_PATH}/{*}" training ${CM_MLPERF_TRAINING_REPO_VERSION}.0 -csv summary.csv
# --xls summary.xlsx   # Does't work with the latest pandas (need .close() instead of .save())

#${CM_MLPERF_LOGGING_SRC_PATH}/scripts/verify_for_v${CM_MLPERF_TRAINING_REPO_VERSION}_training.sh "${CM_MLPERF_TRAINING_REPO_PATH}/ASUSTeK"

test $? -eq 0 || exit $?
