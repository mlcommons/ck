#!/bin/bash

cmd="cd ${CM_RUN_DIR}"
echo "$cmd"
eval "$cmd"

if [[ ${CM_MLPERF_MODEL} == "bert" ]]; then
  bash ${CM_TMP_CURRENT_SCRIPT_PATH}/run-bert-training.sh
  test $? -eq 0 || exit $?
fi
