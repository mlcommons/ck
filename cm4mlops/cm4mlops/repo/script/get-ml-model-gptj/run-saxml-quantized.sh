#!/bin/bash
CUR=$PWD
${CM_PYTHON_BIN_WITH_PATH} -m pip install jaxlib==0.4.24
cd ${CM_TMP_CURRENT_SCRIPT_PATH}
${CM_PYTHON_BIN_WITH_PATH} ${CM_SAXML_REPO_PATH}/saxml/tools/offline_quantize.py --input_dir ${CM_ML_MODEL_FILE_WITH_PATH}/checkpoint_00000000/state --output_dir ${CUR}/int8_ckpt/checkpoint_00000000/state --quantization_configs "gptj" > offline_quantize2.log 
test $? -eq 0 || exit $?
