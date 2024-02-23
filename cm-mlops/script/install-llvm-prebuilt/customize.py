from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    need_version = env.get('CM_VERSION','')
    clang_file_name = "clang"
    if need_version == '':
        return {'return':1, 'error':'internal problem - CM_VERSION is not defined in env'}

    print (recursion_spaces + '    # Requested version: {}'.format(need_version))

    host_os_bits = env['CM_HOST_OS_BITS']

    if os_info['platform'] != 'windows':
        host_os_machine = env['CM_HOST_OS_MACHINE'] # ABI

    # Prepare package name
    # First check if it is forced by external environment
    package_name = env.get('CM_LLVM_PACKAGE','').strip()
    if package_name == '':
        need_version_split = need_version.split('.')

        # If package_name if not forced, attempt to synthesize it based on OS and arch
        if os_info['platform'] == 'darwin':
            force_arch = env.get('CM_LLVM_PACKAGE_FORCE_ARCH','') # To allow x86_64 if needed
            if force_arch == '': force_arch = 'arm64'
            force_darwin_version = env.get('CM_LLVM_PACKAGE_FORCE_DARWIN_VERSION','')
            if force_darwin_version == '':
                if len(need_version_split)>0:
                    hver = 0
                    try:
                        hver = int(need_version_split[0])
                    except:
                        pass

                    if hver>0 and hver<16:
                        force_darwin_version = '21.0'
                    else:
                        force_darwin_version = '22.0'
            package_name = 'clang+llvm-' + need_version + '-'+force_arch+'-apple-darwin'+force_darwin_version+'.tar.xz'

        elif os_info['platform'] == 'windows':
            package_name = 'LLVM-' + need_version + '-win' + host_os_bits + '.exe'
            clang_file_name = "clang.exe"

            print('')
            print('WARNING: Please copy the following path and then paste it')
            print('         when LLVM installer asks you about the "Destination Folder":')
            print('')
            print(os.getcwd())
            print('')
            input('Press Enter to continue!')

        else:
           if host_os_machine.startswith('arm') or host_os_machine.startswith('aarch'):
              if host_os_bits=='64':
                 package_name = 'clang+llvm-' + need_version + '-aarch64-linux-gnu.tar.xz'
              else:
                 package_name = 'clang+llvm-' + need_version + '-armv7a-linux-gnueabihf.tar.xz'
           else:
              host_os_flavor = env['CM_HOST_OS_FLAVOR']

              host_os_version = env['CM_HOST_OS_VERSION']

#              if 'debian' in host_os_flavor:
#                  return {'return':1, 'error':'debian is not supported yet'}
#
#              else:
              # Treat all Linux flavours as Ubuntu for now ...

              if True:
                  default_os = '22.04'

                  if len(need_version_split)>0:
                      hver = 0
                      try:
                          hver = int(need_version_split[0])
                      except:
                          pass

                      if hver>0:
                          if hver<16:
                              default_os='18.04'
                          else:
                              default_os='22.04'

                  if need_version == '10.0.1':
                      default_os = '16.04'

                  elif need_version == '11.0.0':
                      default_os = '20.04'

                  elif need_version == '11.0.1':
                      default_os = '16.04'
                      if host_os_version == '20.10':
                          default_os = '20.10'

                  elif need_version == '12.0.0':
                      default_os = '16.04'
                      if host_os_version == '20.04' or host_os_version == '20.10':
                         default_os = '20.04'

                  elif need_version == '12.0.1':
                      default_os = '16.04'
                      #if host_os_version.startswith('18') or host_os_version.startswith('20'):
                      #   default_os = '18.04'

                  elif need_version == '13.0.0':
                      default_os = '16.04'
                      if host_os_version.startswith('20'):
                         default_os = '20.04'

                  elif need_version == '13.0.1':
                      default_os = '18.04'

                  elif need_version == '14.0.0':
                      default_os = '18.04'

                  elif need_version == '15.0.6':
                      default_os = '18.04'

                  elif need_version == '16.0.0':
                      default_os = '18.04'

                  elif need_version == '16.0.4':
                      default_os = '22.04'

                  elif need_version == '17.0.2':
                      default_os = '22.04'

                  elif need_version == '17.0.2':
                      default_os = '22.04'

                  elif need_version == '17.0.4':
                      default_os = '22.04'

                  elif need_version == '17.0.5':
                      default_os = '22.04'

                  elif need_version == '17.0.6':
                      default_os = '22.04'

              package_name = 'clang+llvm-' + need_version + '-x86_64-linux-gnu-ubuntu-' + default_os + '.tar.xz'


    package_url = 'https://github.com/llvm/llvm-project/releases/download/llvmorg-' + need_version + '/' + package_name

    print (recursion_spaces + '    # Prepared package URL: {}'.format(package_url))

    print ('')
    print ('Downloading from {} ...'.format(package_url))

    cm = automation.cmind

    r = cm.access({'action':'download_file', 
                   'automation':'utils,dc2743f8450541e3', 
                   'url':package_url})
    if r['return']>0: return r

    filename = r['filename'] # 'clang+llvm-12.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz' # f['filename']

    env['CM_LLVM_PACKAGE'] = filename
    env['CM_LLVM_INSTALLED_PATH'] = os.path.join(os.getcwd(), 'bin')
    env['CM_LLVM_CLANG_BIN_WITH_PATH'] = os.path.join(os.getcwd(), 'bin', clang_file_name)
    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_LLVM_CLANG_BIN_WITH_PATH']

    # We don't need to check default paths here because we force install to cache
    env['+PATH'] = [env['CM_LLVM_INSTALLED_PATH']]

    path_include = os.path.join(os.getcwd(), 'include')
    if os.path.isdir(path_include):
        env['+C_INCLUDE_PATH'] = [ path_include ]


    return {'return':0}

def postprocess(i):

    env = i['env']
    version = env['CM_VERSION']
    os_info = i['os_info']

#    cur_dir = os.getcwd()
#    cur_dir_include = os.path.join(cur_dir, 'include')

#    if os.path.isdir(cur_dir_include):
#        if os_info['platform'] == 'darwin':
#           if '+C_INCLUDE_PATH' not in env:
#               env['+C_INCLUDE_PATH'] = []
#           if cur_dir_include not in env['+C_INCLUDE_PATH']:
#               env['+C_INCLUDE_PATH'].append(cur_dir_include)
#
#           if '+CPLUS_INCLUDE_PATH' not in env:
#               env['+CPLUS_INCLUDE_PATH'] = []
#           if cur_dir_include not in env['+CPLUS_INCLUDE_PATH']:
#               env['+CPLUS_INCLUDE_PATH'].append(cur_dir_include)

    
    return {'return':0, 'version': version}
