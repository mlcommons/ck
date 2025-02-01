@echo off

set CUR_DIR=%cd%
set SCRIPT_DIR=%CM_TMP_CURRENT_SCRIPT_PATH%

echo ******************************************************
echo Cloning MLCommons from %CM_GIT_URL% with branch %CM_GIT_CHECKOUT% %CM_GIT_DEPTH% %CM_GIT_RECURSE_SUBMODULES% ...

set folder=src

if not exist %folder% (

  if not "%CM_GIT_SHA%" == "" (
       git clone %CM_GIT_RECURSE_SUBMODULES% -b "%CM_GIT_CHECKOUT%" %CM_GIT_URL% %CM_GIT_DEPTH% %folder%
       IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
       cd %folder%
  ) else (
       git clone %CM_GIT_RECURSE_SUBMODULES% %CM_GIT_URL% %CM_GIT_DEPTH% %folder%
       IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
       cd %folder%

       git checkout "%CM_GIT_CHECKOUT%"
       IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
  )
) else (

  cd %folder%

)


if not "%CM_GIT_SUBMODULES%" == "" (
  for /F %%s in ("%CM_GIT_SUBMODULES%") do (
    echo.
    echo Initializing submodule %%s
    git submodule update --init %%s
    IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
  )
)


if "%CM_GIT_PATCH%" == "yes" (
   echo Git patching is not yet implemented in CM script "get-mlperf-tiny-src" - please add it!
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

rem Based on https://github.com/mwangistan/inference
for %%f in (%SCRIPT_DIR%\patch\windows-*) do (
  echo %%f
  patch -p1 < %%f
)


cd %CUR_DIR%

exit /b 0
