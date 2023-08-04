#!/bin/bash

echo "************************************************"
echo "Installing some system dependencies via sudo apt"


if [[ "$CM_QUIET" != "yes" ]]; then 
 echo "Enter skip to skip this step or press enter to continue:"
 read DUMMY

 if [[ "$DUMMY" == "skip" ]]; then exit 0; fi
fi

CM_APT_TOOL=${CM_APT_TOOL:-apt-get}

${CM_SUDO} ${CM_APT_TOOL} update && \
    ${CM_SUDO} ${CM_APT_TOOL} install -y --no-install-recommends \
           apt-utils \
           git \
           wget \
           curl \
           zip \
           unzip \
           bzip2 \
           zlib1g-dev \
           libbz2-dev \
           openssh-client \
           kmod \
           libmesa-dev \
           libssl-dev \
           vim \
           mc \
           tree \
           gcc \
           g++ \
           tar \
           autoconf \
           autogen \
           libtool \
           make \
           cmake \
           libc6-dev \
           build-essential \
           libbz2-dev \
           libffi-dev \
           liblzma-dev \
           python3 \
           python3-pip \
           python3-dev \
           libtinfo-dev \
           sudo \
           libgl1 \
           libncurses5

. ${CM_TMP_CURRENT_SCRIPT_PATH}/do_pip_installs.sh
test $? -eq 0 || exit $?
