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

    env = i['env']

    script_path = i['run_script_input']['path']

    if env.get('CM_GIT_PATCH_FILENAMES', '') != '':
        patch_files = env['CM_GIT_PATCH_FILENAMES'].split(",")
        patch_files_full_paths = []
        for patch_file in patch_files:
            patch_file_full_path = os.path.join(
                script_path, "patch", patch_file)
            patch_files_full_paths.append(patch_file_full_path)
        env['CM_GIT_PATCH_FILEPATHS'] = ",".join(patch_files_full_paths)

    return {'return': 0}


def postprocess(i):

    env = i['env']
    state = i['state']

    return {'return': 0}
