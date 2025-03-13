if "%CM_EXTRACT_EXTRACTED_PATH%" == "" (
  echo.

  wget -nc https://www.dropbox.com/s/57s11df6pts3z69/ILSVRC2012_img_val_500.tar --no-check-certificate
  IF %ERRORLEVEL% NEQ 0 EXIT 1

  mkdir images

  tar -C images -xvf ILSVRC2012_img_val_500.tar
  IF %ERRORLEVEL% NEQ 0 EXIT 1

  del /Q /S ILSVRC2012_img_val_500.tar

  echo CM_DATASET_PATH=%CD%\images > tmp-run-env.out
  echo CM_DATASET_IMAGENET_PATH=%CD%\images >> tmp-run-env.out
  echo CM_DATASET_IMAGENET_VAL_PATH=%CD%\images >> tmp-run-env.out
)
