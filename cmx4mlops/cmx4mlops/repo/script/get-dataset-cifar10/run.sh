#!/bin/bash

wget -nc ${CM_DATASET_CIFAR10} --no-check-certificate
test $? -eq 0 || exit 1

rm -rf ${CM_DATASET_FILENAME1}

gzip -d ${CM_DATASET_FILENAME}
test $? -eq 0 || exit 1

tar -xvf ${CM_DATASET_FILENAME1}
test $? -eq 0 || exit 1

rm -rf ${CM_DATASET_FILENAME}

echo "CM_DATASET_PATH=$PWD/cifar-10-batches-py" > tmp-run-env.out
echo "CM_DATASET_CIFAR10_PATH=$PWD/cifar-10-batches-py" >> tmp-run-env.out

if [ "${CM_DATASET_CONVERT_TO_TINYMLPERF}" == "yes" ]; then 
  echo ""
  echo "Copying TinyMLPerf convertor ..."
  echo ""

  cp -rf ${CM_MLPERF_TINY_TRAINING_IC}/* .

  echo ""
  echo "Installing Python requirements ..."
  echo ""

  ${CM_PYTHON_BIN} -m pip install -r ${CM_TMP_CURRENT_SCRIPT_PATH}/requirements.txt
  if [ "${?}" != "0" ]; then exit 1; fi

  echo ""
  echo "Converting in $PWD ..."
  echo ""

  ${CM_PYTHON_BIN} perf_samples_loader.py
  if [ "${?}" != "0" ]; then exit 1; fi

  cp -rf y_labels.csv perf_samples

  echo "CM_DATASET_CIFAR10_TINYMLPERF_PATH=$PWD/perf_samples" >> tmp-run-env.out

  echo ""
  echo "Copying to EEMBC runner user space ..."
  echo ""
 
  cp -rf perf_samples/* ${CM_EEMBC_ENERGY_RUNNER_DATASETS}/ic01
fi

