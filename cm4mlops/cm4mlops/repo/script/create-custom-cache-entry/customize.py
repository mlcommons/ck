#
# Copyright: https://github.com/mlcommons/ck/blob/master/cm-mlops/COPYRIGHT.md
# License: https://github.com/mlcommons/ck/blob/master/cm-mlops/LICENSE.md
#
# White paper: https://arxiv.org/abs/2406.16791
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# Original repository: https://github.com/mlcommons/ck/tree/master/cm-mlops
#
# CK and CM project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md
#

from cmind import utils
import os
import shutil


def preprocess(i):

    # CM script internal variables
    env = i['env']

    extra_cache_tags = []
    if env.get('CM_EXTRA_CACHE_TAGS', '').strip() == '':
        print('')
        extra_cache_tags_str = input(
            'Enter extra tags for the custom CACHE entry separated by comma: ')

        extra_cache_tags = extra_cache_tags_str.strip().split(',')

    return {'return': 0, 'add_extra_cache_tags': extra_cache_tags}


def postprocess(i):

    env = i['env']

    path = env.get('CM_CUSTOM_CACHE_ENTRY_PATH', '').strip()

    if path != '':
        if not os.path.isdir(path):
            os.makedirs(path)
    else:
        path = os.getcwd()

    x = ''
    env_key = env.get('CM_CUSTOM_CACHE_ENTRY_ENV_KEY', '')
    if env_key != '':
        x = env_key + '_'

    env['CM_CUSTOM_CACHE_ENTRY_{}PATH'.format(x)] = path
    env['CM_CUSTOM_CACHE_ENTRY_PATH'] = path

    env_key2 = env.get('CM_CUSTOM_CACHE_ENTRY_ENV_KEY2', '')
    v = env.get(env_key2, '')
    real_path = v if v != '' else path

    env['CM_CUSTOM_CACHE_ENTRY_{}REAL_PATH'.format(x)] = real_path

    return {'return': 0}
