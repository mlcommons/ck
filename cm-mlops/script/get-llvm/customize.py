from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    file_name_c = 'clang.exe' if os_info['platform'] == 'windows' else 'clang'
    file_name_cpp = 'clang++.exe' if os_info['platform'] == 'windows' else 'clang++'

    # Will check env['CM_TMP_PATH'] if comes from installation script
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
           if env.get('CM_TMP_FAIL_IF_NOT_FOUND','').lower() == 'yes':
               return r

           print (recursion_spaces+'    # {}'.format(r['error']))

           # Attempt to run installer
           r = {'return':0, 'skip':True, 'script':{'tags':'install,prebuilt,llvm'}}

       return r

    found_path = r['found_path']

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


def postprocess(i):

    env = i['env']

    r = i['automation'].parse_version({'match_text': r'clang version\s*([\d.]+)',
                                       'group_number': 1,
                                       'env_key':'CM_LLVM_CLANG_VERSION',
                                       'which_env':i['env']})
    if r['return'] >0: return r

    version = r['version']

    print (i['recursion_spaces'] + '    Detected version: {}'.format(version))

    env['CM_LLVM_CLANG_CACHE_TAGS'] = 'version-'+version
    env['CM_COMPILER_CACHE_TAGS'] = 'version-'+version+',family-llvm'
    env['CM_COMPILER_FAMILY'] = 'LLVM'
    env['CM_COMPILER_VERSION'] = env['CM_LLVM_CLANG_VERSION']

    return {'return':0, 'version':version}
