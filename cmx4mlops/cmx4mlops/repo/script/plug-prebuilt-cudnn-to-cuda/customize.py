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

    recursion_spaces = i['recursion_spaces']

    cur_dir = os.getcwd()

    os_info = i['os_info']

    env = i['env']

    if str(env.get('CUDA_SKIP_SUDO', '')).lower() == 'true':
        env['CM_SUDO'] = ''

    meta = i['meta']
    automation = i['automation']
    version = env.get('CM_VERSION')

    supported_versions = list(meta['versions'].keys())

    if version not in supported_versions:
        return {'return': 1, 'error': "Only cuDNN versions {} are supported now".format(
            ', '.join(supported_versions))}

    env['CM_CUDNN_VERSION'] = version

    filename = env['CM_CUDNN_TAR_FILE_NAME_TEMPLATE']
    cudnn_md5sum = env.get('CM_CUDNN_TAR_MD5SUM', '')

    cuda_version_split = env['CM_CUDA_VERSION'].split('.')
    cuda_version_major = cuda_version_split[0]

    filename = filename.replace('{{CUDA_MAJOR_VERSION}}', cuda_version_major)

    env['CM_CUDNN_TAR_FILE_NAME'] = filename

    cudnn_dir = filename[:-7]

    cudnn_url = f'https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/linux-x86_64/{filename}'

    print('')
    print(f'URL to download cuDNN: {cudnn_url}')

    env['CM_CUDNN_TAR_DIR'] = cudnn_dir
    env['CM_CUDNN_UNTAR_PATH'] = os.path.join(cur_dir, cudnn_dir)
    env['WGET_URL'] = cudnn_url
    env['CM_DOWNLOAD_CHECKSUM'] = cudnn_md5sum

    return {'return': 0}
