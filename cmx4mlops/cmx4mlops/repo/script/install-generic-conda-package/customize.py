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
import cmind as cm


def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    meta = i['meta']
    automation = i['automation']
    run_script_input = i['run_script_input']

    version_string = env.get('CM_TMP_PIP_VERSION_STRING', '').strip()
    package_name = env['CM_CONDA_PKG_NAME'].strip()

    install_cmd = env['CM_CONDA_BIN_WITH_PATH'] + " install -y "
    if env.get('CM_CONDA_PKG_SRC', '') != '':
        install_cmd += " -c " + env['CM_CONDA_PKG_SRC'] + " "

    install_cmd += package_name
    install_cmd += version_string

    env['CM_CONDA_PKG_INSTALL_CMD'] = install_cmd

    return {'return': 0}


def detect_version(i):

    # TBD
    print(i['recursion_spaces'] + '      Detected version: {}'.format(version))

    return {'return': 0, 'version': version}


def postprocess(i):

    env = i['env']
    version = env.get('CM_VERSION', '')

    if env['CM_CONDA_PKG_NAME'] == "python":
        env['CM_PYTHON_BIN_WITH_PATH'] = os.path.join(
            os.path.dirname(env['CM_CONDA_BIN_WITH_PATH']), "python")

    return {'return': 0, 'version': version}
