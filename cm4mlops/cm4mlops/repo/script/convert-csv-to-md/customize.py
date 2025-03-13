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

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    csv_file = env.get('CM_CSV_FILE', '')
    md_file = env.get('CM_MD_FILE', '')
    process_file = os.path.join(i['run_script_input']['path'], "process.py")

    env['CM_RUN_CMD'] = '{} {} {} {} '.format(
        env["CM_PYTHON_BIN_WITH_PATH"], process_file, csv_file, md_file)

    return {'return': 0}


def postprocess(i):

    env = i['env']

    return {'return': 0}
