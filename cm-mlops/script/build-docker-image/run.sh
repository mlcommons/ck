#!/bin/bash

if [ -f "${CM_DOCKERFILE_WITH_PATH}" ]; then
#  echo ".git" > .dockerignore

#  echo ""
#  echo "docker build ${CM_DOCKER_CACHE_ARG}  ${CM_DOCKER_BUILD_ARGS} -f ${CM_DOCKERFILE_WITH_PATH} -t ${CM_DOCKER_IMAGE_REPO}/${CM_DOCKER_IMAGE_NAME}:${CM_DOCKER_IMAGE_TAG} ."

#  docker build ${CM_DOCKER_CACHE_ARG}  ${CM_DOCKER_BUILD_ARGS} -f "${CM_DOCKERFILE_WITH_PATH}" -t "${CM_DOCKER_IMAGE_REPO}/${CM_DOCKER_IMAGE_NAME}:${CM_DOCKER_IMAGE_TAG}" .

  eval "${CM_DOCKER_BUILD_CMD}"
  test $? -eq 0 || exit 1
fi
