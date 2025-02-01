@echo off
echo Running gh auth:
REM Not printing CM_RUN_CMD as it can contain secret
REM echo %CM_RUN_CMD%
echo.

REM Check if CM_FAKE_RUN is not equal to "yes"
if not "%CM_FAKE_RUN%"=="yes" (
    
    REM Execute the command stored in CM_RUN_CMD
    REM %CM_RUN_CMD%
    echo %CM_GH_AUTH_TOKEN% | gh auth login --with-token
    
    REM Check the exit code and exit with error if non-zero
    if %ERRORLEVEL% neq 0 (
        exit /b 1
    )
)

