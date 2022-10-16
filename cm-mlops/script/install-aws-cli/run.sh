#!/bin/bash

CUR_DIR=$PWD
echo "******************************************************"
echo $CM_CURL_URL
CM_CURL_URL=${CM_CURL_URL//"[OS]"/${CM_HOST_OS_TYPE}}
CM_CURL_URL=${CM_CURL_URL//"[PLATFORM]"/${CM_HOST_PLATFORM_FLAVOR}}
echo $CM_CURL_URL
echo "CM_CURL_URL=${CM_CURL_URL}" >> tmp-run-env.out
FILE="awscliv2.zip"
rm -rf ${FILE}
curl "${CM_CURL_URL}" -o "${FILE}"
unzip ${FILE}
sudo ./aws/install
