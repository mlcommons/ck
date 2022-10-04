from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    r = i['automation'].detect_version_using_script({
               'env': env,
               'run_script_input':i['run_script_input'],
               'recursion_spaces':recursion_spaces})

    if r['return'] >0:
        if r['return'] == 16:
            env['CM_TMP_REQUIRE_INSTALL'] = "yes"
            return {'return': 0}
        else:
            return r

#    add_extra_cache_tags = []
#    if 'CM_PYTHON_VERSION' in env:
#        add_extra_cache_tags = ["deps-python-" + env['CM_PYTHON_VERSION']]


    return {'return':0} #, 'add_extra_cache_tags': add_extra_cache_tags}

def detect_version(i):
    r = i['automation'].parse_version({'match_text': r'\s*([\d.a-z\-]+)',
                                       'group_number': 1,
                                       'env_key':'CM_ONNXRUNTIME_VERSION',
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

    env['CM_ONNXRUNTIME_CACHE_TAGS'] = 'version-'+version
    env['CM_ONNXRUNTIME_VERSION'] = version

    return {'return':0}
