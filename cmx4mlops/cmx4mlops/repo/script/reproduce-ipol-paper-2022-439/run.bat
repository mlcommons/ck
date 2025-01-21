@echo off

echo =======================================================

set CUR_DIR=%cd%
echo Current path in CM script: %CUR_DIR%

echo.
echo Installing extra requirements (latest versions) ...

echo.
%CM_PYTHON_BIN_WITH_PATH% -m pip install -r %CM_TMP_CURRENT_SCRIPT_PATH%\requirements.txt

echo =======================================================

cd %CM_IPOL_PATH%

echo Current path in CM cache: %cd%

echo Running author's code ...

del /F /Q cm.png
del /F /Q %CUR_DIR%\diff.png

echo.
%CM_PYTHON_BIN_WITH_PATH% main.py --input_0=%CM_INPUT_1%  --input_1=%CM_INPUT_2%
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

rem Copy diff png to current path
copy /B cm.png %CUR_DIR%\diff.png
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

echo =======================================================
