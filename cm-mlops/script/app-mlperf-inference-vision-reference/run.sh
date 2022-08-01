#!/bin/bash
if [[ ${CM_RUN_DOCKER_CONTAINER} == "yes" ]]; then
  exit 0
fi
${CM_PYTHON_BIN} -m pip install -r ${CM_TMP_CURRENT_SCRIPT_PATH}/requirements.txt
test $? -eq 0 || exit 1
cp ${CM_DATASET_AUX_PATH}/val.txt ${CM_DATASET_PATH}/val_map.txt
test $? -eq 0 || exit 1

export DATA_DIR=${CM_DATASET_PATH}
export MODEL_DIR=${CM_ML_MODEL_PATH}

echo "Using MLCommons Inference source from ${CM_MLC_INFERENCE_SOURCE}"
RUN_DIR=${CM_MLC_INFERENCE_SOURCE}/vision/classification_and_detection
cd ${RUN_DIR}
#./run_local.sh ${CM_BACKEND} ${CM_MODEL} ${CM_DEVICE} --count 100  --time 6 --scenario Offline
CMD="./run_local.sh ${CM_BACKEND} ${CM_MODEL} ${CM_DEVICE} --scenario ${CM_LOADGEN_SCENARIO} ${CM_LOADGEN_EXTRA_OPTIONS}"
echo $CMD
eval $CMD
