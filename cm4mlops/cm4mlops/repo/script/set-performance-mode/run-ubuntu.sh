#!/bin/bash

#CM Script location: ${CM_TMP_CURRENT_SCRIPT_PATH}

#To export any variable
#echo "VARIABLE_NAME=VARIABLE_VALUE" >>tmp-run-env.out

#${CM_PYTHON_BIN_WITH_PATH} contains the path to python binary if "get,python" is added as a dependency



function exit_if_error() {
  test $? -eq 0 || exit $?
}

function run() {
  echo "Running: "
  echo "$1"
  echo ""
  if [[ ${CM_FAKE_RUN} != 'yes' ]]; then
    eval "$1"
    exit_if_error
  fi
}
CM_SUDO="sudo"
#Add your run commands here...
# run "$CM_RUN_CMD"
run "${CM_SUDO} apt-get install -y linux-tools-common linux-tools-generic linux-tools-`uname -r`"
run "${CM_SUDO} cpupower frequency-set -g performance"
if [[ ${CM_SET_OS_PERFORMANCE_REPRODUCIBILITY_MODE} != "no" ]]; then
  run "${CM_SUDO} sysctl -w vm.dirty_ratio=8"
  run "${CM_SUDO} sysctl -w vm.swappiness=1"
  run "${CM_SUDO} sysctl -w vm.zone_reclaim_mode=1"
  run "${CM_SUDO} sync; sysctl -w vm.drop_caches=3"
  run "${CM_SUDO} sysctl -w kernel.randomize_va_space=0"
fi
