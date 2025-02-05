#!/bin/bash
chmod 777 ${PWD}
#transmission-remote --no-auth --download-dir ${PWD} -a ${CM_TORRENT_FILE}
cmd="transmission-remote --download-dir ${PWD} -a ${CM_TORRENT_FILE}"
echo $cmd
eval $cmd
test $? -eq 0 || exit $?

cmd="transmission-remote -l"
echo $cmd
eval $cmd
test $? -eq 0 || exit $?

if [[ ${CM_TORRENT_WAIT_UNTIL_COMPLETED} == "yes" ]]; then
  while true;
  do
    out=`transmission-remote  -l |grep ${CM_TORRENT_DOWNLOADED_FILE_NAME} | grep "100%"`
    if [[ -z $out ]]; then
      transmission-remote -l
      sleep 6
    else
      break
    fi
  done
fi

id=`transmission-remote -l |grep ${CM_TORRENT_DOWNLOADED_FILE_NAME} |tr -s ' ' | cut -d' ' -f2`
test $? -eq 0 || exit $?
location=`transmission-remote -t${id} -i |grep Location |cut -d':' -f2 |tr -d ' '`
test $? -eq 0 || exit $?
echo "CM_TORRENT_DOWNLOADED_DIR=$location">> tmp-run-env.out
name=`transmission-remote -t${id} -i |grep Name |cut -d':' -f2 |tr -d ' '`
test $? -eq 0 || exit $?
echo "CM_TORRENT_DOWNLOADED_NAME=$name">> tmp-run-env.out
