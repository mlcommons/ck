where rclone.exe > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

rclone --version > tmp-ver.out
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
