from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    # Add extra tags to python
    add_extra_cache_tags = [] # for this script
    add_python_extra_cache_tags = ['virtual'] # for get-python script

    name = env.get('CM_NAME','')
    if not quiet and name == '':
        print ('')
        x = input('Enter some tag to describe this virtual env (mlperf-inf,octoml-bench,etc): ')
        x = x.strip()

        if x != '': name = x

    directory_name = 'venv'
    if name != '':
        directory_name = name.strip().lower()
        name_tag = 'name-' + directory_name

        add_extra_cache_tags.append(name_tag)
        add_python_extra_cache_tags.append(name_tag)

    env['CM_VIRTUAL_ENV_DIR'] = directory_name
    env['CM_VIRTUAL_ENV_PATH'] = os.path.join(os.getcwd(), directory_name)

    s = 'Scripts' if os_info['platform'] == 'windows' else 'bin'
    env['CM_VIRTUAL_ENV_SCRIPTS_PATH'] = os.path.join(env['CM_VIRTUAL_ENV_PATH'], s)

    env['CM_TMP_PATH'] = env['CM_VIRTUAL_ENV_SCRIPTS_PATH']
    env['CM_TMP_FAIL_IF_NOT_FOUND'] = 'yes'


    r = automation.update_deps({'deps':meta['post_deps'], 
                                'update_deps':{'register-python':
                                   {'extra_cache_tags':','.join(add_python_extra_cache_tags)}}})
    if r['return']>0: return r

    env['CM_PYTHON_INSTALLED_PATH'] = env['CM_VIRTUAL_ENV_SCRIPTS_PATH']

    return {'return':0, 'add_extra_cache_tags':add_extra_cache_tags}

def postprocess(i):

    os_info = i['os_info']

    env = i['env']

    state = i['state']

    script_prefix = state.get('script_prefix',[])

    path_to_activate = os.path.join(env['CM_VIRTUAL_ENV_SCRIPTS_PATH'], 'activate')

    # If windows, download here otherwise use run.sh
    if os_info['platform'] == 'windows':
        path_to_activate += '.bat'

    s = os_info['run_bat'].replace('${bat_file}', '"'+path_to_activate+'"')

    script_prefix.append(s)
    state['script_prefix'] = script_prefix

    python_name = 'python.exe' if os_info['platform'] == 'windows' else 'python3'

    # Will be passed to get-python to finalize registering of the new python
    env['CM_PYTHON_BIN_WITH_PATH'] = os.path.join(env['CM_PYTHON_INSTALLED_PATH'], python_name)

    return {'return':0}
