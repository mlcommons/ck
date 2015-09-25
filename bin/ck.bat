@echo off

rem Set default path by detecting the path to this script
set ck_path=%~dp0\..

rem Check if CK_ROOT is defined and used it, otherwise use auto-detected path
IF "%CK_ROOT%"=="" set CK_ROOT=%ck_path%

rem Load kernel module (either GIT/local installation or as package)
IF EXIST %CK_ROOT%\ck\kernel.py (
 python -W ignore::DeprecationWarning %CK_ROOT%\ck\kernel.py %*
) ELSE (
 python -W ignore::DeprecationWarning -m ck.kernel %*
)
