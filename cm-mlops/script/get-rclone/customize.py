from cmind import utils
import os
import configparser

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    file_name = 'rclone.exe' if os_info['platform'] == 'windows' else 'rclone'
    env['FILE_NAME'] = file_name

    run_script_input = i['run_script_input']
    automation = i['automation']

    r = automation.detect_version_using_script({
               'env': env,
               'run_script_input': run_script_input,
               'recursion_spaces':recursion_spaces})

    if r['return'] >0:
        if r['return'] == 16:
            r = automation.run_native_script({'run_script_input':run_script_input, 'env':env, 'script_name':'install'})
            if r['return']>0: return r
        else:
            return r

    return {'return':0}

def detect_version(i):
    r = i['automation'].parse_version({'match_text': r'rclone v([\d.]+)',
                                       'group_number': 1,
                                       'env_key':'CM_RCLONE_VERSION',
                                       'which_env':i['env']})
    if r['return'] >0: return r

    version = r['version']

    print (i['recursion_spaces'] + '    Detected version: {}'.format(version))

    return {'return':0, 'version':version}

def postprocess(i):

    env = i['env']

    gdrive = env.get('CM_RCLONE_GDRIVE', '')
    if gdrive == "yes":
        config = configparser.ConfigParser()
        config_file_path = os.path.join(env['CM_TMP_CURRENT_SCRIPT_PATH'], "configs", "rclone.conf")

        config.read(config_file_path)
        config['cm-team']['service_account_file'] = os.path.join(env['CM_TMP_CURRENT_SCRIPT_PATH'], "accessfiles", "rclone-gdrive.json")

        default_config_path = os.path.join(os.path.expanduser( '~' ), ".config", "rclone", "rclone.conf")

        default_config = configparser.ConfigParser()
        default_config.read(default_config_path)

        for section in config.sections():
            if section not in default_config.sections():
                default_config[section] = config[section]
    
        with open(default_config_path, 'w') as configfile:
            default_config.write(configfile)
        print({section: dict(default_config[section]) for section in default_config.sections()})

    r = detect_version(i)

    if r['return'] >0: return r

    version = r['version']

    env['CM_RCLONE_CACHE_TAGS'] = 'version-'+version

    return {'return':0, 'version': version}
