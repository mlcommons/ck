@echo off
REM Check if the environment variable CM_HF_LOGIN_CMD is defined and not empty
IF DEFINED CM_HF_LOGIN_CMD (
    echo %CM_HF_LOGIN_CMD%
    call %CM_HF_LOGIN_CMD%
    IF ERRORLEVEL 1 (
        echo Command failed with error code %ERRORLEVEL%
        exit /b %ERRORLEVEL%
    )
)

REM Run the Hugging Face CLI version command and save output
huggingface-cli version > tmp-ver.out

