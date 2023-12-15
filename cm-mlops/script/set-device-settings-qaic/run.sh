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

#Add your run commands here...
# run "$CM_RUN_CMD"

set IFS=','
if [[ -n ${CM_QAIC_VC} ]]; then
  for device in ${CM_QAIC_DEVICES}
  do
     run "${CM_QAIC_TOOLS_PATH}/qaic-diag -d $device 0x4B 0x66 0x05 0x1 ${CM_QAIC_VC}"
  done
fi

if [[ ${CM_QAIC_ECC} == "yes" ]]; then
  for device in ${CM_QAIC_DEVICES}
  do
     run "${CM_QAIC_TOOLS_PATH}/qaic-monitor-json -i request_$device.json"
     run "rm request_$device.json"
  done
fi

