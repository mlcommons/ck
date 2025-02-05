#!/bin/bash

export PATH=${CM_CONDA_BIN_PATH}:$PATH

cd ${CM_MLPERF_INFERENCE_INTEL_CALIBRATION_PATH}
CUR_DIR=$(pwd)
export WORKLOAD_DATA=${CUR_DIR}/data
mkdir -p ${WORKLOAD_DATA}

python download-calibration-dataset.py --calibration-list-file calibration-list.txt --output-dir ${WORKLOAD_DATA}/calibration-data
test $? -eq 0 || exit $?

export CALIBRATION_DATA_JSON=${WORKLOAD_DATA}/calibration-data/cnn_dailymail_calibration.json

export CHECKPOINT_DIR=${WORKLOAD_DATA}/gpt-j-checkpoint
cmd="ln -s ${GPTJ_CHECKPOINT_PATH} ${CHECKPOINT_DIR}"
echo $cmd
eval $cmd

export QUANTIZED_MODEL_DIR=${WORKLOAD_DATA}/quantized-int4-model
mkdir -p ${QUANTIZED_MODEL_DIR}

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
CONDA_INSTALL_PATH=`pwd`/miniconda3
rm -rf ${CONDA_INSTALL_PATH}
bash miniconda.sh -b -p ${CONDA_INSTALL_PATH}
export CONDA_PREFIX=${CONDA_INSTALL_PATH}

export PATH=${CONDA_INSTALL_PATH}/bin:$PATH
conda install -y python=3.9.0 numpy=1.23.5
python -m pip install transformers==4.21.2
python -m pip install texttable
python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
python -m pip install datasets
bash run_calibration_int4.sh
test $? -eq 0 || exit $?
#exit 1
