#!/bin/bash
openssl_bin=${CM_OPENSSL_BIN_WITH_PATH}
${openssl_bin} version > tmp-ver.out 2>/dev/null
test $? -eq 0 || exit 1
