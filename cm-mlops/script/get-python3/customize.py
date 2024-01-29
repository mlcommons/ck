from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    if env.get('CM_PYTHON_CONDA', '') == 'yes':
        env['CM_PYTHON_BIN_WITH_PATH'] = os.path.join(env['CM_CONDA_BIN_PATH'], "python")

    recursion_spaces = i['recursion_spaces']

    # we need to understand whether this script is called first and CM_PYTHON_BIN_WITH_PATH is empty
    #   then we should search for related artifacts (python in our case)
    # or this script is called after install-python* and CM_PYTHON_BIN_WITH_PATH is set there
    #   then we do not search for an artifact (python) but pick it up from the installation

    if 'CM_PYTHON_BIN_WITH_PATH' not in env:
        #file_name = 'python.exe' if os_info['platform'] == 'windows' else 'python[0-9|\.]*$'
        file_name = 'python.exe' if os_info['platform'] == 'windows' else 'python3'
        extra_paths = {"include" : "+C_INCLUDE_PATH", "lib" : "+LD_LIBRARY_PATH"}

        r = i['automation'].find_artifact({'file_name': file_name,
                                           'default_path_env_key': 'PATH',
                                           'env': env,
                                           'os_info':os_info,
                                           # this key defines env key with paths where to find an artifact
                                           'detect_version':True,
                                           # the next key is used in run.sh to detect python version
                                           'env_path_key':'CM_PYTHON_BIN_WITH_PATH',
                                           'run_script_input':i['run_script_input'],
                                           'recursion_spaces':i['recursion_spaces'],
                                           'extra_paths': extra_paths
                                           })
        if r['return']>0:
            if r['return'] == 16 and os_info['platform'] != 'windows':
                # If artifact is not found and we are not on windows
                # we should try to install python from src
                # in prehook_deps
                env['CM_REQUIRE_INSTALL'] = "yes"

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
    env['CM_PYTHON_BIN_PATH'] = os.path.dirname(found_file_path)

    # Save tags that can be used to specialize further dependencies (such as python packages)
    tags = 'version-'+version

    add_extra_cache_tags = []

    extra_tags = env.get('CM_EXTRA_CACHE_TAGS','')
    if extra_tags != '':
        tags += ',' + extra_tags

    # Check if called from virtual env installer
    from_virtual = True if 'virtual' in extra_tags.split(',') else False

    if not from_virtual:
        tags += ',non-virtual'

    env['CM_PYTHON_CACHE_TAGS'] = tags

    add_extra_cache_tags = tags.split(',')

    # Check if need to add path, include and lib to env
    # (if not in default paths)
    default_path_list = i['automation'].get_default_path_list(i)
    found_path_root = os.path.dirname(found_path)

    if from_virtual:
        # Clean PATH (it will be in activate script) 
        # but keep LD_LIBRARY_PATH and C_INCLUDE_PATH from the native python
        for k in ['+PATH']:
            if k in env:
                del(env[k])

    elif os_info['platform'] == 'windows':
        extra_path = os.path.join(found_path, 'Scripts')

        if extra_path not in default_path_list and extra_path+os.sep not in default_path_list:
            paths = env.get('+PATH',[])
            if extra_path not in paths:
                paths.append(extra_path)
                env['+PATH']=paths

    version_split = version.split(".")
    python_major_version = version_split[0]
    python_minor_version = version_split[1]
    if len(version_split) > 2:
        python_patch_version = version_split[2]

    env['CM_PYTHON_MAJOR_VERSION'] = python_major_version
    env['CM_PYTHON_MINOR_VERSION'] = python_minor_version
    env['CM_PYTHON_PATCH_VERSION'] = python_patch_version

    return {'return':0, 'version': version, 'add_extra_cache_tags':add_extra_cache_tags}
