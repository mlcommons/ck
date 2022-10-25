#! /bin/bash

# ubuntu [18.04 ; 20.04 ; 22.04]
# debian [9 ; 10]

export CM_OS_NAME="ubuntu"
export set CM_OS_VERSION="22.04"

#export CM_OS_NAME="debian"
#export CM_OS_VERSION="10"

docker build -f cm-ubuntu-debian-cpu.Dockerfile \
   -t ckrepo/cm-ubuntu-debian-cpu:${CM_OS_NAME}-${CM_OS_VERSION} \
   --build-arg cm_os_name=${CM_OS_NAME} \
   --build-arg cm_os_version=${CM_OS_VERSION} \
   .

#    --build-arg cm_version=1.0.1 \
