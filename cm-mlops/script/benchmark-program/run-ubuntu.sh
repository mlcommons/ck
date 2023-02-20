#!/bin/bash

CM_TMP_CURRENT_SCRIPT_PATH=${CM_TMP_CURRENT_SCRIPT_PATH:-$PWD}

cd ${CM_TMP_CURRENT_SCRIPT_PATH}
if [ ${CM_ENABLE_NUMACTL} == "1" ]; then 
  sudo apt-get install numactl
fi

bash ./run.sh
