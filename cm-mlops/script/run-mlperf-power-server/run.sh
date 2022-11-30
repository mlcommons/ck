#!/bin/bash
cmd="power_server -c power-server.conf"
echo $cmd
eval $cmd
test $? -eq 0 || exit $?
