@echo off

echo ******************************************************
echo Cloning MLCommons from %CM_GIT_URL% with branch %CM_GIT_CHECKOUT% %CM_GIT_DEPTH% %CM_GIT_RECURSE_SUBMODULES% ...

git clone %CM_GIT_RECURSE_SUBMODULES% %CM_GIT_URL% %CM_GIT_DEPTH% inference
cd inference
git checkout -b "%CM_GIT_CHECKOUT%"

exit /b 0
