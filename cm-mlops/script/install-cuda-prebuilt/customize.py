from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']
    nvcc_bin = "nvcc"
    env['CM_CUDA_INSTALLED_PATH'] = os.path.join(os.getcwd(), 'install')
    env['CM_NVCC_BIN_WITH_PATH'] = os.path.join(os.getcwd(), 'install', nvcc_bin)
    env['CM_GET_DEPENDENT_CACHED_PATH'] =  os.getcwd()

    return {'return':0}
