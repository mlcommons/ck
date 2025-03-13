#!/bin/bash

#PIP_EXTRA=`${CM_PYTHON_BIN} -c "import pkg_resources; print(' --break-system-packages ' if int(pkg_resources.get_distribution('pip').version.split('.')[0]) >= 23 else '')"`
PIP_EXTRA=`${CM_PYTHON_BIN} -c "import importlib.metadata; print(' --break-system-packages ' if int(importlib.metadata.version('pip').split('.')[0]) >= 23 else '')"`

${CM_PYTHON_BIN_WITH_PATH} -m pip install virtualenv ${PIP_EXTRA}
test $? -eq 0 || exit 1

${CM_PYTHON_BIN_WITH_PATH} -m venv ${CM_VIRTUAL_ENV_DIR}
test $? -eq 0 || exit 1
