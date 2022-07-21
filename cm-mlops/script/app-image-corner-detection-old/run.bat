rem Compile

call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat"

del /Q a.exe
del /Q susan.exe

echo.
echo Checking compiler version ...
echo.

"%CM_C_COMPILER_WITH_PATH%"

echo.
echo Compiling program ...
echo.

cd %CM_TMP_CURRENT_SCRIPT_PATH%

"%CM_C_COMPILER_WITH_PATH%" susan.c 
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

copy /B susan.exe a.exe

rem Return to the original path obtained in CM

echo.
echo Running program ...
echo.

cd %CM_TMP_CURRENT_PATH%

IF NOT DEFINED CM_INPUT SET CM_INPUT=%CM_TMP_CURRENT_SCRIPT_PATH%\data.pgm
IF NOT DEFINED CM_OUTPUT SET CM_OUTPUT=output_image_with_corners.pgm

del /Q %CM_OUTPUT%

%CM_TMP_CURRENT_SCRIPT_PATH%\a.exe "%CM_INPUT%" "%CM_OUTPUT%" -c
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

rem -c
rem -e
rem -s

