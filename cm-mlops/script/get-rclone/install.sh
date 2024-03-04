#!/bin/bash

rm -rf ${CM_RCLONE_ARCHIVE_WITH_EXT}
rm -rf rclone

wget ${CM_RCLONE_URL} --no-check-certificate
test $? -eq 0 || exit 1

unzip ${CM_RCLONE_ARCHIVE_WITH_EXT}
test $? -eq 0 || exit 1

mv ${CM_RCLONE_ARCHIVE}/rclone .
test $? -eq 0 || exit 1
