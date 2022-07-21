#!/bin/bash

if [ -f ${CM_DOCKERFILE_WITH_PATH} ]; then
  echo ".git" > .dockerignore
  docker build  ${CM_DOCKER_BUILD_ARGS} -f ${CM_DOCKERFILE_WITH_PATH} -t ${CM_DOCKER_IMAGE_REPO}:${CM_DOCKER_IMAGE_TAG} .
fi
