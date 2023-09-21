call 0-common.bat

cmr "run docker container" --image_repo=%DOCKER_IMAGE_REPO% --image_tag=%DOCKER_IMAGE_TAG% --script_tags=detect,os
