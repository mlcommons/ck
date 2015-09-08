@echo off

rem
rem Collective Knowledge
rem
rem See CK LICENSE.txt for licensing details.
rem See CK COPYRIGHT.txt for copyright details.
rem
rem Developer: Grigori Fursin
rem

rem Change dir to the CK entry

for /f %%i in ('ck find %1') do cd /d %%i
