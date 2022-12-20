from cmind import utils
import os
import tarfile
import shutil

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    if os_info['platform'] == 'windows':
        return {'return': 1, 'error': 'Windows is currently not supported!'}
    file_name = "trtexec"
    if 'CM_CUDNN_TAR_FILE_WITH_PATH' not in env:
        return {'return': 1, 'error': 'Please use --tar_file option to point to the cudnn tar file'}
    my_tar = tarfile.open(os.path.expanduser(env['CM_CUDNN_TAR_FILE_WITH_PATH']))
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
        #Need to copy to system path
        os.system("sudo cp " + inc_path+ "/*.h " + cuda_inc_path)
        os.system("sudo cp -P " + lib_path+ "/libcudnn* " + cuda_lib_path)

    return {'return':0}

def postprocess(i):

    os_info = i['os_info']

    env = i['env']
    version = env['CM_CUDNN_VERSION']

    return {'return':0, 'version': version}
