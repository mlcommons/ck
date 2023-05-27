#!/bin/bash
if [ ! -f ${CM_DAE_DOWNLOADED_FILENAME} ]; then
  require_download=1
else
  CMD=${CM_DAE_DOWNLOADED_CHECKSUM_CMD}
  echo ${CMD}
  eval ${CMD}
  test $? -eq 0 || require_download=1
fi

if [[ ${require_download} == "1" ]]; then
  CMD=${CM_DAE_DOWNLOAD_CMD}
  echo ${CMD}
  eval ${CMD}
  test $? -eq 0 || exit $?
  CMD=${CM_DAE_DOWNLOADED_CHECKSUM_CMD}
  echo ${CMD}
  eval ${CMD}
fi

test $? -eq 0 || exit $?

if [ ! -f ${CM_DAE_EXTRACTED_FILENAME} ]; then
  require_extract=1
else
  CMD=${CM_DAE_EXTRACTED_CHECKSUM_CMD}
  echo ${CMD}
  eval ${CMD}
  test $? -eq 0 || require_extract=1
fi

if [[ ${require_extract} == 1 ]]; then
  echo "CM_DAE_REQUIRE_EXTRACT=yes" >>tmp-run-env.out
fi
