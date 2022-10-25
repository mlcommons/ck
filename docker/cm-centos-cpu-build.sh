#! /bin/bash

export CM_OS_NAME="centos"
export CM_OS_VERSION="8"

docker build -f cm-centos-cpu.Dockerfile \
   -t ckrepo/cm-centos-cpu:${CM_OS_NAME}-${CM_OS_VERSION} \
   --build-arg cm_os_name=${CM_OS_NAME} \
   --build-arg cm_os_version=${CM_OS_VERSION} \
   .

#    --build-arg cm_version=1.0.1 \
