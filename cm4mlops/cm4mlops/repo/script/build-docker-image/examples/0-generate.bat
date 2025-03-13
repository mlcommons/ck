call 0-common.bat

cmr "build dockerfile" --file_path=%CD%\Dockerfile.%DOCKERFILE_EXT% ^
                       --docker_os=%DOCKER_OS% ^
                       --docker_os_version=%DOCKER_OS_VER% ^
                       --package_manager_update_cmd=%DOCKER_PACKAGE_MANAGER_UPDATE_CMD% ^
                       --pip_extra_flags=%DOCKER_PIP_EXTRA_FLAGS% ^
                       --post_file=%DOCKER_IMAGE_POST_FILE% ^
                       --cm_repo=%DOCKER_CM_MLOPS_REPO%
