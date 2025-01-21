call 0-common.bat

docker run -it %DOCKER_IMAGE_REPO%/%DOCKER_IMAGE_NAME%:%DOCKER_IMAGE_TAG% -c bash
