#!/bin/bash
if [[ ${CM_MLPERF_CPP} == "yes" ]]; then
  exit 0
fi

cmd=${CM_MLPERF_RUN_CMD}
echo "${cmd}"
eval "${cmd}"
test $? -eq 0 || exit 1
