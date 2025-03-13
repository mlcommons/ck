@echo off

if "%CM_RUN_DIR%" == "" (
  echo CM_RUN_DIR is not set
  exit 1
)

cd %CM_RUN_DIR%

if "%CM_DEBUG_SCRIPT_BENCHMARK_PROGRAM%" == "True" (
  echo *****************************************************
  echo You are now in Debug shell with pre-set CM env and can run the following command line manually:

  echo.
  if not "%CM_RUN_CMD0%" == "" (
    echo %CM_RUN_CMD0%
  ) else (
    echo %CM_RUN_CMD%
  )

  echo.
  echo Type exit to return to CM script.
  echo.

  cmd

  exit 0
)

rem Check CM_RUN_CMD0
if not "%CM_RUN_CMD0%" == "" (
  echo.
  %CM_RUN_CMD0%
) else (
  echo.
  %CM_RUN_CMD%
)

IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
