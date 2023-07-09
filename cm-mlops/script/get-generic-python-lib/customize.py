from cmind import utils
import os
import cmind as cm

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    meta = i['meta']
    automation = i['automation']
    run_script_input = i['run_script_input']
    pip_version = env.get('CM_PIP_VERSION')
    print("PIP Version:"+str(pip_version))
    package_name = env.get('CM_GENERIC_PYTHON_PACKAGE_NAME', '').strip()
    if package_name == '':
        return automation._available_variations({'meta':meta})

    if env.get('CM_GENERIC_PYTHON_PIP_UNINSTALL_DEPS'):
        r = automation.run_native_script({'run_script_input':run_script_input, 'env':env, 'script_name':'uninstall_deps'})
        if r['return']>0: return r

    prepare_env_key = env['CM_GENERIC_PYTHON_PACKAGE_NAME']
    for x in ["-", "[", "]"]:
        prepare_env_key = prepare_env_key.replace(x,"_")

    env['CM_TMP_PYTHON_PACKAGE_NAME_ENV'] = prepare_env_key.upper()

    recursion_spaces = i['recursion_spaces']
    
    r = automation.detect_version_using_script({
               'env': env,
               'run_script_input':i['run_script_input'],
               'recursion_spaces':recursion_spaces})

    if r['return'] >0:
        if r['return'] == 16:
            extra = env.get('CM_GENERIC_PYTHON_PIP_EXTRA','')
            if env.get('CM_HOST_OS_FLAVOR', '') == 'ubuntu':
                version = env.get('CM_HOST_OS_VERSION', '')
                if version:
                    version_split = version.split(".")
                    if (pip_version >= "23.0.0") and ('--break-system-packages' not in extra):
                       extra += '  --break-system-packages '

            # Check index URL
            index_url = env.get('CM_GENERIC_PYTHON_PIP_INDEX_URL','').strip()
            if index_url != '':
                # Check special cases
                if '${CM_TORCH_CUDA}' in index_url:
                    index_url=index_url.replace('${CM_TORCH_CUDA}', env.get('CM_TORCH_CUDA'))

                extra += ' --index-url '+index_url

            # Check extra index URL
            extra_index_url = env.get('CM_GENERIC_PYTHON_PIP_EXTRA_INDEX_URL','').strip()
            if extra_index_url != '':
                # Check special cases
                if '${CM_TORCH_CUDA}' in extra_index_url:
                    extra_index_url=extra_index_url.replace('${CM_TORCH_CUDA}', env.get('CM_TORCH_CUDA'))

                extra += ' --extra-index-url '+extra_index_url

            # Check update
            if env.get('CM_GENERIC_PYTHON_PIP_UPDATE','') in [True,'true','yes','on']:
                extra +=' -U'

            env['CM_GENERIC_PYTHON_PIP_EXTRA'] = extra

            package_name = env.get('CM_GENERIC_PYTHON_PACKAGE_NAME', '').strip()
            if package_name == '':
                return automation._available_variations({'meta':meta})

            r = automation.run_native_script({'run_script_input':run_script_input, 'env':env, 'script_name':'install'})

            if r['return']>0: return r

    return {'return':0}

def detect_version(i):

    env = i['env']

    env_version_key = 'CM_'+env['CM_TMP_PYTHON_PACKAGE_NAME_ENV'].upper()+'_VERSION'

    r = i['automation'].parse_version({'match_text': r'\s*([\d.a-z\-]+)',
                                       'group_number': 1,
                                       'env_key':env_version_key,
                                       'which_env':i['env']})
    if r['return'] >0: return r

    version = r['version']
    current_detected_version = version

    print (i['recursion_spaces'] + '      Detected version: {}'.format(version))

    return {'return':0, 'version':version}


def postprocess(i):

    env = i['env']

    env_version_key = 'CM_'+env['CM_TMP_PYTHON_PACKAGE_NAME_ENV'].upper()+'_VERSION'

    if env.get(env_version_key,'')!='':
        version = env[env_version_key]
    else:
        r = detect_version(i)
        if r['return'] >0: return r

        version = r['version']

    env['CM_PYTHONLIB_'+env['CM_TMP_PYTHON_PACKAGE_NAME_ENV']+'_CACHE_TAGS'] = 'version-'+version

    import pkgutil
    package_name = env.get('CM_GENERIC_PYTHON_PACKAGE_NAME', '').strip()
    package=pkgutil.get_loader(package_name)
    if package:
        installed_file_path = package.get_filename()
        env['CM_GET_DEPENDENT_CACHED_PATH'] = installed_file_path

    return {'return':0, 'version': version}
