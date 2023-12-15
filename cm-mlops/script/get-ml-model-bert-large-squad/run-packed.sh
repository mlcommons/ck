#!/bin/bash

cmd="${CM_PYTHON_BIN_WITH_PATH} ${CM_BERT_CONVERTER_CODE_PATH} --src '${CM_BERT_CHECKPOINT_INDEX_PATH}/../model.ckpt-5474' --dest '$PWD/' --config_path '${CM_BERT_CONFIG_PATH}'"
echo $cmd
eval $cmd
test $? -eq 0 || exit $?
