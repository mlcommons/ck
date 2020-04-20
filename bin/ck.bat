@echo off

rem Set default path by detecting the path to this script
set ck_path1=%~dp0
set ck_path2=%ck_path1%\..

if exist "%ck_path1%\ck-python.cfg%" (
   set /p ck_python_pip=<"%ck_path1%\ck-python.cfg"
)

IF "%CK_PYTHON%"=="" (
   set CK_PYTHON=python
   if exist "%ck_python_pip%" (
      set CK_PYTHON=%ck_python_pip%
   )
)

IF "%CK_ROOT%"=="" (
   if exist "%ck_path2%\ck\kernel.py" (
      set CK_ROOT=%ck_path2%
   )
)

rem Load kernel module (either GIT/local installation or as package)
IF EXIST "%CK_ROOT%\ck\kernel.py" (
 %CK_PYTHON% -W ignore::DeprecationWarning "%CK_ROOT%\ck\kernel.py" %*
) ELSE (
 %CK_PYTHON% -W ignore::DeprecationWarning -W ignore::RuntimeWarning -m ck.kernel %*
)
