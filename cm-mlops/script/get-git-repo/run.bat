@echo off

rem echo ******************************************************
rem echo Cloning MLCommons from %CM_GIT_URL% with branch %CM_GIT_CHECKOUT% %CM_GIT_DEPTH% %CM_GIT_RECURSE_SUBMODULES% ...

rem git clone %CM_GIT_RECURSE_SUBMODULES% %CM_GIT_URL% %CM_GIT_DEPTH% inference
rem cd inference
rem git checkout -b "%CM_GIT_CHECKOUT%"
rem 


set CUR_DIR=%cd%
set SCRIPT_DIR=%CM_TMP_CURRENT_SCRIPT_PATH%

set folder=%CM_GIT_CHECKOUT_FOLDER%

if not exist %CM_TMP_GIT_PATH% (

  if exist %folder% (
    deltree %folder%
  )
  echo ******************************************************
  echo Cloning %CM_GIT_REPO_NAME% from %CM_GIT_URL%
  echo "%CM_GIT_CLONE_CMD%"
  %CM_GIT_CLONE_CMD%
  IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
  if not "%CM_GIT_SHA%" == "" (
       echo.
       cd %folder%
       echo.
       git checkout "%CM_GIT_CHECKOUT%"
       IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
  )

) else (

  cd %folder%

)

if "%CM_GIT_PATCH%" == "yes" (
   echo Git patching is not yet implemented in CM script "get-git-repo" - please add it!
   pause

   rem  set patch_filename=%CM_GIT_PATCH_FILENAME%
   rem  if [ ! -n ${CM_GIT_PATCH_FILENAMES} ]; then
   rem    patchfile=${CM_GIT_PATCH_FILENAME:-"git.patch"}
   rem    CM_GIT_PATCH_FILENAMES=$patchfile
   rem  fi
   rem
   rem  IFS=', ' read -r -a patch_files <<< ${CM_GIT_PATCH_FILENAMES}
   rem
   rem  for patch_filename in "${patch_files[@]}"
   rem  do
   rem    echo "Applying patch ${SCRIPT_DIR}/patch/$patch_filename"
   rem    git apply ${SCRIPT_DIR}/patch/"$patch_filename"
   rem    if [ "${?}" != "0" ]; then exit 1; fi
   rem  done

)

cd %CUR_DIR%

exit /b 0
