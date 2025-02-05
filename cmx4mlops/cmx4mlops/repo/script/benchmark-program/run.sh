#!/bin/bash

# function to safely exit the background process
safe_exit() {
  if [[ "${CM_POST_RUN_CMD}" != "" ]]; then
    eval ${CM_POST_RUN_CMD}
    if [ $? -eq 0 ]; then
      exit 0
    else
      exit $?
    fi
  fi
}

# trap signals to redirect the execution flow to safe_exit
trap safe_exit SIGINT SIGTERM

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

echo $CM_PRE_RUN_CMD
eval ${CM_PRE_RUN_CMD}

# Function to run command and check exit status
run_command() {
  local cmd="$1"
  
  if [[ -n "$cmd" ]]; then
    echo "$cmd"
    eval "$cmd"
    exitstatus=$?

    # If 'exitstatus' file exists, overwrite the exit status with its content
    if [[ -e exitstatus ]]; then
      exitstatus=$(cat exitstatus)
    fi

    # If exitstatus is non-zero, exit with that status
    if [[ $exitstatus -ne 0 ]]; then
      exit $exitstatus
    fi
  fi
}

# Run CM_RUN_CMD0 if it exists, otherwise run CM_RUN_CMD
if [[ -n "$CM_RUN_CMD0" ]]; then
    run_command "$CM_RUN_CMD0"
fi

run_command "$CM_RUN_CMD"


# Run post-run command if it exists
if [[ -n "$CM_POST_RUN_CMD" ]]; then
  eval "$CM_POST_RUN_CMD"
  post_exitstatus=$?
  # Exit if post-run command fails
  if [[ $post_exitstatus -ne 0 ]]; then
    exit $post_exitstatus
  fi
fi

# Final check for exitstatus and exit with the appropriate code
if [[ $exitstatus -ne 0 ]]; then
  exit $exitstatus
fi
