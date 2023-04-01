#! /bin/bash

#export CM_CACHE="--no-cache"

export CM_OS_NAME="rhel"
export CM_OS_VERSION="9"

docker build -f cm-${CM_OS_NAME}-cpu.Dockerfile \
   -t ckrepo/cm-${CM_OS_NAME}-cpu:${CM_OS_NAME}-${CM_OS_VERSION} \
   --build-arg cm_os_name=${CM_OS_NAME} \
   --build-arg cm_os_version=${CM_OS_VERSION} \
   --build-arg cm_version="" \
   --build-arg cm_automation_repo="ctuning@mlcommons-ck" \
   --build-arg cm_automation_checkout="" \
   --build-arg cm_python_version="3.10.7" \
   ${CM_CACHE} .
