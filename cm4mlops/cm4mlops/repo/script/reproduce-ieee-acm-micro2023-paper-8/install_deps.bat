@echo off

set CUR_DIR=%cd%

echo.
echo Current execution path: %CUR_DIR%
echo Path to script: %CM_TMP_CURRENT_SCRIPT_PATH%
echo ENV CM_EXPERIMENT: %CM_EXPERIMENT%

if exist "%CM_TMP_CURRENT_SCRIPT_PATH%\requirements.txt" (

  echo.
  echo Installing requirements.txt ...
  echo.

  %CM_PYTHON_BIN_WITH_PATH% -m pip install -r %CM_TMP_CURRENT_SCRIPT_PATH%\requirements.txt
  IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
)
