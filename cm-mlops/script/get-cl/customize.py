from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] != 'windows':
        return {'return':0}

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    file_name = 'cl.exe'

    # Will check env['CM_TMP_PATH'] if comes from installation script
    r = i['automation'].find_artifact({'file_name': file_name,
                                       'env': env,
                                       'os_info':os_info,
                                       'default_path_env_key': 'PATH',
                                       'detect_version':True,
                                       'env_path_key':'CM_CL_BIN_WITH_PATH',
                                       'run_script_input':i['run_script_input'],
                                       'recursion_spaces':recursion_spaces})
    if r['return'] >0 : return r

    found_path = r['found_path']

    # Check vcvarall.bat
    state = i['state']
    script_prefix = state.get('script_prefix',[])

    path_to_vcvarsall = os.path.join(os.path.dirname(found_path), 'vcvarsall.bat')
    if os.path.isfile(path_to_vcvarsall):
        s = os_info['run_bat'].replace('${bat_file}', '"'+path_to_vcvarsall+'"')
        script_prefix.append(s)
        state['script_prefix'] = script_prefix

    env['CM_CL_BIN']=file_name
    env['CM_CL_BIN_WITH_PATH']=os.path.join(found_path, file_name)

    # General compiler for general program compilation
    env['CM_C_COMPILER_BIN']=file_name
    env['CM_C_COMPILER_WITH_PATH']=os.path.join(found_path, file_name)

    env['CM_CPP_COMPILER_BIN']=file_name
    env['CM_CPP_COMPILER_WITH_PATH']=os.path.join(found_path, file_name)

    return {'return':0}


def postprocess(i):

    env = i['env']

    r = i['automation'].parse_version({'match_text': r'Version\s*([\d.]+)',
                                       'group_number': 1,
                                       'env_key':'CM_CL_VERSION',
                                       'which_env':i['env']})
    if r['return'] >0: return r

    version = r['version']

    print (i['recursion_spaces'] + '    Detected version: {}'.format(version))

    env['CM_CL_CACHE_TAGS'] = 'version-'+version
    env['CM_COMPILER_CACHE_TAGS'] = 'version-'+version
    env['CM_COMPILER_FAMILY'] = 'CUDA'
    env['CM_COMPILER_VERSION'] = env['CM_CL_VERSION']

    return {'return':0, 'version':version}
