from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    file_name = 'aws.exe' if os_info['platform'] == 'windows' else 'aws'
    env['FILE_NAME'] = file_name
    if 'CM_AWS_BIN_WITH_PATH' not in env:
        r = i['automation'].find_artifact({'file_name': file_name,
                                       'env': env,
                                       'os_info':os_info,
                                       'default_path_env_key': 'PATH',
                                       'detect_version':True,
                                       'env_path_key':'CM_AWS_BIN_WITH_PATH',
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
    r = i['automation'].parse_version({'match_text': r'aws-cli/([\d.]+)\s',
                                       'group_number': 1,
                                       'env_key':'CM_AWS_VERSION',
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
    found_file_path = env['CM_AWS_BIN_WITH_PATH']

    found_path = os.path.dirname(found_file_path)
    env['CM_AWS_INSTALLED_PATH'] = found_path

    env['CM_AWS_CACHE_TAGS'] = 'version-'+version

    return {'return':0, 'version': version}
