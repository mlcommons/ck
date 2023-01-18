from cmind import utils
import os
import json
from pathlib import Path

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    if os_info['platform'] == 'windows':
        file_name = 'libcudart.dll'

        if env.get('CM_INPUT','').strip()=='' and env.get('CM_TMP_PATH','').strip()=='':
            # Check in "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA"
            paths = []
            for path in ["C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA", "C:\\Program Files (x86)\\NVIDIA GPU Computing Toolkit\\CUDA"]:
                if os.path.isdir(path):
                    dirs = os.listdir(path)
                    for dr in dirs:
                        path2 = os.path.join(path, dr, 'bin')
                        if os.path.isdir(path2):
                            paths.append(path2)

            if len(paths)>0:
                tmp_paths = ';'.join(paths)
                tmp_paths += ';'+os.environ.get('PATH','')
            
                env['CM_TMP_PATH'] = tmp_paths
                env['CM_TMP_PATH_IGNORE_NON_EXISTANT'] = 'yes'
    
    else:
        file_name = 'libcudart.so'

        # paths to nvcc are not always in PATH - add a few typical locations to search for
        # (unless forced by a user)

        if env.get('CM_INPUT','').strip()=='' and env.get('CM_TMP_PATH','').strip()=='':
            env['CM_TMP_PATH'] = '/usr/local/cuda/lib:/usr/cuda/lib:/usr/local/cuda/lib64:/usr/cuda/lib64:/usr/local/cuda-11/lib64:/usr/cuda-11/lib64:/usr/local/cuda-12/lib64:/usr/cuda-12/lib64:/usr/local/packages/cuda'
            env['CM_TMP_PATH_IGNORE_NON_EXISTANT'] = 'yes'

    if 'CM_CUDA_RT_WITH_PATH' not in env:
        r = i['automation'].find_artifact({'file_name': file_name,
                                           'env': env,
                                           'os_info':os_info,
                                           'default_path_env_key': 'PATH',
                                           'detect_version':True,
                                           'env_path_key':'CM_CUDA_RT_WITH_PATH',
                                           'run_script_input':i['run_script_input'],
                                           'recursion_spaces':recursion_spaces})

        if r['return'] >0 : 
            return {'return':1, 'error': 'CUDA installation not found in default paths. Please set --input to the installed path'}

        found_path = r['found_path']

        env['CM_CUDA_PATH_LIB'] = found_path
        env['CM_CUDA_INSTALLED_PATH'] = os.path.abspath(os.path.join(found_path, os.pardir))

    return {'return':0}

def detect_version(i):

    env = i['env']

    cuda_rt_file_path = env['CM_CUDA_RT_WITH_PATH']
    cuda_lib_path=os.path.dirname(cuda_rt_file_path)
    cuda_path = os.path.abspath(os.path.join(cuda_lib_path, os.pardir))

    cuda_version = "version-missing"

    version_json = os.path.join(cuda_path, "version.json")
    if os.path.exists(version_json):
        with open(version_json) as f:
            version_info = json.load(f)
            cuda_version_info = version_info.get('cuda_cudart')
            if cuda_version_info:
                cuda_version = cuda_version_info.get('version')


    env['CM_CUDA_VERSION'] = cuda_version
    version = cuda_version

    print (i['recursion_spaces'] + '    Detected version: {}'.format(version))

    return {'return':0, 'version':version}


def postprocess(i):

    os_info = i['os_info']

    r = detect_version(i)
    if r['return'] > 0:
        return r
    version = r['version']

    env = i['env']
    
    env['CUDA_HOME']=env['CM_CUDA_INSTALLED_PATH']
    env['CUDA_PATH']=env['CM_CUDA_INSTALLED_PATH']
    cuda_path = env['CM_CUDA_INSTALLED_PATH']

    # Check extra paths
    for key in ['+C_INCLUDE_PATH', '+CPLUS_INCLUDE_PATH', '+LD_LIBRARY_PATH', '+DYLD_FALLBACK_LIBRARY_PATH']:
         env[key] = []

    ## Include
    cuda_path_include = os.path.join(cuda_path, 'include')
    if os.path.isdir(cuda_path_include):
        if os_info['platform'] != 'windows':
            env['+C_INCLUDE_PATH'].append(cuda_path_include)
            env['+CPLUS_INCLUDE_PATH'].append(cuda_path_include)

        env['CM_CUDA_PATH_INCLUDE'] = cuda_path_include

    ## Lib
    if os_info['platform'] == 'windows':
        extra_dir='x64'
        extra_pre=''
        extra_ext='lib'
    else:
        extra_dir=''
        extra_pre='lib'
        extra_ext='so'

    for d in ['lib64', 'lib']:
        cuda_path_lib = os.path.join(cuda_path, d)

        if extra_dir != '':
            cuda_path_lib = os.path.join(cuda_path_lib, extra_dir)

        if os.path.isdir(cuda_path):
            env['+LD_LIBRARY_PATH'].append(cuda_path_lib)
            env['+DYLD_FALLBACK_LIBRARY_PATH'].append(cuda_path_lib)

            env['CM_CUDA_PATH_LIB'] = cuda_path_lib

            ## Check sub libs
            cuda_path_lib_cudnn = os.path.join(cuda_path_lib, extra_pre + 'cudnn.'+extra_ext)
            if os.path.isfile(cuda_path_lib_cudnn):
                env['CM_CUDA_PATH_LIB_CUDNN']=cuda_path_lib_cudnn
                env['CM_CUDA_PATH_LIB_CUDNN_EXISTS']='yes'


            break

    return {'return':0, 'version': version}
