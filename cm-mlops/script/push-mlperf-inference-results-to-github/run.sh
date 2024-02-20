#!/bin/bash

cd "${CM_GIT_CHECKOUT_PATH}"
git pull
git add *
if [[ -n ${CM_MLPERF_INFERENCE_SUBMISSION_DIR} ]]; then
    rsync -avz "${CM_MLPERF_INFERENCE_SUBMISSION_DIR}/" "${CM_GIT_CHECKOUT_PATH}/"
    git add *
fi
test $? -eq 0 || exit $?

git commit -a -m "${CM_MLPERF_RESULTS_REPO_COMMIT_MESSAGE}"
git push
test $? -eq 0 || exit $?
