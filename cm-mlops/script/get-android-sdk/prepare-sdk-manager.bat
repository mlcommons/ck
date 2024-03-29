﻿echo %CM_ANDROID_SDK_MANAGER_BIN_WITH_PATH%

call %CM_ANDROID_SDK_MANAGER_BIN_WITH_PATH% --version > tmp-ver.out
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

more tmp-ver.out

call %CM_ANDROID_SDK_MANAGER_BIN_WITH_PATH% --licenses
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

call %CM_ANDROID_SDK_MANAGER_BIN_WITH_PATH% ^
    "tools" ^
    "platform-tools" ^
    "extras;android;m2repository" ^
    "extras;google;m2repository" ^
    "extras;google;google_play_services" ^
    "build-tools;%CM_ANDROID_BUILD_TOOLS_VERSION%"
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

call %CM_ANDROID_SDK_MANAGER_BIN_WITH_PATH% "platforms;android-%CM_ANDROID_VERSION%"
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

call %CM_ANDROID_SDK_MANAGER_BIN_WITH_PATH% "cmake;%CM_ANDROID_CMAKE_VERSION%"
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

call %CM_ANDROID_SDK_MANAGER_BIN_WITH_PATH% "ndk;%CM_ANDROID_NDK_VERSION%"
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
