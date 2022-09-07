from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    file_name = 'cmake.exe' if os_info['platform'] == 'windows' else 'cmake'

    # Will check env['CM_TMP_PATH'] if comes from installation script
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
           if env.get('CM_TMP_FAIL_IF_NOT_FOUND','').lower() == 'yes':
               return r

           print (recursion_spaces+'    # {}'.format(r['error']))

           # Attempt to run installer
           r = {'return':0, 'skip':True, 'script':{'tags':'install,prebuilt,cmake'}}

       return r

    found_path = r['found_path']

    env['CM_CMAKE_BIN']=file_name
    env['CM_CMAKE_BIN_WITH_PATH']=os.path.join(found_path, file_name)

    return {'return':0}



def postprocess(i):

    env = i['env']

    r = i['automation'].parse_version({'match_text': r'cmake version\s*([\d.]+)',
                                       'group_number': 1,
                                       'env_key':'CM_CMAKE_VERSION',
                                       'which_env':i['env']})
    if r['return'] >0: return r

    version = r['version']

    print (i['recursion_spaces'] + '    Detected version: {}'.format(version))

    env['CM_CMAKE_CACHE_TAGS'] = 'version-'+version
    if 'CM_HOST_CPU_TOTAL_CORES' in env:
        env['CM_MAKE_CORES'] =  env['CM_HOST_CPU_TOTAL_CORES']

    return {'return':0, 'version':version}
