@echo off

rem Set default path by detecting the path to this script
set ck_path1=%~dp0
set ck_path=%ck_path1%\..

rem Check if CK_ROOT is defined and used it, otherwise use auto-detected path
IF "%CK_ROOT%"=="" set CK_ROOT=%ck_path%

IF "%CK_PYTHON%"=="" (
   set CK_PYTHON=python
)

rem Load kernel module (either GIT/local installation or as package)
IF EXIST %CK_ROOT%\ck\kernel.py (
 %CK_PYTHON% -W ignore::DeprecationWarning %CK_ROOT%\ck\kernel.py %*
) ELSE (
 %CK_PYTHON% -W ignore::DeprecationWarning -W ignore::RuntimeWarning -m ck.kernel %*
)
