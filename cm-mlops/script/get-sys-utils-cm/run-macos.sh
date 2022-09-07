#!/bin/bash

echo "***************************************************"
echo "Installing some system dependencies via brew update"

if [[ "$CM_TMP_QUIET" != "yes" ]]; then 
 echo "Enter skip to skip this step or press enter to continue:"
 read DUMMY

 if [[ "$DUMMY" == "skip" ]]; then exit 0; fi
fi

brew update && \
     brew install \
           git \
           wget \
           curl \
           zip \
           unzip \
           bzip2 \
           vim \
           mc \
           tree \
           gcc \
           autoconf \
           autogen \
           libtool \
           make \
           cmake \
           openssl \
           readline \
           sqlite3 \
           xz \
           zlib \
           python3
python3 -m pip install ${CM_TMP_CURRENT_SCRIPT_PATH}/requirements.txt
