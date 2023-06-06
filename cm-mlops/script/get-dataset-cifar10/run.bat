wget -nc %CM_DATASET_CIFAR10% --no-check-certificate
IF %ERRORLEVEL% NEQ 0 EXIT 1

del /Q /S %CM_DATASET_FILENAME1%

gzip -d %CM_DATASET_FILENAME%
IF %ERRORLEVEL% NEQ 0 EXIT 1

tar -xvf %CM_DATASET_FILENAME1%
IF %ERRORLEVEL% NEQ 0 EXIT 1

del /Q /S %CM_DATASET_FILENAME1%

echo CM_DATASET_PATH=%CD%\cifar-10-batches-py > tmp-run-env.out
echo CM_DATASET_CIFAR10_PATH=%CD%\cifar-10-batches-py >> tmp-run-env.out

if "%CM_DATASET_CONVERT_TO_TINYMLPERF%" == "yes" (
 echo.
 echo Copying TinyMLPerf convertor ...
 echo.

 copy /B /Y %CM_MLPERF_TINY_TRAINING_IC%\* .

 echo.
 echo Installing Python requirements ...
 echo.

 %CM_PYTHON_BIN% -m pip install -r %CM_TMP_CURRENT_SCRIPT_PATH%\requirements.txt
 IF %ERRORLEVEL% NEQ 0 EXIT 1

 echo.
 echo Converting ...
 echo.

 %CM_PYTHON_BIN% perf_samples_loader.py
 IF %ERRORLEVEL% NEQ 0 EXIT 1

 copy /B /Y y_labels.csv perf_samples

 echo CM_DATASET_CIFAR10_TINYMLPERF_PATH=%CD%\perf_samples >> tmp-run-env.out

 echo.
 echo Copying to EEMBC runner user space ...
 echo.
 
 copy /B /Y perf_samples\* %CM_EEMBC_ENERGY_RUNNER_DATASETS%\ic01
)

