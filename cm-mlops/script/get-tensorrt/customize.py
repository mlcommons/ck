from cmind import utils
import os
import tarfile

def preprocess(i):

    recursion_spaces = i['recursion_spaces']

    os_info = i['os_info']

    env = i['env']


    #Not enforcing dev requirement for now
    if env.get('CM_TENSORRT_TAR_FILE_PATH','')=='' and env.get('CM_TENSORRT_REQUIRE_DEV1', '') != 'yes' and env.get('CM_HOST_PLATFORM_FLAVOR', '') != 'aarch64':

       if os_info['platform'] == 'windows':
           extra_pre=''
           extra_ext='lib'
       else:
           extra_pre='lib'
           extra_ext='so'

       libfilename = extra_pre + 'nvinfer.' +extra_ext
       env['CM_TENSORRT_VERSION'] = 'vdetected'

       if env.get('CM_TMP_PATH', '').strip() != '':
           path = env.get('CM_TMP_PATH')
           if os.path.exists(os.path.join(path, libfilename)):
               env['CM_TENSORRT_LIB_PATH'] = path
               return {'return': 0}

       if not env.get('CM_TMP_PATH'):
           env['CM_TMP_PATH'] = ''

       if os_info['platform'] == 'windows':
           if env.get('CM_INPUT','').strip()=='' and env.get('CM_TMP_PATH','').strip()=='':
               # Check in "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA"
               paths = []
               for path in ["C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA", "C:\\Program Files (x86)\\NVIDIA GPU Computing Toolkit\\CUDA"]:
                   if os.path.isdir(path):
                       dirs = os.listdir(path)
                       for dr in dirs:
                           path2 = os.path.join(path, dr, 'lib')
                           if os.path.isdir(path2):
                               paths.append(path2)

               if len(paths)>0:
                   tmp_paths = ';'.join(paths)
                   tmp_paths += ';'+os.environ.get('PATH','')

                   env['CM_TMP_PATH'] = tmp_paths
                   env['CM_TMP_PATH_IGNORE_NON_EXISTANT'] = 'yes'

       else:
           # paths to cuda are not always in PATH - add a few typical locations to search for
           # (unless forced by a user)

           if env.get('CM_INPUT','').strip()=='':
               if env.get('CM_TMP_PATH','').strip()!='':
                  env['CM_TMP_PATH']+=':'

               env['CM_TMP_PATH_IGNORE_NON_EXISTANT'] = 'yes'

               for lib_path in env.get('+CM_HOST_OS_DEFAULT_LIBRARY_PATH', []):
                   if(os.path.exists(lib_path)):
                      env['CM_TMP_PATH']+=':'+lib_path

       r = i['automation'].find_artifact({'file_name': libfilename,
                                          'env': env,
                                          'os_info':os_info,
                                          'default_path_env_key': 'LD_LIBRARY_PATH',
                                          'detect_version':False,
                                          'env_path_key':'CM_TENSORRT_LIB_WITH_PATH',
                                          'run_script_input':i['run_script_input'],
                                          'recursion_spaces':recursion_spaces})
       if r['return'] >0 :
           if os_info['platform'] == 'windows':
               return r
       else:
           return {'return':0}

    if os_info['platform'] == 'windows':
        return {'return': 1, 'error': 'Windows is currently not supported!'}

    if env.get('CM_TENSORRT_TAR_FILE_PATH','')=='':
        tags = [ "get", "tensorrt" ]
        if env.get('CM_TENSORRT_REQUIRE_DEV', '') != 'yes':
            tags.append("_dev")
        return {'return': 1, 'error': 'Please envoke cmr "' + " ".join(tags) + '" --tar_file={full path to the TensorRT tar file}'}


    print ('Untaring file - can take some time ...')

    file_name = "trtexec"
    my_tar = tarfile.open(os.path.expanduser(env['CM_TENSORRT_TAR_FILE_PATH']))
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
    env['CM_TENSORRT_LIB_PATH'] = os.path.join(os.getcwd(), folder_name, "lib")
    env['CM_TMP_PATH'] = os.path.join(os.getcwd(), folder_name, "bin")
    env['+CPLUS_INCLUDE_PATH'] = [ os.path.join(os.getcwd(), folder_name, "include") ]
    env['+C_INCLUDE_PATH'] = [ os.path.join(os.getcwd(), folder_name, "include") ]
    env['+LD_LIBRARY_PATH'] = [ os.path.join(os.getcwd(), folder_name, "lib") ]

    return {'return':0}

def postprocess(i):

    os_info = i['os_info']

    env = i['env']

    if '+LD_LIBRARY_PATH'  not in env:
        env['+LD_LIBRARY_PATH'] = []

    if '+PATH'  not in env:
        env['+PATH'] = []

    if '+ LDFLAGS' not in env:
        env['+ LDFLAGS'] = []

    #if 'CM_TENSORRT_LIB_WITH_PATH' in env:
    #    tensorrt_lib_path = os.path.dirname(env['CM_TENSORRT_LIB_WITH_PATH'])
    if 'CM_TENSORRT_LIB_PATH' in env:
        env['+LD_LIBRARY_PATH'].append(env['CM_TENSORRT_LIB_PATH'])
        env['+PATH'].append(env['CM_TENSORRT_LIB_PATH']) #for cmake
        env['+ LDFLAGS'].append("-L"+env['CM_TENSORRT_LIB_PATH'])

    version = env['CM_TENSORRT_VERSION']

    return {'return':0, 'version': version}
