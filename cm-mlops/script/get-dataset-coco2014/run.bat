@echo off

set CUR_DIR=%cd%
set SCRIPT_DIR=%CM_TMP_CURRENT_SCRIPT_PATH%

if not exist install mkdir install

set INSTALL_DIR=%CUR_DIR%\install

cd %CM_RUN_DIR%

if not "%CM_DATASET_SIZE%" == "" (
  set MAX_IMAGES=--max-images %CM_DATASET_SIZE% --seed 42
) else (
   set MAX_IMAGES=
)

rem TBD - next file doesn't exist in the latest inference - need to check/fix ...

%CM_PYTHON_BIN% download-coco-2014.py %MAX_IMAGES% --dataset-dir=%INSTALL_DIR% --output-labels=openimages-mlperf.json
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
