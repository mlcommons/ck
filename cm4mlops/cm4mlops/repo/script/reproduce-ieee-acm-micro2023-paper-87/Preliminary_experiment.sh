#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"

echo "${CM_ARTIFACT_CLOCKHANDS_EXTRACTED}"

cd ${CM_ARTIFACT_CLOCKHANDS_EXTRACTED}/Clockhands_Artifact_MICRO2023/ClockhandsPreliminaryExperiments/

cd onikiri2/tool/AutoRunTools/
sed s@/path/to@$(realpath ../../../)@ -i cfg.xml

# You can change this!
GigaInsns=1

echo "Register lifetimes experiment for $GigaInsns giga instructions."
echo "It will take $(echo $GigaInsns \* 4 | bc) minutes."
echo "You can change the number of instructions to evaluate by modifying $BASH_SOURCE"
sed '115 s@".*"@"'"$GigaInsns"'G"@' -i cfg.xml

perl enqueue.pl -t
cd result/001/sh/exec/
for i in *.sh; do sh $i & PID="$PID $!"; done
wait $PID
cd ../../../../
perl summary.pl
cd ../../../
