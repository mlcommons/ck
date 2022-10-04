from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    file_name = 'cmake.exe' if os_info['platform'] == 'windows' else 'cmake'
    env['FILE_NAME'] = file_name
    if 'CM_CMAKE_INSTALLED_PATH' not in env:
        r = i['automation'].find_artifact({'file_name': file_name,
                                       'env':env,
                                       'os_info':os_info,
                                       'default_path_env_key': 'PATH',
                                       'detect_version':True,
                                       'env_path_key':'CM_CMAKE_BIN_WITH_PATH',
                                       'run_script_input':i['run_script_input'],
                                       'recursion_spaces':recursion_spaces})
        if r['return'] >0 : 
            if r['return'] == 16:
                env['CM_TMP_REQUIRE_INSTALL'] = "yes"
                return {'return': 0}
            else:
                return r

        env['CM_CMAKE_INSTALLED_PATH'] =  r['found_path']

    return {'return':0}

def detect_version(i):
    r = i['automation'].parse_version({'match_text': r'cmake version\s*([\d.]+)',
                                       'group_number': 1,
                                       'env_key':'CM_CMAKE_VERSION',
                                       'which_env':i['env']})
    if r['return'] >0: return r

    version = r['version']
    print (i['recursion_spaces'] + '    Detected version: {}'.format(version))

    return {'return':0, 'version':version}

def postprocess(i):

    env = i['env']

    r = detect_version(i)

    if r['return'] >0: return r

    version = r['version']

    env['CM_CMAKE_CACHE_TAGS'] = 'version-'+version
    if 'CM_HOST_CPU_TOTAL_CORES' in env:
        env['CM_MAKE_CORES'] =  env['CM_HOST_CPU_TOTAL_CORES']

    return {'return':0}
