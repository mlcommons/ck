@echo off

set CUR_DIR=%cd%
set SCRIPT_DIR=%CM_TMP_CURRENT_SCRIPT_PATH%

if not exist install mkdir install

set INSTALL_DIR=%CUR_DIR%\install

cd %CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH%

if not "%CM_DATASET_SIZE%" == "" (
  set MAX_IMAGES=--max-images %CM_DATASET_SIZE% --seed 42
) else (
   set MAX_IMAGES=
)

%CM_PYTHON_BIN% tools\openimages.py %MAX_IMAGES% --dataset-dir=%INSTALL_DIR% --output-labels=openimages-mlperf.json --classes %CM_DATASET_OPENIMAGES_CLASSES%
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

rem Next is a hack to support MLPerf inference on Windows
cd %INSTALL_DIR%
if not exist validation\data\annotations mkdir validation\data\annotations
copy annotations\* validation\data\annotations
