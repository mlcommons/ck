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
function run_model() {
  model="$1"
  test_query_count="$2"
  run "$3"
}
division="closed"
device="cuda"
backend="tensorrt"
implementation="nvidia-original"
category="edge,datacenter"

#Add your run commands here...
# run "$CM_RUN_CMD"
find_performance_cmd='cm run script --tags=generate-run-cmds,inference,_find-performance \
--model=$model --implementation=$implementation --device=$device --backend=$backend \
--category=edge --division=open --scenario=Offline  --quiet --test_query_count=$test_query_count'

run "resnet50" "30000" "${find_performance_cmd}"
run "retinanet" "2000" "${find_performance_cmd}"
run "rnnt" "20000" "${find_performance_cmd}"
run "bert-99" "10000" "${find_performance_cmd}"
run "bert-99.9" "5000" "${find_performance_cmd}"
run "3d-unet" "10" "${find_performance_cmd}"


submission_cmd='cm run script --tags=generate-run-cmds,inference,_submission,_all-scenarios \
--model=$model --implementation=$implementation --device=$device --backend=$backend \
--category=$category --division=$division  --quiet'

run "resnet50" "10" "${submission_cmd}"
run "retinanet" "10" "${submission_cmd}"
run "rnnt" "10" "${submission_cmd}"
run "bert-99" "10" "${submission_cmd}"
run "bert-99.9" "10" "${submission_cmd}"
run "3d-unet" "10" "${submission_cmd}"
