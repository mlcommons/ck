#!/bin/bash

if [[ -n ${CM_RUN_DIR} ]]; then
  cur_dir=${CM_RUN_DIR};
  cd $cur_dir
else
  cur_dir=`pwd`
fi
echo "Running power client from $cur_dir"

cmd="${CM_MLPERF_POWER_RUN_CMD}"
echo $cmd
eval $cmd
test $? -eq 0 || exit $?
