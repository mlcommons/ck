from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    if os_info['platform'] == 'windows':
        file_name = 'nvcc.exe'

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
        file_name = 'nvcc'

        # paths to nvcc are not always in PATH - add a few typical locations to search for
        # (unless forced by a user)

        if env.get('CM_INPUT','').strip()=='' and env.get('CM_TMP_PATH','').strip()=='':
            env['CM_TMP_PATH'] = '/usr/local/cuda/bin:/usr/cuda/bin'
            env['CM_TMP_PATH_IGNORE_NON_EXISTANT'] = 'yes'

    if 'CM_NVCC_BIN_WITH_PATH' not in env:
        r = i['automation'].find_artifact({'file_name': file_name,
                                           'env': env,
                                           'os_info':os_info,
                                           'default_path_env_key': 'PATH',
                                           'detect_version':True,
                                           'env_path_key':'CM_NVCC_BIN_WITH_PATH',
                                           'run_script_input':i['run_script_input'],
                                           'recursion_spaces':recursion_spaces})
        if r['return'] >0 : 
            if os_info['platform'] == 'windows':
                return r

            if r['return'] == 16:
                env['CM_REQUIRE_INSTALL'] = "yes"
                return {'return': 0}
            else:
                return r

    return {'return':0}



def detect_version(i):
    r = i['automation'].parse_version({'match_text': r'release\s*([\d.]+)',
                                       'group_number': 1,
                                       'env_key':'CM_CUDA_VERSION',
                                       'which_env':i['env']})
    if r['return'] >0: return r

    version = r['version']

    print (i['recursion_spaces'] + '    Detected version: {}'.format(version))

    return {'return':0, 'version':version}



def postprocess(i):

    os_info = i['os_info']

    env = i['env']
    r = detect_version(i)
    if r['return'] >0: return r
    found_file_path = env['CM_NVCC_BIN_WITH_PATH']

    cuda_path_bin = os.path.dirname(found_file_path)
    env['CM_CUDA_PATH_BIN'] = cuda_path_bin

    cuda_path = os.path.dirname(cuda_path_bin)
    env['CM_CUDA_INSTALLED_PATH'] = cuda_path

    env['CUDA_HOME']=cuda_path
    env['CUDA_PATH']=cuda_path

    env['CM_NVCC_BIN'] = os.path.basename(found_file_path)

    version = r['version']

    env['CM_CUDA_CACHE_TAGS'] = 'version-'+version

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
            if os_info['platform'] == 'windows':
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
