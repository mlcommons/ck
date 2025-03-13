#!/bin/bash

echo "***************************************************"
echo "Installing some system dependencies via sudo pacman"


if [[ "$CM_QUIET" != "yes" ]]; then 
 echo "Enter skip to skip this step or press enter to continue:"
 read DUMMY

 if [[ "$DUMMY" == "skip" ]]; then exit 0; fi
fi

CM_PACKAGE_TOOL=${CM_PACKAGE_TOOL:-pacman}

${CM_SUDO} ${CM_PACKAGE_TOOL} -Syu && \
    ${CM_SUDO} ${CM_PACKAGE_TOOL} -Sy \
           acl autoconf \
           bzip2 \
           ca-certificates curl  cmake \
           gcc git g++ \
           libtool \
           zlib \
           patch python python-pip \
           rsync \
           sudo \
           tar \
           unzip \
           vim \
           wget which \
           xz \
           zip 

# Install Python deps though preference is to install them 
# via cmr "get generic-python-lib _package.{Python PIP package name}"
if [[ "${CM_SKIP_PYTHON_DEPS}" != "yes" ]]; then
 . ${CM_TMP_CURRENT_SCRIPT_PATH}/do_pip_installs.sh
 test $? -eq 0 || exit $?
fi
