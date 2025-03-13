rem Extract file

rem If MD5 is wrong, extrat again!

rem Next line allows ERRORLEVEL inside if statements!
setlocal enabledelayedexpansion

set require_extract=1

if exist "%CM_EXTRACT_EXTRACTED_FILENAME%" (
    set require_extract=0

    echo.
    echo %CM_EXTRACT_EXTRACTED_CHECKSUM_CMD%
    cmd /c %CM_EXTRACT_EXTRACTED_CHECKSUM_CMD%
    IF !ERRORLEVEL! NEQ 0 (
       set require_extract=1
       del /Q %CM_EXTRACT_EXTRACTED_FILENAME%
    )
)

if "!require_extract!" == "1" (
    if not "%CM_EXTRACT_CMD0%" == "" (
     echo.
     echo %CM_EXTRACT_CMD0%
     cmd /c %CM_EXTRACT_CMD0%
     IF !ERRORLEVEL! NEQ 0 EXIT 1
    )

    echo.
    echo %CM_EXTRACT_CMD%
    cmd /c %CM_EXTRACT_CMD%
    IF !ERRORLEVEL! NEQ 0 EXIT 1
      
    echo.
    echo %CM_EXTRACT_EXTRACTED_CHECKSUM_CMD%
    cmd /c %CM_EXTRACT_EXTRACTED_CHECKSUM_CMD%
    IF !ERRORLEVEL! NEQ 0 EXIT 1
)
