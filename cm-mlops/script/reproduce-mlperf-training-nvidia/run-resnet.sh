#!/bin/bash
benchmark_implementation=${benchmark_implementation:-"mxnet-22.04"}
echo "cd ${CM_MLPERF_TRAINING_NVIDIA_CODE_PATH}/benchmarks/resnet/implementations/${benchmark_implementation}"
cd ${CM_MLPERF_TRAINING_NVIDIA_CODE_PATH}/benchmarks/resnet/implementations/${benchmark_implementation}
docker build --pull -t mlperf-nvidia:image_classification .
test $? -eq 0 || exit $?
echo "source ${CONFIG_FILE}"
source ${CONFIG_FILE}
test $? -eq 0 || exit $?

DATADIR=${CM_MLPERF_TRAINING_NVIDIA_RESNET_PREPROCESSED_PATH}
echo "DATADIR=${CM_MLPERF_TRAINING_NVIDIA_RESNET_PREPROCESSED_PATH}"

echo "CONT=mlperf-nvidia:image_classification DATADIR=${DATADIR} LOGDIR=${RESULTS_DIR} ./run_with_docker.sh"
CONT=mlperf-nvidia:image_classification DATADIR=${DATADIR} LOGDIR=${RESULTS_DIR} ./run_with_docker.sh
test $? -eq 0 || exit $?
