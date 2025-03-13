#!/bin/bash

# Compile

rm a.out

# Check if hip-python is installed
echo ""
echo "Checking if hip-python is installed..."
echo ""

if ! python3 -m pip show hip-python > /dev/null 2>&1; then
    echo "hip-python not found. Installing hip-python..."
    python3 -m pip install --extra-index-url https://test.pypi.org/simple hip-python
    if [ $? -ne 0 ]; then
        echo "Failed to install hip-python. Please check your Python environment."
        exit 1
    fi
else
    echo "hip-python is already installed."
fi

echo ""
echo "Running program ..."
echo ""

cd ${CM_TMP_CURRENT_PATH}

python ${CM_TMP_CURRENT_SCRIPT_PATH}/detect.py > tmp-run.out
cat tmp-run.out
test $? -eq 0 || exit 1
