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

    if env.get('CM_DATASET_MIXTRAL_GENERATE_TEST_DATA', '') == "yes":
        env['CM_DATASET_MIXTRAL_TEST_DATA_GENERATED_PATH'] = os.path.join(
            os.getcwd(), "mixtral-test-dataset.pkl")

    return {'return': 0}


def postprocess(i):
    env = i['env']

    env['CM_DATASET_MIXTRAL_PREPROCESSED_PATH'] = env['CM_DATASET_PREPROCESSED_PATH']

    if env.get('CM_DATASET_MIXTRAL_GENERATE_TEST_DATA', '') == "yes":
        env['CM_DATASET_MIXTRAL_PREPROCESSED_PATH'] = env['CM_DATASET_MIXTRAL_TEST_DATA_GENERATED_PATH']

    return {'return': 0}
