#!/bin/bash
if [[ ${CM_MLPERF_POWER} == "yes" && ${CM_MLPERF_LOADGEN_MODE} == "performance" ]]; then
    exit 0
fi
# Run
if [ -z ${CM_RUN_DIR} ]; then
  echo "CM_RUN_DIR is not set"
  exit 1
fi

echo "Run Directory: ${CM_RUN_DIR}"

cd ${CM_RUN_DIR}

echo "CMD: ${CM_RUN_CMD}"
eval ${CM_RUN_CMD}

test $? -eq 0 || exit 1
