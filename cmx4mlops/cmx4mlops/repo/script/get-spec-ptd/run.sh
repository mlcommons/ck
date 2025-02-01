#!/bin/bash

if [[ -n "${CM_INPUT}" ]]; then
  exit 0
fi

cd ${CM_MLPERF_POWER_SOURCE}

chmod +x "inference_v1.0/ptd-linux-x86"
chmod +x "inference_v1.0/ptd-windows-x86.exe"
cd -
