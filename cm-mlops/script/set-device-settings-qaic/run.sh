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
IFS="," read -r -a devices <<< "$CM_QAIC_DEVICES"

if [[ -n ${CM_QAIC_VC} ]]; then
  for device in ${devices[@]}
  do
     run "sudo ${CM_QAIC_TOOLS_PATH}/qaic-diag -d $device -m 0x4B 0x66 0x05 0x1 ${CM_QAIC_VC_HEX}"
  done
fi

if [[ ${CM_QAIC_ECC} == "yes" ]]; then
  for device in ${devices}
  do
     run "sudo ${CM_QAIC_TOOLS_PATH}/qaic-monitor-json -i request_$device.json"
     run "rm request_$device.json"
  done
fi

