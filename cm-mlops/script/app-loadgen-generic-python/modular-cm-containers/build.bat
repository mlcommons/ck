call _common.bat

docker build -f %CM_DOCKER_NAME%--%CM_OS_NAME%-%CM_HW_TARGET%.Dockerfile ^
   -t %CM_DOCKER_ORG%/%CM_DOCKER_NAME%-%CM_HW_TARGET%:%CM_OS_NAME%-%CM_OS_VERSION% ^
   --build-arg cm_os_name=%CM_OS_NAME% ^
   --build-arg cm_hw_target=%CM_HW_TARGET% ^
   --build-arg cm_os_version=%CM_OS_VERSION% ^
   --build-arg cm_version="" ^
   --build-arg cm_automation_repo="ctuning@mlcommons-ck" ^
   --build-arg cm_automation_checkout="" ^
   --build-arg cm_python_version="3.10.8" ^
   --build-arg cm_mlperf_inference_loadgen_version="" ^
   --build-arg cm_mlperf_inference_src_tags="" ^
   --build-arg cm_mlperf_inference_src_version="" ^
   --build-arg CM_ONNXRUNTIME_VERSION="1.13.1" ^
   %CM_CACHE% .
