@echo off

echo =======================================================

set CUR_DIR=%cd%
echo Current path in CM script: %CUR_DIR%

if not "%CM_MLPERF_INFERENCE_LOADGEN_LOCAL_SRC%" == "" (

  echo.
  echo Copying LoadGen sources from %CM_TMP_CURRENT_SCRIPT_PATH%\%CM_MLPERF_INFERENCE_LOADGEN_LOCAL_SRC% to %CUR_DIR%
  echo.

  xcopy /s /e /y /q %CM_TMP_CURRENT_SCRIPT_PATH%\%CM_MLPERF_INFERENCE_LOADGEN_LOCAL_SRC%\* %CUR_DIR%

  set CM_MLPERF_INFERENCE_SOURCE=%CUR_DIR%
)


echo.
echo Switching to %CM_MLPERF_INFERENCE_SOURCE%\loadgen

cd %CM_MLPERF_INFERENCE_SOURCE%\loadgen
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

echo.
echo Running %CM_PYTHON_BIN% setup.py develop

%CM_PYTHON_BIN% setup.py develop
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

echo =======================================================
