@echo off

echo =======================================================

set CUR_DIR=%cd%
echo Env CUR_DIR: %CUR_DIR%
echo Env CM_TMP_CURRENT_SCRIPT_PATH: %CM_TMP_CURRENT_SCRIPT_PATH%
echo Env CM_ABTF_SSD_PYTORCH: %CM_ABTF_SSD_PYTORCH%
echo Env CM_ML_MODEL_FILE_WITH_PATH: %CM_ML_MODEL_FILE_WITH_PATH%

rem Patch model
cd %CM_ABTF_SSD_PYTORCH%
if not exist patchfile-20231129.patch (
  echo.
  echo Patching ABTF SRC
  echo.

  copy %CM_TMP_CURRENT_SCRIPT_PATH%\patches\patchfile-20231129.patch .
  patch -s -p0 < patchfile-20231129.patch
  IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

  copy %CM_TMP_CURRENT_SCRIPT_PATH%\patches\patchfile-202400214-export-to-onnx.patch .
  patch -s < patchfile-202400214-export-to-onnx.patch
  IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
)
cd %CUR_DIR%

echo.
%CM_PYTHON_BIN_WITH_PATH% %CM_ABTF_SSD_PYTORCH%\test_image.py --pretrained-model %CM_ML_MODEL_FILE_WITH_PATH% --input %CM_INPUT_IMAGE% --output %CM_OUTPUT_IMAGE%
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
