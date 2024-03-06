@echo off

echo =======================================================

cd %CM_MLCOMMONS_CROISSANT_PATH%\python\mlcroissant
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

echo.
echo Running %CM_PYTHON_BIN_WITH_PATH% -m pip install -e .[git]

%CM_PYTHON_BIN_WITH_PATH% -m pip install -e .[git]
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

echo.
echo Validating Croissant ...

mlcroissant validate --file ../../datasets/titanic/metadata.json
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

echo =======================================================
