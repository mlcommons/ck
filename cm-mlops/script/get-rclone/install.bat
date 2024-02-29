del /Q /S rclone-v1.65.2-windows-amd64.zip > NUL 2>&1

wget --no-check-certificate https://downloads.rclone.org/v1.65.2/rclone-v1.65.2-windows-amd64.zip
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

unzip -o rclone-v1.65.2-windows-amd64.zip
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

move /Y rclone-v1.65.2-windows-amd64\* .

del /Q /S rclone-v1.65.2-windows-amd64.zip > NUL 2>&1

