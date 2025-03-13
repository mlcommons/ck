#!/bin/bash

wget -nc https://raw.githubusercontent.com/krai/ck-mlperf/master/package/model-tf-mlperf-resnet/fix_input_shape.py
test $? -eq 0 || exit $?
${CM_PYTHON_BIN_WITH_PATH} "fix_input_shape.py" \
--input_name   "input_tensor"   \
--input_graph  "${CM_ML_MODEL_FILE_WITH_PATH}"  \
--output_graph "resnet50_v1.pb"             \
--type b
test $? -eq 0 || exit $?
