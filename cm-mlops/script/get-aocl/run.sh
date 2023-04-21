#!/bin/bash
if [[ -z ${CM_GIT_REPO_CHECKOUT_PATH} ]]; then
    echo "Git repository not found!"
    exit 1
fi
cd ${CM_GIT_REPO_CHECKOUT_PATH}
scons
test $? -eq 0 || exit $?

