@echo off

cd %CM_RUN_DIR%


set PATH=D:\Work1\CM\repos\local\cache\aae20d0b0dde421b\install\onnxruntime-win-x64-1.16.3\lib

echo %PATH%

C:\Windows\System32\where.exe onnxruntime.dll

%CM_RUN_CMD%

IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
