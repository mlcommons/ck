#!/bin/bash
CUR=$PWD
rm -rf pax_gptj_checkpoint
cd ${CM_TMP_CURRENT_SCRIPT_PATH}
${CM_PYTHON_BIN_WITH_PATH} -m convert_gptj_ckpt --base ${GPTJ_CHECKPOINT_PATH} --pax ${CUR}/pax_gptj_checkpoint
test $? -eq 0 || exit $?

cd "$CUR"
