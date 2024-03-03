#!/bin/bash

PIP_EXTRA=`python3 -c "import pkg_resources; print(' --break-system-packages ' if int(pkg_resources.get_distribution('pip').version.split('.')[0]) >= 23 else '')"`
cmd="python3 -m pip install -r ${CM_TMP_CURRENT_SCRIPT_PATH}/requirements.txt ${CM_PYTHON_PIP_USER} ${CM_PYTHON_PIP_COMMON_EXTRA} ${PIP_EXTRA}"
echo $cmd
eval $cmd
