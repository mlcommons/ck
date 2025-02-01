#!/bin/bash
# Safe execution of a command stored in a variable
cmd="${CM_SYS_UTIL_INSTALL_CMD}"
echo "$cmd"

# Execute the command and capture the exit status directly
if ! eval "$cmd"; then
    echo "Command failed with status $?"
    if [[ "${CM_TMP_FAIL_SAFE}" == 'yes' ]]; then
        # Exit safely if fail-safe is enabled
        echo "CM_GET_GENERIC_SYS_UTIL_INSTALL_FAILED=yes" > tmp-run-env.out
        echo "Fail-safe is enabled, exiting with status 0"
        exit 0
    else
        # Otherwise exit with the actual error status
        exit $?
    fi
else
    #echo "Command succeeded"
    exit 0
fi