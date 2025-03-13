#!/bin/bash

if [[ ${CM_TENSORRT_VERSION} == 'vdetected' ]]; then
  exit 0;
fi

PIP_EXTRA=`python3 -c "import importlib.metadata; print(' --break-system-packages ' if int(importlib.metadata.version('pip').split('.')[0]) >= 23 else '')"`

version=${CM_TENSORRT_VERSION}
install_dir=${CM_TENSORRT_INSTALL_PATH}
python_version=${CM_PYTHON_VERSION}
python_version_info=(${python_version//./ })
python_max_version=${python_version_info[0]}
python_min_version=${python_version_info[1]}

cd ${install_dir}/python
${CM_PYTHON_BIN_WITH_PATH} -m pip install tensorrt-*-cp${python_max_version}${python_min_version}-none-${CM_HOST_OS_TYPE}_${CM_HOST_OS_MACHINE}.whl $PIP_EXTRA
test $? -eq 0 || exit $?

cd ${install_dir}/uff
${CM_PYTHON_BIN_WITH_PATH} -m pip install uff-0.6.9-py2.py3-none-any.whl $PIP_EXTRA
test $? -eq 0 || exit $?

cd ${install_dir}/graphsurgeon
${CM_PYTHON_BIN_WITH_PATH} -m pip install graphsurgeon-0.4.6-py2.py3-none-any.whl $PIP_EXTRA
test $? -eq 0 || exit $?

cd ${install_dir}/onnx_graphsurgeon
${CM_PYTHON_BIN_WITH_PATH} -m pip install onnx_graphsurgeon-0.3.12-py2.py3-none-any.whl $PIP_EXTRA
test $? -eq 0 || exit $?

#create softlinks for libnvinfer.so.7 and libnvinfer_plugin.so.7
# https://forums.developer.nvidia.com/t/could-not-load-dynamic-library-libnvinfer-so-7/231606/5
if [ ! -f "${install_dir}/lib/libnvinfer.so.7" ]; then
  ln -s "${install_dir}/lib/libnvinfer.so" "${install_dir}/lib/libnvinfer.so.7"
fi
test $? -eq 0 || exit $?
if [ ! -f "${install_dir}/lib/libnvinfer_plugin.so.7" ]; then
  ln -s "${install_dir}/lib/libnvinfer_plugin.so" "${install_dir}/lib/libnvinfer_plugin.so.7"
fi
test $? -eq 0 || exit $?
