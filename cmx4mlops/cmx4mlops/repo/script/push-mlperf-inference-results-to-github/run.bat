@echo off

REM Check if CM_GIT_REPO_CHECKOUT_PATH is set
if not defined CM_GIT_REPO_CHECKOUT_PATH (
    echo "Error: CM_GIT_REPO_CHECKOUT_PATH is not set."
    exit /b 1
)

cd /d "%CM_GIT_REPO_CHECKOUT_PATH%"
if %errorlevel% neq 0 (
    echo "Error: Failed to change directory to %CM_GIT_REPO_CHECKOUT_PATH%"
    exit /b 1
)

git pull
git add *

REM Check if the CM_MLPERF_INFERENCE_SUBMISSION_DIR variable is set
if defined CM_MLPERF_INFERENCE_SUBMISSION_DIR (
    robocopy "%CM_MLPERF_INFERENCE_SUBMISSION_DIR%" "%CM_GIT_REPO_CHECKOUT_PATH%" /E /COPYALL /DCOPY:DAT
    git add *
)

REM Check if the previous command was successful
if %errorlevel% neq 0 exit /b %errorlevel%

git commit -a -m "%CM_MLPERF_RESULTS_REPO_COMMIT_MESSAGE%"
git push

REM Check if the previous command was successful
if %errorlevel% neq 0 exit /b %errorlevel%
