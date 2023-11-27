rem Download file

rem If MD5 is wrong, download again!

rem Next line allows ERRORLEVEL inside if statements!
setlocal enabledelayedexpansion

set require_download=1
if exist "%CM_DOWNLOAD_DOWNLOADED_PATH%" (
    set require_download=0
    if "%CM_DOWNLOAD_CHECKSUM_CMD_USED%" == "YES" (
        echo.
        echo %CM_DOWNLOAD_CHECKSUM_CMD%
        cmd /c %CM_DOWNLOAD_CHECKSUM_CMD%
        IF !ERRORLEVEL! NEQ 0 (
           if "%CM_DOWNLOAD_CMD_USED%" == "NO" exit 1
           set require_download=1
        )
    )
)

if "!require_download!" == "1" (
    echo.
    del /Q %CM_DOWNLOAD_FILENAME%
 
    echo.
    echo %CM_DOWNLOAD_CMD%
    cmd /c %CM_DOWNLOAD_CMD%
    IF !ERRORLEVEL! NEQ 0 EXIT !ERRORLEVEL!

    if "%CM_DOWNLOAD_CHECKSUM_CMD_USED%" == "YES" (
      echo.
      echo %CM_DOWNLOAD_CHECKSUM_CMD%
      cmd /c %CM_DOWNLOAD_CHECKSUM_CMD%
      IF !ERRORLEVEL! NEQ 0 EXIT 1
    )
)
