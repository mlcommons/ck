#!/bin/bash
if [[ ${CM_MLPERF_CPP} == "yes" ]]; then
  exit 0
fi

${CM_PYTHON_BIN} -m pip install -r ${CM_TMP_CURRENT_SCRIPT_PATH}/requirements.txt
test $? -eq 0 || exit 1

cmd=${CM_MLC_RUN_CMD}
echo "${cmd}"
eval "${cmd}"
test $? -eq 0 || exit 1
