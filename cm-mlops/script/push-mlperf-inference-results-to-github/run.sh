#!/bin/bash

if [[ -n ${CM_MLPERF_INFERENCE_SUBMISSION_DIR} ]]; then
    rsync -avz "${CM_MLPERF_INFERENCE_SUBMISSION_DIR}/" "${CM_GIT_CHECKOUT_PATH}/"
fi
test $? -eq 0 || exit $?
cd "${CM_GIT_CHECKOUT_PATH}"
git add *
git commit -m "Added new results"
git push
test $? -eq 0 || exit $?
