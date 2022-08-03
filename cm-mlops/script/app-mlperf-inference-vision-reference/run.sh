#!/bin/bash
if [[ ${CM_RUN_DOCKER_CONTAINER} == "yes" ]]; then
  exit 0
fi
CUR_DIR=$PWD
${CM_PYTHON_BIN} -m pip install -r ${CM_TMP_CURRENT_SCRIPT_PATH}/requirements.txt
test $? -eq 0 || exit 1
cp ${CM_DATASET_AUX_PATH}/val.txt ${CM_DATASET_PATH}/val_map.txt
test $? -eq 0 || exit 1

export DATA_DIR=${CM_DATASET_PATH}
export MODEL_DIR=${CM_ML_MODEL_PATH}

echo "Using MLCommons Inference source from ${CM_MLC_INFERENCE_SOURCE}"
RUN_DIR=${CM_MLC_INFERENCE_SOURCE}/vision/classification_and_detection

echo "Output Dir: ${OUTPUT_DIR}"
CMD="cd ${RUN_DIR} && ./run_local.sh ${CM_BACKEND} ${CM_MODEL} ${CM_DEVICE} --scenario ${CM_LOADGEN_SCENARIO} ${CM_LOADGEN_EXTRA_OPTIONS}"
echo $CMD
eval $CMD
test $? -eq 0 || exit 1
cd $CUR_DIR
echo "CM_MLC_RUN_CMD=${CMD}" >> tmp-run-env.out
test $? -eq 0 || exit 1
