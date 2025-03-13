#!/bin/bash

cd ${CM_TINYMLPERF_REPO_PATH}
test $? -eq 0 || exit $?

echo ""
${CM_PYTHON_BIN_WITH_PATH} submission_checker.py --input .
test $? -eq 0 || exit $?

echo ""
${CM_PYTHON_BIN_WITH_PATH} generate_final_report.py --input summary.csv 
test $? -eq 0 || exit $?
