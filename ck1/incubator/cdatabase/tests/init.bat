set curpath=%cd%

cd ..

set mypath=%cd%
set PYTHONPATH=%mypath%;%PYTHONPATH%

cd %curpath%
