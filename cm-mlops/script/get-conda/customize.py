from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    automation = i['automation']
    run_script_input = i['run_script_input']

    recursion_spaces = i['recursion_spaces']

    conda_prefix_name = env.get('CM_CONDA_PREFIX_NAME', '')
    r = None
    file_name = 'conda.exe' if os_info['platform'] == 'windows' else 'conda'
    if conda_prefix_name == '':
        tmp_path = env.get('CM_CONDA_INSTALL_PATH', env.get('CM_TMP_PATH', ''))
        if tmp_path:
            x = ';' if os_info['platform'] == 'windows' else ':'
            tmp_path+=x
        conda_path = os.path.join(os.path.expanduser("~"), "miniconda3", "bin")
        if os.path.exists(conda_path):
            tmp_path += os.path.join(os.path.expanduser("~"), "miniconda3", "bin")
        env['CM_TMP_PATH'] = tmp_path

        r = i['automation'].find_artifact({'file_name': file_name,
                                           'env': env,
                                           'os_info':os_info,
                                           'default_path_env_key': 'PATH',
                                           'detect_version':True,
                                           'env_path_key':'CM_CONDA_BIN_WITH_PATH',
                                           'run_script_input':i['run_script_input'],
                                           'recursion_spaces':recursion_spaces})
    else:
        env['CM_CONDA_INSTALL_PATH'] = os.path.join(os.getcwd(), "miniconda3")
        bin_dir = 'Scripts' if os_info['platform'] == 'windows' else 'bin'
        env['CM_CONDA_BIN_WITH_PATH'] = os.path.join(env['CM_CONDA_INSTALL_PATH'], bin_dir, file_name)

    if conda_prefix_name != '' or r['return'] >0 : 
        if conda_prefix_name != '' or r['return'] == 16:
            if conda_prefix_name == '':
                if env.get('CM_TMP_FAIL_IF_NOT_FOUND','').lower() == 'yes':
                    return r

                print (recursion_spaces+'    # {}'.format(r['error']))

            # Attempt to run installer
            r = automation.run_native_script({'run_script_input':run_script_input, 'env':env, 'script_name':'install'})
            if r['return']>0: return r

            # Grigori: temporal fix - should be generalized/improved above
            if os_info['platform'] == 'windows' and env.get('CM_CONDA_BIN_WITH_PATH','')=='':
                env['CM_CONDA_INSTALL_PATH'] = os.path.join(os.getcwd(), "miniconda3")
                env['CM_CONDA_BIN_WITH_PATH'] = os.path.join(env['CM_CONDA_INSTALL_PATH'], 'Scripts', file_name)


    else:
        found_path = r['found_path']
        env['+PATH'] = [ found_path ]

    return {'return':0}

def detect_version(i):
    r = i['automation'].parse_version({'match_text': r'conda\s*([\d.]+)',
                                       'group_number': 1,
                                       'env_key':'CM_CONDA_VERSION',
                                       'which_env':i['env']})
    if r['return'] >0: return r
    return {'return':0, 'version':r['version']}

def postprocess(i):
    env = i['env']

    r = detect_version(i)
    if r['return'] >0: return r

    conda_bin_path = os.path.dirname(env['CM_CONDA_BIN_WITH_PATH'])
    env['CM_CONDA_BIN_PATH'] = conda_bin_path

    conda_prefix = os.path.dirname(conda_bin_path)
    env['CM_CONDA_PREFIX'] = conda_prefix
    env['CONDA_PREFIX'] = conda_prefix

    conda_lib_path = os.path.join(conda_prefix, "lib")

    if os.path.exists(conda_lib_path):
        env['CM_CONDA_LIB_PATH'] = conda_lib_path
        env['+LD_LIBRARY_PATH'] = [ conda_lib_path ]

    version = r['version']

    print (i['recursion_spaces'] + '    Detected version: {}'.format(version))

    return {'return':0, 'version':version}
