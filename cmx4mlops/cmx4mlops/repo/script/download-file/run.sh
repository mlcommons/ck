#!/bin/bash

# Execute config command if it exists
if [[ -n ${CM_DOWNLOAD_CONFIG_CMD} ]]; then
  echo -e "\nExecuting: ${CM_DOWNLOAD_CONFIG_CMD}"
  eval "${CM_DOWNLOAD_CONFIG_CMD}" || exit $?
fi

# Assume download is required by default
require_download=1

# No download needed if a local file path is specified or the tool is 'cmutil'
if [[ -n "${CM_DOWNLOAD_LOCAL_FILE_PATH}" || ${CM_DOWNLOAD_TOOL} == "cmutil" ]]; then
  require_download=0
fi

# If the file exists, check the checksum if necessary
if [[ -e "${CM_DOWNLOAD_DOWNLOADED_PATH}" && -n "${CM_DOWNLOAD_CHECKSUM_CMD}" ]]; then
  echo -e "\nChecking checksum: ${CM_DOWNLOAD_CHECKSUM_CMD}"
  eval "${CM_DOWNLOAD_CHECKSUM_CMD}"
  
  if [[ $? -ne 0 ]]; then
    # If the checksum fails, handle errors based on whether the file is local
    if [[ -n "${CM_DOWNLOAD_LOCAL_FILE_PATH}" ]]; then
      echo "Checksum failed for local file. Exiting."
      exit 1
    else
      echo "Checksum failed. Marking for re-download."
      CM_PRE_DOWNLOAD_CLEAN=true
    fi
  else
    # If checksum succeeds, no download is required
    require_download=0
  fi
fi

# Perform download if required
if [[ ${require_download} == 1 ]]; then
  echo ""

  # If a pre-download clean command is specified and needed, execute it
  if [[ -n "${CM_PRE_DOWNLOAD_CLEAN}" && "${CM_PRE_DOWNLOAD_CLEAN,,}" != "false" ]]; then
    echo "Executing pre-download clean: ${CM_PRE_DOWNLOAD_CLEAN_CMD}"
    eval "${CM_PRE_DOWNLOAD_CLEAN_CMD}" || exit $?
  fi

  # Execute the download command
  echo "Downloading: ${CM_DOWNLOAD_CMD}"
  eval "${CM_DOWNLOAD_CMD}" || exit $?
fi

# Verify checksum again if necessary
if [[ ${CM_DOWNLOAD_TOOL} == "cmutil" || ${require_download} == 1 ]]; then
  if [[ -n "${CM_DOWNLOAD_CHECKSUM_CMD}" ]]; then
    echo -e "\nVerifying checksum after download: ${CM_DOWNLOAD_CHECKSUM_CMD}"
    eval "${CM_DOWNLOAD_CHECKSUM_CMD}" || exit $?
  fi
fi
