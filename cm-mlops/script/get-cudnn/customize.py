from cmind import utils
import os
import tarfile
import shutil

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    env['CM_TMP_RUN_COPY_SCRIPT'] = "no"

    cuda_path_lib = env.get('CM_CUDA_PATH_LIB')
    if os.path.exists(os.path.join(cuda_path_lib, "libcudnn.so")):
        env['CM_CUDNN_VERSION'] = 'vdetected'
        return {'return': 0}

    recursion_spaces = i['recursion_spaces']

    if os_info['platform'] == 'windows':
        return {'return': 1, 'error': 'Windows is currently not supported!'}

    if not env.get('CM_INPUT',''):
        if env.get('CM_CUDNN_TAR_FILE_PATH'):
            env['CM_INPUT'] = env.get('CM_CUDNN_TAR_FILE_PATH')
        else:
            return {'return': 1, 'error': 'Please use --input option to point to the cudnn tar file'}

    my_tar = tarfile.open(os.path.expanduser(env['CM_INPUT']))
    folder_name = my_tar.getnames()[0]
    if not os.path.exists(os.path.join(os.getcwd(), folder_name)):
        my_tar.extractall()
    my_tar.close()

    import re
    version_match = re.match(r'cudnn-.*?-(\d.\d.\d.\d)', folder_name)
    if not version_match:
        return {'return': 1, 'error': 'Extracted CUDNN folder does not seem proper - Version information missing'}
    version = version_match.group(1)
    env['CM_CUDNN_VERSION'] = version

    inc_path = os.path.join(os.getcwd(), folder_name, "include")
    lib_path = os.path.join(os.getcwd(), folder_name, "lib")
    cuda_inc_path = env['CM_CUDA_PATH_INCLUDE']
    cuda_lib_path = env['CM_CUDA_PATH_LIB']

    try:
        print("Copying cudnn include files to {}(CUDA_INCLUDE_PATH)".format(cuda_inc_path))
        shutil.copytree(inc_path, cuda_inc_path, dirs_exist_ok = True)
        print("Copying cudnn lib files to {}CUDA_LIB_PATH".format(cuda_lib_path))
        shutil.copytree(lib_path, cuda_lib_path, dirs_exist_ok = True)
    except:
        #Need to copy to system path via run.sh
        env['CM_TMP_RUN_COPY_SCRIPT'] = "yes"
        env['CM_TMP_INC_PATH'] = inc_path
        env['CM_TMP_LIB_PATH'] = lib_path

    return {'return':0}

def postprocess(i):

    os_info = i['os_info']

    env = i['env']
    version = env['CM_CUDNN_VERSION']

    return {'return':0, 'version': version}
