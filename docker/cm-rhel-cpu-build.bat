rem set CM_CACHE=--no-cache

set CM_OS_NAME=rhel
set CM_OS_VERSION=9

docker build -f cm-rhel-cpu.Dockerfile ^
   -t ckrepo/cm-rhel-cpu:%CM_OS_NAME%-%CM_OS_VERSION% ^
   --build-arg cm_os_name=%CM_OS_NAME% ^
   --build-arg cm_os_version=%CM_OS_VERSION% ^
   --build-arg cm_version="" ^
   --build-arg cm_automation_repo="octoml@ck" ^
   --build-arg cm_automation_checkout="" ^
   %CM_CACHE% .
