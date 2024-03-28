@echo off

rem echo ******************************************************
rem echo Cloning MLCommons from %CM_GIT_URL% with branch %CM_GIT_CHECKOUT% %CM_GIT_DEPTH% %CM_GIT_RECURSE_SUBMODULES% ...

rem git clone %CM_GIT_RECURSE_SUBMODULES% %CM_GIT_URL% %CM_GIT_DEPTH% inference
rem cd inference
rem git checkout -b "%CM_GIT_CHECKOUT%"
rem 

rem Next line allows ERRORLEVEL inside if statements!
setlocal enabledelayedexpansion

set CUR_DIR=%cd%
set SCRIPT_DIR=%CM_TMP_CURRENT_SCRIPT_PATH%

set folder=%CM_GIT_CHECKOUT_FOLDER%

if not exist "%CM_TMP_GIT_PATH%" (

  if exist %folder% (
    deltree %folder%
  )
  echo ******************************************************
  echo Current directory: %CUR_DIR%
  echo.
  echo Cloning %CM_GIT_REPO_NAME% from %CM_GIT_URL%
  echo.
  echo "%CM_GIT_CLONE_CMD%"
  echo.
  %CM_GIT_CLONE_CMD%
  IF !ERRORLEVEL! NEQ 0 EXIT !ERRORLEVEL!
  cd %folder%
  if not "%CM_GIT_SHA%" == "" (
       echo.
       echo.
       git checkout "%CM_GIT_CHECKOUT%"
       IF !ERRORLEVEL! NEQ 0 EXIT !ERRORLEVEL!
  )

) else (

  cd %folder%

)

if not "%CM_GIT_SUBMODULES%" == "" (
  for /F %%s in ("%CM_GIT_SUBMODULES%") do (
    echo.
    echo Initializing submodule %%s
    git submodule update --init %%s
    IF !ERRORLEVEL! NEQ 0 EXIT !ERRORLEVEL!
  )
)

if "%CM_GIT_PATCH%" == "yes" (
   for %%x in (%CM_GIT_PATCH_FILEPATHS%) do (
       echo.
       echo Applying patch %%x ...
       git apply %%x
       IF !ERRORLEVEL! NEQ 0 EXIT !ERRORLEVEL!
   )
)

cd %CUR_DIR%

exit /b 0
