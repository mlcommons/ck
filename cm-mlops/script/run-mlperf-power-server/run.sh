#!/bin/bash
cmd="sudo ${CM_MLPERF_POWER_SOURCE}/ptd_client_server/server.py -c power-server.conf"
echo $cmd
eval $cmd
test $? -eq 0 || exit $?
