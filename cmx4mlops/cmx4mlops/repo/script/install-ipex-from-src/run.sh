#!/bin/bash

#export PATH=${CM_CONDA_BIN_PATH}:${PATH}
#echo $LD_LIBRARY_PATH
#exit 1
rm -rf ipex_src
cp -r ${IPEX_DIR} ipex_src
cd ipex_src
pwd

git submodule sync
git submodule update --init --recursive

if [[ ${CM_INTEL_IPEX_RESNET50_PATCH} == "yes" ]]; then
  bash ${CM_TMP_CURRENT_SCRIPT_PATH}/apply_intel_resnet50_patch.sh
  test "$?" -eq 0 || exit "$?"

elif [[ ${CM_INTEL_IPEX_RETINANET_PATCH} == "yes" ]]; then
  bash ${CM_TMP_CURRENT_SCRIPT_PATH}/apply_intel_retinanet_patch.sh
  test "$?" -eq 0 || exit "$?"

elif [[ ${CM_INTEL_IPEX_3D_UNET_PATCH} == "yes" ]]; then
  cd third_party/mkl-dnn
  git fetch --tags && git checkout v2.7
  test "$?" -eq 0 || exit "$?"
  cd ../../
  bash ${CM_TMP_CURRENT_SCRIPT_PATH}/apply_intel_3d-unet_patch.sh
  test "$?" -eq 0 || exit "$?"

elif [[ ${CM_INTEL_IPEX_DLRM_V2_PATCH} == "yes" ]]; then
  export LD_LIBRARY_PATH=""
  wget https://raw.githubusercontent.com/mlcommons/inference_results_v3.1/main/closed/Intel/code/dlrm-v2-99/pytorch-cpu-int8/ipex.patch
  test "$?" -eq 0 || exit "$?"
  git apply ipex.patch
  test "$?" -eq 0 || exit "$?"
  cd third_party/libxsmm
  git checkout c21bc5ddb4
  test "$?" -eq 0 || exit "$?"
  cd ../ideep && rm -rf mkl-dnn && git checkout b5eadff696
  test "$?" -eq 0 || exit "$?"
  git submodule sync && git submodule update --init --recursive
  test "$?" -eq 0 || exit "$?"
  cd mkl-dnn
  wget https://raw.githubusercontent.com/mlcommons/inference_results_v3.1/main/closed/Intel/code/dlrm-v2-99/pytorch-cpu-int8/onednngraph.patch
  test "$?" -eq 0 || exit "$?"
  git apply -p1 onednngraph.patch
  test "$?" -eq 0 || exit "$?"
  cd ../../../
fi

rm -rf build
echo ${CM_RUN_CMD}
eval ${CM_RUN_CMD}

test "$?" -eq 0 || exit "$?"

echo "******************************************************"

