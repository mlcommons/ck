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

    env['CM_RUN_CMD'] = f"""{env['CM_PYTHON_BIN_WITH_PATH']} {os.path.join(env['CM_TMP_CURRENT_SCRIPT_PATH'],"process-cm-deps.py")}  {env['CM_JSON_INPUT_FILE']}"""

    if env.get('CM_OUTPUT_IMAGE_PATH', '') != '':
        env['CM_RUN_CMD'] += f""" --output_image {env['CM_OUTPUT_IMAGE_PATH']}"""

    if env.get('CM_OUTPUT_MERMAID_PATH', '') != '':
        env['CM_RUN_CMD'] += f""" --output_mermaid {env['CM_OUTPUT_MERMAID_PATH']}"""

    return {'return': 0}


def postprocess(i):

    env = i['env']

    return {'return': 0}
