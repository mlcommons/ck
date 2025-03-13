if exist Miniconda3-latest-Windows-x86_64.exe (
  del /Q /S Miniconda3-latest-Windows-x86_64.exe
)

wget --no-check-certificate https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

start /wait "" Miniconda3-latest-Windows-x86_64.exe /InstallationType=JustMe /RegisterPython=0 /S /D=%CD%\miniconda3
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
