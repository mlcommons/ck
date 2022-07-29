#!/bin/bash

CUR_DIR=$PWD

echo "******************************************************"
echo "Cloning Mlcommons from ${CM_GIT_URL} with branch ${CM_GIT_CHECKOUT}..."

if [ ! -d "inference" ]; then
  git clone --recurse-submodules -b "${CM_GIT_CHECKOUT}" ${CM_GIT_URL} inference
  if [ "${?}" != "0" ]; then exit 1; fi
fi
