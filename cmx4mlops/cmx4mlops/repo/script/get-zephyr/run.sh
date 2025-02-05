#!/bin/bash

CM_TMP_CURRENT_SCRIPT_PATH=${CM_TMP_CURRENT_SCRIPT_PATH:-$PWD}
CM_PYTHON_BIN_WITH_PATH=${CM_PYTHON_BIN_WITH_PATH:-python3}

CUR=`pwd`

if [ "${?}" != "0" ]; then exit 1; fi

if [ ! -d "zephyr" ]; then
  west init --mr ${CM_ZEPHYR_VERSION}-branch $CUR
  if [ "${?}" != "0" ]; then exit 1; fi
fi

cd $CUR/zephyr
west update
if [ "${?}" != "0" ]; then exit 1; fi
west zephyr-export
if [ "${?}" != "0" ]; then exit 1; fi
${CM_PYTHON_BIN_WITH_PATH} -m pip install -r $CUR/zephyr/scripts/requirements.txt
if [ "${?}" != "0" ]; then exit 1; fi

