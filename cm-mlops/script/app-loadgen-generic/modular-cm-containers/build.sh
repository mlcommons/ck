#! /bin/bash

. ./_common.sh

time docker build -f ${CM_DOCKER_NAME}--${CM_OS_NAME}-${CM_HW_TARGET}.Dockerfile \
   -t ${CM_DOCKER_ORG}/${CM_DOCKER_NAME}:${CM_OS_NAME}-${CM_OS_VERSION} \
   --build-arg cm_os_name=${CM_OS_NAME} \
   --build-arg cm_hw_target=${CM_HW_TARGET} \
   --build-arg cm_os_version=${CM_OS_VERSION} \
   --build-arg cm_version="" \
   --build-arg cm_automation_repo="mlcommons@ck" \
   --build-arg cm_automation_checkout="" \
   --build-arg cm_python_version="3.10.8" \
   --build-arg cm_mlperf_inference_loadgen_version="" \
   --build-arg cm_mlperf_inference_src_tags="" \
   --build-arg cm_mlperf_inference_src_version="" \
   --build-arg CM_MLPERF_CHOICE_SCRIPT=",_short,_submission,_dashboard" \
   --build-arg CM_MLPERF_CHOICE_SUBMITTER="Container" \
   --build-arg CM_MLPERF_CHOICE_IMPLEMENTATION="python" \
   --build-arg CM_MLPERF_CHOICE_HW_NAME="default" \
   --build-arg CM_MLPERF_CHOICE_MODEL="resnet50" \
   --build-arg CM_MLPERF_CHOICE_BACKEND="onnxruntime" \
   --build-arg CM_MLPERF_CHOICE_DEVICE=${CM_HW_TARGET} \
   --build-arg CM_MLPERF_CHOICE_SCENARIO="Offline" \
   --build-arg CM_MLPERF_CHOICE_MODE="accuracy" \
   --build-arg CM_MLPERF_CHOICE_QUERY_COUNT="500" \
  ${CM_CACHE} .
