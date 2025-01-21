#!/bin/bash

echo ${CM_VLLM_RUN_CMD}

${CM_VLLM_RUN_CMD}
test $? -eq 0 || exit 1
