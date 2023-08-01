@echo off

set CUR_DIR=%cd%

echo.
echo Current execution path: %CUR_DIR%
echo Path to script: %CM_TMP_CURRENT_SCRIPT_PATH%
echo ENV PIP_REQUIREMENTS: %PIP_REQUIREMENTS%
echo ENV CM_VAR1: %CM_VAR1%

if "%PIP_REQUIREMENTS%" == "True" (
  if exist "%CM_TMP_CURRENT_SCRIPT_PATH%\requirements.txt" (

    echo.
    echo Installing requirements.txt ...
    echo.

    %CM_PYTHON_BIN_WITH_PATH% -m pip install -r %CM_TMP_CURRENT_SCRIPT_PATH%\requirements.txt
    IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
  )
)

echo.
%CM_PYTHON_BIN_WITH_PATH% %CM_TMP_CURRENT_SCRIPT_PATH%\main.py
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
