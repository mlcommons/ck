from cmind import utils
import os

def preprocess(i):

    # Pre-set by CM
    os_info = i['os_info']
    env = i['env']
    recursion_spaces = i['recursion_spaces']
    automation = i['automation']
    run_script_input = i['run_script_input']

    # Check if a given tool is already installed
    file_name_core = 'aria2c'
    file_name = file_name_core+'.exe' if os_info['platform'] == 'windows' else file_name_core

    force_install = env.get('CM_FORCE_INSTALL', False) == True

    if not force_install:
        r = i['automation'].find_artifact({'file_name': file_name,
                                           'env':env,
                                           'os_info':os_info,
                                           'default_path_env_key': 'PATH',
                                           'detect_version':True,
                                           'env_path_key':'CM_ARIA2_BIN_WITH_PATH',
                                           'run_script_input':i['run_script_input'],
                                           'recursion_spaces':recursion_spaces})
        if r['return'] >0 : 
            if r['return'] == 16:
                # Not found, try install
                force_install = True
            else:
                return r

    # Force install
    if force_install:
        # Attempt to run installer
        version = env.get('CM_VERSION','')
        if version == '': version = env['CM_ARIA2_DEFAULT_INSTALL_VERSION']

        if os_info['platform'] == 'windows':
            archive = 'aria2-{}-win-64bit-build1'
            ext = '.zip'
            ext2 = ''
        else:
            archive = 'aria2-{}' 
            ext = '.tar.bz2'
            ext2 = '.tar'

        archive = archive.format(version)
        archive_with_ext = archive+ext

        env['CM_ARIA2_DOWNLOAD_DIR'] = archive

        env['CM_ARIA2_DOWNLOAD_FILE'] = archive_with_ext
        if ext2!='':
            env['CM_ARIA2_DOWNLOAD_FILE2'] = archive+ext2

        url = 'https://github.com/aria2/aria2/releases/download/release-{}/{}'.format(version, archive_with_ext)
        env['CM_ARIA2_DOWNLOAD_URL'] = url

        print ('URL to download ARIA2: {}'.format(url))

        r = automation.run_native_script({'run_script_input':run_script_input, 'env':env, 'script_name':'install'})
        if r['return']>0: return r

        if os_info['platform'] == 'windows' or env.get('CM_ARIA2_BUILD_FROM_SRC', '').lower() == 'true':
            install_path = os.path.join(os.getcwd(), archive)

            path_to_file = os.path.join(install_path, file_name)
            if not os.path.isfile(path_to_file):
                return {'return':1, 'error':'file not found: {}'.format(path_to_file)}

            env['CM_ARIA2_BIN_WITH_PATH'] = path_to_file
            env['CM_ARIA2_INSTALLED_TO_CACHE'] = 'yes'
        else:
            path_to_bin = r['env_tmp'].get('CM_ARIA2_BIN_WITH_PATH','')
            env['CM_ARIA2_BIN_WITH_PATH'] = path_to_bin

            r = i['automation'].find_artifact({'file_name': file_name,
                                               'env':env,
                                               'os_info':os_info,
                                               'default_path_env_key': 'PATH',
                                               'detect_version':True,
                                               'env_path_key':'CM_ARIA2_BIN_WITH_PATH',
                                               'run_script_input':i['run_script_input'],
                                               'recursion_spaces':recursion_spaces})
            if r['return']>0: return r

    return {'return':0}

def detect_version(i):
    env = i['env']

    r = i['automation'].parse_version({'match_text': r'aria2 version\s*([\d.]+)',
                                       'group_number': 1,
                                       'env_key':'CM_ARIA2_VERSION',
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
    found_file_path = env['CM_ARIA2_BIN_WITH_PATH']

    found_path = os.path.dirname(found_file_path)

    env['CM_ARIA2_INSTALLED_PATH'] = found_path

    if env.get('CM_ARIA2_INSTALLED_TO_CACHE','')=='yes':
        env['+PATH'] = [env['CM_ARIA2_INSTALLED_PATH']]

    return {'return':0, 'version': version}
