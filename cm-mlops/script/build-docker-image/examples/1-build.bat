call 0-common.bat

cmr "build docker image" --dockerfile=%CD%\Dockerfile.%DOCKERFILE_EXT% ^
                         --docker_os=%DOCKER_OS% ^
                         --docker_os_version=%DOCKER_OS_VER% ^
                         --image_repo=%DOCKER_IMAGE_REPO% ^
                         --image_name=%DOCKER_IMAGE_NAME% ^
                         --image_tag=%DOCKER_IMAGE_TAG%
