#!/bin/bash

cmd="${CMD}"
if [[ -n ${cmd} ]]; then
  echo "$cmd"
  eval "$cmd"
  test $? -eq 0 || exit $?
fi
