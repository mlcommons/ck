#!/bin/bash
python_bin=${CM_PYTHON_INSTALLED_PATH}/${FILE_NAME}
python_bin=${CM_PYTHON_BIN_WITH_PATH:-${python_bin}}
${python_bin} --version > tmp-ver.out
test $? -eq 0 || exit 1

PYTHON_BIN_PATH="${python_bin%/*}"

if [[ ! -f ${PYTHON_BIN_PATH}/python ]]; then
  echo "Creating softlink of python to python3"
  cmd="sudo ln -s ${python_bin} ${PYTHON_BIN_PATH}/python"
  echo $cmd
  eval $cmd
fi
