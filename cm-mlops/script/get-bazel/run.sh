#!/bin/bash
if [[ ${CM_VERSION} == "0.26.1" ]]; then
  ${CM_BAZEL_BIN_WITH_PATH} version |grep "Build label" |sed 's/Build label:/bazel/' > tmp-ver.out
else
  ${CM_BAZEL_BIN_WITH_PATH} --version  > tmp-ver.out
fi
test $? -eq 0 || exit 1
