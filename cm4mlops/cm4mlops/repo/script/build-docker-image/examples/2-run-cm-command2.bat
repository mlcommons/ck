call 0-common.bat

cmr "run docker container" --image_repo=%DOCKER_IMAGE_REPO% --image_name=%DOCKER_IMAGE_NAME% --image_tag=%DOCKER_IMAGE_TAG%  --run_cmd="cmr 'detect os' -j"
