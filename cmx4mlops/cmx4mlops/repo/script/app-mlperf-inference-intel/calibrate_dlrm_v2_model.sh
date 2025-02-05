#!/bin/bash

export MODEL_DIR=${CM_ML_MODEL_FILE_WITH_PATH}
export DATA_DIR=/mnt/dlrm_data
echo ${CM_HARNESS_CODE_ROOT}
cd ${CM_HARNESS_CODE_ROOT}
python -m pip install scikit-learn==1.3.0 torchsnapshot torchrec==0.3.2
test $? -eq 0 || exit $?
python -m pip install fbgemm-gpu==0.3.2 --index-url https://download.pytorch.org/whl/cpu
test $? -eq 0 || exit $?
python python/dump_torch_model.py --model-path=$MODEL_DIR --dataset-path=$DATA_DIR
test $? -eq 0 || exit $?

python python/calibration.py \
        --max-batchsize=65536 \
        --model-path=${MODEL_DIR}/../dlrm-multihot-pytorch.pt \
        --dataset-path=/mnt/dlrm_data/ \
        --use-int8 --calibration
test $? -eq 0 || exit $?
