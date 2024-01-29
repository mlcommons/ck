#!/bin/bash

export PATH=${CM_CONDA_BIN_PATH}:$PATH

export CALIBRATION_DATA_JSON=${CM_CALIBRATION_DATASET_CNNDM_PATH}


if [[ ${CM_ML_MODEL_WEIGHT_DATA_TYPES} == "int4" ]]; then
  export INT4_CALIBRATION_DIR=${PWD}/quantized-int4-model
  bash ${CM_TMP_CURRENT_SCRIPT_PATH}/run-int4-calibration.sh
  cd ${CM_HARNESS_CODE_ROOT}
  bash run_quantization_int4.sh
else
  cd ${CM_HARNESS_CODE_ROOT}
  bash run_quantization.sh
fi

test $? -eq 0 || exit $?
