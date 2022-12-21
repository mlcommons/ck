from cmind import utils
import os
import tarfile

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    if os_info['platform'] == 'windows':
        return {'return': 1, 'error': 'Windows is currently not supported!'}

    if 'CM_INPUT' not in env:
        return {'return': 1, 'error': 'Please use --input option to point to the tensorrt tar file downloaded from Nvidia website'}

    file_name = "trtexec"
    my_tar = tarfile.open(os.path.expanduser(env['CM_TENSORRT_TAR_FILE_WITH_PATH']))
    folder_name = my_tar.getnames()[0]
    if not os.path.exists(os.path.join(os.getcwd(), folder_name)):
        my_tar.extractall()
    my_tar.close()

    import re
    version_match = re.match(r'TensorRT-(\d.\d.\d.\d)', folder_name)
    if not version_match:
        return {'return': 1, 'error': 'Extracted TensorRT folder does not seem proper - Version information missing'}
    version = version_match.group(1)

    env['CM_TENSORRT_VERSION'] = version
    env['CM_TENSORRT_INSTALL_PATH'] = os.path.join(os.getcwd(), folder_name)
    env['CM_TMP_PATH'] = os.path.join(os.getcwd(), folder_name, "bin")
    env['+CPLUS_INCLUDE_PATH'] = os.path.join(os.getcwd(), folder_name, "include")
    env['+C_INCLUDE_PATH'] = os.path.join(os.getcwd(), folder_name, "include")
    env['+LD_LIBRARY_PATH'] = os.path.join(os.getcwd(), folder_name, "lib")

    return {'return':0}

def postprocess(i):

    os_info = i['os_info']

    env = i['env']
    version = env['CM_TENSORRT_VERSION']

    return {'return':0, 'version': version}
