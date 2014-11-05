@echo off

rem
rem Collective Knowledge
rem
rem See CK LICENSE.txt for licensing details.
rem See CK Copyright.txt for copyright details.
rem
rem Developer: Grigori Fursin
rem

rem CK entry point

rem Set default path by detecting the path to this script
set ck_path=%~dp0\..

rem Check if CK_ROOT is defined and used it, otherwise use auto-detected path
IF "%CK_ROOT%"=="" set CK_ROOT=%ck_path%

rem Load kernel module
IF EXIST %CK_ROOT%\ck\kernel.py (
 python -W ignore::DeprecationWarning %CK_ROOT%\ck\kernel.py %*
) ELSE (
  echo cK Error: kernel module not found!
)
