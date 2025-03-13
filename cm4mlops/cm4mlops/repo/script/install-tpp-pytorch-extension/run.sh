#!/bin/bash

export PATH=${CM_CONDA_BIN_PATH}:${PATH}

cd ${CM_RUN_DIR}
echo ${CM_RUN_CMD}
eval ${CM_RUN_CMD}

if [ "${?}" != "0" ]; then exit 1; fi

echo "******************************************************"
