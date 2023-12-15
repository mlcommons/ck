#!/bin/bash

if [ -e "${CM_EXTRACT_EXTRACTED_FILENAME}" ] ; then
  CMD=${CM_EXTRACT_EXTRACTED_CHECKSUM_CMD}
  echo ""
  echo "${CMD}"
  eval "${CMD}"
  test $? -eq 0 && exit 0
fi

CMD=${CM_EXTRACT_CMD}
echo ""
echo "${CMD}"
eval "${CMD}"
test $? -eq 0 || exit $?
  
CMD=${CM_EXTRACT_EXTRACTED_CHECKSUM_CMD}
echo ""
echo "${CMD}"
eval "${CMD}"
test $? -eq 0 || exit $?
