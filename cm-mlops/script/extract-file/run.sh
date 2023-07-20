#!/bin/bash

echo ""
echo $PWD
if [ -e "${CM_EXTRACT_EXTRACTED_FILENAME}" ] ; then
  CMD=${CM_EXTRACT_EXTRACTED_CHECKSUM_CMD}
  echo "${CMD}"
  eval "${CMD}"
  test $? -eq 0 && exit 0
fi

CMD=${CM_EXTRACT_CMD}
echo "${CMD}"
eval "${CMD}"
test $? -eq 0 || exit $?
  
CMD=${CM_EXTRACT_EXTRACTED_CHECKSUM_CMD}
echo "${CMD}"
eval "${CMD}"
test $? -eq 0 || exit $?
