del /Q /S rclone-v%CM_VERSION%-windows-amd64.zip > NUL 2>&1

wget --no-check-certificate https://downloads.rclone.org/v%CM_VERSION%/rclone-v%CM_VERSION%-windows-amd64.zip
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

unzip -o rclone-v%CM_VERSION%-windows-amd64.zip
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

move /Y rclone-v%CM_VERSION%-windows-amd64\* .

del /Q /S rclone-v%CM_VERSION%-windows-amd64.zip > NUL 2>&1

