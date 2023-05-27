#!/bin/bash
if [ ! -f ${CM_DOWNLOAD_DOWNLOADED_FILENAME} ]; then
  require_download=1
else
  CMD=${CM_DOWNLOAD_CHECKSUM_CMD}
  echo ${CMD}
  eval ${CMD}
  test $? -eq 0 || require_download=1
fi

if [[ ${require_download} == "1" ]]; then
  CMD=${CM_DOWNLOAD_CMD}
  echo ${CMD}
  eval ${CMD}
  test $? -eq 0 || exit $?
  CMD=${CM_DOWNLOAD_CHECKSUM_CMD}
  echo ${CMD}
  eval ${CMD}
fi

test $? -eq 0 || exit $?
