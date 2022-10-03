from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    file_name_c = 'clang.exe' if os_info['platform'] == 'windows' else 'clang'
    file_name_cpp = 'clang++.exe' if os_info['platform'] == 'windows' else 'clang++'
    env['FILE_NAME_C'] = file_name_c
    env['FILE_NAME_CPP'] = file_name_cpp
    if 'CM_LLVM_INSTALLED_PATH' not in env:

        r = i['automation'].find_artifact({'file_name': file_name_c,
                                       'env': env,
                                       'os_info':os_info,
                                       'default_path_env_key': 'PATH',
                                       'detect_version':True,
                                       'env_path_key':'CM_LLVM_CLANG_BIN_WITH_PATH',
                                       'run_script_input':i['run_script_input'],
                                       'recursion_spaces':recursion_spaces})
        if r['return'] >0 : 
            if r['return'] == 16:
                env['CM_TMP_REQUIRE_INSTALL'] = "yes"
                return {'return': 0}
            else:
                return r

        env['CM_LLVM_INSTALLED_PATH'] =  r['found_path']

    return {'return':0}

def detect_version(i):

    r = i['automation'].parse_version({'match_text': r'clang version\s*([\d.]+)',
                                       'group_number': 1,
                                       'env_key':'CM_LLVM_CLANG_VERSION',
                                       'which_env':i['env']})
    if r['return'] >0: return r

    version = r['version']

    print (i['recursion_spaces'] + '    Detected version: {}'.format(version))

    return {'return':0, 'version':version}

def postprocess(i):

    env = i['env']
    r = detect_version(i)
    if r['return'] >0: return r
    version = env['CM_LLVM_CLANG_VERSION']
    env['CM_LLVM_CLANG_CACHE_TAGS'] = 'version-'+version
    env['CM_COMPILER_CACHE_TAGS'] = 'version-'+version+',family-llvm'
    env['CM_COMPILER_FAMILY'] = 'LLVM'
    env['CM_COMPILER_VERSION'] = env['CM_LLVM_CLANG_VERSION']

    file_name_c = env['FILE_NAME_C']
    file_name_cpp = env['FILE_NAME_CPP']
    found_path = env['CM_LLVM_INSTALLED_PATH']
    env['CM_LLVM_CLANG_BIN']=file_name_c
    env['CM_LLVM_CLANG_BIN_WITH_PATH']=os.path.join(found_path, file_name_c)

    # General compiler for general program compilation
    env['CM_C_COMPILER_BIN']=file_name_c
    env['CM_C_COMPILER_WITH_PATH']=os.path.join(found_path, file_name_c)

    env['CM_CXX_COMPILER_BIN']=file_name_cpp
    env['CM_CXX_COMPILER_WITH_PATH']=os.path.join(found_path, file_name_cpp)

    env['FAST_COMPILER_FLAGS'] = "-O3"
    env['FAST_LINKER_FLAGS'] = "-O3 -flto"
    env['DEBUG_COMPILER_FLAGS'] = "-O0"
    env['DEBUG_LINKER_FLAGS'] = "-O0"
    env['DEFAULT_COMPILER_FLAGS'] = "-O2"
    env['DEFAULT_LINKER_FLAGS'] = "-O2"

    return {'return':0}
