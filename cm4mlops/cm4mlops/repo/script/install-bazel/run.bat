@echo off

del /Q /S %CM_BAZEL_DOWNLOAD_FILE%
del /Q /S bazel.exe

wget -c %CM_BAZEL_DOWNLOAD_URL% -O %CM_BAZEL_DOWNLOAD_FILE% --no-check-certificate
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

ren %CM_BAZEL_DOWNLOAD_FILE% bazel.exe
