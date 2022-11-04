#!/bin/bash

if [[ ${CM_HOST_OS_FLAVOR} == "macos" ]]; then
    sysctl -a | grep hw > tmp-lscpu.out
else
    lscpu > tmp-lscpu.out
    memory_capacity=`free -h --si | grep Mem: | tr -s ' ' | cut -d' ' -f2`
    echo "CM_HOST_MEMORY_CAPACITY=$memory_capacity">>tmp-run-env.out
    disk_capacity=`df -h --total -l |grep total |tr -s ' '|cut -d' ' -f2`
    echo "CM_HOST_DISK_CAPACITY=$disk_capacity">>tmp-run-env.out
fi
