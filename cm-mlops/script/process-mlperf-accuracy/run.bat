echo Running command:
echo.
echo %CM_RUN_CMDS%
echo.

%CM_RUN_CMDS%

IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
