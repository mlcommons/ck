#! /bin/bash

# ubuntu [18.04 ; 20.04 ; 22.04]
# debian [9 ; 10]

#export CM_CACHE="--no-cache"

export CM_OS_NAME="ubuntu"
export CM_OS_VERSION="22.04"

#export CM_OS_NAME="debian"
#export CM_OS_VERSION="10"

docker build -f cm-ubuntu-debian-cpu.Dockerfile \
   -t ckrepo/cm-ubuntu-debian-cpu:${CM_OS_NAME}-${CM_OS_VERSION} \
   --build-arg cm_os_name=${CM_OS_NAME} \
   --build-arg cm_os_version=${CM_OS_VERSION} \
   --build-arg cm_version="" \
   --build-arg cm_automation_repo="ctuning@mlcommons-ck" \
   --build-arg cm_automation_checkout="" \
   --build-arg cm_python_version="3.10.7" \
   ${CM_CACHE} .
