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
division=$DIVISION
model=$MODEL
device=$DEVICE
category=$CATEGORY
rerun=$RERUN

function run_test() {
  model=$1
  backend=$2
  test_query_count=$3
  implementation=$4
  device=$5
  EXTRA_RUN_ARGS=$7
  echo "model=$model, backend=$2, test_query_count=$3, implementation=$4, device=$5, EXTRA_RUN_ARGS=$7"
  run "$6"
}

#power=' --power=yes --adr.mlperf-power-client.power_server=192.168.0.15 --adr.mlperf-power-client.port=4950 '
results_dir=$HOME/results_dir

#Add your run commands here...
find_performance_cmd='cm run script --tags=generate-run-cmds,inference,_find-performance \
--model=$model --implementation=$implementation --device=$device --backend=$backend \
--category=edge --division=open --scenario=Offline  --quiet --test_query_count=$test_query_count $rerun ${EXTRA_ARGS}'

find_ss_performance_cmd='cm run script --tags=generate-run-cmds,inference,_find-performance \
--model=$model --implementation=$implementation --device=$device --backend=$backend \
--category=edge --division=open --scenario=SingleStream  --quiet --test_query_count=$test_query_count $rerun ${EXTRA_RUN_ARGS}  ${EXTRA_ARGS}'

submission_cmd='cm run script --tags=generate-run-cmds,inference,_submission,_all-scenarios \
--model=$model --implementation=$implementation --device=$device --backend=$backend \
--category=$category --division=$division  --quiet  \
--skip_submission_generation=yes --execution-mode=valid ${POWER_STRING} ${EXTRA_RUN_ARGS} ${EXTRA_ARGS}'

submission_cmd_scenario='cm run script --tags=generate-run-cmds,inference,_submission  --scenario=$scenario \
--model=$model --implementation=$implementation --device=$device --backend=$backend \
--category=$category --division=$division  --quiet  \
--skip_submission_generation=yes --execution-mode=valid ${POWER_STRING} ${EXTRA_RUN_ARGS} ${EXTRA_ARGS}'

readme_cmd_single='cm run script --tags=generate-run-cmds,inference,_populate-readme --scenario=$scenario \
--model=$model --implementation=$implementation --device=$device --backend=$backend \
--category=$category --division=$division  --quiet  \
--skip_submission_generation=yes --execution-mode=valid ${POWER_STRING} ${EXTRA_RUN_ARGS} ${EXTRA_ARGS}'

readme_cmd='cm run script --tags=generate-run-cmds,inference,_populate-readme,_all-scenarios \
--model=$model --implementation=$implementation --device=$device --backend=$backend \
--category=$category --division=$division  --quiet  \
--skip_submission_generation=yes --execution-mode=valid ${POWER_STRING} ${EXTRA_RUN_ARGS} ${EXTRA_ARGS}'


tflite_accuracy_cmd='cm run script --tags=run,mobilenet-models,_tflite,_accuracy-only$extra_tags \
--adr.compiler.tags=gcc \
${extra_option} \
 ${EXTRA_ARGS}'

tflite_performance_cmd='cm run script --tags=run,mobilenet-models,_tflite,_performance-only$extra_tags \
${POWER_STRING} \
--adr.compiler.tags=gcc \
${extra_option} \
 ${EXTRA_ARGS}'

tflite_readme_cmd='cm run script --tags=run,mobilenet-models,_tflite,_populate-readme$extra_tags \
${POWER_STRING} \
--adr.compiler.tags=gcc \
${extra_option} \
 ${EXTRA_ARGS}'
