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


def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']

    cm = automation.cmind

    path = os.getcwd()

    url = env['CM_PACKAGE_URL']

    print('Downloading from {}'.format(url))

    r = cm.access({'action': 'download_file',
                   'automation': 'utils,dc2743f8450541e3',
                   'url': url})
    if r['return'] > 0:
        return r

    filename = r['filename']

    if env.get('CM_UNZIP') == "yes":
        os.system("unzip " + filename)
        filename = env['CM_ML_MODEL_FILE']
        env['CM_ML_MODEL_FILE_WITH_PATH'] = os.path.join(path, filename)
    else:
        # Add to path
        env['CM_ML_MODEL_FILE'] = filename
        env['CM_ML_MODEL_FILE_WITH_PATH'] = r['path']

    env['CM_ML_MODEL_PATH'] = path

    return {'return': 0}
