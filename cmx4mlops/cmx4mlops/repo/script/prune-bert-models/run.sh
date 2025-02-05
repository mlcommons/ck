#!/bin/bash

echo "===================================================================="
echo "Start pruning ..."
echo ""

CM_TMP_CURRENT_SCRIPT_PATH=${CM_TMP_CURRENT_SCRIPT_PATH:-$PWD}

time ${CM_PYTHON_BIN_WITH_PATH} \
   ${CM_GIT_REPO_BERT_PRUNER_NEURIPS_2022_CHECKOUT_PATH}/main.py \
   --model_name ${CM_BERT_PRUNE_MODEL_NAME} \
   --task_name ${CM_BERT_PRUNE_TASK} \
   --ckpt_dir ${CM_BERT_PRUNE_CKPT_PATH} \
   --constraint ${CM_BERT_PRUNE_CONSTRAINT} \
   --output_dir ${CM_BERT_PRUNE_OUTPUT_DIR}

test $? -eq 0 || exit $?

echo "===================================================================="
