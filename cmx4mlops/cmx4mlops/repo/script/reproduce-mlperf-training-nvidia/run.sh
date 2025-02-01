#!/bin/bash
if [[ ${CM_CALL_MLPERF_RUNNER} == "no" ]]; then
  cd ${CM_RUN_DIR}
  cmd=${CM_RUN_CMD}
  echo "${cmd}"
  eval "${cmd}"
  test $? -eq 0 || exit $?
fi
