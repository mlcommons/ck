CM_PYTHON_BIN=${CM_PYTHON_BIN:-python3}

${CM_PYTHON_BIN} -m pip install --upgrade pip
${CM_PYTHON_BIN} -m pip install setuptools testresources wheel h5py --user --upgrade --ignore-installed

curl https://sh.rustup.rs -sSf -o tmp.sh
sh tmp.sh -y 

export PATH=$PATH:$HOME/.cargo/bin

${CM_PYTHON_BIN} -m pip install tensorflow-aarch64${CM_TMP_PIP_VERSION_STRING} -f https://tf.kmtea.eu/whl/stable.html --user
test $? -eq 0 || exit 1
