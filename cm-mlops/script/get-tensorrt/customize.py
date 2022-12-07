from cmind import utils
import os
import tarfile

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    if os_info['platform'] == 'windows':
        return {'return': 1, 'error': 'Windows is currently not supported!'}
    file_name = "trtexec"
    if 'CM_TENSORRT_TAR_FILE_WITH_PATH' not in env:
        return {'return': 1, 'error': 'Please use --tar_file option to point to the tensorrt tar file'}
    my_tar = tarfile.open(os.path.expanduser(env['CM_TENSORRT_TAR_FILE_WITH_PATH']))
    folder_name = my_tar.getnames()[0]
    if not os.path.exists(os.path.join(os.getcwd(), folder_name)):
        my_tar.extractall()
    my_tar.close()
    import re
    version_match = re.match(r'TensorRT-(\d.\d.\d.\d)', folder_name)
    if not version_match:
        return {'return': 1, 'error': 'Extracted TensorRT folder does not seem proper - Version infor missing'}
    version = version_match.group(1)
    env['CM_TENSORRT_VERSION'] = version
    env['CM_TMP_PATH'] = os.path.join(os.getcwd(), folder_name, "bin")
    extra_paths = {"include" : "+C_INCLUDE_PATH", "lib" : "+LD_LIBRARY_PATH"}
    r = i['automation'].find_artifact({'file_name': file_name,
                                           'env': env,
                                           'os_info':os_info,
                                           'default_path_env_key': 'PATH',
                                           'detect_version':False,
                                           'env_path_key':'CM_TENSORRT_BIN_WITH_PATH',
                                           'run_script_input':i['run_script_input'],
                                           'extra_paths': extra_paths,
                                           'recursion_spaces':recursion_spaces})
    if r['return'] > 0:
        return r
    return {'return':0}

def postprocess(i):

    os_info = i['os_info']

    env = i['env']
    version = env['CM_TENSORRT_VERSION']

    return {'return':0, 'version': version}
