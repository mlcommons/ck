export PATH=${CM_CONDA_BIN_PATH}:$PATH

export DATA_CAL_DIR=${CM_HARNESS_CODE_ROOT}/calibration_dataset
export CHECKPOINT=${CM_ML_MODEL_FILE_WITH_PATH}

cd ${CM_HARNESS_CODE_ROOT}

bash generate_torch_model.sh
test "$?" -eq 0 || exit "$?"
