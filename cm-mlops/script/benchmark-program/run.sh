#!/bin/bash
if [[ ${CM_MLPERF_POWER} == "yes" && ${CM_MLPERF_LOADGEN_MODE} == "performance" ]]; then
    exit 0
fi

# Run
if [ -z ${CM_RUN_DIR} ]; then
  echo "CM_RUN_DIR is not set"
  exit 1
fi

cd ${CM_RUN_DIR}

if [[ "${CM_DEBUG_SCRIPT_BENCHMARK_PROGRAM}" == "True" ]]; then
  echo "*****************************************************"
  echo "You are now in Debug shell with pre-set CM env and can run the following command line manually:"

  echo ""
  if [[ "${CM_RUN_CMD0}" != "" ]]; then
    echo "${CM_RUN_CMD0}"
  else
    echo "${CM_RUN_CMD}"
  fi

  echo ""
  echo "Type exit to return to CM script."
  echo ""
#  echo "You can also run . ./debug-script-benchmark-program.sh to reproduce and customize run."
#  echo ""
#
#  cp -f tmp-run.sh debug-script-benchmark-program.sh
#
#  sed -e 's/CM_DEBUG_SCRIPT_BENCHMARK_PROGRAM="True"/CM_DEBUG_SCRIPT_BENCHMARK_PROGRAM="False"/g' -i debug-script-benchmark-program.sh

  bash

  # do not re-run command below to pick up manual run!
  exit 0
fi

# Check CM_RUN_CMD0
if [[ "${CM_RUN_CMD0}" != "" ]]; then
  eval ${CM_RUN_CMD0}
else
  eval ${CM_RUN_CMD}
fi

test $? -eq 0 || exit 1
