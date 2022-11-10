#!/bin/bash

# For now login to WANDB anonymously
wandb login --anonymously --relogin

${CM_PYTHON_BIN_WITH_PATH} ${CM_TMP_CURRENT_SCRIPT_PATH}/code.py
test $? -eq 0 || exit $?
