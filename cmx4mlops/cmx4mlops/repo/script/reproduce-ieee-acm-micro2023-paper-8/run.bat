@echo off

set CUR_DIR=%cd%

echo.
echo Current execution path: %CUR_DIR%
echo Path to script: %CM_TMP_CURRENT_SCRIPT_PATH%
echo ENV CM_EXPERIMENT: %CM_EXPERIMENT%

echo.
%CM_PYTHON_BIN_WITH_PATH% %CM_TMP_CURRENT_SCRIPT_PATH%\main.py
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
