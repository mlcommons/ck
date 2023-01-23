#!/bin/bash
cd ${CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH}
cmd=${RUN_CMD}
echo $cmd
eval $cmd
test $? -eq 0 || exit $?
