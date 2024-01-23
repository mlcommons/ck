#!/bin/bash

export PATH=${CM_CONDA_BIN_PATH}:$PATH
echo $PWD

if [ ! -d harness ]; then
  mkdir -p harness
fi

echo ${CM_HARNESS_CODE_ROOT}
cd ${CM_HARNESS_CODE_ROOT}
cd utils
python -m pip install .
test $? -eq 0 || exit $?
cd ../
sudo -E bash run_quantization.sh
test $? -eq 0 || exit $?
