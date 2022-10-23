#!/bin/bash

CM_TMP_CURRENT_SCRIPT_PATH=${CM_TMP_CURRENT_SCRIPT_PATH:-$PWD}
cp -r ${CM_TMP_CURRENT_SCRIPT_PATH}/imagenet_helper $PWD/

echo "PYTHONPATH=${PYTHONPATH}:$PWD" > tmp-run-env.out
