set DOCKER_IMAGE_REPO=cknowledge

set DOCKER_OS=ubuntu

rem set DOCKER_OS_VER=22.04
set DOCKER_OS_VER=23.04
set DOCKER_PIP_EXTRA_FLAGS=--break-system-packages

rem set DOCKER_IMAGE_NAME=cm-base
set DOCKER_IMAGE_NAME=cm-script-app-image-classification-onnx-py
set DOCKER_IMAGE_POST_FILE=%CD%\extra-cmd.cm-script-app-image-classification-onnx-py

rem set DOCKER_IMAGE_TAG=%DOCKER_OS%-%DOCKER_OS_VER%-20230804

set DOCKER_IMAGE_TAG=%DOCKER_OS%-%DOCKER_OS_VER%-latest
set DOCKERFILE_EXT=%DOCKER_IMAGE_NAME%-%DOCKER_IMAGE_TAG%

set DOCKER_PACKAGE_MANAGER_UPDATE_CMD="apt-get update -y && apt-get upgrade -y"

set DOCKER_CM_MLOPS_REPO="ctuning@mlcommons-ck"
rem set DOCKER_CM_MLOPS_REPO="mlcommons@ck"
