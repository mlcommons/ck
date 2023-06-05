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
