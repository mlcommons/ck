#!/bin/bash
export PATH=${CM_CONDA_BIN_PATH}:$PATH
cd ${CM_MLPERF_INFERENCE_INTEL_CALIBRATION_PATH}
CUR_DIR=$(pwd)
export WORKLOAD_DATA=${CUR_DIR}/data
mkdir -p ${WORKLOAD_DATA}

echo $PATH
python download-calibration-dataset.py --calibration-list-file calibration-list.txt --output-dir ${WORKLOAD_DATA}/calibration-data

export CALIBRATION_DATA_JSON=${WORKLOAD_DATA}/calibration-data/cnn_dailymail_calibration.json

export CHECKPOINT_DIR=${WORKLOAD_DATA}/gpt-j-checkpoint
cmd="ln -s ${GPTJ_CHECKPOINT_PATH} ${CHECKPOINT_DIR}"
echo $cmd
eval $cmd

export QUANTIZED_MODEL_DIR=${WORKLOAD_DATA}/quantized-int4-model

mkdir -p ${QUANTIZED_MODEL_DIR}
bash run_calibration_int4.sh
test $? -eq 0 || exit $?
exit 0
