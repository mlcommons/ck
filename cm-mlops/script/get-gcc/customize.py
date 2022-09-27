from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    file_name_c = 'gcc.exe' if os_info['platform'] == 'windows' else 'gcc'
    file_name_cpp = 'g++.exe' if os_info['platform'] == 'windows' else 'g++'

    # Will check env['CM_TMP_PATH'] if comes from installation script
    r = i['automation'].find_artifact({'file_name': file_name_c,
                                       'env': env,
                                       'os_info':os_info,
                                       'default_path_env_key': 'PATH',
                                       'detect_version':True,
                                       'env_path_key':'CM_GCC_BIN_WITH_PATH',
                                       'run_script_input':i['run_script_input'],
                                       'recursion_spaces':recursion_spaces})
    if r['return'] >0 : 
#       if r['return'] == 16:
#           if env.get('CM_TMP_FAIL_IF_NOT_FOUND','').lower() == 'yes':
#               return r
#
#           print (recursion_spaces+'    # {}'.format(r['error']))
#
#           # Attempt to run installer
#           r = {'return':0, 'skip':True, 'script':{'tags':'install,prebuilt,gcc'}}

       return r

    # G: changed next line to handle cases like gcc-8
    # found_path = r['found_path']
    full_path = r['full_path']

    found_path = os.path.dirname(full_path)
    found_file = os.path.basename(full_path)

    file_name_c = found_file
    file_name_cpp = found_file.replace('gcc','g++')

    env['CM_GCC_BIN']=file_name_c
    env['CM_GCC_BIN_WITH_PATH']=os.path.join(found_path, file_name_c)

    # General compiler for general program compilation
    env['CM_C_COMPILER_BIN']=file_name_c
    env['CM_C_COMPILER_WITH_PATH']=os.path.join(found_path, file_name_c)

    env['CM_CXX_COMPILER_BIN']=file_name_cpp
    env['CM_CXX_COMPILER_WITH_PATH']=os.path.join(found_path, file_name_cpp)

    env['FAST_COMPILER_FLAGS'] = "-O3"
    env['FAST_LINKER_FLAGS'] = "-O3"
    env['DEBUG_COMPILER_FLAGS'] = "-O0"
    env['DEBUG_LINKER_FLAGS'] = "-O0"
    env['DEFAULT_COMPILER_FLAGS'] = "-O2"
    env['DEFAULT_LINKER_FLAGS'] = "-O2"

    return {'return':0}


def postprocess(i):

    env = i['env']

    r = i['automation'].parse_version({'match_text': r' \(.*\)\s*([\d.]+)',
                                       'group_number': 1,
                                       'env_key':'CM_GCC_VERSION',
                                       'which_env':i['env']})

    if r['return'] >0: return r

    version = r['version']

    print (i['recursion_spaces'] + '    Detected version: {}'.format(version))

    env['CM_COMPILER_FAMILY'] = 'GCC'
    env['CM_COMPILER_VERSION'] = env['CM_GCC_VERSION']
    env['CM_GCC_CACHE_TAGS'] = 'version-'+version
    env['CM_COMPILER_CACHE_TAGS'] = 'version-'+version+',family-gcc'

    return {'return':0, 'version':version}
