#!/bin/bash
cmd=${CM_MLPERF_POWER_RUN_CMD}
echo $cmd
eval $cmd
test $? -eq 0 || exit $?
