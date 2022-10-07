from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    # we need to understand whether this script is called first and CM_PYTHON_BIN_WITH_PATH is empty
    #   then we should search for related artifacts (python in our case)
    # or this script is called after install-python* and CM_PYTHON_BIN_WITH_PATH is set there
    #   then we do not search for an artifact (python) but pick it up from the installation

    if 'CM_PYTHON_BIN_WITH_PATH' not in env:
        file_name = 'python.exe' if os_info['platform'] == 'windows' else 'python3'

        r = i['automation'].find_artifact({'file_name': file_name,
                                           'env': env,
                                           'os_info':os_info,
                                           # this key defines env key with paths where to find an artifact
                                           'default_path_env_key': 'PATH',
                                           'detect_version':True,
                                           # the next key is used in run.sh to detect python version
                                           'env_path_key':'CM_PYTHON_BIN_WITH_PATH',
                                           'run_script_input':i['run_script_input'],
                                           'recursion_spaces':i['recursion_spaces']})
        if r['return']>0:
            if r['return'] == 16 and os_info['platform'] != 'windows':
                # If artifact is not found and we are not on windows
                # we should try to install python from src
                # in prehook_deps
                env['CM_TMP_REQUIRE_INSTALL'] = "yes"

                return {'return': 0}
            else:
                return r

    return {'return':0}

def detect_version(i):
    r = i['automation'].parse_version({'match_text': r'Python\s*([\d.]+)',
                                       'group_number': 1,
                                       'env_key':'CM_PYTHON_VERSION',
                                       'which_env':i['env']})
    if r['return'] >0: return r

    version = r['version']

    print (i['recursion_spaces'] + '      Detected version: {}'.format(version))
    return {'return':0, 'version':version}

def postprocess(i):

    env = i['env']
    os_info = i['os_info']

    r = detect_version(i)
    if r['return'] >0: return r

    version = r['version']

    found_file_path = env['CM_PYTHON_BIN_WITH_PATH']

    found_path = os.path.dirname(found_file_path)

    env['CM_PYTHON_BIN'] = os.path.basename(found_file_path)

    default_path_list = i['automation'].get_default_path_list(i)


    # Check if need to add path, include and lib to env
    # (if not in default paths)
    found_path_root = os.path.dirname(found_path)
    for x in [{'path': found_path, 'var':'PATH'},
              {'path': os.path.join(found_path_root, 'lib'), 'var':'LD_LIBRARY_PATH'},
              {'path': os.path.join(found_path_root, 'include'), 'var':'C_INCLUDE_PATH'}]:
        path = x['path']
        var = x['var']

        if os.path.isdir(path):
            default_path = os.environ.get(var, '').split(os_info['env_separator'])
            if path not in default_path and path+os.sep not in default_path:
                env['+'+var] = [path]

    # Add extra dir to path on Windows
    if os_info['platform'] == 'windows':

        extra_path = os.path.join(os.path.dirname(found_path), 'Scripts')

        if extra_path not in default_path_list and extra_path+os.sep not in default_path_list:
            paths = env.get('+PATH',[])
            if extra_path not in paths:
                paths.append(extra_path)
                env['+PATH']=paths

    # Save tags that can be used to specialize further dependencies (such as python packages)
    tags = 'version-'+version

    extra_tags = env.get('CM_EXTRA_CACHE_TAGS','')
    if extra_tags != '':
        tags += ',' + extra_tags

    if 'virtual' not in extra_tags.split(','):
        tags += ',non-virtual'

    env['CM_PYTHON_CACHE_TAGS'] = tags

    return {'return':0}
