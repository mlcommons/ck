set CM_OS_NAME=centos
set CM_OS_VERSION=8

docker build -f cm-centos-cpu.Dockerfile ^
   -t ckrepo/cm-centos-cpu:%CM_OS_NAME%-%CM_OS_VERSION% ^
   --build-arg cm_os_name=%CM_OS_NAME% ^
   --build-arg cm_os_version=%CM_OS_VERSION% ^
   --build-arg cm_version="" ^
   --build-arg cm_automation_repo="octoml@ck" ^
   --build-arg cm_automation_checkout="" ^
   .

rem    --build-arg cm_version=1.0.1 ^
