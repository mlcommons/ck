from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    file_name_c = 'clang.exe' if os_info['platform'] == 'windows' else 'clang'

    env['FILE_NAME_C'] = file_name_c

    if 'CM_LLVM_CLANG_BIN_WITH_PATH' not in env:
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
                env['CM_REQUIRE_INSTALL'] = "yes"
                return {'return': 0}
            else:
                return r

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

    found_file_path = env['CM_LLVM_CLANG_BIN_WITH_PATH']

    found_path = os.path.dirname(found_file_path)

    file_name_c = os.path.basename(found_file_path)
    file_name_cpp = file_name_c.replace("clang", "clang++")

    env['CM_LLVM_CLANG_BIN']=file_name_c

    # General compiler for general program compilation
    env['CM_C_COMPILER_BIN']=file_name_c
    env['CM_C_COMPILER_WITH_PATH']=found_file_path
    env['CM_C_COMPILER_FLAG_OUTPUT']='-o '
    env['CM_C_COMPILER_FLAG_VERSION']='--version'
    env['CM_C_COMPILER_FLAG_INCLUDE']='-I'

    env['CM_CXX_COMPILER_BIN']=file_name_cpp
    env['CM_CXX_COMPILER_WITH_PATH']=os.path.join(found_path, file_name_cpp)
    env['CM_CXX_COMPILER_FLAG_OUTPUT']='-o '
    env['CM_CXX_COMPILER_FLAG_VERSION']='--version'
    env['CM_CXX_COMPILER_FLAG_INCLUDE']='-I'

    env['CM_COMPILER_FLAGS_FAST'] = "-O4"
    env['CM_LINKER_FLAGS_FAST'] = "-O4" # "-flto" - this flag is not always available (requires LLVMgold.so)
    env['CM_COMPILER_FLAGS_DEBUG'] = "-O0"
    env['CM_LINKER_FLAGS_DEBUG'] = "-O0"
    env['CM_COMPILER_FLAGS_DEFAULT'] = "-O2"
    env['CM_LINKER_FLAGS_DEFAULT'] = "-O2"

    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_LLVM_CLANG_BIN_WITH_PATH']

    return {'return':0, 'version': version}
