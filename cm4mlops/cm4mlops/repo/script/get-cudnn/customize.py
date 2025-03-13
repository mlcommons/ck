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
import tarfile
import shutil


def preprocess(i):

    recursion_spaces = i['recursion_spaces']

    os_info = i['os_info']

    env = i['env']

    env['CM_TMP_RUN_COPY_SCRIPT'] = "no"

    # If TAR file is not explicitly specified, search
    if env.get('CM_CUDNN_TAR_FILE_PATH', '') == '':

        cuda_path_lib = env.get('CM_CUDA_PATH_LIB')

        if os_info['platform'] == 'windows':
            extra_pre = ''
            extra_ext = 'lib'
        else:
            extra_pre = 'lib'
            extra_ext = 'so'

        libfilename = extra_pre + 'cudnn.' + extra_ext
        env['CM_CUDNN_VERSION'] = 'vdetected'

        if os.path.exists(os.path.join(cuda_path_lib, libfilename)):
            env['CM_CUDA_PATH_LIB_CUDNN'] = env['CM_CUDA_PATH_LIB']
            return {'return': 0}

        if env.get('CM_TMP_PATH', '').strip() != '':
            path = env.get('CM_TMP_PATH')
            if os.path.exists(os.path.join(path, libfilename)):
                env['CM_CUDA_PATH_LIB_CUDNN'] = path
                return {'return': 0}

        if env.get('CM_INPUT', '').strip() == '':
            if os_info['platform'] == 'windows':
                if env.get('CM_TMP_PATH', '').strip() == '':
                    # Check in "C:\Program Files\NVIDIA GPU Computing
                    # Toolkit\CUDA"
                    paths = []
                    for path in ["C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA",
                                 "C:\\Program Files (x86)\\NVIDIA GPU Computing Toolkit\\CUDA"]:
                        if os.path.isdir(path):
                            dirs = os.listdir(path)
                            for dr in dirs:
                                path2 = os.path.join(path, dr, 'lib')
                                if os.path.isdir(path2):
                                    paths.append(path2)

                    if len(paths) > 0:
                        tmp_paths = ';'.join(paths)
                        tmp_paths += ';' + os.environ.get('PATH', '')

                        env['CM_TMP_PATH'] = tmp_paths
                        env['CM_TMP_PATH_IGNORE_NON_EXISTANT'] = 'yes'

            else:
                # paths to cuda are not always in PATH - add a few typical locations to search for
                # (unless forced by a user)

                cm_tmp_path = env.get('CM_TMP_PATH', '').strip()
                if cm_tmp_path != '':
                    cm_tmp_path += ':'
                cm_tmp_path += '/usr/local/cuda/lib64:/usr/cuda/lib64:/usr/local/cuda/lib:/usr/cuda/lib:/usr/local/cuda-11/lib64:/usr/cuda-11/lib:/usr/local/cuda-12/lib:/usr/cuda-12/lib:/usr/local/packages/cuda/lib'
                cm_tmp_path += os.path.expandvars(':$CUDNN_ROOT/lib')
                env['CM_TMP_PATH'] = cm_tmp_path
                env['CM_TMP_PATH_IGNORE_NON_EXISTANT'] = 'yes'

                for lib_path in env.get(
                        '+CM_HOST_OS_DEFAULT_LIBRARY_PATH', []):
                    if (os.path.exists(lib_path)):
                        env['CM_TMP_PATH'] += ':' + lib_path

        r = i['automation'].find_artifact({'file_name': libfilename,
                                           'env': env,
                                           'os_info': os_info,
                                           'default_path_env_key': 'LD_LIBRARY_PATH',
                                           'detect_version': False,
                                           'env_path_key': 'CM_CUDA_PATH_LIB_CUDNN',
                                           'run_script_input': i['run_script_input'],
                                           'recursion_spaces': recursion_spaces})
        if r['return'] > 0:
            if os_info['platform'] == 'windows':
                return r

            if r['return'] == 16:
                env['CM_TMP_REQUIRE_INSTALL'] = "yes"
            else:
                return r
        else:
            # On Linux we may detected file instead of path to cudnn
            if os.path.isfile(env['CM_CUDA_PATH_LIB_CUDNN']):
                env['CM_CUDA_PATH_LIB_CUDNN'] = os.path.dirname(
                    env['CM_CUDA_PATH_LIB_CUDNN'])

            return {'return': 0}

    if env.get('CM_CUDNN_TAR_FILE_PATH', '') == '':
        return {'return': 1, 'error': 'Please envoke cm run script "get cudnn" --tar_file={full path to the cuDNN tar file}'}

    print('Untaring file - can take some time ...')

    my_tar = tarfile.open(os.path.expanduser(env['CM_CUDNN_TAR_FILE_PATH']))
    folder_name = my_tar.getnames()[0]
    if not os.path.exists(os.path.join(os.getcwd(), folder_name)):
        my_tar.extractall()
    my_tar.close()

    import re
    version_match = re.match(r'cudnn-.*?-(\d+.\d+.\d+.\d+)', folder_name)
    if not version_match:
        return {
            'return': 1, 'error': 'Extracted CUDNN folder does not seem proper - Version information missing'}
    version = version_match.group(1)
    env['CM_CUDNN_VERSION'] = version

    inc_path = os.path.join(os.getcwd(), folder_name, "include")
    lib_path = os.path.join(os.getcwd(), folder_name, "lib")
    cuda_inc_path = env['CM_CUDA_PATH_INCLUDE']
    cuda_lib_path = env['CM_CUDA_PATH_LIB']
    env['CM_CUDA_PATH_LIB_CUDNN'] = env['CM_CUDA_PATH_LIB']
    env['CM_CUDA_PATH_INCLUDE_CUDNN'] = env['CM_CUDA_PATH_INCLUDE']

    try:
        print(
            "Copying cudnn include files to {}(CUDA_INCLUDE_PATH)".format(cuda_inc_path))
        shutil.copytree(inc_path, cuda_inc_path, dirs_exist_ok=True)
        print("Copying cudnn lib files to {}CUDA_LIB_PATH".format(cuda_lib_path))
        shutil.copytree(lib_path, cuda_lib_path, dirs_exist_ok=True)
    except BaseException:
        # Need to copy to system path via run.sh
        env['CM_TMP_RUN_COPY_SCRIPT'] = "yes"
        env['CM_TMP_INC_PATH'] = inc_path
        env['CM_TMP_LIB_PATH'] = lib_path

    return {'return': 0}


def postprocess(i):

    os_info = i['os_info']

    env = i['env']

    version = env['CM_CUDNN_VERSION']

    if version == 'vdetected':
        path_to_cudnn = env.get('CM_CUDA_PATH_LIB_CUDNN', '')
        if os.path.isdir(path_to_cudnn):
            path_to_include = path_to_cudnn
            path_to_include_file = ''
            for j in range(0, 2):
                path_to_include = os.path.dirname(path_to_include)
                x = os.path.join(path_to_include, 'include', 'cudnn_version.h')
                if os.path.isfile(x):
                    path_to_include_file = x
                    break

            if path_to_include_file == '' and path_to_cudnn.startswith('/lib'):
                x = os.path.join('/usr', 'include', 'cudnn_version.h')
                if os.path.isfile(x):
                    path_to_include_file = x

            if path_to_include_file != '':
                env['CM_CUDA_PATH_INCLUDE_CUDNN'] = os.path.dirname(
                    path_to_include_file)

                r = utils.load_txt(path_to_include_file, split=True)
                if r['return'] == 0:
                    lst = r['list']

                    xversion = ''

                    for l in lst:
                        l = l.strip()

                        x = '#define CUDNN_MAJOR '
                        if l.startswith(x):
                            xversion = l[len(x):]

                        x = '#define CUDNN_MINOR '
                        if l.startswith(x):
                            xversion += '.' + l[len(x):]

                        x = '#define CUDNN_PATCHLEVEL '
                        if l.startswith(x):
                            xversion += '.' + l[len(x):]

                    if xversion != '':
                        version = xversion
                        env['CM_CUDNN_VERSION'] = xversion

    env['CM_CUDA_PATH_LIB_CUDNN_EXISTS'] = 'yes'

    return {'return': 0, 'version': version}
