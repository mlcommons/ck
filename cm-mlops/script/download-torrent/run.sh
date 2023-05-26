#!/bin/bash
#transmission-remote --no-auth --download-dir ${PWD} -a ${CM_TORRENT_FILE}
transmission-remote --download-dir ${PWD} -a ${CM_TORRENT_FILE}
test $? -eq 0 || exit $?
transmission-remote -l
test $? -eq 0 || exit $?

if [[ ${CM_TORRENT_WAIT_UNTIL_COMPLETED} == "yes" ]]; then
  while true;
  do
    out=`transmission-remote  -l |grep ${CM_TORRENT_DOWNLOADED_FILE_NAME} | grep "100%"`
    if [[ -z $out ]]; then
      transmission-remote -l
      sleep 120
    else
      break
    fi
  done
fi
