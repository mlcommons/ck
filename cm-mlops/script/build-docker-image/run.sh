#!/bin/bash

if [ -f "${CM_DOCKERFILE_WITH_PATH}" ]; then
  echo ".git" > .dockerignore
  echo "docker build ${CM_DOCKER_CACHE}  ${CM_DOCKER_BUILD_ARGS} -f ${CM_DOCKERFILE_WITH_PATH} -t ${CM_DOCKER_IMAGE_REPO}:${CM_DOCKER_IMAGE_TAG} ."
  docker build ${CM_DOCKER_CACHE}  ${CM_DOCKER_BUILD_ARGS} -f "${CM_DOCKERFILE_WITH_PATH}" -t "${CM_DOCKER_IMAGE_REPO}:${CM_DOCKER_IMAGE_TAG}" .
  if [ "${CM_RUN_DOCKER_CONTAINER}" == "yes" ]; then
    echo "Running ${CM_DOCKER_IMAGE_RUN_CMD}"
    ID=`docker run -dt --rm "${CM_DOCKER_IMAGE_REPO}:${CM_DOCKER_IMAGE_TAG}" bash`
    CMD="docker exec $ID bash -c '${CM_DOCKER_IMAGE_RUN_CMD}'"
    echo $CMD
    eval $CMD
  fi
fi
