echo ${JAVA_HOME}
echo ${CM_ANDROID_SDK_MANAGER_BIN_WITH_PATH}

${CM_ANDROID_SDK_MANAGER_BIN_WITH_PATH} --version > tmp-ver.out
cat tmp-ver.out

${CM_ANDROID_SDK_MANAGER_BIN_WITH_PATH} --licenses
test $? -eq 0 || exit 1

${CM_ANDROID_SDK_MANAGER_BIN_WITH_PATH} \
    "tools" \
    "platform-tools" \
    "extras;android;m2repository" \
    "extras;google;m2repository" \
    "extras;google;google_play_services" \
    "build-tools;${CM_ANDROID_BUILD_TOOLS_VERSION}"
test $? -eq 0 || exit 1

${CM_ANDROID_SDK_MANAGER_BIN_WITH_PATH} "platforms;android-${CM_ANDROID_VERSION}"
test $? -eq 0 || exit 1

${CM_ANDROID_SDK_MANAGER_BIN_WITH_PATH} "cmake;${CM_ANDROID_CMAKE_VERSION}"
test $? -eq 0 || exit 1

${CM_ANDROID_SDK_MANAGER_BIN_WITH_PATH} "ndk;${CM_ANDROID_NDK_VERSION}"
test $? -eq 0 || exit 1
