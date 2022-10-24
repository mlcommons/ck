#!/bin/bash

cd ${CM_MLPERF_INFERENCE_SOURCE}
git submodule update --init language/bert/DeepLearningExamples
if [ "${?}" != "0" ]; then exit 1; fi
cd -

