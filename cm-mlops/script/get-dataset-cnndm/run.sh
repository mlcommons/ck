#!/bin/bash

CUR=${PWD}
mkdir -p install
export DATASET_CNNDM_PATH=${CUR}/install

cd ${CM_MLPERF_INFERENCE_SOURCE}
cd language/gpt-j

if [[ ${CM_DATASET_CALIBRATION} == "no" ]]; then
  cmd="${CM_PYTHON_BIN_WITH_PATH} download_cnndm.py"
  echo $cmd
  eval $cmd
  test $? -eq 0 || exit 1
else
  cmd="${CM_PYTHON_BIN_WITH_PATH} prepare-calibration.py --calibration-list-file calibration-list.txt --output-dir ${DATASET_CNNDM_PATH}"
  echo $cmd
  eval $cmd
  test $? -eq 0 || exit 1
fi
test $? -eq 0 || exit 1
