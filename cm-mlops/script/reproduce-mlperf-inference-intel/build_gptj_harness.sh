#!/bin/bash

export PATH=${CM_CONDA_BIN_PATH}:$PATH
echo $PWD

if [ ! -d harness ]; then
  mkdir -p harness
fi

echo ${CM_HARNESS_CODE_ROOT}
cd ${CM_HARNESS_CODE_ROOT}
cd utils
python -m pip install .
test $? -eq 0 || exit $?
cd ../


mkdir -p data
export WORKLOAD_DATA=$(pwd)/data
mkdir -p ${WORKLOAD_DATA}/model

export INT8_MODEL_DIR=${WORKLOAD_DATA}/gpt-j-int8-model
export INT4_MODEL_DIR=${WORKLOAD_DATA}/gpt-j-int4-model
python download-calibration-dataset.py --calibration-list-file calibration-list.txt --output-dir ${WORKLOAD_DATA}/calibration-data

python download-dataset.py --split validation --output-dir ${WORKLOAD_DATA}/validation-data

export CALIBRATION_DATA_JSON=${WORKLOAD_DATA}/calibration-data/cnn_dailymail_calibration.json
export VALIDATION_DATA_JSON=${WORKLOAD_DATA}/validation-data/cnn_dailymail_validation.json
export INT4_CALIBRATION_DIR=${WORKLOAD_DATA}/quantized-int4-model
#sudo -E bash run_quantization.sh
python -m pip install mpi4py
bash run_quantization.sh
exit 1
test $? -eq 0 || exit $?
