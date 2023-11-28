#!/bin/bash

CUR=${PWD}
mkdir -p install
INSTALL_DIR=${CUR}/install

cd ${CM_RUN_DIR}

if [[ ${CM_DATASET_CALIBRATION} == "no" ]]; then
  if [ ! -z ${CM_DATASET_SIZE} ]; then
    max_images=" -m ${CM_DATASET_SIZE}"
  else
    max_images=""
  fi
  cmd="./download-coco-2014.sh -d ${INSTALL_DIR}  ${max_images}"
  echo $cmd
  eval $cmd
  test $? -eq 0 || exit 1
else
  cmd="./download-coco-2014-calibration.sh -d ${INSTALL_DIR}"
  echo $cmd
  eval $cmd
  test $? -eq 0 || exit 1
fi
cd ${INSTALL_DIR}

test $? -eq 0 || exit 1
