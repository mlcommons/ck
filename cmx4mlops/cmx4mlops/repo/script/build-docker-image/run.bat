if exist %CM_DOCKERFILE_WITH_PATH% (
rem  echo .git > .dockerignore

rem  echo.
rem  echo docker build %CM_DOCKER_CACHE_ARG%  %CM_DOCKER_BUILD_ARGS% -f %CM_DOCKERFILE_WITH_PATH% -t %CM_DOCKER_IMAGE_REPO%/%CM_DOCKER_IMAGE_NAME%:%CM_DOCKER_IMAGE_TAG% .

rem  echo.
rem  docker build %CM_DOCKER_CACHE_ARG%  %CM_DOCKER_BUILD_ARGS% -f "%CM_DOCKERFILE_WITH_PATH%" -t "%CM_DOCKER_IMAGE_REPO%/%CM_DOCKER_IMAGE_NAME%:%CM_DOCKER_IMAGE_TAG%" .

  %CM_DOCKER_BUILD_CMD%
  IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

  echo.
)
