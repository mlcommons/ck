#!/bin/bash

#CM Script location: ${CM_TMP_CURRENT_SCRIPT_PATH}

#To export any variable
#echo "VARIABLE_NAME=VARIABLE_VALUE" >>tmp-run-env.out

#${CM_PYTHON_BIN_WITH_PATH} contains the path to python binary if "get,python" is added as a dependency



function exit_if_error() {
  test $? -eq 0 || exit $?
}

function run() {
  echo "Running: "
  echo "$1"
  echo ""
  if [[ ${CM_FAKE_RUN} != 'yes' ]]; then
    eval "$1"
    exit_if_error
  fi
}

#Add your run commands here...
# run "$CM_RUN_CMD"
CUR=$PWD
run "wget --no-check-certificate -nc https://raw.githubusercontent.com/krai/ck-mlperf/master/package/dataset-squad-tokenized_for_bert/tokenize_and_pack.py"

run "${CM_PYTHON_BIN_WITH_PATH} tokenize_and_pack.py \
    ${CM_DATASET_SQUAD_VAL_PATH} \
    ${CM_ML_MODEL_BERT_VOCAB_FILE_WITH_PATH} \
    ${CUR}/bert_tokenized_squad_v1_1 \
    ${CM_DATASET_MAX_SEQ_LENGTH} \
    ${CM_DATASET_MAX_QUERY_LENGTH} \
    ${CM_DATASET_DOC_STRIDE} \
    ${CM_DATASET_RAW} \
    ${DATASET_CALIBRATION_FILE} \
    ${DATASET_CALIBRATION_ID}"

