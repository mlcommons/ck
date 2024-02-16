#!/bin/bash

echo "************************************************"
echo "Installing some system dependencies via package manager"


if [[ "$CM_QUIET" != "yes" ]]; then 
 echo "Enter skip to skip this step or press enter to continue:"
 read DUMMY

 if [[ "$DUMMY" == "skip" ]]; then exit 0; fi
fi

if [[ "$CM_HOST_OS_FLAVOR" == "amzn" ]]; then
  ${CM_SUDO} yum groupinstall "Development Tools"
fi

CM_PACKAGE_TOOL=${CM_PACKAGE_TOOL:-dnf}

${CM_SUDO} ${CM_PACKAGE_TOOL} update && \
    ${CM_SUDO} ${CM_PACKAGE_TOOL} --skip-broken install -y \
           acl autoconf \
           bzip2-devel bzip2 \
           ca-certificates curl  cmake \
           gcc git g++ \
           libtool libffi-devel libssl-devel\
           zlib-devel \
           libbz2-devel \
           openssh-client \
           make mesa-libGL \
           patch python3 python3-pip python3-devel \
           openssl-devel \
           rsync \
           tar \
           unzip \
           vim \
           wget which \
           xz \
           zip 

. ${CM_TMP_CURRENT_SCRIPT_PATH}/do_pip_installs.sh
test $? -eq 0 || exit $?
