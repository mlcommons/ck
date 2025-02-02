#!/bin/bash
if  [[ -n ${CM_HF_LOGIN_CMD} ]]; then
  echo "${CM_HF_LOGIN_CMD}"
  eval ${CM_HF_LOGIN_CMD}
  test $? -eq 0 || exit $?
fi
huggingface-cli version > tmp-ver.out
