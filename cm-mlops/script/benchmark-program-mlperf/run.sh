#!/bin/bash

# Run
if [ -z ${CM_RUN_DIR} ]; then
  echo "CM_RUN_DIR is not set"
  exit 1
fi

cd ${CM_RUN_DIR}

if [[ "${CM_DEBUG_SCRIPT_BENCHMARK_PROGRAM}" == "True" ]]; then
  echo "*****************************************************"
  echo "You are now in Debug shell with pre-set CM env and can run above CMD manually."
  echo ""
  echo "Type exit to return to CM script."
  echo ""
  echo "You can also run . ./debug-script-benchmark-program.sh to reproduce and customize run."
  echo ""

  cp -f tmp-run.sh debug-script-benchmark-program.sh

  sed -e 's/CM_DEBUG_SCRIPT_BENCHMARK_PROGRAM="True"/CM_DEBUG_SCRIPT_BENCHMARK_PROGRAM="False"/g' -i debug-script-benchmark-program.sh

  bash

  exit 1
fi

eval ${CM_RUN_CMD}

test $? -eq 0 || exit 1
