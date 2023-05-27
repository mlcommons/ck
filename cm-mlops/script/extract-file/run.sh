#!/bin/bash

CMD=${CM_EXTRACT_CMD}
echo ${CMD}
eval ${CMD}
test $? -eq 0 || exit $?
  
CMD=${CM_EXTRACT_EXTRACTED_CHECKSUM_CMD}
echo ${CMD}
eval ${CMD}
test $? -eq 0 || exit $?
