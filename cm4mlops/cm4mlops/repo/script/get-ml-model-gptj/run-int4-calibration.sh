#!/bin/bash

export PATH=${CM_CONDA_BIN_PATH}:$PATH

echo ${CM_CALIBRATION_CODE_ROOT}
cd ${CM_CALIBRATION_CODE_ROOT}/gpt-j/pytorch-cpu/INT4
pip install -r requirements.txt
bash run_calibration_int4.sh

test $? -eq 0 || exit $?
