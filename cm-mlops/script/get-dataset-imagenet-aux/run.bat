echo.

wget -nc %CM_WGET_URL% --no-check-certificate
IF %ERRORLEVEL% NEQ 0 EXIT 1

mkdir data

gzip -d caffe_ilsvrc12.tar.gz
IF %ERRORLEVEL% NEQ 0 EXIT 1

tar -C data -xvf caffe_ilsvrc12.tar
IF %ERRORLEVEL% NEQ 0 EXIT 1

del /Q /S caffe_ilsvrc12.tar

echo CM_DATASET_AUX_PATH=%CD%\data > tmp-run-env.out
