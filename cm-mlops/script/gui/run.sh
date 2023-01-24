#!/bin/bash

streamlit run ${CM_TMP_CURRENT_SCRIPT_PATH}/app.py ${CM_GUI_EXTRA_CMD}
test $? -eq 0 || exit $?
