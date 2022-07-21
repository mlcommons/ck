#!/bin/bash

if [[ ${CM_HOST_OS_FLAVOR} == "macos" ]]; then
    sysctl -a | grep machdep.cpu > tmp-lscpu.out
else
    lscpu > tmp-lscpu.out
fi
