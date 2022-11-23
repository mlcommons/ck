from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    meta = i['meta']
    automation = i['automation']

    package_name = env.get('CM_GENERIC_PYTHON_PACKAGE_NAME', '').strip()
    if package_name == '':
        return automation._available_variations({'meta':meta})
    
    env['CM_TMP_PYTHON_PACKAGE_NAME_ENV'] = env['CM_GENERIC_PYTHON_PACKAGE_NAME'].replace("-", "_")

    recursion_spaces = i['recursion_spaces']

    r = automation.detect_version_using_script({
               'env': env,
               'run_script_input':i['run_script_input'],
               'recursion_spaces':recursion_spaces})
    if r['return'] >0:
        if r['return'] == 16:
            env['CM_REQUIRE_INSTALL'] = "yes"
            return {'return':0}

        return r

    return {'return':0}

def detect_version(i):
    env = i['env']
    r = i['automation'].parse_version({'match_text': r'\s*([\d.a-z\-]+)',
                                       'group_number': 1,
                                       'env_key':'CM_'+env['CM_TMP_PYTHON_PACKAGE_NAME_ENV'].upper()+'_VERSION',
                                       'which_env':i['env']})
    if r['return'] >0: return r

    version = r['version']

    print (i['recursion_spaces'] + '      Detected version: {}'.format(version))
    return {'return':0, 'version':version}


def postprocess(i):

    env = i['env']
    r = detect_version(i)
    if r['return'] >0: return r

    version = r['version']

    env['CM_PYTHONLIB_'+env['CM_TMP_PYTHON_PACKAGE_NAME_ENV'].upper()+'_CACHE_TAGS'] = 'version-'+version

    return {'return':0, 'version': version}
