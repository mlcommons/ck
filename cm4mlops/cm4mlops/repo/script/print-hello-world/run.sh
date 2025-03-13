#!/bin/bash

if [[ ${CM_PRINT_HELLO_WORLD_SKIP_PRINT_ENV} != "yes" ]]; then
  echo ""
  echo "CM_ENV_TEST1 = ${CM_ENV_TEST1}"
  echo "CM_ENV_TEST2 = ${CM_ENV_TEST2}"
  echo "CM_ENV_TEST3 = ${CM_ENV_TEST3}"
fi

echo ""
echo "HELLO WORLD!"
if [[ ${CM_PRINT_HELLO_WORLD_TEXT} != "" ]]; then

  echo ""
  echo "${CM_PRINT_HELLO_WORLD_TEXT}"

fi
echo ""
