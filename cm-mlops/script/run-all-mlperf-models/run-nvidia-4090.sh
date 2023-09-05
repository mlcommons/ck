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
division="open"
division="closed"
device="cuda"
backend="tensorrt"
implementation="nvidia-original"
category="datacenter-edge"
category="edge"
power=""
power=" --power=yes --adr.mlperf-power-client.power_server=192.168.0.15"
#Add your run commands here...
# run "$CM_RUN_CMD"
find_performance_cmd='cm run script --tags=generate-run-cmds,inference,_find-performance \
--model=$model --implementation=$implementation --device=$device --backend=$backend \
--category=edge --division=open --scenario=Offline  --quiet --test_query_count=$test_query_count'

#run "resnet50" "100000" "${find_performance_cmd}"
#run "retinanet" "10000" "${find_performance_cmd}"
#run "rnnt" "100000" "${find_performance_cmd}"
#run "bert-99" "20000" "${find_performance_cmd}"
#run "3d-unet" "30" "${find_performance_cmd}"


submission_cmd='cm run script --tags=generate-run-cmds,inference,_submission,_all-scenarios \
--model=$model --execution-mode=valid --implementation=$implementation --device=$device --backend=$backend --results_dir=$HOME/results_dir \
--category=$category --division=$division --skip_submission_generation=yes --quiet $power'

#run_model "bert-99.9" "10" "${submission_cmd} --offline_target_qps=1680 --server_target_qps=1520"
run_model "resnet50" "10" "${submission_cmd} --offline_target_qps=45000 --server_target_qps=38000 --singlestream_target_latency=0.2 --multistream_target_latency=0.4"
run_model "rnnt" "10" "${submission_cmd} --offline_target_qps=15200 --server_target_qps=14150 --singlestream_target_latency=23"
run_model "retinanet" "10" "${submission_cmd} --offline_target_qps=620 --server_target_qps=590 --singlestream_target_latency=2 --multistream_target_latency=14"
run_model "bert-99" "10" "${submission_cmd} --offline_target_qps=4100 --server_target_qps=3950 --singlestream_target_latency=1"
run_model "3d-unet-99.9" "10" "${submission_cmd} --offline_target_qps=4 --singlestream_target_latency=433 --env.CM_MLPERF_USE_MAX_DURATION=no"
