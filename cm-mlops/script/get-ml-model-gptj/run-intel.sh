#!/bin/bash

echo ${CM_HARNESS_CODE_ROOT}
cd ${CM_HARNESS_CODE_ROOT}


export CALIBRATION_DATA_JSON=${CM_CALIBRATION_DATASET_CNNDM_PATH}
export VALIDATION_DATA_JSON=${CM_DATASET_CNNDM_EVAL_PATH}
export INT4_CALIBRATION_DIR=${WORKLOAD_DATA}/quantized-int4-model
#sudo -E bash run_quantization.sh
bash run_quantization.sh
