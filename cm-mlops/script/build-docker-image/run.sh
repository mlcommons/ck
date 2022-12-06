#!/bin/bash

if [ -f "${CM_DOCKERFILE_WITH_PATH}" ]; then
  echo ".git" > .dockerignore
  echo "docker build ${CM_DOCKER_CACHE_ARG}  ${CM_DOCKER_BUILD_ARGS} -f ${CM_DOCKERFILE_WITH_PATH} -t ${CM_DOCKER_IMAGE_REPO}:${CM_DOCKER_IMAGE_TAG} ."

  docker build ${CM_DOCKER_CACHE_ARG}  ${CM_DOCKER_BUILD_ARGS} -f "${CM_DOCKERFILE_WITH_PATH}" -t "${CM_DOCKER_IMAGE_REPO}:${CM_DOCKER_IMAGE_TAG}" .
  test $? -eq 0 || exit 1

  if [ "${CM_RUN_DOCKER_CONTAINER}" == "yes" ]; then
    # TBD: THIS PART HAS TO BE CHECKED/CLEANED
    echo "Running ${CM_DOCKER_RUN_CMD}"

    ID=`docker run -dt --rm "${CM_DOCKER_IMAGE_REPO}/${CM_DOCKER_IMAGE_NAME}:${CM_DOCKER_IMAGE_TAG}" bash`

    CMD="docker exec $ID bash -c '${CM_DOCKER_RUN_CMD}'"

    echo $CMD
    eval $CMD
    test $? -eq 0 || exit 1
  fi
fi
