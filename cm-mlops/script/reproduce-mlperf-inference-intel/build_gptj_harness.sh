#!/bin/bash

export PATH=${CM_CONDA_BIN_PATH}:$PATH
echo $PWD

if [ ! -d harness ]; then
  mkdir -p harness
fi

cd ${CM_HARNESS_CODE_ROOT}
cd utils
python -m pip install .
test $? -eq 0 || exit $?

