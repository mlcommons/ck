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
run "screen cmr 'run mobilenet-models _tflite _accuracy-only' \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results"

screen cmr "run mobilenet-models _tflite _performance-only" \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results

cmr "run mobilenet-models _tflite _populate-readme" \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results

cmr "run mobilenet-models _tflite _armnn _neon _accuracy-only" \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results

cmr "run mobilenet-models _tflite _armnn _neon _accuracy-only" \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results

cmr "run mobilenet-models _tflite _armnn _neon _accuracy-only" \
--adr.compiler.tags=gcc \
--results_dir=$HOME/mobilenet_results
