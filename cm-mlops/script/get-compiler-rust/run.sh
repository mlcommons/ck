CM_PYTHON_BIN=${CM_PYTHON_BIN_WITH_PATH:-python3}

${CM_PYTHON_BIN} -m pip install --upgrade pip ${CM_PYTHON_PIP_COMMON_EXTRA}
${CM_PYTHON_BIN} -m pip install setuptools testresources wheel h5py --user --upgrade --ignore-installed ${CM_PYTHON_PIP_COMMON_EXTRA}

curl https://sh.rustup.rs -sSf -o tmp.sh
sh tmp.sh -y 
