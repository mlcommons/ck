from cmind import utils
import os


def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if env.get('CM_ABTF_SCRATCH_PATH', '') == '':
        env['CM_ABTF_SCRATCH_PATH'] = os.getcwd()

    return {'return': 0}


def postprocess(i):

    env = i['env']

    env['CM_ABTF_SCRATCH_PATH_MODELS'] = os.path.join(
        env['CM_ABTF_SCRATCH_PATH'], "models")
    env['CM_ABTF_SCRATCH_PATH_DATASETS'] = os.path.join(
        env['CM_ABTF_SCRATCH_PATH'], "datasets")

    if not os.path.exists(env['CM_ABTF_SCRATCH_PATH_MODELS']):
        os.makedirs(env['CM_ABTF_SCRATCH_PATH_MODELS'])

    if not os.path.exists(env['CM_ABTF_SCRATCH_PATH_DATASETS']):
        os.makedirs(env['CM_ABTF_SCRATCH_PATH_DATASETS'])

    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_ABTF_SCRATCH_PATH']

    return {'return': 0}
