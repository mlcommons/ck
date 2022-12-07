from cmind import utils
import os

def preprocess(i):
    
    os_info = i['os_info']
    platform = os_info['platform']

    env = i['env']

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    run_script_input = i['run_script_input']

    # Check if ANDROID_HOME is already set
    android_home = os.environ.get('ANDROID_HOME','').strip()

    # We are inside CM cache entry
    cur_dir = os.getcwd()

    if android_home == '':
        android_home = cur_dir

    env['CM_ANDROID_HOME']=android_home
    env['ANDROID_HOME']=android_home

    paths = []

    # Check SDK manager
    ext = ''
    host_os_for_android = 'linux'
    host_os_for_ndk = 'linux-x86_64'
    if platform == "windows":
        host_os_for_android = 'win'
        host_os_for_ndk = 'windows-x86_64'
        ext = '.bat'
    elif platform == "darwin":
        host_os_for_android = 'mac'

    sdk_manager_file = 'sdkmanager'+ext

    print ('')

    found = False

    for x in ['cmdline-tools', 'cmdline-tools'+os.sep+'tools', 'tools']:
        sdk_manager_path = os.path.join(android_home, x, 'bin', sdk_manager_file)
        if os.path.isfile(sdk_manager_path):
            found = True
            break

    if not found:
        # Some magic for cmdline tools (need specific directory)
        new_path = os.path.join(android_home, 'cmdline-tools')
        if not os.path.isdir(new_path):
            os.makedirs(new_path)
        
        os.chdir(new_path)
        
        cmdline_tools_version=env.get('CM_ANDROID_CMDLINE_TOOLS_VERSION','')

        env['CM_ANDROID_CMDLINE_TOOLS_VERSION'] = cmdline_tools_version
        
        package_url = env['CM_ANDROID_CMDLINE_TOOLS_URL']
        package_url = package_url.replace('${CM_ANDROID_CMDLINE_TOOLS_OS}', host_os_for_android)
        package_url = package_url.replace('${CM_ANDROID_CMDLINE_TOOLS_VERSION}', cmdline_tools_version)

        env['CM_ANDROID_CMDLINE_TOOLS_URL'] = package_url

        print ('')
        print ('Downloading from {} ...'.format(package_url))

        cm = automation.cmind

        r = cm.access({'action':'download_file', 
                       'automation':'utils,dc2743f8450541e3', 
                       'url':package_url})
        if r['return']>0: return r

        filename = r['filename']

        print ('Unzipping file {}'.format(filename))

        r = cm.access({'action':'unzip_file', 
                       'automation':'utils,dc2743f8450541e3', 
                       'filename':filename,
                       'strip_folders':0})
        if r['return']>0: return r

#        if os.path.isfile(filename):
#            print ('Removing file {}'.format(filename))
#            os.remove(filename)

        os.rename('cmdline-tools', 'tools')

        os.chdir(cur_dir)

        sdk_manager_path = os.path.join(android_home, 'cmdline-tools', 'tools', 'bin', sdk_manager_file)
    
    sdk_manager_dir = os.path.dirname(sdk_manager_path)
    
    env['CM_ANDROID_SDK_MANAGER_BIN'] = sdk_manager_file
    env['CM_ANDROID_SDK_MANAGER_BIN_WITH_PATH'] = sdk_manager_path

    env['CM_GET_DEPENDENT_CACHED_PATH'] = cur_dir

    paths.append(sdk_manager_dir)

    # Prepare SDK
    print ('Preparing Android SDK manager ...')

    r = automation.run_native_script({'run_script_input':run_script_input, 'env':env, 'script_name':'prepare-sdk-manager'})
    if r['return']>0: return r


    build_tools_version=env['CM_ANDROID_BUILD_TOOLS_VERSION']

    path_build_tools = os.path.join(android_home, 'build-tools', build_tools_version)
    env['CM_ANDROID_BUILD_TOOLS_PATH']=path_build_tools
    paths.append(path_build_tools)


    cmake_version=env['CM_ANDROID_CMAKE_VERSION']

    path_cmake = os.path.join(android_home, 'cmake', cmake_version, 'bin')
    env['CM_ANDROID_CMAKE_PATH']=path_cmake
    paths.append(path_cmake)


    path_emulator = os.path.join(android_home, 'emulator')
    env['CM_ANDROID_EMULATOR_PATH']=path_emulator
    paths.append(path_emulator)

    path_platform_tools = os.path.join(android_home, 'platform-tools')
    env['CM_ANDROID_PLATFORM_TOOLS_PATH']=path_platform_tools
    paths.append(path_platform_tools)


    android_version=env['CM_ANDROID_VERSION']

    path_platforms = os.path.join(android_home, 'platforms', android_version)
    env['CM_ANDROID_PLATFORMS_PATH']=path_platforms


    path_tools = os.path.join(android_home, 'tools')
    env['CM_ANDROID_TOOLS_PATH']=path_tools
    paths.append(path_tools)
    
    android_ndk_version=env['CM_ANDROID_NDK_VERSION']

    # Check Android NDK
    path_ndk = os.path.join(android_home, 'ndk', android_ndk_version)
    env['CM_ANDROID_NDK_PATH']=path_ndk
    env['ANDROID_NDK_HOME']=path_ndk
    

    
    path_ndk_compiler = os.path.join(path_ndk, 'toolchains', 'llvm', 'prebuilt', host_os_for_ndk, 'bin')
    env['CM_ANDROID_LLVM_PATH']=path_ndk_compiler
    env['CM_ANDROID_LLVM_CLANG_BIN_WITH_PATH']=os.path.join(path_ndk_compiler, 'clang.exe')
    paths.append(path_ndk_compiler)



    env['+PATH'] = paths

    return {'return':0} #, 'version': version}
