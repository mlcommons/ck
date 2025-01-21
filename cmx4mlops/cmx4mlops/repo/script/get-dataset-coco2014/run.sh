#!/bin/bash
python3() {
  ${CM_PYTHON_BIN_WITH_PATH} "$@"
}
export -f python3

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

  # deleting existing incomplete downloads if any
  if [ -f "${INSTALL_DIR}/download_aux/annotations_trainval2014.zip" ]; then
    echo "File annotations_trainval2014.zip already exists. Deleting it."
    rm ${INSTALL_DIR}/download_aux/annotations_trainval2014.zip
  fi
  
  cmd="./download-coco-2014.sh -d ${INSTALL_DIR}  ${max_images}"
  echo $cmd
  eval $cmd
  test $? -eq 0 || exit $?
else
  cmd="./download-coco-2014-calibration.sh -d ${INSTALL_DIR}"
  echo $cmd
  eval $cmd
  test $? -eq 0 || exit $?
fi
if [[ ${CM_GENERATE_SAMPLE_ID} == "yes" ]]; then
  cmd="python3 sample_ids.py --tsv-path ${INSTALL_DIR}/captions/captions.tsv --output-path ${INSTALL_DIR}/sample_ids.txt"
  echo $cmd
  eval $cmd
  test $? -eq 0 || exit $?
fi
cd ${INSTALL_DIR}

test $? -eq 0 || exit $?
