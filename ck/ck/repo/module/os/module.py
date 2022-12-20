#
# Collective Knowledge (os)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin, Grigori.Fursin@cTuning.org, http://fursin.net
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

# Local settings

##############################################################################
# Initialize module

def init(i):
    """

    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    return {'return':0}

##############################################################################
# find close OS

def find_close(i):
    """
    Input:  {
              (os_uoa)     - load info from a given OS
              (os_dict)    - if non-empty, return this dict
            }

    Output: {
              return     - return code =  0

              platform   - 'win' or 'linux'. Careful - it is always for current host OS! 
                           Use 'ck_name' key from meta for the target OS!

              bits       - (str) 32 or 64. Careful - it is always for current host OS!
                           Use 'bits' key from meta for the target OS!

              os_uoa     - UOA of the most close OS
              os_uid     - UID of the most close OS
              os_dict    - meta of the most close OS

              (add_path) - list of extra path ...
            }
    """

    r=ck.get_os_ck({})
    if r['return']>0: return r

    bits=r['bits']
    plat=r['platform']

    xos=i.get('os_uoa','')
    fc=i.get('find_close','')

    if xos=='':
       # Detect host platform
       # Search the most close OS
       ii={'action':'search',
           'module_uoa':work['self_module_uid'],
           'search_dict':{'ck_name':plat,
                          'bits':bits,
                          'generic':'yes',
                          'priority':'yes'},
           'internal':'yes'}

       # Adding extra tags to separate different Linux flavours such as Mac OS X:
       import sys
       pl=sys.platform

       if pl=='darwin':
          ii['tags']='macos'
       elif plat=='linux':
          ii['tags']='standard'

       rx=ck.access(ii)
       if rx['return']>0: return rx

       lst=rx['lst']
       if len(lst)==0:
          return {'return':1, 'error':'most close platform was not found in CK'}

       pl=lst[0]

       xos=pl.get('data_uoa','')

    rr={'return':0, 'platform':plat, 'bits':bits}

    # Load OS
    if xos!='':
       r=ck.access({'action':'load',
                    'module_uoa':'os', 
                    'data_uoa':xos})
       if r['return']>0: return r

       os_uoa=r['data_uoa']
       os_uid=r['data_uid']

       dd=r['dict']

       if len(i.get('os_dict',{}))!=0: # Substitute from 'machine' description (useful for remote access)
           dd=i['os_dict']

       rr['os_uoa']=os_uoa
       rr['os_uid']=os_uid
       rr['os_dict']=dd

       # Check if need to add path
       x=dd.get('add_to_path_os_uoa','')
       if x!='':
          rx=ck.access({'action':'find',
                        'module_uoa':work['self_module_uid'],
                        'data_uoa':x})
          if rx['return']>0: return rx
          px=rx['path']

          rr['add_path']=[px]

    return rr

##############################################################################
# shell in OS

def shell(i):
    """
    Input:  {
              (target)
              (host_os)
              (target_os)
              (device_id)

              (cmd) -               cmd string (can have \n)

              (split_to_list) -     if 'yes', split stdout and stderr to list

              (should_be_remote) -  if 'yes', can run only on remote target

              (output_to_console) - if 'yes', output to console instead of files

              (encoding)            - if !='', use this encoding
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              return_code

              stdout or stdout_lst
              stderr or stderr_lst
            }

    """

    import os

    o=i.get('out','')
    oo=''
    if o=='con': oo='con'

    stl=i.get('split_to_list','')
    sbr=i.get('should_be_remote','')
    otc=i.get('output_to_console','')

    # Check if need to initialize device and directly update input i !
    ii={'action':'init',
        'module_uoa':cfg['module_deps']['machine'],
        'input':i}
    r=ck.access(ii)
    if r['return']>0: return r

    device_cfg=i.get('device_cfg',{})

    encoding=i.get('encoding','')

    # Check host/target OS/CPU
    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('device_id','')

    # Get some info about platforms
    ii={'action':'detect',
        'module_uoa':cfg['module_deps']['platform.os'],
        'host_os':hos,
        'target_os':tos,
        'device_cfg':device_cfg,
        'device_id':tdid,
        'skip_info_collection':'yes'}
    r=ck.access(ii)
    if r['return']>0: return r

    hos=r['host_os_uid']
    hosx=r['host_os_uoa']
    hosd=r['host_os_dict']

    tos=r['os_uid']
    tosx=r['os_uoa']
    tosd=r['os_dict']

    tdid=i.get('device_id','')

    xtdid=''
    if tdid!='': xtdid=' -s '+tdid

    envsep=hosd.get('env_separator','')
    sext=hosd.get('script_ext','')
    sexe=hosd.get('set_executable','')
    sbp=hosd.get('bin_prefix','')
    scall=hosd.get('env_call','')
    ubtr=hosd.get('use_bash_to_run','')
    stro=tosd.get('redirect_stdout','')
    stre=tosd.get('redirect_stderr','')

    cmd=i.get('cmd','')

    if otc!='yes':
       # Tmp file for stdout
       rx=ck.gen_tmp_file({'prefix':'tmp-', 'suffix':'.tmp', 'remove_dir':'no'})
       if rx['return']>0: return rx
       fno=rx['file_name']

       # Tmp file for stderr
       rx=ck.gen_tmp_file({'prefix':'tmp-', 'suffix':'.tmp', 'remove_dir':'no'})
       if rx['return']>0: return rx
       fne=rx['file_name']

    # Check remote shell
    rs=tosd.get('remote_shell','')
    if sbr=='yes' and rs=='':
        return {'return':1, 'error':'target mush be remote'}

    if rs!='':
        # ADB dependency
        deps={'adb':{
                     "force_target_as_host": "yes",
                     "local": "yes", 
                     "name": "adb tool", 
                     "sort": -10, 
                     "tags": "tool,adb"
                     }
             }

        ii={'action':'resolve',
            'module_uoa':cfg['module_deps']['env'],
            'host_os':hos,
            'target_os':tos,
            'device_id':tdid,
            'deps':deps,
            'add_customize':'yes',
            'out':oo}
        rx=ck.access(ii)
        if rx['return']>0: return rx

        x='"'
        cmd=rx['cut_bat']+'\n'+rs.replace('$#device#$',xtdid)+' '+x+cmd+x

    # Record to tmp batch and run
    rx=ck.gen_tmp_file({'prefix':'tmp-', 'suffix':sext, 'remove_dir':'no'})
    if rx['return']>0: return rx
    fn=rx['file_name']

    rx=ck.save_text_file({'text_file':fn, 'string':cmd})
    if rx['return']>0: return rx

    # Prepare CMD for the host
    y=''
    if sexe!='':
       y+=sexe+' '+fn+envsep
    y+=' '+scall+' '+fn

    if ubtr!='': y=ubtr.replace('$#cmd#$',y)

    if otc!='yes':
       y=y+' '+stro+' '+fno+' '+stre+' '+fne

    rx=os.system(y)

    if os.path.isfile(fn):
        os.remove(fn)

    rr={'return':0, 'return_code':rx, 'target_os_dict':tosd}

    # Reading stdout file
    if otc!='yes':
       rx=ck.load_text_file({'text_file':fno, 'delete_after_read':'yes', 'split_to_list':stl, 'encoding':encoding})
       if rx['return']>0: return rx

       if stl=='yes':
           stdout=''

           rr['stdout_lst']=rx['lst']

           for q in rx['lst']:
               stdout+=q+'\n'
       else:
           stdout=rx['string']
           rr['stdout']=stdout

       # Reading stderr file
       rx=ck.load_text_file({'text_file':fne, 'delete_after_read':'yes', 'split_to_list':stl, 'encoding':encoding})
       if rx['return']>0: return rx
       if stl=='yes':
           stderr=''

           rr['stderr_lst']=rx['lst']

           for q in rx['lst']:
               stderr+=q+'\n'
       else:
           stderr=rx['string']
           rr['stderr']=stderr

       # Print if needed
       if o=='con':
          if stdout!='': ck.out(stdout)
          if stderr!='': ck.eout(stderr)

    return rr

##############################################################################
# convert UID to alias (UID) for user-friendly printing

def convert_uid_to_alias(i):
    """
    Input:  {
              uoa - OS uoa
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
              string - "UID" if now alias or "alias (UID)"
            }

    """

    uoa=i['uoa']

    s=uoa

    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':uoa})
    if r['return']>0: return r

    da=r['data_alias']
    if da!='':
       s=da+' ('+r['data_uid']+')'

    return {'return':0, 'string':s}

##############################################################################
# generates shell script for exporting library path variables for the given platform

def lib_path_export_script(i):
    """
    Input:  {
              host_os_dict          - host OS meta
              (dynamic_lib_path)    - dynamic (shared) library path, or a list of paths
              (static_lib_path)     - dynamic (shared) library path, or a list of paths
              (lib_path)            - if set, and dynamic_path/static_lib_path is not set, 
                                      uses this value as dynamic_lib_path and/or static_lib_path
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              script       - script to execute to add the given path to the dynamic and/or static library path env vars
            }

    """

    host_d = i.get('host_os_dict', {})
    dynamic_path = _convert_lib_path_list_to_string(i.get('dynamic_lib_path', i.get('lib_path', '')))
    static_path = _convert_lib_path_list_to_string(i.get('static_lib_path', i.get('lib_path', '')))

    dynamic_var_name = host_d.get('env_ld_library_path', 'LD_LIBRARY_PATH')
    static_var_name = host_d.get('env_library_path', 'LIBRARY_PATH')

    hplat=host_d.get('ck_name','')
    s = ''
    if hplat != 'win' and (dynamic_path != '' or static_path != ''):
      s += '\n'
      if dynamic_path != '':
        s += 'export {name}="{value}":${name}\n'.format(name=dynamic_var_name, value=dynamic_path)
      if static_path != '':
        s += 'export {name}="{value}":${name}\n'.format(name=static_var_name, value=static_path)
      s += '\n'

    return {'return': 0, 'script': s}

##############################################################################
def _convert_lib_path_list_to_string(lst):
    return '":"'.join(lst) if isinstance(lst, list) else lst

##############################################################################
# convert win path to cygwin path

def convert_to_cygwin_path(i):
    """
    Input:  {
              path - path to convert
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              path         - updated path
            }

    """

    p=i['path']

    pp=p.replace('\\','/')

    if i.get('out','')=='con':
       ck.out(pp)

    return {'return':0, 'path':pp}

##############################################################################
# convert multiple paths to cygwin paths

def convert_to_cygwin_paths(i):
    """
    Input:  {
              paths - dict with paths to convert
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              paths - updated dict with paths
            }

    """

    pp=i['paths']

    for k in pp:
        p=pp[k]

        r=convert_to_cygwin_path({'path':p})
        if r['return']>0: return r

        pp[k]=r['path']

    return {'return':0, 'paths':pp}

##############################################################################
# run command and get stdout
def run_and_get_stdout(i):
  """
  Input:  {
            cmd       - list of command line arguments, starting with the command itself
            (shell)   - if 'yes', reuse shell environment
          }

  Output: {
            return       - return code =  0, if successful
                                       >  0, if error
                                       =  8, if timeout
            (error)      - error text if return > 0

            return_code  - return code from app

            stdout       - string, standard output of the command
          }
  """

  import subprocess
  import shlex
  import platform
  import sys

  cmd=i['cmd']
  if type(cmd)!=list:
      # Split only on non-Windows platforms (since Windows takes a string in Popen)
      if not platform.system().lower().startswith('win'):
          cmd=shlex.split(cmd)

  xshell=False
  if i.get('shell','')=='yes':
      xshell=True

  p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=xshell)
  output, error = p1.communicate()

  if sys.version_info[0]>2:
      output = output.decode(encoding='UTF-8')
      error = error.decode(encoding='UTF-8')

  return {'return':0, 'return_code':p1.returncode, 'stdout':output, 'stderr':error}

##############################################################################
# find file or directory in all above directories from a given path

def find_file_above_path(i):
    """
    Input:  {
              (path) - if not specified, use current path
              file   - search for file or directory
            }

    Output: {
              path   - path where file or directory was found (or empty if not found)

              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    path_found=''

    sfile=i['file']

    path=i.get('path','')
    if path=='':
       path=os.getcwd()

    while True:
       path1=os.path.dirname(path)

       print (path1)

       if path1==path:
          break

       path=path1

       path2=os.path.join(path, sfile)
       print (path2)
       if os.path.isfile(path2) or os.path.isdir(path2):
          path_found=path
          break

    return {'return':0, 'path': path_found}
