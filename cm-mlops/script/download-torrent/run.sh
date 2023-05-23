#!/bin/bash
transmission-daemon --download-dir ${PWD}
transmission-remote --no-auth -a ${CM_TORRENT_FILE}
test $? -eq 0 || exit $?
transmission-remote -l
test $? -eq 0 || exit $?
