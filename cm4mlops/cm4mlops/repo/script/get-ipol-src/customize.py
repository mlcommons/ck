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

    script_path = i['artifact'].path

    automation = i['automation']

    cm = automation.cmind

    path = os.getcwd()

    url = env['CM_IPOL_SRC_URL']

    year = env.get('CM_IPOL_YEAR', '')
    number = env.get('CM_IPOL_NUMBER', '')

    url = url.replace(
        '{{CM_IPOL_YEAR}}',
        year).replace(
        '{{CM_IPOL_NUMBER}}',
        number)

    print('Downloading from {}'.format(url))

    r = cm.access({'action': 'download_file',
                   'automation': 'utils,dc2743f8450541e3',
                   'url': url})
    if r['return'] > 0:
        return r

    filename = r['filename']

    print('Unzipping file {}'.format(filename))

    r = cm.access({'action': 'unzip_file',
                   'automation': 'utils,dc2743f8450541e3',
                   'filename': filename})
    if r['return'] > 0:
        return r

    if os.path.isfile(filename):
        print('Removing file {}'.format(filename))
        os.remove(filename)

    # Get sub-directory from filename
    ff = os.path.splitext(filename)

    subdir = ff[0]

    env['CM_IPOL_PATH'] = os.path.join(path, subdir)

    # Applying patch
    cmd = 'patch -p0 < {}'.format(os.path.join(script_path,
                                  'patch', '20240127.patch'))

    print('Patching code: {}'.format(cmd))
    os.system(cmd)

    return {'return': 0}
