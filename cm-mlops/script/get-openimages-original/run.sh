#!/bin/bash

CUR=${PWD}
mkdir -p install
INSTALL_DIR=${CUR}/install

${CM_PYTHON_BIN} -m pip install fiftyone

cd ${CM_MLC_INFERENCE_VISION_PATH}
cd tools

if [[ ${CM_DATASET_CALIBRATION} == "no" ]]; then
  ./openimages_mlperf.sh -d ${INSTALL_DIR}
  test $? -eq 0 || exit 1
  cd $CUR
  echo "CM_DATASET_PATH=${INSTALL_DIR}/validation/data" > tmp-run-env.out
else
  ./openimages_calibration_mlperf.sh -d ${INSTALL_DIR}
  test $? -eq 0 || exit 1
  cd $CUR
  echo "CM_CALIBRATION_DATASET_PATH=${INSTALL_DIR}" > tmp-run-env.out
  cd $INSTALL_DR
  wget ${CM_CALIBRATION_DATASET_WGET_URL}
  test $? -eq 0 || exit 1
fi

