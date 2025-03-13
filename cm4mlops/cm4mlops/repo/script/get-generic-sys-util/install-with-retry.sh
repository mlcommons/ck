#!/bin/bash
# Safe execution of a command stored in a variable
cmd="${CM_SYS_UTIL_INSTALL_CMD}"
echo "$cmd"

# set the max number of retries as well as the delay between the retries
max_retries=3
delay_in_retry=3


for ((i=1; i<=max_retries; i++)); do
    echo "Attempting to install ${CM_SYS_UTIL_NAME} - $i of $max_retries..."
    output=$(eval "$cmd" 2>&1)
    echo "$output"
    exit_status=$?

    if [[ $exit_status -ne 0 || "$output" == *"Temporary failure resolving"* || "$output" == *"Unable to fetch some archives"* ]]; then
        # Check for network-related errors in the output
        if echo "$output" | grep -q -E "Could not resolve|Temporary failure resolving"; then
            echo "Network issue detected, retrying in $delay_in_retry seconds..."
            sleep $delay_in_retry
        else
            # If it's a non-network error, handle based on fail-safe setting
            if [[ "${CM_TMP_FAIL_SAFE}" == 'yes' ]]; then
                echo "CM_GET_GENERIC_SYS_UTIL_INSTALL_FAILED=yes" > tmp-run-env.out
                echo "Fail-safe is enabled, exiting with status 0."
                exit 0
            else
                echo "Fail-safe is not enabled, exiting with error status $exit_status."
                exit $exit_status
            fi
        fi
    else
        # If the command succeeded
        echo "Successfully installed ${CM_SYS_UTIL_NAME}."
        exit 0
    fi

    # If this was the last retry, print a final failure message
    if [[ $i -eq $max_retries ]]; then
        echo "Installation failed after $max_retries attempts due to persistent network issues."
        if [[ "${CM_TMP_FAIL_SAFE}" == 'yes' ]]; then
            exit 0
        else
            exit 1
        fi
    fi
done
