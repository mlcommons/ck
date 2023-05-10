#!/bin/bash
if [ -f ${CM_DAE_DOWNLOADED_FILENAME} ]; then
  CMD=${CM_DAE_DOWNLOADED_CHECKSUM_CMD}
  echo ${CMD}
  eval ${CMD}
else
  CMD="wget -nc ${CM_DAE_URL}"
  echo ${CMD}
  eval ${CMD}
  test $? -eq 0 || exit $?
  CMD=${CM_DAE_DOWNLOADED_CHECKSUM_CMD}
  echo ${CMD}
  eval ${CMD}
fi

test $? -eq 0 || exit $?

if [ -f ${CM_DAE_EXTRACTED_FILENAME} ]; then
  CMD=${CM_DAE_DOWNLOADED_CHECKSUM_CMD}
  echo ${CMD}
  eval ${CMD}
  test $? -eq 0 || exit $?
else
  CMD=${CM_DAE_EXTRACT_CMD}
  echo ${CMD}
  eval ${CMD}
  test $? -eq 0 || exit $?
  CMD=${CM_DAE_DOWNLOADED_CHECKSUM_CMD}
  echo ${CMD}
  eval ${CMD}
  test $? -eq 0 || exit $?
fi
