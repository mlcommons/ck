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
import stat


def preprocess(i):

    os_info = i['os_info']

    return {'return': 0}


def postprocess(i):

    env = i['env']
    state = i['state']

    if env['CM_HOST_OS_TYPE'].lower() == "windows":
        binary_name = "ptd-windows-x86.exe"
    else:
        binary_name = "ptd-linux-x86"
    if env.get('CM_MLPERF_PTD_PATH', '') == '':
        env['CM_MLPERF_PTD_PATH'] = os.path.join(
            env['CM_MLPERF_POWER_SOURCE'], 'PTD', 'binaries', binary_name)

    file_path = env['CM_MLPERF_PTD_PATH']
    current_permissions = os.stat(file_path).st_mode

    # Check if the file already has execute permissions
    if not (current_permissions & stat.S_IXUSR):  # Check user execute permission
        # Add execute permissions for the user
        os.chmod(file_path, current_permissions | stat.S_IXUSR)

    env['CM_SPEC_PTD_PATH'] = env['CM_MLPERF_PTD_PATH']

    return {'return': 0}
