#!/bin/bash

echo ""
echo "Clearing OS kernel cache. It make take some time ..."

sync

echo "sudo /sbin/sysctl vm.drop_caches=3"
time sudo /sbin/sysctl vm.drop_caches=3
