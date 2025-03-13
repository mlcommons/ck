del /Q /S install
del /Q %FILENAME%

wget --no-check-certificate %URL%
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

unzip %FILENAME% -d install
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

echo CM_TMP_INSTALL_FOLDER=%FOLDER% > tmp-run-env.out
