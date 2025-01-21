#!/bin/bash
bazel_bin=${CM_BAZEL_BIN_WITH_PATH}
if [[ ${CM_VERSION} == "0.26.1" ]]; then
  ${bazel_bin} version |grep "Build label" |sed 's/Build label:/bazel/' > tmp-ver.out
else
  ${bazel_bin} --version  > tmp-ver.out
fi
test $? -eq 0 || exit 1
