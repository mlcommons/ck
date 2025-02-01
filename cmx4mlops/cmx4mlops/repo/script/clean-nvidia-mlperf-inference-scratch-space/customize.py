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

    quiet = (env.get('CM_QUIET', False) == 'yes')

    clean_cmd = ''
    cache_rm_tags = ''
    extra_cache_rm_tags = env.get('CM_CLEAN_EXTRA_CACHE_RM_TAGS', '')

    if env.get('CM_MODEL', '') == 'sdxl':
        if env.get('CM_CLEAN_ARTIFACT_NAME', '') == 'downloaded_data':
            clean_cmd = f"""rm -rf {os.path.join(env['CM_NVIDIA_MLPERF_SCRATCH_PATH'], "data", "coco", "SDXL")} """
            cache_rm_tags = "nvidia-harness,_preprocess_data,_sdxl"
        if env.get('CM_CLEAN_ARTIFACT_NAME', '') == 'preprocessed_data':
            clean_cmd = f"""rm -rf {os.path.join(env['CM_NVIDIA_MLPERF_SCRATCH_PATH'], "preprocessed_data", "coco2014-tokenized-sdxl")} """
            cache_rm_tags = "nvidia-harness,_preprocess_data,_sdxl"
        if env.get('CM_CLEAN_ARTIFACT_NAME', '') == 'downloaded_model':
            clean_cmd = f"""rm -rf {os.path.join(env['CM_NVIDIA_MLPERF_SCRATCH_PATH'], "models", "SDXL")} """
            cache_rm_tags = "nvidia-harness,_download_model,_sdxl"

    cache_rm_tags = cache_rm_tags + extra_cache_rm_tags

    if cache_rm_tags:
        r = cm.access({'action': 'rm', 'automation': 'cache',
                      'tags': cache_rm_tags, 'f': True})
        print(r)
        if r['return'] != 0 and r['return'] != 16:  # ignore missing ones
            return r
        if r['return'] == 0:  # cache entry found
            if clean_cmd != '':
                env['CM_RUN_CMD'] = clean_cmd
    else:
        if clean_cmd != '':
            env['CM_RUN_CMD'] = clean_cmd

    return {'return': 0}


def postprocess(i):

    env = i['env']

    return {'return': 0}
