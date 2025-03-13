#/bin/bash
echo "Running: $CMD"
eval $CMD
test $? -eq 0 || exit $?
