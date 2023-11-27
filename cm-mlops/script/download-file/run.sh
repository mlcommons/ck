#!/bin/bash

if [ -e ${CM_DOWNLOAD_DOWNLOADED_PATH} ]; then
  CMD=${CM_DOWNLOAD_CHECKSUM_CMD}
  if [[ "${CMD}" != "" ]]; then
    echo ""
    echo ${CMD}
    eval ${CMD}
    test $? -eq 0 || require_download="1"
  fi
else
  require_download="1"
fi

if [[ ${require_download} == "1" ]]; then
  echo ""
  rm -f ${CM_DOWNLOAD_FILENAME}
  
  CMD=${CM_DOWNLOAD_CMD}
  echo ""
  echo ${CMD}
  eval ${CMD}
  test $? -eq 0 || exit $?

  CMD=${CM_DOWNLOAD_CHECKSUM_CMD}
  if [[ "${CMD}" != "" ]]; then
     echo ""
     echo ${CMD}
     eval ${CMD}
  fi
fi

test $? -eq 0 || exit $?
