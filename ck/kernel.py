#
# Collective Knowledge (CK)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin
#

# This is the kernel of CK. It is implemented in just one file 
# with a minimal set of common portable functions and without OO
# to make it simpler to re-implement it in any another language if needed.
# For example, we implemented some functions in Java, C, C++ and Fortran
# (see our xOpenME library used in Android)

__version__ = "1.12.3.1"  # We use 3 digits for the main (released) version and 4th digit for development revision
                          # Do not use characters (to detect outdated version)!

# Extra modules global for the whole kernel
import sys
import json
import os
import imp   # Loading Python modules

initialized=False      # True if initialized
allow_print=True       # Needed to suppress all output
con_encoding=''        # Use non-default console encoding

# This configuration dictionary will be overloaded at run-time
# from the CK entry default:kernel:default (from this CK distro)
# and then from the local:kernel:default (from a local user repository)

cfg={
      "name":"Collective Knowledge",
      "desc":"exposing ad-hoc experimental setups to extensible repository and big data predictive analytics",
      "cmd":"ck <action> $#module_uoa#$ (cid1/uid1) (cid2/uid2) (cid3/uid3) key_i=value_i ... @file.json",

      "wiki_data_web":"https://cKnowledge.io/c/",           # Collective Knowledge Base (ckb)
      "private_wiki_data_web":"https://github.com/ctuning/ck/wiki/ckb_",   # Collective Knowledge Base (ckb)
      "api_web":"https://cKnowledge.io/c/module/",
      "status_url":"https://raw.githubusercontent.com/ctuning/ck/master/setup.py",

      "help_examples":"  Example of obtaining, compiling and running a shared benchmark on Linux with GCC:\n    $ ck pull repo:ctuning-programs\n    $ ck compile program:cbench-automotive-susan --speed\n    $ ck run program:cbench-automotive-susan\n\n  Example of an interactive CK-powered article:\n    http://cknowledge.org/repo\n",
      "help_web":"  Documentation:\n        https://github.com/ctuning/ck/wiki",

      "ck_web":"https://github.com/ctuning/ck",
      "ck_web_wiki":"https://github.com/ctuning/ck/wiki",

      "default_shared_repo_url":"https://github.com/ctuning",
      "github_repo_url":"https://github.com",

#      "default_license":"See CK LICENSE.txt for licensing details",
#      "default_copyright":"See CK COPYRIGHT.txt for copyright details",
#      "default_developer":"cTuning foundation",
#      "default_developer_email":"admin@cTuning.org",
#      "default_developer_webpage":"http://cTuning.org",

      "detect_cur_cid":"#",
      "detect_cur_cid1":"^",

      "error":"CK error: ",
      "json_sep":"*** ### --- CK JSON SEPARATOR --- ### ***",
      "default_module":"data",
      "module_name":"module",
      "module_uids":["032630d041b4fd8a"],
      "repo_name":"repo",
      "module_code_name":"module",
      "module_full_code_name":"module.py",

      "env_key_root":"CK_ROOT",
      "env_key_local_repo":"CK_LOCAL_REPO",
      "env_key_local_kernel_uoa":"CK_LOCAL_KERNEL_UOA",
      "env_key_default_repo":"CK_DEFAULT_REPO",
      "env_key_repos":"CK_REPOS",

      "subdir_default_repos":"repos",

      "user_home_dir_ext":"CK", # if no path to repos is defined, use user home dir with this extension

      "kernel_dir":"ck",
      "kernel_dirs":["ck",""],

      "file_kernel_py":"ck/kernel.py",

      "subdir_default_repo":"repo",
      "subdir_kernel":"kernel",
      "subdir_kernel_default":"default",
      "subdir_ck_ext":".cm", # keep compatibility with Collective Mind V1.x
      "file_for_lock":"ck_lock.txt",

      "special_directories":[".cm", ".svn", ".git"], # special directories that should be ignored when copying/moving entries

      "ignore_directories_when_archive_repo":[".svn", ".git"], 

      "file_meta_old":"data.json", # keep compatibility with Collective Mind V1.x
      "file_meta":"meta.json",
      "file_info":"info.json",
      "file_desc":"desc.json",
      "file_updates":"updates.json",

      "file_alias_a": "alias-a-", 
      "file_alias_u": "alias-u-",

      "linux_sudo":"sudo",
      "install_ck_as_lib":"python setup.py install",

      "repo_file":".ckr.json",

      "file_cache_repo_uoa":".ck.cache_repo_uoa.json",
      "file_cache_repo_info":".ck.cache_repo_info.json",

      "default_host":"localhost",
      "default_port":"3344",

      "detached_console":{"win":{"cmd":"start $#cmd#$", "use_create_new_console_flag":"yes"},
                          "linux":{"cmd":"xterm -hold -e \"$#cmd#$\""}},

      "batch_extension":{"win":".bat",
                         "linux":".sh"},

      "default_archive_name":"ck-archive.zip",

      # TODO: remove "http://"?
      "index_host":"http://localhost",
      "index_port":"9200",
      "index_use_curl":"no",

      "cknowledge_api":"https://cKnowledge.io/api/v1/?",
#      "download_missing_components":"yes",

      "wfe_template":"default",

      "module_repo_name":"repo",
      "repo_name_default":"default",
      "repo_uid_default":"604419a9fcc7a081",
      "repo_name_local":"local",
      "repo_uid_local":"9a3280b14a4285c9",

      "default_exchange_repo_uoa":"remote-ck",
      "default_exchange_subrepo_uoa":"upload",

      "external_editor":{"win":"wordpad $#filename#$",
                         "linux":"vim $#filename#$"},

      "shell":{"linux":{
                         "redirect_stdout":">",
                         "env_separator": ";" 
                       },
               "win":  {
                         "redirect_stdout":">",
                         "env_separator": "&&"
                       }
      },

      "forbid_global_delete": "no", 
      "forbid_global_writing": "no", 
      "forbid_writing_modules": "no", 
      "forbid_writing_to_default_repo": "no", 
      "forbid_writing_to_local_repo": "no", 
      "allow_writing_only_to_allowed": "no", 

      "allow_run_only_from_allowed_repos": "no",
      "repo_uids_to_allow_run":["604419a9fcc7a081", 
                                "9a3280b14a4285c9", 
                                "76c4424a1473c873",
                                "a4328ba99679e0d1",
                                "7fd7e76e13f4cd6a",
                                "215d441c19db1fed",
                                "43eaa6c2d1892c32"],

      "use_indexing": "no",

      "internal_keys": [
                         "action",
                         "repo_uoa",
                         "module_uoa",
                         "data_uoa",
                         "cid",
                         "cids",
                         "cid1",
                         "cid2",
                         "cid3",
                         "xcids",
                         "unparsed_cmd",
                         "con_encoding",
                         "ck_profile",
                         "out",
                         "out_file"
                       ],

      "repo_types":{
                     "git":{
                            "clone":"git clone $#url#$ $#path#$",
                            "pull":"git pull",
                            "push":"git push",
                            "add":"git add $#files#$",
                            "rm":"git rm -rf $#files#$",
                            "commit":"git commit *",
                            "version":"git --version",
                            "checkout":"git checkout $#id#$"
                           }
                   },

      "actions":{
                 "uid":{"desc":"generate UID", "for_web": "yes"},
                 "version":{"desc":"print CK version", "for_web": "yes"},
                 "python_version":{"desc":"print python version used by CK", "for_web": "no"},
                 "status":{"desc":"check CK version status", "for_web": "yes"},
                 "copy_path_to_clipboard":{"desc":"copy current path to clipboard", "for_web": "no"},

                 "wiki":{"desc":"<CID> open discussion wiki page for a given entry"},           # Collective Knowledge Base (ckb)
                 "pwiki":{"desc":"<CID> open private discussion wiki page for a given entry"}, 

                 "help":{"desc":"<CID> print help about data (module) entry"},
                 "short_help":{"desc":"<CID> print short help about CK"},
                 "webhelp":{"desc":"<CID> open browser with online help (description) for a given CK entry"}, 
                 "webapi":{"desc":"<CID> open browser with online API for a given module"}, 
                 "guide":{"desc":"open CK wiki with user/developer guides"}, 
                 "info":{"desc":"<CID> print help about module"},

                 "browser":{"desc":"start CK web service and open browser"},

                 "add":{"desc":"<CID> add entry", "for_web":"yes"},
                 "update":{"desc":"<CID> update entry", "for_web":"yes"},
                 "load":{"desc":"<CID> load meta description of entry", "for_web": "yes"},
                 "edit":{"desc":"<CID> edit entry description using external editor", "for_web":"no"},

                 "zip":{"desc":"<CID> zip entries", "for_web":"no"},

                 "find":{"desc":"<CID> find path to entry"},
                 "cd":{"desc":"<CID> print 'cd {path to entry}'"},
                 "cdc":{"desc":"<CID> print 'cd {path to entry} and copy to clipboard, if supported"},
                 "path":{"desc":"<CID> detect CID in the current directory"},
                 "cid":{"desc":"<CID> get CID of the current entry"},

                 "rm":{"desc":"<CID> delete entry", "for_web":"yes"},
                 "remove":{"desc":"see 'rm'", "for_web":"yes"},
                 "delete":{"desc":"see 'rm'", "for_web":"yes"},

                 "ren":{"desc":"<CID> <new name) (data_uid) (remove_alias) rename entry", "for_web":"yes"},
                 "rename":{"desc":"see 'ren' function", "for_web":"yes"},

                 "cp":{"desc":"<CID> <CID1> copy entry", "for_web":"yes"},
                 "copy":{"desc":"see 'cp'", "for_web":"yes"},

                 "mv":{"desc":"<CID> <CID1> move entry", "for_web":"yes"},
                 "move":{"desc":"see 'mv'", "for_web":"yes"},

                 "list_files":{"desc":" list files recursively in a given entry", "for_web": "yes"},
                 "delete_file":{"desc":"<file> delete file from a given entry", "for_web":"yes"},

                 "list":{"desc":"<CID> list entries", "for_web": "yes"},
                 "ls":{"desc":"see 'list'", "for_web": "yes"},

                 "search":{"desc":"<CID> search entries", "for_web": "yes"},

                 "pull":{"desc":"<CID> (filename) or (empty to get the whole entry as archive) pull file from entry"},
                 "push":{"desc":"<CID> (filename) push file to entry"},

                 "add_action":{"desc":"add action (function) to existing module"},
                 "remove_action":{"desc":"remove action (function) from existing module"},
                 "list_actions":{"desc":"list actions (functions) in existing module", "for_web":"yes"},

                 "add_index":{"desc":"<CID> add index"},
                 "delete_index":{"desc":"<CID> remove index"},

                 "convert_cm_to_ck":{"desc":"<CID> convert old CM entries to CK entries"},

                 "create_entry":{"desc":"<directory> create an entry for a given directory name"},

                 "get_api":{"desc":"--func=<func> print API of a function in a given module"},

                 "download":{"desc":"<CID> attempt to download entry from remote host (experimental)", "for_web": "yes"},

                 "print_input":{"desc":"prints input"},

                },

      "actions_redirect":{"list":"list_data2",
                          "ls":"list_data2"},

      "common_actions":["webhelp", "webapi", "help", "info", "print_input",
                        "wiki",
                        "path", "find", "cid", "cd", "cdc",
                        "browser",
                        "add",
                        "edit", 
                        "load", 
                        "zip",
                        "rm", "remove", "delete",
                        "update",
                        "ren", "rename",
                        "cp", "copy",
                        "mv", "move",
                        "ls",
                        "list",
                        "search",
                        "pull",
                        "push",
                        "list_files",
                        "delete_file",
                        "add_action",
                        "remove_action",
                        "list_actions",
                        "create_entry",
                        "add_index",
                        "delete_index",
                        "get_api",
                        "download",
                        "convert_cm_to_ck"]
    }

work={
      "env_root":"",               # Path to CK installation

      "dir_default_repo":"",
      "dir_default_repo_path":"",
      "dir_default_kernel":"",
      "dir_default_cfg":"",

      "dir_local_repo":"",
      "dir_local_repo_path":"",
      "dir_local_kernel":"",
      "dir_local_cfg":"",

      "local_kernel_uoa":"",

      "dir_work_repo":"",
      "dir_work_repo_path":"",
      "dir_work_cfg":"",

      "dir_repos":"",

      "dir_cache_repo_uoa":"",
      "dir_cache_repo_info":"",

      "repo_name_work":"",
      "repo_uid_work":"",

      'cached_module_by_path':{},
      'cached_module_by_path_last_modification':{}
     }

paths_repos=[]        # First path to local repo (if exist), than global

cache_repo_init=False # True, if initialized
paths_repos_all=[]    # Path to all repos
cache_repo_uoa={}     # Disambiguate repo UOA to repo UID
cache_repo_info={}    # Cache repo info with path and type

type_long=None        # In Python 3 -> int, in Python 2 -> long
string_io=None        # StringIO, which is imported differently in Python 2 and 3

log_ck_entries=False  # If true, log CK entries to record all dependencies

##############################################################################
# Save CK state
#
# TARGET: end users

def save_state():
    """
    Input:  None

    Output: dict with state
    """

    import copy
    import os

    r={}

    r['cfg']=copy.deepcopy(cfg)
    r['paths_repos']=copy.deepcopy(paths_repos)

    r['cache_repo_init']=cache_repo_init
    r['paths_repos_all']=copy.deepcopy(paths_repos_all)
    r['cache_repo_uoa']=copy.deepcopy(cache_repo_uoa)
    r['cache_repo_info']=copy.deepcopy(cache_repo_info)

    r['os.environ']=copy.deepcopy(os.environ)

    return r

##############################################################################
# Restore CK state
#
# TARGET: end users

def restore_state(r):
    """
    Input:  dict with state

    Output: output from "init" function
    """

    global initialized, cfg, paths_repos, cache_repo_init, paths_repos_all, cache_repo_uoa, cache_repo_info

    import copy
    import os

    cfg=r['cfg']
    paths_repos=r['paths_repos']

    cache_repo_init=r['cache_repo_init']
    paths_repos_all=r['paths_repos_all']
    cache_repo_uoa=r['cache_repo_uoa']
    cache_repo_info=r['cache_repo_info']

    os.environ=r['os.environ']

    initialized=False

    return init({})

##############################################################################
# Reinitialize CK
#
# TARGET: end users

def reinit():
    """
    Input:  None

    Output: output from "init" function
    """

    global initialized, paths_repos, cache_repo_init, paths_repos_all, cache_repo_uoa, cache_repo_info

    initialized=False
    paths_repos=[]

    cache_repo_init=False
    paths_repos_all=[]
    cache_repo_uoa={}
    cache_repo_info={}

    return init({})

##############################################################################
# Universal print of unicode string in utf8 that supports Python 2.x and 3.x
#
# TARGET: end users

def out(s):
    """
    Input:  s - unicode string to print

    Output: Nothing
    """

    if allow_print: 
       if con_encoding=='':
          x=sys.stdin.encoding
          if x==None: 
             b=s.encode()
          else:
             b=s.encode(x, 'ignore')
       else:
          b=s.encode(con_encoding, 'ignore')

       if sys.version_info[0]>2:
          try: # We encountered issues on ipython with Anaconda
               # and hence made this work around
             sys.stdout.buffer.write(b)
             sys.stdout.buffer.write(b'\n')
          except Exception as e: 
             print(s)
             pass
       else:
          print(b)

    sys.stdout.flush()

    return None

##############################################################################
# Universal debug print of a dictionary (removing unprintable parts)
#
# TARGET: end users

def debug_out(i):
    """
    Input:  i - dictionary

    Output: return = 0
    """

    import copy
    import json

    ii={}

    # Check main unprintable keys
    for k in i:
        try:
           s=json.dumps(i[k])
        except Exception as e: 
           pass
        else:
           ii[k]=i[k]

    # Dump
    out(json.dumps(ii, indent=2))

    return {'return':0}

##############################################################################
# Universal print of unicode error string in utf8 that supports Python 2.x and 3.x to stderr
#
# TARGET: end users

def eout(s):
    """
    Input:  s - unicode string to print

    Output: Nothing
    """

    if allow_print: 
       if con_encoding=='':
          x=sys.stdin.encoding
          if x==None: 
             b=s.encode()
          else:
             b=s.encode(x, 'ignore')
       else:
          b=s.encode(con_encoding, 'ignore')

       if sys.version_info[0]>2:
          try: # We encountered issues on ipython with Anaconda
               # and hence made this work around
             sys.stderr.buffer.write(b)
             sys.stderr.buffer.write(b'\n')
          except Exception as e: 
             sys.stderr.write(s)
             pass
       else:
          sys.stderr.write(b)

    sys.stderr.flush()

    return None

##############################################################################
# Universal error print and exit
#
# TARGET: end users

def err(r):
    """
    Input:  {
              return - return code
              error - error text
            }

    Output: Nothing; quits program
    """

    import sys

    rc=r['return']
    re=r['error']

    out('Error: '+re)
    sys.exit(rc)

##############################################################################
# Universal error print for Jupyter Notebook with raise KeyboardInterrupt
#
# TARGET: end users

def jerr(r):
    """
    Input:  {
              return - return code
              error - error text
            }

    Output: Nothing; quits program
    """

    rc=r['return']
    re=r['error']

    out('Error: '+re)

    raise KeyboardInterrupt

##############################################################################
# Support function for safe float (useful for sorting function)
#
# TARGET: end users

def safe_float(i,d):
    r=d
    try:
       r=float(i)
    except Exception as e: 
       pass

    return r

##############################################################################
# Support function to lower values in a list
#
# TARGET: internal

def lower_list(lst):

    nlst=[]

    for v in lst:
        nlst.append(v.lower())

    return nlst

##############################################################################
# Support function for checking splitting entry number
#
# TARGET: CK kernel and low-level developers

def get_split_dir_number(repo_dict, module_uid, module_uoa):

    # Check if there is a split of directories for this module in local config
    # to handle numerous entries (similar to MediaWiki)
    found=False
    split_dir_number=0

    # Check global split for all repositories (in cfg) or for a given repo
    for xcfg in [cfg, repo_dict]:
        x=xcfg.get('split_all_dirs','')
        if x!='':
           x=safe_int(x,0)
           if x!=0:
              found=True
              split_dir_number=x
              break

    # Check split per module
    if not found:
       for xcfg in [cfg, repo_dict]:
           xsplit_dirs=xcfg.get('split_dirs',{})

           found=False
           for m in [module_uid, module_uoa]:
               x=safe_int(xsplit_dirs.get(m,0),0)
               if x!=0:
                  split_dir_number=x
                  found=True
                  break

           if found:
              break

    return split_dir_number


##############################################################################
# Support function for splitting entry name
#
# TARGET: CK kernel and low-level developers

def split_name(name, number):

    sd1=name
    sd2=''

    if number!='': 
       number=int(number)
       if number!=0:
          if len(name)>number:
             sd1=name[:number]
             sd2=name[number:]
          else:
             sd1='_'
             sd2=name

    return (sd1,sd2)

##############################################################################
# Support function for checking whether to index data or not ...
#
# TARGET: CK kernel and low-level developers

def index_module(module_uoa, repo_uoa):

    ret=True

    # First check if index the whole repo
    ir=cfg.get('index_repos',[])
    if len(ir)>0 and repo_uoa!='':
       if repo_uoa in ir:
          return ret

    im=cfg.get('index_modules',[])

    # Next check if index module (if im is empty index all)
    if len(im)>0:
       ret=False

       if module_uoa in im:
          ret=True

    return ret

##############################################################################
# Support function for safe int (useful for sorting function)
#
# TARGET: end users

def safe_int(i,d):
    r=d
    try:
       r=int(i)
    except Exception as e: 
       pass

    return r

##############################################################################
# Support function to get value from list without error if out of bounds
# (useful for various sorting)
#
# TARGET: end users

def safe_get_val_from_list(lst, index, default_value):
    v=default_value
    if index<len(lst):
       v=lst[index]
    return v

##############################################################################
# Support function for system_with_timeout
#
# TARGET: end users

def system_with_timeout_kill(proc):

    # First via psutil (works better on Windows but may not be installed)

    loaded=True
    try:
       import psutil
    except ImportError:
       loaded=False
       pass

    if loaded: # pragma: no cover
       try:
          pid=proc.pid

          p=psutil.Process(pid)
          pc=p.get_children(recursive=True)

          for px in pc:
              px.kill()

          p.kill()
       except Exception as e: 
          loaded=False
          pass

    # Try traditional way
    if not loaded:
       try:
          proc.terminate()
       except Exception as e: 
          pass

    return

##############################################################################
# Substituting os.system with possibility for time out 
#
# TARGET: end users

def system_with_timeout(i):

    """
    Input:  {
              cmd       - command line
              (timeout) - timeout in seconds (granularity 0.01 sec) - may cause overheads ...
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
                                         =  8, if timeout
              (error)      - error text if return > 0

              return_code  - return code from app
            }
    """

    import subprocess
    import time

    cmd=i['cmd']

    rc=0

    to=i.get('timeout','')

    p=subprocess.Popen(cmd, shell=True)

    if to != '':
       xto=float(to)

       t0=time.time()
       t=0
       tx=float(i['timeout'])

       while p.poll() == None and t<xto:
          time.sleep(0.1)
          t=time.time()-t0

       if t>=xto and p.poll()==None:
          system_with_timeout_kill(p)
          return {'return':8, 'error':'process timed out and had been terminated'}
    else:
       p.wait()

    rc=p.returncode
    return {'return':0, 'return_code':rc}

##############################################################################
# Run command and get stdout
#
# TARGET: end users

def run_and_get_stdout(i):
  """
  Input:  {
            cmd [list] - list of command line arguments, starting with the command itself
            (shell)    - if 'yes', reuse shell environment
          }

  Output: {
            return       - return code =  0, if successful
                                       >  0, if error
                                       =  8, if timeout
            (error)      - error text if return > 0

            return_code  - return code from app

            stdout       - string, standard output of the command
            stderr       - string, standard error of the command
          }
  """

  import subprocess
  import shlex
  import platform

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
     try:
       output = output.decode(encoding='UTF-8')
     except Exception as e:
       return {'return':1, 'error':'problem encoding stdout ('+format(e)+')'}

     try:
       error = error.decode(encoding='UTF-8')
     except Exception as e:
       return {'return':1, 'error':'problem encoding stderr ('+format(e)+')'}

  return {'return':0, 'return_code':p1.returncode, 'stdout':output, 'stderr':error}

##############################################################################
# Get value from one dict, remove it from there and move to another
#
# TARGET: end users

def get_from_dicts(dict1, key, default_value, dict2, extra=''):
    """
    Input:  dict1         - first check in this dict (and remove if there)
            key           - key in dict1
            default_value - default value if not found
            dict2         - then check from here

    Output: value
    """

    value=default_value

    if key not in dict1:
       if dict2!=None:
          value=dict2.get(extra+key, default_value)
    else:
       value=dict1[key]
       del(dict1[key])

       if dict2!=None:
          dict2[extra+key]=value

    return value

##############################################################################
# Converting iso text time to datetime object
#
# TARGET: end users

def convert_iso_time(i):
    """
    Input:  {
              iso_datetime - iso date time
            }

    Output: { 
              return         - return code =  0, if successful
                                           >  0, if error
              (error)        - error text if return > 0
              (datetime_obj) - datetime object
            }
    """

    t=i['iso_datetime']

    import datetime
    import time

    dto=None

    ok=True

    try: dto=datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%S.%f")
    except Exception as e: 
       ok=False
       pass

    if not ok:
       ok=True
       try: dto=datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%S")
       except Exception as e: 
          ok=False
          pass

    if not ok:
       ok=True
       try: dto=datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M")
       except Exception as e: 
          ok=False
          pass

    if not ok:
       ok=True
       try: dto=datetime.datetime.strptime(t, "%Y-%m-%dT%H")
       except Exception as e: 
          ok=False
          pass

    if not ok:
       ok=True
       try: dto=datetime.datetime.strptime(t, "%Y-%m-%d")
       except Exception as e: 
          ok=False
          pass

    if not ok:
       ok=True
       try: dto=datetime.datetime.strptime(t, "%Y-%m")
       except Exception as e: 
          ok=False
          pass

    if not ok:
       ok=True
       try: dto=datetime.datetime.strptime(t, "%Y")
       except Exception as e: 
          return {'return':1, 'error':'can\'t parse ISO date time: '+t}

    return {'return':0, 'datetime_obj':dto}

##############################################################################
# Safe convert dict str keys to int to be sorted
#
# TARGET: end users

def convert_str_key_to_int(key):
    try:
       return int(key)
    except ValueError:
       return 0

##############################################################################
# Universal input of unicode string in utf8 that supports Python 2.x and 3.x
#
# TARGET: end users

def inp(i):
    """
    Input:  {
              text - text to print
            }

    Output: {
              return       - return code =  0

              string       - input string
            }
    """

    t=i['text']

    if con_encoding=='':
       x=sys.stdin.encoding
       if x==None: 
          b=t.encode()
       else:
          b=t.encode(x, 'ignore')
    else:
       b=t.encode(con_encoding, 'ignore') # pragma: no cover 

    if sys.version_info[0]>2:
       try: b=b.decode(sys.stdin.encoding)
       except Exception as e: 
         try: b=b.decode('utf8')
         except Exception as e: pass

    if sys.version_info[0]>2:
       s=input(b)
    else:
       x=sys.stdin.encoding
       if x==None:
          x='utf8'
       s=raw_input(b).decode(x).encode('utf8')

    return {'return':0, 'string':s}

##############################################################################
# Universal selector of dictionary entry
#
# TARGET: end users (advanced version available in module "choice")

def select(i):
    """
    Input:  {
              dict             - dict with values being dicts with 'name' as string to display and 'sort' as int (for ordering)
              (title)          - print title
              (error_if_empty) - if 'yes' and Enter, make error
              (skip_sort)      - if 'yes', do not sort array
            }

    Output: {
              return       - return code =  0

              string       - selected dictionary key
            }
    """

    s=''

    title=i.get('title','')
    if title!='':
       out(title)
       out('')

    d=i['dict']
    if i.get('skip_sort','')!='yes':
       kd=sorted(d, key=lambda v: d[v].get('sort',0))
    else:
       kd=d

    j=0
    ks={}
    for k in kd:
        q=d[k]

        sj=str(j)
        ks[sj]=k

        qn=q.get('name','')

        out(sj+') '+qn)

        j+=1

    out('')
    rx=inp({'text':'Make your selection (or press Enter for 0): '})
    if rx['return']>0: return rx
    sx=rx['string'].strip()

    if sx=='':
       if i.get('error_if_empty','')=='yes':
          return {'return':1, 'error':'selection is empty'}

       s=kd[0]
    else:
       if sx not in ks:
          return {'return':1, 'error':'selection is not recognized'}
       s=ks[sx]

    return {'return':0, 'string':s}

##############################################################################
# Universal UOA selector
#
# TARGET: end users (advanced version available in module "choice")

def select_uoa(i):
    """
    Input:  {
              choices      - list from search function
              (skip_enter) - if 'yes', do not select 0 when user presses Enter
              (skip_sort)  - if 'yes', do not sort array
            }

    Output: {
              return  - return code =  0, if successful
                                    >  0, if error
              (error) - error text if return > 0
              choice  - data UOA
            }

    """

    se=i.get('skip_enter','')

    lst=i.get('choices',[])

    if i.get('skip_sort','')!='yes':
       klst=sorted(lst, key=lambda v: v['data_uoa'])
    else:
       klst=lst

    zz={}
    iz=0

    for z1 in klst:
        z=z1['data_uid']
        zu=z1['data_uoa']

        zs=str(iz)
        zz[zs]=z

        out(zs+') '+zu+' ('+z+')')

        iz+=1

    out('')
    y='Select UOA'
    if se!='yes': y+=' (or press Enter for 0)'
    y+=': '

    rx=inp({'text':y})
    x=rx['string'].strip()
    if x=='' and se!='yes': x='0' 

    if x not in zz:
       return {'return':1, 'error':'number is not recognized'}

    dduoa=zz[x]

    return {'return':0, 'choice':dduoa}

##############################################################################
# Convert string to list
#
# TARGET: end users

def convert_str_tags_to_list(i):
    """
    Input:  either a list, or a string of comma-separated tags.

    Output: If i is a list, it's returned.
            If i is a string, the list of tags it represents is returned 
            (each tag is stripped of leading and trailing whitespace).

    """

    r=[]

    if type(i)==list:
       r=i
    else:
       ii=i.split(',')
       for q in ii:
           q=q.strip()
           if q!='':
              r.append(q)

    return r

##############################################################################
# Check writing possibility
#
# TARGET: CK kernel and low-level developers

def check_writing(i):
    """
    Input:  {
              (module_uoa)
              (module_uid)

              (repo_uoa)
              (repo_uid)
              (repo_dict)

              (delete)     - if 'yes', check if global delete operation is allowed
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
              (repo_dict)  - repo cfg if available
            }

    """

    dl=i.get('delete','')

    if dl=='yes' and cfg.get('forbid_global_delete','')=='yes':
       return {'return':1, 'error':'delete/rename operations are forbidden'}

    if cfg.get('forbid_global_writing','')=='yes':
       return {'return':1, 'error':'global writing is forbidden'}

    if len(i)==0: 
       return {'return':0} # Check only global writing

    if cfg.get('forbid_writing_modules','')=='yes':
       muoa=i.get('module_uoa','')
       muid=i.get('module_uid','')
       if muoa==cfg['module_name'] or (muid!='' and muid in cfg['module_uids']):
          return {'return':1, 'error':'writing/changing modules is forbidden'}

    ruoa=i.get('repo_uoa','')
    ruid=i.get('repo_uid','')

    if cfg.get('forbid_writing_to_default_repo','')=='yes':
       if ruoa==cfg['repo_name_default'] or ruid==cfg['repo_uid_default']:
          return {'return':1, 'error':'writing to default repo is forbidden'}

    if cfg.get('forbid_writing_to_local_repo','')=='yes':
       if ruoa==cfg['repo_name_local'] or ruid==cfg['repo_uid_local']:
          return {'return':1, 'error':'writing to local repo is forbidden'}

    rr={'return':0}

    # Load info about repo
    rd={}
    if ruoa!='':
       if 'repo_dict' in i:
          rd=i['repo_dict']
       else:
          rx=load_repo_info_from_cache({'repo_uoa':ruoa})
          if rx['return']>0: return rx
          rd=rx.get('dict',{})
       rr['repo_dict']=rd

    if cfg.get('allow_writing_only_to_allowed','')=='yes':
       if rd.get('allow_writing','')!='yes':
          return {'return':1, 'error':'writing to this repo is forbidden'}

    if rd.get('forbid_deleting','')=='yes' and dl=='yes':
       return {'return':1, 'error':'deleting in this repo is forbidden'}

    return rr

##############################################################################
# Get CK version
#
# TARGET: end users

def get_version(i):
    """
    Input:  {}

    Output: {
              return       - return code =  0

              version      - list starting from major version number
              version_str  - version string
            }

    """

    import copy

    s=''

    x=copy.deepcopy(cfg['version'])

    for q in x:
        if s!='': s+='.'
        s+=str(q)

    return {'return':0, 'version':x, 'version_str':s}

##############################################################################
# Generate temporary files
#
# TARGET: end users

def gen_tmp_file(i):
    """
    Input:  {
              (suffix)     - temp file suffix
              (prefix)     - temp file prefix
              (remove_dir) - if 'yes', remove dir
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              file_name    - temp file name 
            }

    """

    xs=i.get('suffix','')
    xp=i.get('prefix','')
    s=i.get('string','')

    import tempfile
    fd, fn=tempfile.mkstemp(suffix=xs, prefix=xp)
    os.close(fd)
    os.remove(fn)

    if i.get('remove_dir','')=='yes':
       fn=os.path.basename(fn)

    return {'return':0, 'file_name':fn}

##############################################################################
# Get host platform (currently win or linux) and OS bits
#
# TARGET: end users

def get_os_ck(i):
    """
    Input:  {
              (bits)      - force OS bits
            }

    Output: {
              return      - return code =  0
              platform    - 'win' or 'linux'
              bits        - OS bits in string: 32 or 64
              python_bits - Python installation bits in string: 32 or 64

            }
    """

    import os
    import platform
    import struct

    pbits=str(8 * struct.calcsize("P"))

    plat='linux'
    if platform.system().lower().startswith('win'): # pragma: no cover
       plat='win'

    obits=i.get('bits','')
    if obits=='':
       obits='32'
       if plat=='win':
          # Trying to get fast way to detect bits
          if os.environ.get('ProgramW6432','')!='' or os.environ.get('ProgramFiles(x86)','')!='': # pragma: no cover
             obits='64'
       else:
          # On Linux use first getconf LONG_BIT and if doesn't work use python bits

          obits=pbits

          r=gen_tmp_file({})
          if r['return']>0: return r
          fn=r['file_name']

          cmd='getconf LONG_BIT > '+fn
          rx=os.system(cmd)
          if rx==0:
             r=load_text_file({'text_file':fn, 
                               'delete_after_read':'yes'})
             if r['return']==0:
                s=r['string'].strip()
                if len(s)>0 and len(s)<4:
                   obits=s

    return {'return':0, 'platform':plat, 'bits':obits, 'python_bits':pbits}

##############################################################################
# Generate CK UID
#
# TARGET: end users

def gen_uid(i):
    """
    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              data_uid     - UID in string format (16 characters 0..9,a..f)
            }
    """

    import uuid
    import random

    uid=str(uuid.uuid4().hex)

    if len(uid)!=32:
       return {'return':1, 'error':'problem generating UID : len='+str(len(uid))+' !=32'} # pragma: no cover 

    random.seed

    x=random.randrange(0,16)
    return {'return':0, 'data_uid':uid[x:x+16]}

##############################################################################
# Check if string is CK UID
#
# TARGET: end users

def is_uid(str):
    """
    Input:  string to check

    Output: True if UID, otherwise False
    """

    import re

    if len(str)!=16:
       return False

    pattern = r'[^\.a-f0-9]'
    if re.search(pattern, str.lower()):
        return False

    return True

##############################################################################
# Check if string is correct CK UOA 
#   (i.e. does not have special characters including *, ?)
#
# TARGET: end users

def is_uoa(str):
    """
    Input:  string to check

    Output: True if allowed UOA, False otherwise
    """

    if str.find(cfg['detect_cur_cid'])>=0 or str.find(cfg['detect_cur_cid1'])>=0: return False
    if str.find('*')>=0: return False
    if str.find('?')>=0: return False

    return True

##############################################################################
# Prepare special info about entry (engine used, author, date, etc)
#
# TARGET: CK kernel and low-level developers

def prepare_special_info_about_entry(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              dict         - dict with info
            }
    """

    # Add control info
    d={'engine':'CK',
       'version':cfg['version']}

    if cfg.get('default_developer','')!='':
       d['author']=cfg['default_developer']

    if cfg.get('default_developer_email','')!='':
       d['author_email']=cfg['default_developer_email']

    if cfg.get('default_developer_webpage','')!='':
       d['author_webpage']=cfg['default_developer_webpage']

    if cfg.get('default_license','')!='':
       d['license']=cfg['default_license']

    if cfg.get('default_copyright','')!='':
       d['copyright']=cfg['default_copyright']

    r=get_current_date_time({})
    d['iso_datetime']=r['iso_datetime']

    return {'return':0, 'dict': d}

##############################################################################
# Convert string of a special format to json
#
# TARGET: end users

def convert_json_str_to_dict(i):
    """
    Input:  {
              str                      - string (use ' instead of ", i.e. {'a':'b'} 
                                         to avoid issues in CMD in Windows and Linux!)

              (skip_quote_replacement) - if 'yes', do not make above replacement
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              dict         - dict from json file
            }
    """

    s=i['str']

    if i.get('skip_quote_replacement','')!='yes':
       s=s.replace('"', '\\"')
       s=s.replace('\'', '"')

    try:
       d=json.loads(s, encoding='utf8')
    except Exception as e:
       return {'return':1, 'error':'problem converting text to json ('+format(e)+')'}

    return {'return':0, 'dict': d}



##############################################################################
def load_json_file(i):
    import ck.files
    return ck.files.load_json_file(i)

##############################################################################
def save_json_to_file(i):
    import ck.files
    return ck.files.save_json_to_file(i)


##############################################################################
def load_yaml_file(i):
    import ck.files
    return ck.files.load_yaml_file(i)

##############################################################################
def save_yaml_to_file(i):
    import ck.files
    return ck.files.save_yaml_to_file(i)


##############################################################################
def load_text_file(i):
    import ck.files
    return ck.files.load_text_file(i)

##############################################################################
def save_text_file(i):
    import ck.files
    return ck.files.save_text_file(i)









##############################################################################
# Substitute string in file
#
# TARGET: end users

def substitute_str_in_file(i):
    """
    Input:  {
              filename - file
              string1  - string to be replaced
              string2  - replace string
            }

    Output: {
              return       - return code =  0, if successful
                                         = 16, if file not found
                                         >  0, if error
              (error)  - error text if return > 0
            }
    """

    fn=i['filename']
    s1=i['string1']
    s2=i['string2']

    # Load text file (unicode)
    r=load_text_file({'text_file':fn})
    if r['return']>0: return r

    # Replace
    x=r['string']
    x=x.replace(s1,s2)

    # Save text file (unicode)
    r=save_text_file({'text_file':fn, 'string':x})
    if r['return']>0: return r

    return {'return':0}



##############################################################################
# Deprecated
def dumps_json(i):
    import ck.strings
    return ck.strings.dump_json(i)

##############################################################################
def dump_json(i):
    import ck.strings
    return ck.strings.dump_json(i)

##############################################################################
def copy_to_clipboard(i): # pragma: no cover 
    import ck.strings
    return ck.strings.copy_to_clipboard(i)



##############################################################################
# Merge intelligently dict1 with dict2 key by key in contrast with dict1.update(dict2)
#
# TARGET: end users

def merge_dicts(i):
    """
    Input:  {
              dict1 - merge this dict with dict2 (will be directly modified!)
              dict2 - dict

    Output: {
              return       - return code =  0, if successful

              dict1        - output dict
            }
    """

    a=i['dict1']
    b=i['dict2']

    for k in b:
        v=b[k]
        if type(v) is dict:
           if k not in a:
              a.update({k:b[k]})
           elif type(a[k])==dict:
              merge_dicts({'dict1':a[k], 'dict2':b[k]})
           else:
              a[k]=b[k]
        elif type(v) is list:
           a[k]=[]
           for y in v:
               a[k].append(y)
        else:
           a[k]=b[k]

    return {'return':0, 'dict1':a}

##############################################################################
# Convert file to upload string
#
# TARGET: end users

def convert_file_to_upload_string(i):
    """
    Input:  {
              filename - file name to convert
            }

    Output: {
              return              - return code =  0, if successful
                                                >  0, if error
              (error)             - error text if return > 0
              file_content_base64 - string that can be transmitted through Internet
            }
    """

    import base64

    fn=i['filename']

    if not os.path.isfile(fn):
       return {'return':1, 'error':'file '+fn+' not found'}

    s=b''
    try:
       f=open(fn, 'rb')
       while True:
          x = f.read(32768);
          if not x: break
          s+=x
       f.close()
    except Exception as e:
       return {'return':1, 'error':'error reading file ('+format(e)+')'}

    s=base64.urlsafe_b64encode(s).decode('utf8')

    return {'return':0, 'file_content_base64': s}

##############################################################################
# Convert upload string to file
#
# TARGET: end users

def convert_upload_string_to_file(i):
    """
    Input:  {
              file_content_base64 - string transmitted through Internet
              (filename)          - file name to write (if empty, generate tmp file)
            }

    Output: {
              return              - return code =  0, if successful
                                                >  0, if error
              (error)             - error text if return > 0
              filename            - filename with full path
              filename_ext        - filename extension
            }
    """

    import base64

    x=i['file_content_base64']

    fc=base64.urlsafe_b64decode(str(x)) # convert from unicode to str since base64 works on strings
                                        # should be safe in Python 2.x and 3.x

    fn=i.get('filename','')

    if fn=='':
       rx=gen_tmp_file({'prefix':'tmp-'})
       if rx['return']>0: return rx
       px=rx['file_name']
    else:
       px=fn

    fn1, fne = os.path.splitext(px)

    if os.path.isfile(px):
       return {'return':1, 'error':'file already exists in the current directory'}
    try:
       fx=open(px, 'wb')
       fx.write(fc)
       fx.close()
    except Exception as e:
       return {'return':1, 'error':'problem writing file='+px+' ('+format(e)+')'}

    return {'return':0, 'filename':px, 'filename_ext': fne}

##############################################################################
# Input JSON from console (double enter to finish)
#
# TARGET: end users

def input_json(i):
    """
    Input:  {
              text - text to print
            }

    Output: {
              return              - return code =  0, if successful
                                                >  0, if error
              (error)             - error text if return > 0

              string
              dict                - parsed JSON
            }
    """


    t=i['text']

    out(t)

    s=''

    while True:
       r=inp({'text':''})
       if r['return']>0: return r
       ss=r['string'].strip()
       if ss=='': break
       s+=ss

    s=s.strip()

    if s=='': s='{}' # empty json
    else:
       if not s.startswith('{'): s='{'+s
       if not s.endswith('}'): s+='}'

    r=convert_json_str_to_dict({'str':s, 'skip_quote_replacement':'yes'})
    if r['return']>0: return r

    d=r['dict']

    return {'return':0, 'string': s, 'dict':d}

##############################################################################
# Convert CK list to CK dict with unicode in UTF-8 (unification of interfaces)
#
# TARGET: CK kernel and low-level developers

def convert_ck_list_to_dict(i):
    """
    Input:  [ 
              CK list: see 'action' function from this kernel
            ]

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              ck_dict      - {
                               "action":action
                               "cid":module_uoa or CID (x means that it may not be really CID 
                                       and has to be processed specially
                               "cids":[cid1, cid2, cid3, ...]
                               "key1":value1
                               "key2":value2
                               ...
                               "key10":""
                               "key11":value11
                               keys/values from file_json; if file extension is .tmp, 
                                                           it will be deleted after read!
                               keys/values from cmd_json
                               "unparsed":unparsed_cmd
                             }

    """
    obj={}
    obj['cids']=[]

    l=len(i)

    if l>0: obj['action']=i[0]

    module_uoa_or_cid=''

    # Parsing
    cx=True # Start first processing CIDs and then turn it off when something else is encountered

    if l>1:
       for x in range(1, len(i)):
           p=i[x].rstrip()

           #####################################
           if p=='--':
              cx=False
              p2=i[x+1:]
              obj['unparsed']=p2
              break

           #####################################
           elif p.startswith('--'):
              cx=False

              p=p[2:]
              p1=p 
              p2='yes'
              q=p.find("=")
              if q>0:
                 p1=p[0:q]
                 if len(p)>q:
                   p2=p[q+1:]
              obj[p1]=p2

           #####################################
           elif p.startswith('-'):
              cx=False

              p=p[1:]
              p1=p 
              p2='yes'
              q=p.find("=")
              if q>0:
                 p1=p[0:q]
                 if len(p)>q:
                   p2=p[q+1:]
              obj[p1]=p2

           #####################################
           elif p.startswith("@@@"):
              cx=False
              jd=p[3:]
              if len(jd)<3:
                 return {'return':1, 'error':'can\'t parse command line option '+p}

              y=convert_json_str_to_dict({'str':jd})
              if y['return']>0: return y

              merge_dicts({'dict1':obj, 'dict2':y['dict']})

           #####################################
           elif p.startswith("@@"):
              cx=False
              key=p[2:]

              x='Add JSON to input'
              if key!='': x+=' for key "'+key+'"'
              x+=' (double Enter to stop):\n'

              rx=input_json({'text':x})
              if rx['return']>0: return rx

              dy=rx['dict']

              dx=obj
              if key!='':
                 if key not in obj: obj[key]={}
                 dx=obj[key]

              merge_dicts({'dict1':dx, 'dict2':dy})

           #####################################
           elif p.startswith("@"):
              cx=False

              name=p[1:]
              if len(name)<2:
                 return {'return':1, 'error':'can\'t parse command line option '+p}

              y=load_json_file({'json_file':name})
              if y['return']>0: return y

              if name.endswith('.tmp'):
                 os.remove(name)   

              merge_dicts({'dict1':obj, 'dict2':y['dict']})

           #####################################
           elif p.find('=')>=0:
              cx=False

              p1=p 
              p2=''
              q=p.find("=")
              if q>0:
                 p1=p[0:q]
                 if len(p)>q:
                   p2=p[q+1:]
              obj[p1]=p2
           #####################################
           else:
              # If no module_uoa_or_cid -> set it
              if module_uoa_or_cid=='': 
                 module_uoa_or_cid=p
              else:
                 # Otherwise add to CIDs
                 obj['cids'].append(p)

    if module_uoa_or_cid!='': obj['cid']=module_uoa_or_cid

    return {'return':0, 'ck_dict':obj}

##############################################################################
# Init CK (current instance - has state!)
#
# TARGET: internal use

def init(i): # pragma: no cover
    """
    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """

    global cfg, work, initialized, paths_repos, type_long, string_io, log_ck_entries

    if initialized:
       return {'return':0}

    # Add this path to syspath to be able to call other modules
    this_kernel_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.insert(0, this_kernel_dir)

    # Split version
    cfg['version']=__version__.split('.')

    # Default URL. FIXME: should be formed from wfe_host and wfe_port when they are known.
    # cfg['wfe_url_prefix'] = 'http://%s:%s/web?' % (cfg['default_host'], cfg['default_port'])

    # Check long/int types
    try:
       x=long
    except Exception as e:
       type_long=int
    else:
       type_long=long

    # Import StringIO
    if sys.version_info[0]>2:
       import io
       string_io=io.StringIO
    else:
       from StringIO import StringIO
       string_io=StringIO

    # Check where are repos (to keep compatibility with past CK < V1.5)
    p=''

    searched_places=[]

    import inspect
    pxx=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    px=os.path.dirname(pxx)
    py=os.path.join(pxx, cfg['subdir_default_repo'])
    searched_places.append(py)
    if os.path.isdir(py):
       p=py

    if p=='':
       from distutils.sysconfig import get_python_lib
       px=get_python_lib()
       py=os.path.join(px, cfg['kernel_dir'], cfg['subdir_default_repo'])
       searched_places.append(py)
       if os.path.isdir(py):
          p=py

    if p=='':
       import site
       for px in site.getsitepackages():
           py=os.path.join(px, cfg['kernel_dir'],cfg['subdir_default_repo'])
           searched_places.append(py)
           if os.path.isdir(py):
              p=py
              break

    # Check CK_ROOT environment variable
    s=os.environ.get(cfg['env_key_root'],'').strip()
    if s!='':
       work['env_root']=os.path.realpath(s)

       for px in cfg['kernel_dirs']:
           searched_places.append(py)
           py=os.path.join(work['env_root'], px, cfg['subdir_default_repo'])
           if os.path.isdir(py):
              p=py
              break
    elif px!='':
      work['env_root']=px

    # Get home user directory
    from os.path import expanduser
    home=expanduser("~")

    # Check default repo
    x=os.environ.get(cfg['env_key_default_repo'],'').strip()

    if x!='' and os.path.isdir(x):
       work['dir_default_repo']=x
    else:
       if p=='':
          # Attempt to find in userspace (since V1.11.2.1)
          x=os.path.join(home, '.ck', __version__, cfg['subdir_default_repo'])
          if os.path.isfile(os.path.join(x, cfg['repo_file'])):
             p=x

       if p=='':
          return {'return':1, 'error':'Unusual CK installation detected since we can\'t find the CK package path with the default repo (searched in '+str(searched_places)+'). It often happens when you install CK under root while other tools (which use CK) under user and vice versa.  Please reinstall other tools that use CK in the same way as CK (root or user). If the problem persists, please report to the author (Grigori.Fursin@cTuning.org).'}

       work['dir_default_repo']=p

    work['dir_default_repo_path']=os.path.join(work['dir_default_repo'], cfg['module_repo_name'], cfg['repo_name_default'])
    work['dir_default_kernel']=os.path.join(work['dir_default_repo'], cfg['subdir_kernel'])
    work['dir_default_cfg']=os.path.join(work['dir_default_kernel'], cfg['subdir_kernel_default'], cfg['subdir_ck_ext'], cfg['file_meta'])

    work['dir_work_repo']=work['dir_default_repo']
    work['dir_work_repo_path']=work['dir_default_repo_path']
    work['dir_work_kernel']=work['dir_default_kernel']
    work['dir_work_cfg']=work['dir_default_cfg']

    if os.path.isfile(work['dir_default_cfg']):
       r=load_json_file({'json_file':work['dir_default_cfg']})
       if r['return']>0: return r
       cfg1=r['dict']

       # Update cfg
       r=merge_dicts({'dict1':cfg, 'dict2':cfg1})
       if r['return']>0: return r

    work['repo_name_work']=cfg['repo_name_default']
    work['repo_uid_work']=cfg['repo_uid_default']

    # Check external repos
    rps=os.environ.get(cfg['env_key_repos'],'').strip()
    if rps=='': 
       # In the original version, if path to repos was not defined, I was using CK path,
       # however, when installed as root, it will fail
       # rps=os.path.join(work['env_root'],cfg['subdir_default_repos'])
       # hence I changed to <user home dir>/CK
       rps=os.path.join(home, cfg['user_home_dir_ext'])
       if not os.path.isdir(rps):
          os.makedirs(rps)

    work['dir_repos']=rps

    # Check CK_LOCAL_REPO environment variable - if doesn't exist, create in user space
    s=os.environ.get(cfg['env_key_local_repo'],'').strip()

    if s=='':
       # Set up local default repository
       s=os.path.join(rps, cfg['repo_name_local'])
       if not os.path.isdir(s):
          os.makedirs(s)

          # Create description
          rq=save_json_to_file({'json_file':os.path.join(s,cfg['repo_file']),
                                'dict':{'data_alias':cfg['repo_name_local'],
                                        'data_uoa':cfg['repo_name_local'],
                                        'data_name':cfg['repo_name_local'],
                                        'data_uid':cfg['repo_uid_local']},
                                'sort_keys':'yes'})
          if rq['return']>0: return rq

    if s!='':
       work['local_kernel_uoa']=cfg['subdir_kernel_default']
       x=os.environ.get(cfg['env_key_local_kernel_uoa'],'').strip()
       if x!='': work['local_kernel_uoa']=x

       work['dir_local_repo']=os.path.realpath(s)
       work['dir_local_repo_path']=os.path.join(work['dir_local_repo'], cfg['module_repo_name'], cfg['repo_name_local'])
       work['dir_local_kernel']=os.path.join(work['dir_local_repo'], cfg['subdir_kernel'])
       work['dir_local_cfg']=os.path.join(work['dir_local_kernel'], work['local_kernel_uoa'], cfg['subdir_ck_ext'], cfg['file_meta'])

       # Update work repo!
       work['dir_work_repo']=work['dir_local_repo']
       work['dir_work_repo_path']=work['dir_local_repo_path']
       work['dir_work_kernel']=work['dir_local_kernel']
       work['dir_work_cfg']=work['dir_local_cfg']

       work['repo_name_work']=cfg['repo_name_local']
       work['repo_uid_work']=cfg['repo_uid_local']

       paths_repos.append({'path':work['dir_local_repo'],
                           'repo_uoa':cfg['repo_name_local'],
                           'repo_uid':cfg['repo_uid_local'],
                           'repo_alias':cfg['repo_name_local']})

    paths_repos.append({'path':work['dir_default_repo'],
                        'repo_uoa':cfg['repo_name_default'],
                        'repo_uid':cfg['repo_uid_default'],
                        'repo_alias':cfg['repo_name_default']})

    # Prepare repo cache
    work['dir_cache_repo_uoa']=os.path.join(work['dir_work_repo'],cfg['file_cache_repo_uoa'])
    work['dir_cache_repo_info']=os.path.join(work['dir_work_repo'],cfg['file_cache_repo_info'])

    # Check if first time and then copy local cache files (with remote-ck)
    if not os.path.isfile(work['dir_cache_repo_uoa']) and not os.path.isfile(work['dir_cache_repo_info']):
       rx=load_text_file({'text_file':os.path.join(work['dir_default_repo'],cfg['file_cache_repo_uoa'])})
       if rx['return']>0: return rx
       x1=rx['string']

       rx=load_text_file({'text_file':os.path.join(work['dir_default_repo'],cfg['file_cache_repo_info'])})
       if rx['return']>0: return rx
       x2=rx['string']

       rx=save_text_file({'text_file':work['dir_cache_repo_info'], 'string':x2})
       if rx['return']>0: return rx

       rx=save_text_file({'text_file':work['dir_cache_repo_uoa'], 'string':x1})
       if rx['return']>0: return rx

    # Check if local configuration exists, and if not, create it
    if not os.path.isfile(work['dir_local_cfg']):
       # Create empty local configuration
       rx=add({'repo_uoa':cfg['repo_name_local'],
               'module_uoa':cfg['subdir_kernel'],
               'data_uoa':work['local_kernel_uoa']})
       if rx['return']>0:
          return {'return':rx['return'],
                  'error':'can\'t create local configuration entry'}

    # Read kernel configuration (if exists)
    if os.path.isfile(work['dir_work_cfg']):
       r=load_json_file({'json_file':work['dir_work_cfg']})
       if r['return']>0: return r
       cfg1=r['dict']

       # Update cfg
       r=merge_dicts({'dict1':cfg, 'dict2':cfg1})
       if r['return']>0: return r

    # Check if need to log CK entries
    if cfg.get('log_ck_entries','')!='':
       log_ck_entries=True

    initialized=True

    return {'return':0}

##############################################################################
# List all files recursively in a given directory
#
# TARGET: CK kernel and low-level developers

def list_all_files(i):
    """
    Input:  {
              path               - top level path
              (file_name)        - search for a specific file name
              (pattern)          - return only files with this pattern
              (path_ext)         - path extension (needed for recursion)
              (limit)            - limit number of files (if directories with a large number of files)
              (number)           - current number of files
              (all)              - if 'yes' do not ignore special directories (like .cm)
              (ignore_names)     - list of names to ignore
              (ignore_symb_dirs) - if 'yes', ignore symbolically linked dirs 
                                   (to avoid recursion such as in LLVM)
              (add_path)         - if 'yes', add path
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              list         - dictionary of all files:
                               {"file_with_full_path":{"size":.., "path":..}
              sizes        - sizes of files (the same order)
              number       - number of files in a current directory (needed for recursion)
            }
    """

    number=0
    if i.get('number','')!='': 
       number=int(i['number'])

    inames=i.get('ignore_names',[])

    fname=i.get('file_name','')

    limit=-1
    if i.get('limit','')!='': 
       limit=int(i['limit'])

    a={} 

    iall=i.get('all','')

    pe=''
    if i.get('path_ext','')!='': 
       pe=i['path_ext']

    po=i.get('path','')
    if sys.version_info[0]<3: po=unicode(po)

    pattern=i.get('pattern','')
    if pattern!='':
       import fnmatch

    xisd=i.get('ignore_symb_dirs','')
    isd=False
    if xisd=='yes': isd=True

    ap=i.get('add_path','')

    try:
       dirList=os.listdir(po)
    except Exception as e:
        None
    else:
        for fn in dirList:
            p=os.path.join(po, fn)
            if iall=='yes' or fn not in cfg['special_directories']:
               if len(inames)==0 or fn not in inames:
                  if os.path.isdir(p):
                     if not isd or os.path.realpath(p)==p:
                        r=list_all_files({'path':p, 'all':iall, 'path_ext':os.path.join(pe, fn),
                                          'number':str(number), 'ignore_names':inames, 'pattern':pattern,
                                          'file_name':fname, 'ignore_symb_dirs':xisd, 'add_path':ap, 'limit': limit})
                        if r['return']>0: return r
                        a.update(r['list'])
                  else:
                     add=True

                     if fname!='' and fname!=fn:
                        add=False

                     if pattern!='' and not fnmatch.fnmatch(fn, pattern):
                        add=False

                     if add:
                        pg=os.path.join(pe, fn)
                        if os.path.isfile(p):
                           a[pg]={'size':os.stat(p).st_size}

                           if ap=='yes': a[pg]['path']=po

                  number=len(a)
                  if limit!=-1 and number>=limit:
                     break

    return {'return':0, 'list':a, 'number':str(number)}

##############################################################################
# Download entry from remote host (experimental)
#
# TARGET: end users
def download(i):
    """
    Input:  {
              (repo_uoa)   
              (module_uoa) 
              (data_uoa)  

              (new_repo_uoa)   - new repo UOA; "local" by default

              (skip_module_check) - if 'yes', do not check if module for a given component exists
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    smc=(i.get('skip_module_check','')=='yes')

    # Check components to skip
    if muoa in ['repo', 'befd7892b0d469e9',
                'env', '9b9b3208ac44b891', 
                'kernel', 'b1e99f6461424276',
                'cfg', 'b34231a3467566f8']:
       return {'return':0}

    if muoa=='':
       return {'return':1, 'error':'module UOA is not defined'}

    if duoa=='': duoa='*'
#       return {'return':1, 'error':'data UOA is not defined'}

    nruoa=i.get('new_repo_uoa','')
    if nruoa=='': nruoa='local'

    # Check if writing to new repo is allowed
    r=find_path_to_repo({'repo_uoa':nruoa})
    if r['return']>0: return r

    nruoa=r['repo_uoa']
    nruid=r['repo_uid']
    nrd=r['dict']

    npath=r['path']

    ii={'repo_uoa':nruoa, 'repo_uid':nruid, 'repo_dict':nrd}
    r=check_writing(ii)
    if r['return']>0: return r

    rz={'return':0}

    if o=='con':
#       out('')
       out('  WARNING: downloading missing CK component "'+muoa+':'+duoa+'" from the cKnowledge.io portal ...')

    # Import modules compatible with Python 2.x and 3.x
    import urllib

    try:    import urllib.request as urllib2
    except: import urllib2

    try:    from urllib.parse import urlencode
    except: from urllib import urlencode

    # Prepare dict to send to CK portal
    ii={
        'action':'download',
        'dict':{
                'module_uoa':muoa,
                'data_uoa':duoa
               }
       }

    # Prepare post variables
    r=dumps_json({'dict':ii, 'skip_indent':'yes'})
    if r['return']>0: return r

    s=r['string']
    if sys.version_info[0]>2: s=s.encode('utf8')

    # Prepare request
    request = urllib2.Request(cfg['cknowledge_api'], s, {'Content-Type': 'application/json'})

    # Connect
    try:
       f=urllib2.urlopen(request)
    except Exception as e:
       return {'return':1, 'error':'Access to the CK portal failed ('+format(e)+')'}

    # Read from Internet
    try:
       s=f.read()
       f.close()
    except Exception as e:
       return {'return':1, 'error':'Failed reading stream from the CK portal ('+format(e)+')'}

    # Check output
    try: s=s.decode('utf8')
    except Exception as e: pass

    # Try to convert output to dictionary
    r=convert_json_str_to_dict({'str':s, 'skip_quote_replacement':'yes'})
    if r['return']>0: 
       return {'return':1, 'error':'can\'t parse output from the CK portal ('+r['error']+'):\n'+s[:256]+'\n\n...)'}

    d=r['dict']

    if 'return' in d: 
       d['return']=int(d['return'])
    else:
       return {'return':99, 'error':'repsonse doesn\'t follow the CK API standard'}

    if d['return']>0:
       if d['return']!=16:
          return {'return':d['return'], 'error':d['error']}
       out('      Warning: component not found')
       return {'return':0}

    nlst=d.get('components',[])

    # Check if module:module there (bootstrapping)
    lst1=[]
    lst=[]
    path_to_module=''
    for q in nlst:
        nmuoa=q['module_uoa']
        nmuid=q['module_uid']
        nduoa=q['data_uoa']
        nduid=q['data_uid']

        if nmuoa=='module' and nduoa=='module':
           out('      Bootstrapping '+nmuoa+':'+nduoa+' ...')

           # TBD: Check split dirs in local repo...
           iii={'path':npath, 'data_uoa':'module', 'data_uid':nduid}
           rz=find_path_to_entry(iii)
           if rz['return']>0 and rz['return']!=16: return rz
           elif rz['return']==16:
              rz=create_entry(iii)
              if rz['return']>0: return rz

           npath2=rz['path']

           iii={'path':npath2, 'data_uoa':'module', 'data_uid':nduid}
           rz=find_path_to_entry(iii)
           if rz['return']>0 and rz['return']!=16: return rz
           elif rz['return']==16:
              rz=create_entry(iii)
              if rz['return']>0: return rz

           path_to_module=rz['path']

           lst.append(q)
        else:
           lst1.append(q)

    lst+=lst1

    # Recording downloaded components
    for q in lst:
        # Get UOA
        nmuoa=q['module_uoa']
        nmuid=q['module_uid']
        nduoa=q['data_uoa']
        nduid=q['data_uid']

        file_url=q['file_url']
        file_md5=q['file_md5']

        out('      Downloading and extracting '+nmuoa+':'+nduoa+' ...')

        # Check that module:module exists
        if nmuoa=='module' and nduoa=='module' and path_to_module!='':
           new_path=path_to_module
        else:
           if not smc:
              save_state=cfg['download_missing_components']
              cfg['download_missing_components']='no'

              rz=access({'action':'find',
                         'module_uoa':'module',
                         'data_uoa':'module',
                         'common_func':'yes'})
              if rz['return']>0 and rz['return']!=16: return rz

              if rz['return']==16:
                 rz=download({'repo_uoa':nruoa,
                              'module_uoa':'module',
                              'data_uoa':'module',
                              'skip_module_check':'yes'})
                 if rz['return']>0: return rz

              cfg['download_missing_components']=save_state

           # Adding dummy module
           rz=access({'action':'add',
                      'module_uoa':nmuoa,
                      'module_uid':nmuoa,
                      'data_uoa':nduoa,
                      'data_uid':nduid,
                      'repo_uoa':'local',
                      'common_func':'yes'})
           if rz['return']>0:
              out('        Skipping ...')
              continue

           new_path=rz['path']

        # Prepare pack
        ppz=os.path.join(new_path, 'pack.zip')

        if os.path.isfile(ppz):
           os.remove(ppz)

        # Download file
        # Import modules compatible with Python 2.x and 3.x
        import urllib

        try:    from urllib.request import urlretrieve
        except: from urllib import urlretrieve

        # Connect
        try:
           urlretrieve(file_url, ppz)
        except Exception as e:
           return {'return':1, 'error':'download failed ('+format(e)+')'}

        statinfo = os.stat(ppz)
        file_size=statinfo.st_size

        # MD5 of the pack
        rx=load_text_file({'text_file':ppz, 'keep_as_bin':'yes'})
        if rx['return']>0: return rx
        bpack=rx['bin']

        import hashlib
        md5=hashlib.md5(bpack).hexdigest()

        if md5!=file_md5:
           return {'return':1, 'error':'MD5 of the newly created pack ('+md5+') did not match the one from the portal ('+file_md5+')'}

        # Unzipping archive
        import zipfile

        new_f=open(ppz, 'rb')
        new_z=zipfile.ZipFile(new_f)

        for new_d in new_z.namelist():
            if new_d!='.' and new_d!='..' and not new_d.startswith('\\'):
               new_pp=os.path.join(new_path,new_d)
               if new_d.endswith('/'): 
                  if not os.path.exists(new_pp): os.makedirs(new_pp)
               else:
                  new_ppd=os.path.dirname(new_pp)
                  if not os.path.exists(new_ppd): os.makedirs(new_ppd)

                  # extract file
                  new_fo=open(new_pp, 'wb')
                  new_fo.write(new_z.read(new_d))
                  new_fo.close()
        new_f.close()

        # Remove pack file
        os.remove(ppz)

    return {'return':0}

##############################################################################
# Reload repo cache 
#
# TARGET: CK kernel and low-level developers

def reload_repo_cache(i):
    """
    Input:  {
              (force)      - if 'yes', force recaching
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """

    global cache_repo_uoa, cache_repo_info, paths_repos_all, cache_repo_init

    if i.get('force','')=='yes': # pragma: no cover
       cache_repo_init=False
       paths_repos_all=[]

    if not cache_repo_init:
       # Load repo UOA -> UID disambiguator
       r=load_json_file({'json_file':work['dir_cache_repo_uoa']})
       if r['return']!=16 and r['return']>0: return r
       cache_repo_uoa=r.get('dict',{})

       # Load cached repo info
       r=load_json_file({'json_file':work['dir_cache_repo_info']})
       if r['return']!=16 and r['return']>0: return r
       cache_repo_info=r.get('dict',{})

       # Prepare all paths
       for q in cache_repo_info:
           qq=cache_repo_info[q]
           dd=qq['dict']
           p=dd.get('path','')
           if p!='':
              paths_repos_all.append({'path':os.path.normpath(p),
                                      'dict': dd, # Added in version 1.11.2.1 to support dir split per repo
                                      'repo_uoa':qq['data_uoa'],
                                      'repo_uid':qq['data_uid'],
                                      'repo_alias':qq['data_alias']})

    cache_repo_init=True

    return {'return':0}

##############################################################################
# Save repo cache 
#
# TARGET: CK kernel and low-level developers

def save_repo_cache(i):
    """
    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """

    r=save_json_to_file({'json_file':work['dir_cache_repo_uoa'], 'dict':cache_repo_uoa})
    if r['return']>0: return r

    r=save_json_to_file({'json_file':work['dir_cache_repo_info'], 'dict':cache_repo_info})
    if r['return']>0: return r

    return {'return':0}

##############################################################################
# Load repo from cache
#
# TARGET: CK kernel and low-level developers

def load_repo_info_from_cache(i):
    """
    Input:  {
              repo_uoa - repo_uoa
            }

    Output: {
              return       - return code =  0, if successful
                                           16, if repo not found (may be warning)
                                         >  0, if error
              (error)      - error text if return > 0

              repo_uoa     - repo UOA
              repo_uid     - repo UID
              repo_alias   - repo alias

              all other info from repo dict
            }
    """

    ruoa=i['repo_uoa']
    ruid=ruoa

    if cfg.get('force_lower','')=='yes':
       ruoa=ruoa.lower()
       ruid=ruid.lower()

    if ruoa==cfg['repo_name_default'] or ruoa==cfg['repo_uid_default']:
       d={}
       d["path_to_repo_desc"]=work['dir_default_repo_path']
       d["data_uid"]=cfg['repo_uid_default']
       d["data_alias"]=cfg['repo_name_default']
       d["data_uoa"]=cfg['repo_name_default']
       d["dict"]={"default":"yes"}
    elif ruoa==cfg['repo_name_local'] or ruoa==cfg['repo_uid_local']:
       d={}
       d["path_to_repo_desc"]=work['dir_local_repo_path']
       d["data_uid"]=cfg['repo_uid_local']
       d["data_alias"]=cfg['repo_name_local']
       d["data_uoa"]=cfg['repo_name_local']
       d["dict"]={"default":"yes"}
    else:
       r=reload_repo_cache({}) # Ignore errors
       if r['return']>0: return r

       if not is_uid(ruoa): 
          ruid=cache_repo_uoa.get(ruoa,'')
          if ruid=='':
             return {'return':1, 'error':'repository "'+ruoa+'" was not found in the cache. Check if repository exists or try "ck recache repo"'}

       d=cache_repo_info.get(ruid,{})
       if len(d)==0:
          return {'return':1, 'error':'repository was not found in the cache'}

    r={'return':0}
    r.update(d)

    return r

##############################################################################
# Find repo by path
#
# TARGET: CK kernel and low-level developers

def find_repo_by_path(i):
    """
    Input:  {
              path - path to repo
            }

    Output: {
              return       - return code =  0, if successful
                                           16, if repo not found (may be warning)
                                         >  0, if error
              (error)      - error text if return > 0

              repo_uoa     - repo UOA
              repo_uid     - repo UID
              repo_alias   - repo alias
            }
    """

    p=i['path']
    if p!='': p=os.path.normpath(p)

    dd={}

    found=False
    if p==work['dir_default_repo']:
       uoa=cfg['repo_name_default']
       uid=cfg['repo_uid_default']
       alias=uoa
       found=True
    elif p==work['dir_local_repo']:
       uoa=cfg['repo_name_local']
       uid=cfg['repo_uid_local']
       alias=uoa
       found=True
    else:
       r=reload_repo_cache({}) # Ignore errors
       if r['return']>0: return r

       for q in cache_repo_info:
           qq=cache_repo_info[q]
           dd=qq['dict']
           if p==dd.get('path',''):
              uoa=qq['data_uoa']
              uid=qq['data_uid']
              alias=uid
              if not is_uid(uoa): alias=uoa
              found=True
              break

    if not found:
       return {'return':16, 'error': 'repository not found in this path'}

    return {'return':0, 'repo_uoa': uoa, 'repo_uid': uid, 'repo_alias':alias, 'repo_dict':dd}

##############################################################################
# Find path to a given repo
#
# TARGET: end users

def find_path_to_repo(i):
    """
    Input:  {
              (repo_uoa) - repo UOA; if empty, get the default repo
            }

    Output: {
              return       - return code =  0, if successful
                                           16, if repo not found (may be warning)
                                         >  0, if error
              (error)      - error text if return > 0

              dict         - dict from cache
              path         - path to repo

              repo_uoa     - repo UOA
              repo_uid     - repo UID
              repo_alias   - repo alias
            }
    """

    a=i.get('repo_uoa','')

    if cfg.get('force_lower','')=='yes':
       a=a.lower()

    ai=a

    pr=''
    if a!='':
       if a==cfg['repo_name_default'] or a==cfg['repo_uid_default']:
          pr=work['dir_default_repo']
          uoa=cfg['repo_name_default']
          uid=cfg['repo_uid_default']
          alias=uoa
          dt={}
       elif a==cfg['repo_name_local'] or a==cfg['repo_uid_local']:
          pr=work['dir_local_repo']
          uoa=cfg['repo_name_local']
          uid=cfg['repo_uid_local']
          alias=uoa
          dt={}
       else:
          # Reload cache if not initialized
          r=reload_repo_cache({}) # Ignore errors
          if r['return']>0: return r

          if not is_uid(a):
             ai=cache_repo_uoa.get(a,'')
             if ai=='':
                return {'return':1, 'error':'repository "'+a+'" was not found in cache'}

          cri=cache_repo_info.get(ai, {})
          if len(cri)==0:
             return {'return':1, 'error':'repository "'+ai+'" was not found in cache'}

          dt=cri.get('dict',{})
          pr=dt.get('path','')

          uoa=cri['data_uoa']
          uid=cri['data_uid']
          alias=cri['data_alias']

    else:
       # Get current repo path
       pr=work['dir_work_repo']
       uoa=work['repo_name_work']
       uid=work['repo_uid_work']
       alias=uoa
       dt={}

    return {'return':0, 'path':pr, 'repo_uoa':uoa, 'repo_uid':uid, 'repo_alias':alias, 'dict':dt}

##############################################################################
# Find path to data (first search in default repo, then local one and then all other repos)
#
# TARGET: CK kernel and low-level developers

def find_path_to_data(i):
    """
    Input:  {
              (repo_uoa) - repo UOA
              module_uoa - module UOA
              data_uoa   - data UOA
            }

    Output: {
              return       - return code =  0, if successful
                                           16, if data not found (may be warning)
                                         >  0, if error
              (error)      - error text if return > 0
              path         - path to data
              path_module  - path to module entry with this entry
              path_repo    - path to the repository of this entry
              repo_uoa     - repo UOA 
              repo_uid     - repo UID
              repo_alias   - repo alias
              module_uoa   - module UOA 
              module_uid   - module UID
              module_alias - module alias
              uoa          - data UOA
              uid          - data UID
              alias        - data alias
            }
    """
    muoa=i['module_uoa']
    muid='?'
    duoa=i['data_uoa']
    duid='?'

    ruoa=i.get('repo_uoa','')
    ruid=''
    ralias=''
    if ruoa!='':
       r=find_path_to_repo({'repo_uoa':ruoa})
       if r['return']>0: return r
       ps=[r]
       qmax=1
    else:
       ps=paths_repos
       qmax=2

    # Search
    found=False

    pr=''
    pm=''
    pd=''

    for q in range(0,qmax):
        if found: break

        if q==1:
           # Check / reload all repos
           r=reload_repo_cache({}) # Ignore errors
           if r['return']>0: return r
           ps=paths_repos_all

        for prx in ps:
            pr=prx['path']
            ruoa=prx['repo_uoa']
            ruid=prx['repo_uid']
            ralias=prx['repo_alias']
            r=find_path_to_entry({'path':pr, 'data_uoa':muoa})
            if r['return']>0 and r['return']!=16: return r
            elif r['return']==0:
               muoa=r['data_uoa']
               muid=r['data_uid']
               malias=r['data_alias']
               pm=r['path']

               # Check if there is a split of directories for this module in local config
               # to handle numerous entries (similar to MediaWiki)
               split_dirs=get_split_dir_number(prx.get('dict',{}), muid, muoa)

               iii={'path':pm, 'data_uoa':duoa}
               if split_dirs!=0:
                  iii['split_dirs']=split_dirs

               r1=find_path_to_entry(iii)
               if r1['return']>0 and r1['return']!=16: return r1
               elif r1['return']==0:
                  found=True
                  pd=r1['path']
                  duoa=r1['data_uoa']
                  duid=r1['data_uid']
                  dalias=r1['data_alias']
                  break

               if found: break

    if not found:
       s=''
#       if ruoa!='': s+=ruoa+':'
       s+=muoa+':'+duoa+'" ('
       if ruoa!='': 
#          if ruid!='':s+=ruid+':'
#          else: s+='?:'
          s+='?:'
       s+=muid+':'+duid+')'

       return {'return':16, 'error':'can\'t find path to CK entry "'+s}

#    # Get info about repo
#    if ruid=='':
#       r=find_repo_by_path({'path':pr})
#       if r['return']>0: return r
#       ruoa=r['repo_uoa']
#       ruid=r['repo_uid']
#       ralias=r['repo_alias']
#       qmax=1

    # Check logging of repo:module:uoa to be able to rebuild CK dependencies
    if log_ck_entries:
       lce=cfg.get('log_ck_entries','')
       if lce!='':
          rl=save_text_file({'text_file':lce,
                             'string':'"action":"find", "repo_uoa":"'+
                                      ruoa+'", "repo_uid":"'+
                                      ruid+'", "module_uoa":"'+
                                      muoa+'", "module_uid":"'+
                                      muid+'", "data_uoa":"'+
                                      duoa+'", "data_uid":"'+
                                      duid+'"\n',
                             'append':'yes'})
          if rl['return']>0: return rl


    return {'return':0, 'path':pd, 'path_module':pm, 'path_repo':pr,
                        'repo_uoa':ruoa, 'repo_uid':ruid, 'repo_alias':ralias,
                        'module_uoa':muoa, 'module_uid':muid, 'module_alias':malias,
                        'data_uoa':duoa, 'data_uid':duid, 'data_alias':dalias}

##############################################################################
# Find path to an UOA entry (check UID or alias)
#
# TARGET: CK kernel and low-level developers

def find_path_to_entry(i):
    """
    Input:  {
              path         - (str) path to a repository
              data_uoa     - (str) data UOA
              (split_dirs) - (int/str) number of first characters to split directory into subdirectories
                                       to be able to handle many entries (similar to Mediawiki)
            }

    Output: {
              return       - return code =  0, if successful
                                           16, if data not found (may be warning)
                                         >  0, if error
              (error)      - error text if return > 0

              path         - path to data entry
              data_uid     - data uid (from UOA)
              data_alias   - data alias (from UOA)
              data_uoa     - data alias or data uid, if data alias==''
            }
    """

    p=i['path']
    duoa=i['data_uoa']
    if cfg.get('force_lower','')=='yes':
       duoa=duoa.lower()

    if duoa=='': # pragma: no cover
       raise Exception('data_uoa is empty')

    split_dirs=safe_int(i.get('split_dirs',0),0)

    # Check split
    pp=p

    # Disambiguate UOA
    alias=''
    if is_uid(duoa):
       # If UID
       uid=duoa

       # Check if alias exists
       p1=os.path.join(pp, cfg['subdir_ck_ext'], cfg['file_alias_u'] + uid)
       found_alias=False
       if os.path.isfile(p1):
          try:
             f=open(p1)
             alias=f.readline().strip()
             f.close()
             found_alias=True
          except Exception as e:
             None

       # If alias exists, check directory with alias
       if found_alias:
          sd1,sd2=split_name(alias, split_dirs)
          if sd2!='': # otherwise name is smaller than the split number
             p=os.path.join(p,sd1)

          p2=os.path.join(p, alias)
          return {'return':0, 'path':p2, 'data_uid':uid, 'data_alias':alias, 'data_uoa':alias}

       sd1,sd2=split_name(uid, split_dirs)
       if sd2!='': # otherwise name is smaller than the split number
          p=os.path.join(p,sd1)

       p2=os.path.join(p, uid)
       if os.path.isdir(p2):
          return {'return':0, 'path':p2, 'data_uid':uid, 'data_alias':'', 'data_uoa':uid}

       return {'return':-1}

    sd1,sd2=split_name(duoa, split_dirs)
    if sd2!='': # otherwise name is smaller than the split number
       p=os.path.join(p,sd1)

    # If alias
    alias=duoa

    p1=os.path.join(p, alias)
    if sys.version_info[0]<3: 
       try: p1=p1.encode('utf8')
       except Exception as e: pass
    if os.path.isdir(p1):
       # Check uid for this alias
       p2=os.path.join(pp, cfg['subdir_ck_ext'], cfg['file_alias_a'] + alias)
       try:
          f=open(p2)
          uid=f.readline().strip()
          f.close()
       except Exception as e:
          return {'return':10, 'error':'inconsistent entry: alias "'+alias+'" exists, but not the UID in file '+p2, 
                               'path':p1, 'data_alias':alias}

       return {'return':0, 'path':p1, 'data_uid':uid, 'data_alias':alias, 'data_uoa':alias}

    return {'return':16, 'error':'can\'t find path to CK entry'}

##############################################################################
# Load meta description from a path
#
# TARGET: CK kernel and low-level developers

def load_meta_from_path(i):
    """
    Input:  {
              path           - path to a data entry

              (skip_updates) - if 'yes', do not load updates
              (skip_desc)    - if 'yes', do not load descriptions
            }

    Output: {
              return         - return code =  0, if successful
                                           >  0, if error
              (error)        - error text if return > 0

              dict           - dict with meta description
              path           - path to json file with meta description

              (info)         - dict with info if exists
              (path_info)    - path to json file with info

              (updates)      - dict with updates if exists
              (path_updates) - path to json file with updates
              (path_desc)    - path to json file with API description
            }
    """

    p=i['path']

    slu=i.get('skip_updates','')
    sld=i.get('skip_desc','')

    p1=os.path.join(p, cfg['subdir_ck_ext'], cfg['file_meta'])
    if not os.path.isfile(p1):
       p1=os.path.join(p, cfg['subdir_ck_ext'], cfg['file_meta_old']) # For compatibility with cM
       if not os.path.isfile(p1):
          p1=''

    if p1!='':
       rx={'return':0}

       r=load_json_file({'json_file':p1})
       if r['return']>0: return r
       rx['path']=p1
       rx['dict']=r['dict']

       # Check info file
       p2=os.path.join(p, cfg['subdir_ck_ext'], cfg['file_info'])
       if os.path.isfile(p2):
          r=load_json_file({'json_file':p2})
          if r['return']>0: return r
          rx['path_info']=p2
          rx['info']=r['dict']

       # Check updates file
       if slu!='yes':
          p3=os.path.join(p, cfg['subdir_ck_ext'], cfg['file_updates'])
          if os.path.isfile(p3):
             r=load_json_file({'json_file':p3})
             if r['return']>0: return r
             rx['path_updates']=p3
             rx['updates']=r['dict']

       # Check desc file
       if sld!='yes':
          p4=os.path.join(p, cfg['subdir_ck_ext'], cfg['file_desc'])
          if os.path.isfile(p4):
             r=load_json_file({'json_file':p4})
             if r['return']>0: return r
             rx['path_desc']=p4
             rx['desc']=r['dict']

       return rx
    else:
       return {'return':1, 'error':'meta description is not found in path '+p}

##############################################################################
# Load (CK) python module
#
# TARGET: end users

def load_module_from_path(i):
    """
    Input:  {
              path             - module path
              module_code_name - module name
              (cfg)            - configuration of the module if exists ...
              (skip_init)      - if 'yes', skip init
              (data_uoa)       - module UOA (useful when printing error)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              code         - python code object
              path         - full path to the module
              cuid         - internal UID of the module
            }
    """

    p=i['path']
    n=i['module_code_name']

    xcfg=i.get('cfg',None)

    # Find module
    try:
       x=imp.find_module(n, [p])
    except ImportError as e: # pragma: no cover
       return {'return':1, 'error':'can\'t find module code (path='+p+', name='+n+', err='+format(e)+')'}

    ff=x[0]
    full_path=x[1]

    # Check if code has been already loaded
    if full_path in work['cached_module_by_path'] and work['cached_module_by_path_last_modification'][full_path]==os.path.getmtime(full_path):
       ff.close()
       # Code already loaded 
       return work['cached_module_by_path'][full_path]

    # Check if has dependency on specific CK kernel version
    if xcfg!=None:
       kd=xcfg.get('min_kernel_dep','')
       if kd!='':
          rx=check_version({'version':kd})
          if rx['return']>0: return rx

          ok=rx['ok']
          version_str=rx['current_version']

          if ok!='yes':
             return {'return':1, 'error':'module "'+i.get('data_uoa','')+'" requires minimal CK kernel version '+kd+' while your version is '+version_str} 

    # Generate uid for the run-time extension of the loaded module 
    # otherwise modules with the same extension (key.py for example) 
    # will be reloaded ...

    r=gen_uid({})
    if r['return']>0: return r
    ruid='rt-'+r['data_uid']

    try:
       c=imp.load_module(ruid, ff, full_path, x[2])
    except ImportError as e: # pragma: no cover
       return {'return':1, 'error':'can\'t load module code (path='+p+', name='+n+', err='+format(e)+')'}

    x[0].close()

    # Initialize module with this CK instance 
    c.ck=sys.modules[__name__]
    if xcfg!=None: c.cfg=xcfg

    # Initialize module
    if i.get('skip_init','')!='yes':
       # Check if init function exists
       if getattr(c, 'init')!=None:
          r=c.init(i)
          if r['return']>0: return r

    r={'return':0, 'code':c, 'path':full_path, 'cuid':ruid}

    # Cache code together with its time of change
    work['cached_module_by_path'][full_path]=r
    work['cached_module_by_path_last_modification'][full_path]=os.path.getmtime(full_path)

    return r

##############################################################################
# Perform remote action via CK web service
#
# TARGET: CK kernel and low-level developers

def perform_remote_action(i):
    """
    Input:  { See 'perform_action' function }
    Output: { See 'perform_action' function }
    """

    # Import modules compatible with Python 2.x and 3.x
    import urllib

    try:    import urllib.request as urllib2
    except: import urllib2 # pragma: no cover

    try:    from urllib.parse import urlencode
    except: from urllib import urlencode # pragma: no cover

    rr={'return':0}

    # Get action
    act=i.get('action','')

    # Check output
    o=i.get('out','')

    if o=='con':
#       out('Initiating remote access ...')
#       out('')
       i['out']='con'
       i['quiet']='yes'
       if act=='pull':
          i['out']='json'
    else:
       i['out']='json'

#    # Clean up input
#    if o!='json_file': 
#       rr['out']='json' # Decided to return json to show that it's remote ...

    if 'cid' in i: 
       del(i['cid']) # already processed

    # Get URL
    url=i.get('remote_server_url','')

    # Process i
    if 'remote_server_url' in i: del(i['remote_server_url'])

    # Pre process if push file ...
    if act=='push':
       # Check file
       fn=i.get('filename','')
       if fn=='':
          x=i.get('cids',[])
          if len(x)>0:
             fn=x[0]

       if fn=='':
          return {'return':1, 'error':'filename is empty'}

       if not os.path.isfile(fn):
          return {'return':1, 'error':'file '+fn+' not found'}

       rx=convert_file_to_upload_string({'filename':fn})
       if rx['return']>0: return rx

       i['file_content_base64']=rx['file_content_base64']

       # Leave only filename without path
       i['filename']=os.path.basename(fn)

    # Prepare post variables
    r=dumps_json({'dict':i, 'skip_indent':'yes'})
    if r['return']>0: return r
    s=r['string'].encode('utf8')

    post=urlencode({'ck_json':s})
    if sys.version_info[0]>2: post=post.encode('utf8')

    # Check if skip SSL certificate
    ctx=None
    add_ctx=False

    if i.get('remote_skip_certificate_validation','')=='yes':
       del(i['remote_skip_certificate_validation'])

       import ssl

       ctx = ssl.create_default_context()
       ctx.check_hostname = False
       ctx.verify_mode = ssl.CERT_NONE

       add_ctx=True

    # If auth
    auth=None
    add_auth=False

    au=i.get('remote_server_user','')
    if au!='': 
       del(i['remote_server_user'])

       ap=i.get('remote_server_pass','')
       if ap!='': 
          del(i['remote_server_pass'])

       auth = urllib2.HTTPPasswordMgrWithDefaultRealm()
       auth.add_password(None, url, au, ap)

       add_auth=True

    # Prepare handler (TBD: maybe there is another, more elegant way?)
    if add_auth and add_ctx:
       urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(auth), urllib2.HTTPSHandler(context=ctx)))
    elif add_auth:
       urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(auth)))
    elif add_ctx:
       urllib2.install_opener(urllib2.build_opener(urllib2.HTTPSHandler(context=ctx)))

    # Prepare request
    request = urllib2.Request(url, post)

    # Connect
    try:
       f=urllib2.urlopen(request)
    except Exception as e:
       return {'return':1, 'error':'Access to remote CK repository failed ('+format(e)+')'}

    # Read from Internet
    try:
       s=f.read()
       f.close()
    except Exception as e:
       return {'return':1, 'error':'Failed reading stream from remote CK web service ('+format(e)+')'}

    # Check output
    try: s=s.decode('utf8')
    except Exception as e: pass
    if o=='con' and act!='pull':
       out(s.rstrip())
    else:
       # Try to convert output to dictionary
       r=convert_json_str_to_dict({'str':s, 'skip_quote_replacement':'yes'})
       if r['return']>0: 
          return {'return':1, 'error':'can\'t parse output from remote CK server ('+r['error']+'):\n'+s[:256]+'\n\n...)'}

       d=r['dict']

       if 'return' in d: d['return']=int(d['return']) # Fix for some strange behavior when 'return' is not integer - should check why ...

       if d.get('return',0)>0:
          return d

       # Post process if pull file ...
       if act=='pull':
          if o!='json' and o!='json_file':
             # Convert encoded file to real file ...
             x=d.get('file_content_base64','')

             fn=d.get('filename','')
             if fn=='': fn=cfg['default_archive_name']

             r=convert_upload_string_to_file({'file_content_base64':x, 'filename':fn})
             if r['return']>0: return r

             if 'file_content_base64' in d: del(d['file_content_base64'])

       rr.update(d)

    # Restore original output
    i['out']=o

    return rr

##############################################################################
# Perform action (find module or use kernel)
#
# TARGET: CK kernel and low-level developers

def perform_action(i):
    """
    Input:  {
              all parameters from function 'access'

              (web)         - if 'yes', called from the web

              (common_func) - if 'yes', ignore search for modules 
                                        and call common func from the CK kernel
                  or
              (kernel)

              (local)       - if 'yes', run locally even if remote repo ...
            }

    Output: {
              return  - return code =  0, if successful
                                         >  0, if error
              (error) - error text if return > 0

              (out)   - if action change output, return it
              Output from the module/action
            }
    """

    # Check action
    action=i.get('action','')
    if action=='':
       action='short_help'
    elif action=='-?' or action=='-h' or action=='--help':
       action='help'

    # Check web
    wb=i.get('web','')

    # Substitute # in CIDs
    cid=i.get('cid','')
    cids=i.get('cids',[])

    xout=i.get('out','')

    ruoa=''
    ruid=''

    repo_module_uoa=i.get('repo_module_uoa','')

    need_subst=False
    rc={} # If CID from current directory

    if cid.startswith(cfg['detect_cur_cid']) or cid.startswith(cfg['detect_cur_cid1']):
       need_subst=True
    else:
       for c in cids:
           if c.startswith(cfg['detect_cur_cid']) or c.startswith(cfg['detect_cur_cid1']): 
              need_subst=True
              break

    # If need to substitute #, attempt to detect current CID
    if need_subst:
       rc=detect_cid_in_current_path({})
       if rc['return']>0: return rc

    # Process cid (module or CID)
    module_uoa=cid
    if cid.find(':')>=0 or cid.startswith(cfg['detect_cur_cid']) or cid.startswith(cfg['detect_cur_cid1']):
       # Means that CID
       r=parse_cid({'cid':cid, 'cur_cid':rc})
       if r['return']>0: return r
       module_uoa=r.get('module_uoa','')

       duoa=r.get('data_uoa','')
       if duoa!='': i['data_uoa']=duoa

       ruoa=r.get('repo_uoa','')
       if ruoa!='': i['repo_uoa']=ruoa

    # If module_uoa exists in input, set module_uoa
    if i.get('module_uoa','')!='': module_uoa=i['module_uoa']
    i['module_uoa']=module_uoa

    # Check if repo exists and possibly remote!
    remote=False

    local=i.get('local','')

    rs=i.get('remote_server_url','')
    if rs=='': 
       ruoa=i.get('repo_uoa','')
       if ruoa!='' and ruoa.find('*')<0 and ruoa.find('?')<0:
          rq=load_repo_info_from_cache({'repo_uoa':ruoa})
          if rq['return']>0: return rq

          dd=rq.get('dict',{})
          if dd.get('remote','')=='yes' and local!='yes':
             rs=dd.get('url','')
             if rs=='':
                return {'return':1, 'error':'URL of remote repository is not defined'}

             i['remote_server_url']=rs

             if dd.get('remote_user','')!='':
                i['remote_server_user']=dd['remote_user']

             # It is completely unsave - just for proof of concept ...
             if dd.get('remote_password','')!='':
                i['remote_server_pass']=dd['remote_password']

             if dd.get('remote_skip_certificate_validation','')!='':
                i['remote_skip_certificate_validation']=dd['remote_skip_certificate_validation']

             if dd.get('remote_repo_uoa','')!='':
                i['repo_uoa']=dd['remote_repo_uoa']
             else:
                del (i['repo_uoa'])

             if i.get('remote_repo_uoa','')!='':
                i['repo_uoa']=i['remote_repo_uoa']
                del(i['remote_repo_uoa'])

    if rs!='' and local!='yes':
       return perform_remote_action(i)

    # Process and parse cids -> xcids
    xcids=[]

    for c in cids:
       r=parse_cid({'cid':c, 'cur_cid':rc, 'ignore_error':'yes'}) # here we ignore errors, since can be a file name, etc
       if r['return']>0: return r
       xcids.append(r)
    i['xcids']=xcids

    # Check if common function
    cf=i.get('common_func','')
    if cf=='': cf=i.get('common','') # making it easier to call it from the command line

    # Check if no module_uoa, not common function, then try to get module from current 
    module_detected_from_dir=False
    if not need_subst and cf!='yes' and module_uoa=='' and action not in cfg['common_actions']:
       rc=detect_cid_in_current_path({})
       if rc['return']==0:
          module_uoa=rc.get('module_uoa','')
          module_detected_from_dir=True

    display_module_uoa  = module_uoa
    default_action_name = None
    loaded_module       = None

    ## If a specific module_uoa was given (not a wildcard) :
    #
    if cf!='yes' and module_uoa!='' and module_uoa.find('*')<0 and module_uoa.find('?')<0:
       # Find module and load meta description
       rx=load({'repo_uoa':repo_module_uoa,
                'module_uoa':cfg['module_name'], 
                'data_uoa':module_uoa})
       if rx['return']>0: 
          if cfg.get('download_missing_components','')!='yes':
             return rx

          # Check if search in remote server ...
          restarted=False
          if rx['return']==16:
             xout2=''
             if xout=='con': xout2=xout

             # Try to download missing action/module
             ry=download({'module_uoa':cfg['module_name'],
                          'data_uoa':module_uoa,
                          'out':xout2})
             if ry['return']>0: return ry

             # Attempt to load module again
             rx=load({'module_uoa':cfg['module_name'], 
                      'data_uoa':module_uoa})
             if rx['return']>0: return rx

             restarted=True

             xout=''

             if xout=='con':
                out('')

          if not restarted:
             return rx

       xmodule_uoa=rx['data_uoa']
       xmodule_uid=rx['data_uid']
       display_module_uoa = '"{}"'.format(xmodule_uoa)
       if xmodule_uoa!=xmodule_uid:
          display_module_uoa += ' ({})'.format(xmodule_uid)

       # Check if allowed to run only from specific repos
       if cfg.get('allow_run_only_from_allowed_repos','')=='yes':# and cf!='yes':
          ruid=rx['repo_uid']

          if ruid not in cfg.get('repo_uids_to_allow_run',[]):
             return {'return':1, 'error':'executing commands is not allowed from this repository "'+ruid+'"'}

       u=rx['dict']
       p=rx['path']

       # Check logging of repo:module:uoa to be able to rebuild CK dependencies
       if log_ck_entries:
          lce=cfg.get('log_ck_entries','')
          if lce!='':
             rl=save_text_file({'text_file':lce,
                                'string':'"action":"'+action+'", "repo_uoa":"'+
                                         i.get('repo_uoa','')+'", "repo_module_uoa":"'+
                                         repo_module_uoa+'", "module_uoa":"'+
                                         xmodule_uoa+'", "module_uid":"'+
                                         xmodule_uid+'", "data_uoa":"'+
                                         i.get('data_uoa','')+'"\n',
                                'append':'yes'})
             if rl['return']>0: return rl

       declared_action      = action in u.get('actions',{})
       default_action_name  = u.get('default_action_name','')
       intercept_kernel     = i.get('{}.intercept_kernel'.format(module_uoa),'')

       if declared_action or default_action_name:
          # Load module
          mcn=u.get('module_name',cfg['module_code_name'])

          if i.get('module_version','')!='': 
             mcnv=i['module_version'].strip()
             if mcnv=='0': 
                mcnv=''
          else: 
             mcnv=u.get('module_version','')

          if mcnv!='':
             mcn+='.'+mcnv

          r=load_module_from_path({'path':p, 'module_code_name':mcn, 'cfg':u, 'data_uoa':rx['data_uoa']})
          if r['return']>0: return r

          loaded_module=r['code']
          loaded_module.work['self_module_uid']=rx['data_uid']
          loaded_module.work['self_module_uoa']=rx['data_uoa']
          loaded_module.work['self_module_alias']=rx['data_alias']
          loaded_module.work['path']=p

          action1=u.get('actions_redirect',{}).get(action,'')
          if action1=='': action1=action

          if i.get('help','')=='yes' or i.get('api','')=='yes':
             return get_api({'path':p, 'func':action1, 'out':xout})

          if wb=='yes' and (xout=='con' or xout=='web') and u.get('actions',{}).get(action,{}).get('for_web','')!='yes':
             return {'return':1, 'error':'this action is not supported in remote/web mode'}

          if declared_action:
              a=getattr(loaded_module, action1)
              return a(i)
          elif default_action_name and intercept_kernel:
              a=getattr(loaded_module, default_action_name)
              return a(i)
          # otherwise fall through and try a "special" kernel method first


    # Check if action == special keyword (add, delete, list, etc)
    if (module_uoa!='' and action in cfg['common_actions']) or \
       ((module_uoa=='' or module_detected_from_dir) and action in cfg['actions']):
       # Check function redirect - needed if action 
       #   is the same as internal python keywords such as list
       action1=cfg['actions_redirect'].get(action,'')
       if action1=='': action1=action

       if i.get('help','')=='yes' or i.get('api','')=='yes':
          return get_api({'path':'', 'func':action1, 'out':xout})

       if wb=='yes' and (xout=='con' or xout=='web') and cfg.get('actions',{}).get(action,{}).get('for_web','')!='yes':
          return {'return':1, 'error':'this action is not supported in remote/web mode '}

       a=getattr(sys.modules[__name__], action1)
       return a(i)

    if default_action_name:
       a=getattr(loaded_module, default_action_name)
       return a(i)

    # Prepare error
    if module_uoa=='':
       er='in kernel'
    else:
       er='in module '+display_module_uoa

    return {'return':1,'error':'action "'+action+'" not found '+er}

##############################################################################
# Print API from module for a given action #
#
# TARGET: CK kernel and low-level developers

def get_api(i):
    """
    Input:  {
              (path)       - path to module, if comes from access function
                or
              (module_uoa) - if comes from CMD

              (func)       - func for API

              (out)  - output
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              title        - title string
              desc         - original description
              module       - module name
              api          - api as string
              line         - line in found module
            }
    """

    p=i.get('path','')
    f=i.get('func','')
    o=i.get('out','')

    muoa=i.get('module_uoa','')

    t=''      # last function description (if redirect to another API)
    t_orig='' # original function description
    l=0       # API line
    a=''      # accumulated API

    if p=='' and muoa!='':
       rx=load({'module_uoa':cfg['module_name'], 
                'data_uoa':muoa})
       if rx['return']>0: return rx
       p=rx['path']

    if p=='':
       p1=os.path.dirname(os.path.dirname(work['dir_default_repo']))
       p=os.path.join(p1, cfg['file_kernel_py'])

       if not os.path.isfile(p):
          return {'return':1, 'error':'kernel not found in '+p}
    else:
       p=os.path.join(p, 'module.py')

    if os.path.isfile(p):
       rx=load_text_file({'text_file':p, 'split_to_list':'yes'})
       if rx['return']>0: return rx

       lst=rx['lst']

       k=-1
       while k<len(lst)-1:
             k+=1
             q=lst[k]

             if q.find('def '+f+'(')>=0 or q.find('def '+f+' (')>=0 or \
                q.find('def\t'+f+'(')>=0 or q.find('def\t'+f+' (')>=0:

                j=k-1
                if j>=0 and lst[j].strip()=='': j-=1

                x='x'
                while j>=0 and x!='' and not x.startswith('###'):
                  x=lst[j].strip()
                  if x!='' and not x.startswith('###'):
                     if x=='#': x=' '
                     elif x.startswith('# '): x=x[2:]
                     t=x+'\n'+t
                  j-=1

                if t!='':
                   l=j+2
                   if t_orig=='': t_orig=t 

                # Find starting point of an API
                j=k+1
                if j<len(lst) and lst[j].find('"""')>=0: 
                   j+=1

                # Check if redirect to another function
                restart=False
                if j<len(lst):
                   x=lst[j].strip()
                   if x.lower().startswith("see"):
                      z1=x.find('"')
                      if z1>0:
                         z2=x.find('"',z1+1)
                         if z2>0:
                            f=x[z1+1:z2] # new function name
                            k=-1
                            restart=True # restart search for new function
                   
                if not restart:
                   x=''
                   while x.find('"""')<0 and j<len(lst):
                       x=lst[j]
                       if x.find('"""')<0:
                          a+=x+'\n'
                       j+=1

    if t=='' and a=='':
       return {'return':1, 'error':'function not found'}

    dd=t_orig.strip()
    if o=='con':
       out('Description: '+dd)
       out('')
       out('Module: '+p)
       out('')
       out('Line: '+str(l))
       out('')
       out('API:')
       out(a)
    elif o=='web':
       out('<B>Function:</B> '+t+'<BR>')
       out('<BR>')
       out('<B>Module:</B> '+p+'<BR>')
       out('<BR>')
       out('<B>API:</B><BR>')
       out('<pre>')
       out(a)
       out('</pre><BR>')

    return {'return':0, 'title':t, 'desc':dd, 'module':p, 'api':a, 'line':l}

##############################################################################
# Convert CID to dict and add missing parts in CID with current path if #
#
# TARGET: CK kernel and low-level developers

def parse_cid(i):
    """
    Input:  {
              cid            - in format (REPO_UOA:)MODULE_UOA:DATA_UOA 
              (cur_cid)      - output of function 'detect_cid_in_current_path'
              (ignore_error) - if 'yes', ignore wrong format
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              data_uoa     - data UOA
              module_uoa   - module UOA
              (repo_uoa)   - repo UOA
            }
    """

    r={'return':0}
    c=i['cid'].strip()

    ie=i.get('ignore_error','')

    cc=i.get('cur_cid', {})

    a0=cc.get('repo_uoa','')
    m0=cc.get('module_uoa','')
    d0=cc.get('data_uoa','')

    if c.startswith(cfg['detect_cur_cid']) or c.startswith(cfg['detect_cur_cid1']):
       c=c[1:]

    x=c.split(':')
    if len(x)<2 and m0=='':
       if ie!='yes': 
          return {'return':1, 'error':'unknown CID format'}
       else: 
          return r

    if c=='':
       r['repo_uoa']=a0
       r['module_uoa']=m0
       r['data_uoa']=d0
    elif len(x)==1:
       if a0!='': r['repo_uoa']=a0
       r['module_uoa']=m0
       r['data_uoa']=x[0]
    elif len(x)==2:
       if a0!='': r['repo_uoa']=a0
       r['module_uoa']=x[0]
       r['data_uoa']=x[1]
    elif len(x)==3:
       r['repo_uoa']=x[0]
       r['module_uoa']=x[1]
       r['data_uoa']=x[2]
    else:
       if ie!='yes': 
          return {'return':1, 'error':'unknown CID format'}

    return r

##############################################################################
# Create an UOA entry in a given path
#
# TARGET: CK kernel and low-level developers

def create_entry(i):
    """
    Input:  {
              path         - path where to create an entry
              (split_dirs) - (int) number of first characters to split directory into subdirectories
                                   to be able to handle many entries (similar to Mediawiki)
              (data_uoa)   - data UOA
              (data_uid)   - if uoa is an alias, we can force data UID

              (force)      - if 'yes', force creation even if directory already exists

              (allow_multiple_aliases) - if 'yes', allow multiple aliases for the same UID 
                                         (needed for cKnowledge.io to publish
                                         renamed components with the same UID)
            }

    Output: {
              return       - return code =  0, if successful
                                           16, if data entry already exists
                                         >  0, if error
              (error)      - error text if return > 0

              path         - path to data entry
              data_uid     - data UID (from UOA)
              data_alias   - data alias (from UOA)
              data_uoa     - data alias or data uid if data alias==''
            }
    """

    p0=i.get('path','')
    d=i.get('data_uoa','')
    di=i.get('data_uid','')

    ama=(i.get('allow_multiple_aliases','')=='yes') # Experimental functionality for cKnowledge.io

    split_dirs=safe_int(i.get('split_dirs',0),0)

    xforce=i.get('force','')
    if xforce=='yes':
       force=True
    else:
       force=False

    # If no uoa, generate UID
    alias=''
    uid=''
    if d=='':
       if di=='':
          r=gen_uid({})
          if r['return']>0: return r
          uid=r['data_uid']
       else:
          uid=di

          # Check if already exists
          iii={'path':p0, 'data_uoa':uid}
          if split_dirs!=0:
             iii['split_dirs']=split_dirs
          r=find_path_to_entry(iii)
          if r['return']>0 and r['return']!=16: return r
          elif r['return']==0:
             r['return']=16
             return r

       alias=''
    else:
       # Check if already exists
       if not force:
          # Check if already exists
          iii={'path':p0, 'data_uoa':d}
          if split_dirs!=0:
             iii['split_dirs']=split_dirs
          r=find_path_to_entry(iii)
          if r['return']>0 and r['return']!=16: return r
          elif r['return']==0:
             r['return']=16
             return r

       if is_uid(d):
          uid=d
          alias=''
       else:
          alias=d
          if di!='':
             uid=i['data_uid']
          else: 
             r=gen_uid({})
             if r['return']>0: return r
             uid=r['data_uid']

    # Check dir name
    dir_name=(alias,uid) [alias=='']

    # Check split
    p00=p0
    sd1,sd2=split_name(dir_name, split_dirs)
    if sd2!='': # otherwise name is smaller than the split number
       p00=os.path.join(p0,sd1)

       # Create first split if doesn't exist
       if not os.path.isdir(p00):
          os.mkdir(p00)

    # Finalize path to entry
    p=os.path.join(p00, dir_name)

    # Check alias disambiguation
    if alias!='':
       p1=os.path.join(p0, cfg['subdir_ck_ext'])
       if not os.path.isdir(p1):
          # Create .cm directory
          try:    # pragma: no cover
             os.mkdir(p1)
          except Exception as e:
             return {'return':1, 'error':format(e)}

       # Check if alias->uid exist
       p3=os.path.join(p1, cfg['file_alias_a'] + alias)
       if os.path.isfile(p3):     # pragma: no cover
          try:
             fx=open(p3)
             uid1=fx.readline().strip()
             fx.close()
          except Exception as e:
             None

          if uid1!=uid:
             return {'return':1, 'error':'different alias->uid disambiguator already exists in '+p3}

       # Check if uid->alias exist
       xalias=alias
       p2=os.path.join(p1, cfg['file_alias_u'] + uid)
       if os.path.isfile(p2):     # pragma: no cover
          alias1=''
          alias1s=[]
          try:
             fx=open(p2)
             alias1=fx.read().strip()
             alias1s=alias1.split('\n')
             fx.close()
          except Exception as e:
             None

          if alias not in alias1s:
             if ama:
                xalias=alias+'\n'+alias1
             else:
                return {'return':1, 'error':'different uid->alias disambiguator already exists in '+p2}

       ru=save_text_file({'text_file':p3, 'string':uid+'\n'})
       if ru['return']>0: return ru

       ru=save_text_file({'text_file':p2, 'string':xalias+'\n'})
       if ru['return']>0: return ru

    # Create directory
    if not os.path.exists(p):
       try:
          os.mkdir(p)
       except Exception as e:
          return {'return':1, 'error':format(e)}

    uoa=uid
    if alias!='': uoa=alias

    return {'return':0, 'path':p, 'data_uid':uid, 'data_alias':alias, 'data_uoa':uoa}

##############################################################################
# Delete entry alias from path
#
# TARGET: CK kernel and low-level developers

def delete_alias(i):
    """
    Input:  {
              path         - path to the entry
              data_uid     - data UID
              (data_alias) - data alias
              (repo_dict)  - repo cfg if available to check sync
              (share)      - if 'yes', try to rm via GIT
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """

    rd=i.get('repo_dict',{})
    rshared=rd.get('shared','')
    rsync=rd.get('sync','')

    if i.get('share','')=='yes': rshared='git'

    p=i['path']
    alias=i.get('data_alias','')
    uid=''

    if alias!='' and os.path.isdir(p):
       p0=os.path.join(p, cfg['subdir_ck_ext'])

       p9=cfg['file_alias_a'] + alias
       p1=os.path.join(p0, p9)

       if rshared!='':
          ppp=os.getcwd()
          os.chdir(p0)

       if os.path.isfile(p1):
          try:
             f=open(p1)
             uid=f.readline().strip()
             f.close()
          except Exception as e:
             None

          if rshared!='':
             ss=cfg['repo_types'][rshared]['rm'].replace('$#files#$', p9)
             rx=os.system(ss)

          if os.path.isfile(p1): os.remove(p1)

       if uid=='': uid=i['data_uid']

       if uid!='':
          p9=cfg['file_alias_u'] + uid
          p1=os.path.join(p0, p9)
          if os.path.isfile(p1):
             # Check if multiple aliases
             delete=True

             alias1=''
             alias1s=[]
             try:
                fx=open(p1)
                alias1=fx.read().strip()
                alias1s=alias1.split('\n')
                fx.close()
             except Exception as e:
                None

             if len(alias1s)>1:
                delete=False
                alias1s.remove(alias)
                xalias='\n'.join(alias1s)

                # Update alias disambiguator
                ru=save_text_file({'text_file':p1, 'string':xalias})
                if ru['return']>0: return ru

             if delete:
                if rshared!='':
                   ss=cfg['repo_types'][rshared]['rm'].replace('$#files#$', p9)
                   rx=os.system(ss)

                if os.path.isfile(p1): 
                   os.remove(p1)

       if rshared!='':
          os.chdir(ppp)

    return {'return':0}

##############################################################################
# Delete a given directory with subdirectories (be careful)
#
# TARGET: CK kernel and low-level developers

def delete_directory(i):
    """
    Input:  {
              path - path to delete
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """

    import shutil

    p=i['path']

    if os.path.isdir(p):
       shutil.rmtree(p, onerror=rm_read_only)

    return {'return':0}

##############################################################################
# Convert dictionary into CK flat format
#
# TARGET: end users

def flatten_dict(i):
    """
    Any list item is converted to @number=value
    Any dict item is converted to #key=value
    # is always added at the beginning 

    Input:  {
              dict         - python dictionary

              (prefix)     - prefix (for recursion)

              (prune_keys) - list of keys to prune (can have wildcards)
            }

    Output: {
              return  - return code =  0, if successful
                                    >  0, if error
              (error) - error text if return > 0
              dict    - flattened dictionary
            }
    """

    prefix='#'
    if i.get('prefix','')!='': prefix=str(i['prefix'])

    a=i['dict']
    aa={}

    pk=i.get('prune_keys','')
    if pk=='': pk=[]

    flatten_dict_internal(a, aa, prefix, pk)

    return {'return':0, 'dict': aa}

##############################################################################
# Convert dictionary into CK flat format (internal, used for recursion)
#
# TARGET: internal use

def flatten_dict_internal(a, aa, prefix, pk):
    # Start flattening
    if type(a) is dict or type(a) is list:
       i=0
       for x in a:
           if type(a) is dict: 
              v=a[x] 
              prefix1=prefix+'#'+str(x)
           else: 
              prefix1=prefix+'@'+str(i)
              v=x
           if type(v) is dict or type(v) is list:
              flatten_dict_internal(v, aa, prefix1, pk)
           else:
              if flatten_dict_internal_check_key(prefix1, pk):
                 aa[prefix1]=v
           i+=1
    else:
       if flatten_dict_internal_check_key(prefix, pk):
          aa[prefix]=a

    return {'return':0, 'dict': a}

##############################################################################
# Convert dictionary into CK flat format (internal, used for recursion)
#
# TARGET: end users

def flatten_dict_internal_check_key(prefix, pk):
    import fnmatch

    add=False

    if len(pk)==0:
       add=True
    else:
       for c in pk:
           if '*' in c or '?' in c:
               if fnmatch.fnmatch(prefix,c):
                  add=True
                  break
           else:
              if prefix==c:
                 add=True
                 break

    return add

##############################################################################
# Get value from dict by flat key
#
# TARGET: end users

def get_by_flat_key(i):
    """
    Input:  {
              dict  - dictionary
              key   - flat key
            }

    Output: {
              return  - return code =  0, if successful
                                    >  0, if error
              (error) - error text if return > 0
              value   - value or None, if doesn't exist
            }
    """
    # Check vars
    v=None

    a=i['dict']
    k=i['key']

    # Remove leading # if exists
    if len(k)>0 and k[0:1]=='#': k=k[1:]

    k1=''
    kt='' # type '#' or '@'
    x=0
    finish=False

    while not finish:
        y=k[x]
        x+=1

        if y=='#' or y=='@':
           if kt=='#':
              if k1 not in a: break
              a=a[k1]
           elif kt=='@':
              if len(a)<=type_long(k1): break
              a=a[type_long(k1)]
           k1=''
           kt=y
        else:
           k1+=y

        if x>=len(k): break

    if k1!='' and kt!='':
       if kt=='#':   
          if k1 in a: v=a[k1]
       else:         
          if len(a)>type_long(k1): v=a[type_long(k1)]

    return {'return':0, 'value': v}

##############################################################################
# Set value in array using flattened key
#
# TARGET: end users

def set_by_flat_key(i):
    """

    Input:  {
              dict            - dict (it will be directly changed!)
              key             - flat key (or not if doesn't start with #)
              value           - value to set
            }

    Output: {
              return  - return code =  0, if successful
                                    >  0, if error
              (error) - error text if return > 0
              dict    - modified dict
            }
    """
    a=i['dict']
    k=i['key']
    v=i['value']

    # Remove leading # if there 
    if len(k)>0 and k[0:1]=='#': k=k[1:]

    k1=''
    kt='' # type '#' or '@'
    x=0
    finish=False

    while not finish:
        y=k[x]
        x+=1

        if y=='#' or y=='@':
           if kt=='#':
              if k1 not in a: 
                 if y=='#': a[k1]={}
                 else: a[k1]=[]
              a=a[k1]
           elif kt=='@':
              if len(a)<=type_long(k1):
                 for q in range(len(a)-1,type_long(k1)):
                     if y=='#': a.append({})
                     else: a.append([])
              a=a[type_long(k1)]
           k1=''
           kt=y
        else:
           k1+=y

        if x>=len(k): break

    if k1!='' and kt!='':
       if kt=='#':
          a[k1]=v
       else:
          if len(a)<=type_long(k1): 
             for q in range(len(a)-1,type_long(k1)):
                 if y=='#': a.append({})
                 else: a.append([])
          a[type_long(k1)]=v

    return {'return':0, 'dict': i['dict']}

##############################################################################
# Restore flattened dict
#
# TARGET: end users

def restore_flattened_dict(i):
    """
    Input:  {
              dict - flattened dict
            }

    Output: {
              return  - return code =  0, if successful
                                    >  0, if error
              (error) - error text if return > 0
              dict    - restored dict
            }
    """
    # Check vars
    a={} # default
    b=i['dict']
    first=True
    for x in b:
        if first: 
           first=False
           y=x[1:2]
           if y=='@': a=[]
           else: a={}

        set_by_flat_key({'dict':a, 'key':x, 'value':b[x]})

    return {'return':0, 'dict': a}

##############################################################################
# Set lock for path
#
# TARGET: CK kernel and low-level developers

def set_lock(i):
    """
    Input:  {
              path               - path to be locked

              (get_lock)         - if 'yes', lock this entry
              (lock_retries)     - number of retries to aquire lock (default=11)
              (lock_retry_delay) - delay in seconds before trying to aquire lock again (default=3)
              (lock_expire_time) - number of seconds before lock expires (default=30)

              (unlock_uid)       - UID of the lock to release it
            }

    Output: {
              return       - return code =  0, if successful
                                         = 32, couldn't acquire lock (still locked after all retries)
                                         >  0, if error
              (error)      - error text if return > 0

              (lock_uid)   - lock UID, if locked successfully
            }
    """
    p=i['path']

    gl=i.get('get_lock','')
    uuid=i.get('unlock_uid','')
    exp=float(i.get('lock_expire_time','30'))

    rr={'return':0}

    if gl=='yes' or uuid!='':
       pl=os.path.join(p, cfg['subdir_ck_ext'], cfg['file_for_lock'])

       luid=''
       if os.path.isfile(pl):
          import time

          # Read lock file
          try:
             f=open(pl)
             luid=f.readline().strip()
             exp=float(f.readline().strip())
             if exp<0: exp=1
             f.close()
          except Exception as e:
             return {'return':1, 'error':'problem reading lock file'}

          # Check if lock has expired
          if gl=='yes' and uuid=='':
             # Retry if locked
             retry=int(i.get('lock_retries','11'))
             retryd=float(i.get('lock_retry_delay','3'))

             dt=os.path.getmtime(pl)+exp-time.time()
             if dt>0: 
                while retry>0 and os.path.isfile(pl) and dt>0:
                   retry-=1
                   time.sleep(retryd)
                   if os.path.isfile(pl): 
                      dt=os.path.getmtime(pl)+exp-time.time()

                if retry==0 and dt>0 and os.path.isfile(pl):
                   return {'return':32, 'error':'entry is still locked'}

             luid=''
             if os.path.isfile(pl): os.remove(pl)

       # Release lock if requested (and if not locked by another UID)
       if luid!='' and uuid!='':
          if luid!=uuid:
             return {'return':32, 'error': 'entry is locked with another UID'}
          luid=''
          os.remove(pl)

       # Finish acquiring lock
       if gl=='yes':
          # (Re)acquire lock
          if uuid=='':
             r=gen_uid({})
             if r['return']>0: return r
             luid=r['data_uid']
          else:
             luid=uuid

          # Write lock file
          try:
             f=open(pl,'w')
             f.write(luid+'\n')
             f.write(str(exp)+'\n')
             f.close()
          except Exception as e:
             return {'return':1, 'error':'problem writing lock file'}

          rr['lock_uid']=luid

    return rr

##############################################################################
# Check if locked and unlock if needed
#
# TARGET: CK kernel and low-level developers

def check_lock(i):
    """
    Input:  {
              path               - path to be locked
              (unlock_uid)       - UID of the lock to release it
            }

    Output: {
              return       - return code =  0, if successful
                                         = 32, lock UID is not matching
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """
    p=i['path']
    uuid=i.get('unlock_uid','')

    pl=os.path.join(p, cfg['subdir_ck_ext'], cfg['file_for_lock'])

    luid=''
    if os.path.isfile(pl):
       import time

       # Read lock file
       try:
          f=open(pl)
          luid=f.readline().strip()
          exp=float(f.readline().strip())
          if exp<0: exp=1
          f.close()
       except Exception as e:
          return {'return':1, 'error':'problem reading lock file'}

       # Check if lock has expired
       dt=os.path.getmtime(pl)+exp-time.time()
       if dt<0: 
          # Expired
          if uuid=='' or uuid==luid:
             os.remove(pl)
          else:
             return {'return':32, 'error':'entry lock UID is not matching'}
       else:
          if uuid=='':
             return {'return':32, 'error':'entry is locked'}
          elif uuid!=luid:
             return {'return':32, 'error':'entry is locked with different UID'}

    elif uuid!='':
       return {'return':32, 'error':'lock was removed or expired'}

    return {'return':0}

##############################################################################
# Get current date and time
#
# TARGET: end users

def get_current_date_time(i):
    """
    Input:  {}

    Output: {
              return       - return code =  0

              array        - array with date and time
              iso_datetime - date and time in ISO format
            }
    """

    import datetime

    a={}

    now1=datetime.datetime.now()
    now=now1.timetuple()

    a['date_year']=now[0]
    a['date_month']=now[1]
    a['date_day']=now[2]
    a['time_hour']=now[3]
    a['time_minute']=now[4]
    a['time_second']=now[5]

    return {'return':0, 'array':a, 'iso_datetime':now1.isoformat()}

##############################################################################
###########################################################
# Detect CID of the current directory (repository entry)
#
# TARGET: CK kernel and low-level developers

def detect_cid_in_current_path(i):
    """
    Input:  {
              (path)     - path, otherwise current directory
            }

    Output: {
              return         - return code =  0, if successful
                                           >  0, if error
              (error)        - error text if return > 0

              repo_uoa       - repo UOA
              repo_uid       - repo UID
              repo_alias     - repo alias
              (module_uoa)   - module UOA
              (module_uid)   - module UID
              (module_alias) - module alias
              (data_uoa)     - data UOA
              (data_uid)     - data UID
              (data_alias)   - data alias
            }
    """

    p=i.get('path','')
    if p=='': p=os.getcwd()
    p=os.path.normpath(p)

    dirs=[]
    p1=''
    pr='*'
    found=False

    while pr!='':
       p1=os.path.join(p, cfg['repo_file'])

       if os.path.isfile(p1): 
          found=True
          break

       p2=os.path.split(p)
       p=p2[0]
       pr=p2[1]
       dirs.append(pr)

    if not found:
       return {'return':16, 'error':'repository is not detected in the current path'}

    # Find info about repo (prepared as return dict)
    r=find_repo_by_path({'path':p})
    if r['return']>0: return r

    repo_dict=r.get('repo_dict',{})

    # Check info about module
    ld=len(dirs)

    if ld>0:
       m=dirs[ld-1]

       split_dirs=0
       rx=find_path_to_entry({'path':p, 'data_uoa':m})
       if rx['return']>0 and rx['return']!=16: return rx
       elif rx['return']==0:
          r['module_uoa']=rx['data_uoa']
          r['module_uid']=rx['data_uid']
          r['module_alias']=rx['data_alias']

          muid=rx['data_uid']
          muoa=rx['data_uoa']

          # Check if there is a split of directories for this module in local config
          # to handle numerous entries (similar to MediaWiki)
          split_dirs=get_split_dir_number(repo_dict, muid, muoa)

       # Check info about data
       if ld>1:
          d=dirs[ld-2]
          iii={}

          if split_dirs!=0:
             d=dirs[ld-3]
             iii['split_dirs']=split_dirs

          iii['path']=os.path.join(p,m)
          iii['data_uoa']=d

          rx=find_path_to_entry(iii)
          if rx['return']>0 and rx['return']!=16: return rx
          elif rx['return']==0:
             r['data_uoa']=rx['data_uoa']
             r['data_uid']=rx['data_uid']
             r['data_alias']=rx['data_alias']

    return r

# **************************************************************************
# Actions, visible outside through module '*' such as [ck uid] or [ck uid *]
# **************************************************************************

############################################################
# Action: generate CK UID
#
# TARGET: end users

def uid(i):
    """
    Input:  {}

    Output: {
              Output from 'gen_uid' function
            }

    """

    o=i.get('out','')

    r=gen_uid({})
    if r['return']>0: return r

    if o=='con':
       out(r['data_uid'])

    return r

############################################################
# Action: print CK version
#
# TARGET: end users

def version(i):
    """
    Input:  {}

    Output: {
              output from function 'get_version'
            }

    """

    o=i.get('out','')

    r=get_version({})
    if r['return']>0: return r
    version_str=r['version_str']

    if o=='con':
       out('V'+version_str)

    return r

############################################################
# Action: print python version used by CK
#
# TARGET: end users

def python_version(i):
    """
    Input:  {}

    Output: {
               version - sys.version
               version_info - sys.version_info
            }

    """

    import sys

    o=i.get('out','')

    v1=sys.version
    v2=sys.version_info

    if o=='con':
       out(v1)

    return {'return':0, 'version':v1, 'version_info':v2}

############################################################
# Action: check CK status
#
# TARGET: CK kernel and low-level developers

def status(i):
    """
    Input:  {}

    Output: {
              outdated     - if 'yes', newer version exists

              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    outdated=''

    o=i.get('out','')

    try:    import urllib.request as urllib2
    except: import urllib2

    try:    from urllib.parse import urlencode
    except: from urllib import urlencode

    page=''
    try:
       res=urllib2.urlopen(cfg['status_url'])
       page=res.read()
    except urllib2.HTTPError as e:
       return {'return':1, 'error':'Problem accessing server ('+format(e)+')'}
    except urllib2.URLError as e:
       return {'return':1, 'error':'Problem accessing server ('+format(e)+')'}

    # Support for Python 3
    if sys.version_info[0]>2:
       try: 
          page=page.decode('utf-8')
       except Exception as e: 
          pass

    if page!='':
       s1='version=\''
       i1=page.find(s1)
       if i1>0:
          i2=page.find('\'',i1+9)
          if i2>0:
             lversion_str=page[i1+len(s1):i2].strip()

             rx=check_version({'version':lversion_str})
             if rx['return']>0: return rx

             ok=rx['ok']
             version_str=rx['current_version']
             if ok!='yes':
                outdated='yes'

                if o=='con':
                   out('Your version is outdated: V'+version_str)
                   out('New available version   : V'+lversion_str)
                   u=cfg.get('ck_web','')
                   if u!='':
                      out('')
                      out('If you install CK via pip, upgrade it as follows (prefix with "sudo" on Linux):')
                      out(' $ pip install ck --upgrade')
                      out('')
                      out('If you use GitHub version, update CK kernel (and all other repositories) as follows:')
                      out(' $ ck pull all --kernel')
                      out('')
                      out('Visit '+u+' for more details!')

    if o=='con':
       if outdated!='yes':
          out('Your version is up-to-date: V'+version_str)
       elif outdated=='':
          out('Problem checking version ...')

    return {'return':0, 'outdated':outdated}

############################################################
# Compare versions 
#
# TARGET: CK kernel and low-level developers

def check_version(i):
    """
    Input:  {
              version      - your version (string)
            }

    Output: {
              return          - return code =  0

              ok              - if 'yes', your CK kernel version is outdated
              current_version - your CK kernel version
            }

    """

    ok='yes'

    r=get_version({})
    if r['return']>0: return r
    version=r['version']
    version_str=r['version_str']

    lversion_str=i['version'].replace('dev','.1') # for compatibility with older versions
    lversion=lversion_str.split('.')

    # Comparing
    for q in range(0, len(version)):
        if len(lversion)<=q:
            break

        v=version[q]
        lv=lversion[q]

        # try int first, then try string
        try:
           lv=int(lv)
           v=int(v)
        except Exception as e:
            pass

        if lv>v:
            ok='no'
            break

        if lv<v:
            break

    return {'return':0, 'ok':ok, 'current_version':version_str}

############################################################
# Convert info about entry to CID
#
# TARGET: CK kernel and low-level developers

def convert_entry_to_cid(i):
    """
    Input:  {
               (repo_uoa)   - Repo UOA
               (repo_uid)   - Repo UID
               (module_uoa) - Module UOA
               (module_uid) - Module UID
               (data_uoa)   - Data UOA
               (data_uid)   - Data UID
            }

    Output: {
              return       - return code =  0

              cuoa         - module_uoa:data_uoa           (substituted with ? if can't find)
              cid          - module_uid:data_uid           (substituted with ? if can't find)
              xcuoa        - repo_uoa:module_uoa:data_uoa  (substituted with ? if can't find)
              xcid         - repo_uid:module_uid:data_uid  (substituted with ? if can't find)
            }

    """

    xcuoa=''
    xcid=''

    if i.get('module_uoa','')!='': cuoa=i['module_uoa']
    else: cuoa='?'
    if i.get('module_uid','')!='': cid=i['module_uid']
    else: cid='?'

    cuoa+=':'
    cid+=':'

    if i.get('data_uoa','')!='': cuoa+=i['data_uoa']
    else: cuoa+='?'
    if i.get('data_uid','')!='': cid+=i['data_uid']
    else: cid+='?'

    if i.get('repo_uoa','')!='': xcuoa=i['repo_uoa']+':'+cuoa
    else: xcuoa='?:'+cuoa
    if i.get('repo_uid','')!='': xcid=i['repo_uid']+':'+cid
    else: xcid='?:'+cid

    r={'return':0}
    r['cuoa']=cuoa
    r['cid']=cid
    r['xcuoa']=xcuoa
    r['xcid']=xcid

    return r

# **************************************************************************
# Common actions (if not found in other modules, call these functions here)
# **************************************************************************

############################################################
# Special function: open webbrowser with help
#
# TARGET: CK kernel and low-level developers

def webhelp(i):
    """
    Input:  { from access function }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    a=i.get('repo_uoa','')
    m=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    url=cfg['wiki_data_web']

    if m!='':
       if duoa=='': 
          duoa=m
          m=cfg['module_name']

       r=find_path_to_data({'repo_uoa':a, 'module_uoa':m, 'data_uoa':duoa})
       if r['return']>0: return r
       p=r['path']

       muoa=r.get('module_uoa','')
       duoa=r.get('data_uoa','')

       rx=convert_entry_to_cid(r)
       if rx['return']>0: return rx

       cuoa=rx['cuoa']
       cid=rx['cid']
       xcuoa=rx['xcuoa']
       xcid=rx['xcid']

       # Prepare URL
       url+=muoa+':'+duoa #cid.replace(':','/')

    out('Opening web page '+url+' ...')

    import webbrowser
    webbrowser.open(url)

    return {'return':0}

############################################################
# Special function: open webbrowser with discussion wiki page for collaborative R&D
#  URL is taken from default kernel configuration cfg['wiki_data_web']
#
# TARGET: CK kernel and low-level developers

def wiki(i):
    """
    Input:  { 
               (repo_uoa)
               (module_uoa)
               (data_uoa)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    url=cfg['wiki_data_web']

    if muoa=='' or duoa=='':
       # Try to detect CID in current path
       rx=detect_cid_in_current_path({})
       if rx['return']==0:
          muoa=rx.get('module_uoa','')
          duoa=rx.get('data_uoa','')

    if muoa=='' or duoa=='':
       return guide({}) #{'return':1, 'error':'entry is not defined'}

    r=find_path_to_data({'repo_uoa':ruoa, 'module_uoa':muoa, 'data_uoa':duoa})
    if r['return']>0: return r

    rx=convert_entry_to_cid(r)
    if rx['return']>0: return rx

    cuoa=rx['cuoa']
    cid=rx['cid']
    xcuoa=rx['xcuoa']
    xcid=rx['xcid']

    # Prepare URL
    url+=cid.replace(':','_')

    out('Opening web page '+url+' ...')

    import webbrowser
    webbrowser.open(url)

    return {'return':0}

############################################################
# Special function: open webbrowser with private discussion wiki page for collaborative R&D
#  URL is taken from default kernel configuration cfg['private_wiki_data_web']
#
# TARGET: CK kernel and low-level developers

def pwiki(i):
    """
    Input:  { 
               (repo_uoa)
               (module_uoa)
               (data_uoa)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    url=cfg['private_wiki_data_web']

    if muoa=='' or duoa=='':
       # Try to detect CID in current path
       rx=detect_cid_in_current_path({})
       if rx['return']==0:
          muoa=rx.get('module_uoa','')
          duoa=rx.get('data_uoa','')

    if muoa=='' or duoa=='':
       return {'return':1, 'error':'entry is not defined'}

    r=find_path_to_data({'repo_uoa':ruoa, 'module_uoa':muoa, 'data_uoa':duoa})
    if r['return']>0: return r

    rx=convert_entry_to_cid(r)
    if rx['return']>0: return rx

    cuoa=rx['cuoa']
    cid=rx['cid']
    xcuoa=rx['xcuoa']
    xcid=rx['xcid']

    # Prepare URL
    url+=cid.replace(':','_')

    out('Opening web page '+url+' ...')

    import webbrowser
    webbrowser.open(url)

    return {'return':0}

############################################################
# Special function: open webbrowser with API, if exists
#
# TARGET: CK kernel and low-level developers

def webapi(i):
    """
    Input:  { from access function }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    url=cfg['api_web']

    if muoa=='':
       muoa=duoa

    if muoa=='':
       url+='ck_'+cfg['subdir_kernel']+'_api/html/kernel_8py.html'
    else:
       duoa=muoa
       muoa=cfg['module_name']

       r=load({'repo_uoa':ruoa, 'module_uoa':muoa, 'data_uoa':duoa})
       if r['return']>0: return r
       muoa=r['data_uoa']

       url+=muoa+'/#api'

    out('Opening web page '+url+' ...')

    import webbrowser
    webbrowser.open(url)

    return {'return':0}

############################################################
# Special function: open webbrowser with API, if exists
#
# TARGET: CK kernel and low-level developers

def browser(i):
    """
    Input:  {
              (template)   - use this web template
              (repo_uoa)   -
              (module_uoa) - 
              (data_uoa)   - view a given entry
              (extra_url)  - extra URL
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Check if ck-web is installed
    r=find({'module_uoa':'module',
            'data_uoa':'wfe'})
    if r['return']>0:
       if r['return']!=16: return r
 
       out('Seems like ck-web repository is not installed (can\'t find wfe module)!')
       out('Please, install it via "ck pull repo:ck-web" and try again!')

       return {'return':0}

    t=i.get('template','')

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    cid=''
    if duoa!='' or muoa!='' or ruoa!='':
       if ruoa!='': cid=ruoa+':'
       if muoa!='': cid+=muoa+':'
       if duoa!='': cid+=duoa

    # Starting web service and asking to open page
    return access({'action':'start', 'module_uoa':'web', 'browser':'yes', 
                   'template':t, 'cid':cid, 'extra_url':i.get('extra_url','')})

############################################################
# Special function: open webbrowser with user/developer guide wiki
#
# TARGET: CK kernel and low-level developers

def guide(i):
    """
    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    url=cfg['ck_web_wiki']

    out('Opening web page '+url+' ...')

    import webbrowser
    webbrowser.open(url)

    return {'return':0}

#########################################################
# Common action: print help for a given module
#
# TARGET: CK kernel and low-level developers

def help(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              help         - help text
            }

    """

    o=i.get('out','')

    m=i.get('module_uoa','')
    if m=='':
       m='<module_uoa>'

    h= 'Usage: '+cfg['cmd'].replace('$#module_uoa#$', m)+'\n'

    if m=='<module_uoa>':
       h+='\n'
       h+='  Common actions for all CK modules (unless overloaded):\n'

       for q in sorted(cfg['common_actions']):
           s=q
           desc=cfg['actions'][q].get('desc','')
           if desc!='': s+=' - '+desc
           h+='    * '+s+'\n'

       h+='\n'
       h+='  CK kernel actions:\n'

       for q in sorted(cfg['actions']):
           if q not in cfg['common_actions']:
              s=q
              desc=cfg['actions'][q].get('desc','')
              if desc!='': s+=' - '+desc
              h+='    * '+s+'\n'
    else:
       h+='\n'
       h+='  Available actions:\n\n'

       # Attempt to load 
       r=list_actions({'module_uoa':m}) 
       if r['return']>0: return r
       actions=r['actions']

       if len(actions)==0:
          h+='    Not described yet ...\n'
       else:
          for q in sorted(actions.keys()):
              s=q
              desc=actions[q].get('desc','')
              if desc!='': s+=' - '+desc
              h+='    * '+s+'\n'

       h+='\n'
       h+='  Common actions for this module from the CK kernel:\n'
       h+='    $ ck help\n'

    if m=='<module_uoa>':
       h+='\n'
       h+=cfg['help_examples']

    h+='\n'
    h+=cfg['help_web']

    if o=='con': out(h)

    return {'return':0, 'help':h}

#########################################################
# Common action: print help for a given module
#
# TARGET: CK kernel and low-level developers

def short_help(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              help         - help text
            }



    """

    import sys

    o=i.get('out','')

    r=version({})
    if r['return']>0: return r

    h='CK version: '+r['version_str']+'\n'

    r=python_version({})
    if r['return']>0: return r

    x=sys.executable
    if x!=None and x!='':
       h+='\nPython executable used by CK: '+x+'\n'

    h+='\nPython version used by CK: '+r['version'].replace('\n','\n   ')+'\n'

    h+='\nPath to the default repo: '+work['dir_default_repo']+'\n'
    h+=  'Path to the local repo:   '+work['dir_local_repo']+'\n'
    h+=  'Path to CK repositories:  '+work['dir_repos']+'\n'

    h+='\n'+cfg['help_web'].replace('\n','').strip()+'\n' #.replace('   ','')+'\n'

    h+='CK Google group:      https://bit.ly/ck-google-group\n'
    h+='CK Slack channel:     https://cKnowledge.org/join-slack\n'
    h+='Stable CK components: https://cKnowledge.io'

    if o=='con': 
       out(h)

    return {'return':0, 'help':h}

#########################################################
# Common action: print input
#
# TARGET: CK kernel and low-level developers

def print_input(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              html         - input as JSON
            }

    """

    o=i.get('out','')

    rx=dumps_json({'dict':i, 'sort_keys':'yes'})
    if rx['return']>0: return rx

    h=rx['string']

    if o=='con': out(h)

    return {'return':0, 'html':h}

#########################################################
# Common action: print info about a given CK entry
#
# TARGET: CK kernel and low-level developers

def info(i):
    """
    Input:  {
              (repo_uoa)
              module_uoa
              (data_uoa)
            }

    Output: {
              Output of 'load' function
            }

    """

    o=i.get('out','')

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    if muoa=='':
       return {'return':1, 'error':'module UOA is not defined'}

    module_info=False
    if duoa=='':
       module_info=True
       duoa=muoa
       muoa=cfg['module_name']

    ii={'module_uoa':muoa, 'data_uoa':duoa}
    if ruoa!='': ii['repo_uoa']=ruoa
    r=load(ii)
    if r['return']>0: return r

    if o=='con':
       if module_info:
          p=r['path']
          dd=r['dict']

          developer=dd.get('developer','')
          license=dd.get('license','')
          desc=dd.get('desc','')

          # Get user-friendly CID
          rx=convert_entry_to_cid(r)
          if rx['return']>0: return rx

          cuoa=rx['cuoa']
          cid=rx['cid']
          xcuoa=rx['xcuoa']
          xcid=rx['xcid']

          out('*** CID ***')
          out(cuoa+' ('+cid+')')

          out('')
          out('*** Path ***')
          out(p)

          if desc!='':
             out('')
             out('*** Description ***')
             out(desc)

          if developer!='':
             out('')
             out('*** Developer ***')
             out(developer)

          if license!='':
             out('')
             out('*** License ***')
             out(license)

       else:
          p=r['path']
          duid=r['data_uid']
          dalias=r['data_alias']
          muid=r['module_uid']
          malias=r['module_alias']

          out('Path  =        '+p)
          out('')
          out('Data alias =   '+dalias)
          out('Data UID   =   '+duid)
          out('')
          out('Module alias = '+malias)
          out('Module UID   = '+muid)

    return r

############################################################
# Common action: get CID from current path
#
# TARGET: CK kernel and low-level developers

def path(i):
    """
    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              Output from from 'detect_cid_in_current_path' function
            }

    """

    o=i.get('out','')

    r=detect_cid_in_current_path(i)
    if r['return']>0: return r

    rx=convert_entry_to_cid(r)
    if rx['return']>0: return rx

    cuoa=rx['cuoa']
    cid=rx['cid']
    xcuoa=rx['xcuoa']
    xcid=rx['xcid']

    # If console, print CIDs
    if o=='con':
       out(cuoa)
       out(cid)
       out(xcuoa)
       out(xcid)

    return r

############################################################
# Common action: get CID from current path or given CID (module_uid:data_uid)
#
# TARGET: end users

def cid(i):
    """
    Input:  {
              (repo_uoa)   - repo UOA
              (module_uoa) - module UOA
              (data_uoa)   - data UOA

                 If above is empty, detect in current path !

            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              Output from from 'detect_cid_in_current_path' function

              data_uoa     - data UOA
              module_uoa   - module UOA
              (repo_uoa)   - repo UOA
            }

    """

    o=i.get('out','')

    # Check which CID to detect
    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    if ruoa=='' and muoa=='' and duoa=='':
       r=detect_cid_in_current_path(i)
    else:
       r=find({'repo_uoa':ruoa, 'module_uoa':muoa, 'data_uoa':duoa})
    if r['return']>0: return r

    rx=convert_entry_to_cid(r)
    if rx['return']>0: return rx

    cid=rx['cid']

    # If console, print CIDs
    if o=='con':
       out(cid)
       # Try to copy to Clipboard if supported by OS
       rx=copy_to_clipboard({'string':cid})
       # Ignore error

    return r

############################################################
# Copy current path to clipboard (productivity function)
#
# TARGET: CK kernel and low-level developers

def copy_path_to_clipboard(i):
    """
    Input:  {
              (add_quotes) - if 'yes', add quotes
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    p=os.getcwd()

    if i.get('add_quotes','')=='yes':
       p='"'+p+'"'

    rx=copy_to_clipboard({'string':p})
    # Ignore error

    return {'return':0}

#########################################################
# Common action: load data (module) meta description
#
# TARGET: CK kernel and low-level developers

def load(i):
    """
    Input:  {
              (repo_uoa)              - repo UOA
              module_uoa              - module UOA
              data_uoa                - data UOA

              (get_lock)              - if 'yes', lock this entry
              (lock_retries)          - number of retries to aquire lock (default=5)
              (lock_retry_delay)      - delay in seconds before trying to aquire lock again (default=10)
              (lock_expire_time)      - number of seconds before lock expires (default=30)

              (skip_updates)          - if 'yes', do not load updates
              (skip_desc)             - if 'yes', do not load descriptions

              (load_extra_json_files) - list of files to load from the entry

              (unlock_uid)            - UID of the lock to release it

              (min)                   - show minimum when output to console (i.e. meta and desc)

              (create_if_not_found)   - if 'yes', create, if entry is not found - useful to create and lock entries
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              dict         - entry meta description
              (info)       - entry info
              (updates)    - entry updates
              (desc)       - entry description

              path         - path to data entry
              path_module  - path to module entry with this entry
              path_repo    - path to the repository of this entry
              repo_uoa     - repo UOA 
              repo_uid     - repo UID
              repo_alias   - repo alias
              module_uoa   - module UOA 
              module_uid   - module UID
              module_alias - module alias
              data_uoa     - data UOA
              data_uid     - data UID
              data_alias   - data alias
              data_name    - user friendly name

              (extra_json_files) - dict with extra json files (key is the filename from 'load_extra_json_files')

              (lock_uid)   - unlock UID, if locked successfully
            }
    """

    o=i.get('out','')

    a=i.get('repo_uoa','')
    m=i.get('module_uoa','')
    d=i.get('data_uoa','')

    if d=='':
       return {'return':1, 'error':'data UOA is not defined'}

    r=find_path_to_data({'repo_uoa':a, 'module_uoa':m, 'data_uoa':d})
    if r['return']>0: 
       if r['return']==16 and i.get('create_if_not_found','')=='yes':
          r=add({'repo_uoa':a, 'module_uoa':m, 'data_uoa':d})
          if r['return']>0:
             return r
          r=find_path_to_data({'repo_uoa':a, 'module_uoa':m, 'data_uoa':d})
          if r['return']>0: return r
       else:
          return r

    p=r['path']

    slu=i.get('skip_updates','')
    sld=i.get('skip_desc','')

    # Set/check lock
    i['path']=p
    rx=set_lock(i)
    if rx['return']>0: return rx

    luid=rx.get('lock_uid','')

    # Load meta description
    r1=load_meta_from_path({'path':p, 'skip_updates':slu, 'skip_desc':sld})
    if r1['return']>0: return r1

    r.update(r1)
    r['path']=p

    r['data_name']=r1.get('info',{}).get('data_name','')

    if luid!='': r['lock_uid']=luid

    # If load extra files
    lejf=i.get('load_extra_json_files',[])
    if len(lejf)>0:
       ejf={}
       for ff in lejf:
           rx=load_json_file({'json_file':os.path.join(p,ff)})
           if rx['return']>0: return rx
           ejf[ff]=rx['dict']
       r['extra_json_files']=ejf

    # If console mode, print json
    if o=='con':
       dd=r
       if i.get('min','')=='yes':
          dd={
              'desc':r.get('desc',{}),
              'dict':r.get('dict',{})
             }

       rr=dumps_json({'dict':dd, 'sort_keys':'yes'})
       if rr['return']==0:
          out(rr['string'])

    return r

#########################################################
# Common action: find data (module) - uses 'load' function
#
# TARGET: CK kernel and low-level developers

def find(i):
    """
    Input:  {
              (repo_uoa)  - repo UOA
              module_uoa  - module UOA
              data_uoa    - data UOA
            }

    Output: { 
              Output of the 'load' function 

              number_of_entries - total number of found entries
            }
    """

    o=i.get('out','')

    rr=find2(i)
    if rr['return']>0:
       if rr['return']==16 and cfg.get('download_missing_components','')=='yes':
          import copy

          muoa=i.get('module_uoa','')
          duoa=i.get('data_uoa','')

#          out('')
#          out('  WARNING: checking missing components "'+muoa+':'+duoa+'" at the CK portal ...')

          ii=copy.deepcopy(i)

          ii['repo_uoa']=cfg['default_exchange_repo_uoa']
          ii['out']='con'

          # Try to download 
          ry=download(ii)
          if ry['return']>0: return ry
                  
          # Restart local find
          rr=find2(i)

    return rr

#########################################################
# original find

def find2(i):

    o=i.get('out','')
    i['out']=''

    # Check wildcards
    lst=[]

    a=i.get('repo_uoa','')
    m=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    if m=='':
       return {'return':1, 'error':'module UOA is not defined'}
    if duoa=='':
       return {'return':1, 'error':'data UOA is not defined'}

    if a.find('*')>=0 or a.find('?')>=0 or m.find('*')>=0 or m.find('?')>=0 or duoa.find('*')>=0 or duoa.find('?')>=0: 
       r=list_data({'repo_uoa':a, 'module_uoa':m, 'data_uoa':duoa})
       if r['return']>0: return r

       lst=r['lst']

       r={'return':0}

       if len(lst)>0:
          r.update(lst[0])
       else:
          return {'return':1, 'error':'entry was not found'}

    else:
       # Find path to data
       r=find_path_to_data(i)
       if r['return']>0: return r

       p=r['path']
       ruoa=r.get('repo_uoa','')
       ruid=r.get('repo_uid','')
       muoa=r.get('module_uoa','')
       muid=r.get('module_uid','')
       duid=r.get('data_uid','')
       duoa=r.get('data_alias','')
       if duoa=='': duoa=duid

       lst.append({'path':p, 'repo_uoa':ruoa, 'repo_uid':ruid, 
                             'module_uoa':muoa, 'module_uid':muid, 
                             'data_uoa':duoa, 'data_uid': duid})

    if o=='con':
       pf='' 
       for q in lst:
           p=q['path']
           out(p)
           if pf=='': pf=p

    i['out']=o

    r['number_of_entries']=len(lst)

    return r

#########################################################
# Common action: print 'cd {path to CID}'
#
# TARGET: CK kernel and low-level developers

def cd(i):
    """
    Input:  {
              (repo_uoa)  - repo UOA
              module_uoa  - module UOA
              data_uoa    - data UOA
                 or
              cid

            }

    Output: { 
              Output of the 'load' function 

              string - prepared string 'cd {path to entry}'
            }
    """

    o=i.get('out','')

    i['out']=''
    r=find(i)
    i['out']=o

    if r['return']>0: return r

    noe=r.get('number_of_entries','')
    if noe=='': noe=0

    if noe>1 and o=='con':
       out('CK warning: '+str(noe)+' entries found! Selecting the first one ...')
       out('')

    p=r.get('path','')
    if p!='':
       rx=get_os_ck({})
       if rx['return']>0: return rx

       plat=rx['platform']

       s='cd '
       if plat=='win':
          s+='/D '

       if p.find(' ')>0:
          p='"'+p+'"'
       s+=p

       out(s)

       r['string']=s

       import platform
       import subprocess

       out('')
       out('Warning: you are in a new shell with a reused environment. Enter "exit" to return to the original one!')

       if platform.system().lower().startswith('win'): # pragma: no cover
          p = subprocess.Popen(["cmd", "/k", s], shell = True, env=os.environ)
          p.wait()

       else:
          rx=gen_tmp_file({})
          if rx['return']>0: return rx
          fn=rx['file_name']

          rx=save_text_file({'text_file':fn, 'string':s})
          if rx['return']>0: return rx

          os.system("bash --rcfile "+fn)

    return r

#########################################################
# Common action: print 'cd {path to CID} and copy to clipboard'
#
# TARGET: CK kernel and low-level developers

def cdc(i): # pragma: no cover
    """
    Input:  {
              (repo_uoa)  - repo UOA
              module_uoa  - module UOA
              data_uoa    - data UOA
                 or
              cid

            }

    Output: { 
              Output of the 'load' function 
            }
    """

    r=cd(i)
    if r['return']>0: return r

    s=r.get('string','')
    if s!='':
       rx=copy_to_clipboard({'string':s})
       if rx['return']>0: return rx

    return r

##############################################################################
# Common action: add data (module) meta-description to a repository
#
# TARGET: CK kernel and low-level developers

def add(i):
    """
    Input:  {
              (repo_uoa)             - repo UOA
              module_uoa             - module UOA
              data_uoa               - data UOA
              (data_uid)             - data UID (if uoa is an alias)
              (data_name)            - user friendly data name

              (dict_from_cid)        -
              (dict_from_repo_uoa)   - 
              (dict_from_module_uoa) - 
              (dict_from_data_uoa)   - if present, pre-load dict 
                                       from this (module_uoa):data_uoa (analog of copy)

              (update)               - if == 'yes' and entry exists, update it

              (dict)                 - meta description to record
              (substitute)           - if 'yes' and update=='yes' substitute dictionaries, otherwise merge!

              (desc)                 - description of an entry (gradually adding API description in flat format)

              (extra_json_files)     - dict with extra json files to save to entry (key is a filename)

              (tags)                 - list or comma separated list of tags to add to entry

              (info)                 - entry info to record - normally, should not use it!
              (extra_info)           - enforce extra info such as
                                          author
                                          author_email
                                          author_webpage
                                          license
                                          copyright
                                       If not specified then taken from kernel (prefix 'default_')

              (updates)              - entry updates info to record - normally, should not use it!
              (ignore_update)        - if 'yes', do not add info about update

              (ask)                  - if 'yes', ask questions, otherwise silent

              (unlock_uid)           - unlock UID if was previously locked

              (sort_keys)            - by default, 'yes'

              (share)                - if 'yes', try to add via GIT

              (skip_indexing)        - if 'yes', skip indexing even if it is globally on

              (allow_multiple_aliases) - if 'yes', allow multiple aliases for the same UID 
                                         (needed for cKnowledge.io to publish
                                         renamed components with the same UID)
            }

    Output: {
              return       - return code =  0, if successful
                                           16, if entry already exists
                                         >  0, if error
              (error)      - error text if return > 0

              Output from the 'create_entry' function
            }

    """

    o=i.get('out','')

    t='added'

    ra=i.get('repo_uoa','')
    m=i.get('module_uoa','')
    d=i.get('data_uoa','')
    di=i.get('data_uid','')
    dn=i.get('data_name','')

    ama=(i.get('allow_multiple_aliases','')=='yes') # Experimental functionality for cKnowledge.io

    if cfg.get('allowed_entry_names','')!='':
       import re

       anames=cfg.get('allowed_entry_names','')

       if not re.match(anames, ra) or \
          not re.match(anames, m) or \
          not re.match(anames, d) or \
          not re.match(anames, di):
          return {'return':1, 'error':'found disallowed characters in names (allowed: "'+anames+'")'}

    if cfg.get('force_lower','')=='yes':
       ra=ra.lower()
       m=m.lower()
       d=d.lower()
       di=di.lower()

    uuid=i.get('unlock_uid','')

    up=i.get('update','')

    ask=i.get('ask','')

    # Get repo path
    r=find_path_to_repo({'repo_uoa':ra})
    if r['return']>0: return r
    pr=r['path']

    ruoa=r['repo_uoa']
    ruid=r['repo_uid']
    ralias=r['repo_alias']

    rd=r['dict']
    rshared=rd.get('shared','')
    rsync=rd.get('sync','')

    if i.get('share','')=='yes': rsync='yes'

    # Check if writing is allowed
    ii={'module_uoa':m, 'repo_uoa':r['repo_uoa'], 'repo_uid':r['repo_uid'], 'repo_dict':rd}
    r=check_writing(ii)
    if r['return']>0: return r

    # Load info about module
    r=load({'module_uoa':cfg['module_name'],
            'data_uoa':m})
    if r['return']>0: return r
    elif r['return']==16: 
       return {'return':8, 'error':'can\'t find path to module "'+m+'"'}
    muoa=r['data_uoa']
    muid=r['data_uid']
    malias=r['data_alias']
    pm=r['path']

    uid=r['data_uid']
    alias=r['data_alias']
    if alias=='': alias=uid
    module_desc=r['dict']

    # Check if there is a split of directories for this module in local config
    # to handle numerous entries (similar to MediaWiki)
    split_dirs=get_split_dir_number(rd, muid, muoa)

    # Ask additional questions
    if o=='con' and ask=='yes':
       # Asking for alias
       if d=='' or is_uid(d):
          r=inp({'text':'Enter an alias (or Enter to skip it): '})
          d=r['string']

       # Asking for user-friendly name
       if dn=='' and up!='yes':
          r=inp({'text':'Enter a user-friendly name of this entry (or Enter to reuse alias): '})
          dn=r['string']

    # Load dictionary from other entry if needed
    dfcid=i.get('dict_from_cid','')
    dfruoa=i.get('dict_from_repo_uoa','')
    dfmuoa=i.get('dict_from_module_uoa','')
    dfduoa=i.get('dict_from_data_uoa','')

    if dfcid!='':
       r=parse_cid({'cid':dfcid})
       if r['return']>0: return r
       dfruoa=r.get('repo_uoa','')
       dfmuoa=r.get('module_uoa','')
       dfduoa=r.get('data_uoa','')

    if d!='' and not is_uoa(d):
       return {'return':1, 'error':'alias has disallowed characters'}

    if dfduoa!='':
       if dfmuoa=='': dfmuoa=m

       ii={'module_uoa':dfmuoa, 'data_uoa':dfduoa}
       if dfruoa!='': ii['repo_uoa']=dfruoa

       r=load(ii)
       if r['return']>0: return r

       df=r.get('dict',{})

    # Create first level entry (module) 
    r=create_entry({'path':pr, 'data_uoa':alias, 'data_uid':uid})
    if r['return']>0 and r['return']!=16: return r
    p1=r['path']

    # Create second level entry (data)
    i1={'path':p1}
    if split_dirs!=0:
       i1['split_dirs']=split_dirs
    pdd=''
    if di!='': 
       i1['data_uid']=di
    if d!='': 
       i1['data_uoa']=d
    if ama:
       i1['allow_multiple_aliases']='yes'

    rr=create_entry(i1)
    if rr['return']>0 and rr['return']!=16: return rr

    duid=rr['data_uid']
    pdd=rr['data_uoa']
    dalias=rr['data_alias']

    # Preparing meta-description
    a={}
    info={}
    updates={}
    desc={}

    p2=rr['path']
    p3=os.path.join(p2, cfg['subdir_ck_ext'])
    p4=os.path.join(p3, cfg['file_meta'])
    p4i=os.path.join(p3, cfg['file_info'])
    p4u=os.path.join(p3, cfg['file_updates'])
    p4d=os.path.join(p3, cfg['file_desc'])

    # If last entry exists
    if rr['return']==16:
       if up=='yes':
          t='updated'

          # Check if locked
          rl=check_lock({'path':p2, 'unlock_uid':uuid})
          if rl['return']>0: 
             if rl['return']==32:
                rl['data_uoa']=pdd
                rl['data_uid']=duid
             return rl

          # Entry exists, load configuration if update
          r2=load_meta_from_path({'path':p2})
          if r2['return']>0: return r2
          a=r2['dict']
          info=r2.get('info',{})
          updates=r2.get('updates',{})
          desc=r2.get('desc',{})

          if dn=='': dn=info.get('data_name','')
       else:
          return {'return':16,'error':'entry already exists in path ('+p2+')'}
    else:
       # Create configuration directory
       if not os.path.isdir(p3):
          try:
             os.mkdir(p3)
          except Exception as e:
             return {'return':1, 'error':format(e)}

    if dn=='' and not is_uid(d):
       dn=d

    if dfduoa!='':
       r=merge_dicts({'dict1':a, 'dict2':df})
       if r['return']>0: return r

    # If dict, info and updates are in input, try to merge ...
    cma=i.get('dict',{})
    cmad=i.get('desc',{})
    if i.get('substitute','')=='yes':
       a=cma
       desc=cmad
    else:
       r=merge_dicts({'dict1':a, 'dict2':cma})
       if r['return']>0: return r
       r=merge_dicts({'dict1':desc, 'dict2':cmad})
       if r['return']>0: return r

    # Check tags 
    xtags=a.get('tags',[])

    tags=i.get('tags','')
    if tags=='': tags=[]
    elif type(tags)!=list:
       tags=tags.split(',')

    for l in range(0,len(tags)):
        ll=tags[l].strip()
        if ll not in xtags:
           xtags.append(ll)

    if len(xtags)>0:
       a['tags']=xtags

    # Process info
    cminfo=i.get('info',{})
    if len(cminfo)!=0:
       info=cminfo
#       r=merge_dicts({'dict1':info, 'dict2':cminfo})
#       if r['return']>0: return r

    cmupdates=i.get('updates',{})
    if len(cmupdates)!=0:
       updates=cmupdates
#       r=merge_dicts({'dict1':updates, 'dict2':cmupdates})
#       if r['return']>0: return r

    # If name exists, add
    info['backup_module_uoa']=muoa
    info['backup_module_uid']=muid
    info['backup_data_uid']=duid
    if dn!='': info['data_name']=dn

    # Add control info
    ri=prepare_special_info_about_entry({})
    if ri['return']>0: return ri
    x=ri['dict']

    # Check if pre-set control params such as author, copyright, license
    ei=i.get('extra_info',{})
    if len(ei)!=0: x.update(ei)

    y=info.get('control',{})

    if i.get('ignore_update','')!='yes':
       if len(y)==0:
          info['control']=x
       else:
          y=updates.get('control',[])
          y.append(x)
          updates['control']=y

    sk=i.get('sort_keys','')
    if sk=='': sk='yes'

    if len(updates)>0:
       # Record updates
       rx=save_json_to_file({'json_file':p4u, 'dict':updates, 'sort_keys':sk})
       if rx['return']>0: return rx

    # Record meta description
    rx=save_json_to_file({'json_file':p4, 'dict':a, 'sort_keys':sk})
    if rx['return']>0: return rx

    # Record info
    rx=save_json_to_file({'json_file':p4i, 'dict':info, 'sort_keys':sk})
    if rx['return']>0: return rx

    # Record desc
    rx=save_json_to_file({'json_file':p4d, 'dict':desc, 'sort_keys':sk})
    if rx['return']>0: return rx

    # Record extra files if there
    ejf=i.get('extra_json_files',{})
    if len(ejf)>0:
       for ff in ejf:
           dff=ejf[ff]
           rz=save_json_to_file({'json_file':os.path.join(p2,ff), 'dict':dff, 'sort_keys':sk})
           if rz['return']>0: return rz

    if o=='con':
       out('Entry '+d+' ('+duid+', '+p2+') '+t+' successfully!')

    # Check if needs to be synced
    if rshared!='' and rsync=='yes':
       ppp=os.getcwd()

       os.chdir(pr)
       if os.path.isdir(cfg['subdir_ck_ext']):
          ss=cfg['repo_types'][rshared]['add'].replace('$#path#$', pr).replace('$#files#$', cfg['subdir_ck_ext'])
          rx=os.system(ss)

       os.chdir(p1)
       if os.path.isdir(cfg['subdir_ck_ext']):
          ss=cfg['repo_types'][rshared]['add'].replace('$#path#$', pr).replace('$#files#$', cfg['subdir_ck_ext'])
          rx=os.system(ss)

       ss=cfg['repo_types'][rshared]['add'].replace('$#path#$', pr).replace('$#files#$', pdd)
       rx=os.system(ss)

       os.chdir(ppp)

    # Prepare output
    rr={'return':0,
        'dict': a,
        'info': info,
        'updates': updates, 
        'path':p2,
        'path_module': pm,
        'path_repo': pr,
        'repo_uoa':ruoa,
        'repo_uid':ruid,
        'repo_alias':ralias,
        'module_uoa':muoa,
        'module_uid':muid,
        'module_alias':malias,
        'data_uoa':pdd,
        'data_uid':duid,
        'data_alias':dalias,
        'data_name':dn}

    # Check if need to add index
    if i.get('skip_indexing','')!='yes' and cfg.get('use_indexing','')=='yes':
       muid=rr['module_uid']
       if index_module(muid,ruid):
          duid=rr['data_uid']
          path='/'+muid+'/'+duid+'/1'
          ri=access_index_server({'request':'DELETE', 'path':path})
          if ri['return']>0: return ri
          ri=access_index_server({'request':'PUT', 'path':path, 'dict':rr})
          if ri['return']>0: return ri

    # Remove lock after update if needed
    if uuid!='':
       pl=os.path.join(p2, cfg['subdir_ck_ext'], cfg['file_for_lock'])
       if os.path.isfile(pl): os.remove(pl)

    rr['return']=0

    return rr

##############################################################################
# Common action: update data (module) meta-description to a repository
#
# TARGET: CK kernel and low-level developers

def update(i):
    """
    Input:  {
              (repo_uoa)             - repo UOA
              module_uoa             - module UOA
              data_uoa               - data UOA
              (data_uid)             - data UID (if uoa is an alias)
              (data_name)            - user friendly data name

              (dict_from_cid)        -
              (dict_from_repo_uoa)   - 
              (dict_from_module_uoa) - 
              (dict_from_data_uoa)   - if present, pre-load dict 
                                       from this (module_uoa):data_uoa (analog of copy)

              (dict)                 - meta description to record
              (substitute)           - if 'yes', substitute dictionaries, otherwise merge!

              (tags)                 - list or comma separated list of tags to add to entry

              (info)                 - entry info to record - normally, should not use it!
              (updates)              - entry updates info to record - normally, should not use it!
              (ignore_update)        - if 'yes', do not add info about update

              (ask)                  - if 'yes', ask questions, otherwise silent

              (unlock_uid)           - unlock UID if was previously locked

              (sort_keys)            - if 'yes', sort keys

              (skip_indexing)        - if 'yes', skip indexing even if it is globally on
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              Output from the 'add' function (the last one in case of wildcards)
            }

    """

    # Check if global writing is allowed
    r=check_writing({})
    if r['return']>0: return r

    # Try to load entry, if doesn't exist, add entry
    dd={}

    o=i.get('out','')
    i['out']=''

    # Check wildcards
    lst=[]

    a=i.get('repo_uoa','')
    m=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    if duoa=='': duoa='*'

    single_not_found=False # If no wild cards and entry not found, then add

    if a.find('*')>=0 or a.find('?')>=0 or m.find('*')>=0 or m.find('?')>=0 or duoa.find('*')>=0 or duoa.find('?')>=0: 
       r=list_data({'repo_uoa':a, 'module_uoa':m, 'data_uoa':duoa})
       if r['return']>0: return r

       lst=r['lst']
    else:
       # Find path to data
       r=find_path_to_data(i)
       if r['return']>0: 
          single_not_found=True
       else:
          p=r['path']
          ruoa=r.get('repo_uoa','')
          ruid=r.get('repo_uid','')
          muoa=r.get('module_uoa','')
          muid=r.get('module_uid','')
          duid=r.get('data_uid','')
          duoa=r.get('data_alias','')
          if duoa=='': duoa=duid

          lst.append({'path':p, 'repo_uoa':ruoa, 'repo_uid':ruid, 
                                'module_uoa':muoa, 'module_uid':muid, 
                                'data_uoa':duoa, 'data_uid': duid})

    # Update entries
    i['out']=o

    r={'return':0}
    if single_not_found:
       r=add(i)
    else:
       i['update']='yes'

       for q in lst:
           ii={}
           ii.update(i)
           ii.update(q)
           r=add(ii)
           if r['return']>0: return r

    return r

##############################################################################
# Common action: edit data meta-description through external editor
#
# TARGET: CK kernel and low-level developers

def edit(i): # pragma: no cover
    """
    Input:  {
              (repo_uoa)             - repo UOA
              module_uoa             - module UOA
              data_uoa               - data UOA

              (ignore_update)        - (default==yes) if 'yes', do not add info about update
              (sort_keys)            - (default==yes) if 'yes', sort keys

              (edit_desc)            - if 'yes', edit description rather than meta 
                                       (useful for compiler descriptions)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    iu=i.get('ignore_update','')
    if iu=='': iu='yes'

    ed=i.get('edit_desc','')

    sk=i.get('sort_keys','')
    if sk=='': sk='yes'

    ii={'action':'load',
        'repo_uoa':ruoa,
        'module_uoa':muoa,
        'data_uoa':duoa,
        'common_func':'yes'}
    r=access(ii)
    if r['return']>0: return r

    desc=r.get('desc',{})
    meta=r['dict']

    # Record to tmp file
    import tempfile
    fd, fn=tempfile.mkstemp(suffix='.tmp', prefix='ck-') # suffix is important - CK will delete such file!
    os.close(fd)
    os.remove(fn)

    if ed=='yes': dd=desc
    else:         dd=meta

    r=save_json_to_file({'json_file':fn, 'dict':dd, 'sort_keys':sk})
    if r['return']>0: return r

    # Get OS
    r=get_os_ck({})
    if r['return']>0: return r
    plat=r['platform']

    x=cfg['external_editor'][plat].replace('$#filename#$', fn)

    os.system(x)

    # Load file
    r=load_json_file({'json_file':fn})
    if r['return']>0: return r

    if ed=='yes': desc=r['dict']
    else:         meta=r['dict']

    # Update entry to finish sync/indexing
    ii={'action':'update',
        'repo_uoa':ruoa,
        'module_uoa':muoa,
        'data_uoa':duoa,
        'common_func':'yes',
        'ignore_update':iu,
        'dict':meta,
        'desc':desc,
        'substitute':'yes',
        'sort_keys':sk,
        'out':o}
    r=access(ii)

    # Delete tmp file
    if os.path.isfile(fn): 
       os.remove(fn)

    return r

##############################################################################
# Common action: delete data (module) entry
#
# TARGET: CK kernel and low-level developers

def rm(i):
    """
    Input:  {
              (repo_uoa)      - repo UOA    ; can be wild cards
              module_uoa      - module UOA  ; can be wild cards
              data_uoa        - data UOA    ; can be wild cards

              (force)         - if 'yes', force deleting without questions
                 or
              (f)             - to be compatible with rm -f 

              (share)         - if 'yes', try to remove via GIT

              (tags)          - use these tags in format tags=x,y,z to prune rm
                   or
              (search_string) - prune entries with expression *?
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    a=i.get('repo_uoa','')

    # Check if global writing is allowed
    r=check_writing({'repo_uoa':a, 'delete':'yes'})
    if r['return']>0: return r

    o=i.get('out','')

    m=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    if duoa=='':
       return {'return':1, 'error':'data UOA is not defined'}

    lst=[]

    tags=i.get('tags','')
    ss=i.get('search_string','')

    # Check wildcards
    if a.find('*')>=0 or a.find('?')>=0 or m.find('*')>=0 or m.find('?')>=0 or duoa.find('*')>=0 or duoa.find('?')>=0: 
       if tags=='' and ss=='':
          r=list_data({'repo_uoa':a, 'module_uoa':m, 'data_uoa':duoa})
          if r['return']>0: return r
       else:
          r=search({'repo_uoa':a, 'module_uoa':m, 'data_uoa':duoa, 'tags':tags, 'search_string':ss})
          if r['return']>0: return r

       lst=r['lst']
    else:
       # Find path to data
       r=find_path_to_data({'repo_uoa':a, 'module_uoa':m, 'data_uoa':duoa})
       if r['return']>0: return r

       p=r['path']

       ruoa=r.get('repo_uoa','')
       ruid=r.get('repo_uid','')

       muoa=r.get('module_uoa','')
       muid=r.get('module_uid','')

       duid=r.get('data_uid','')
       duoa=r.get('data_alias','')

       if duoa=='': duoa=duid

       uu={'path':p, 'repo_uoa':ruoa, 'repo_uid':ruid, 
           'module_uoa':muoa, 'module_uid':muid, 
           'data_uoa':duoa, 'data_uid': duid}
       lst.append(uu)

    force=i.get('force','')
    if force=='':
       force=i.get('f','')

    first=True
    for ll in lst:
        p=ll['path']
        pm=os.path.split(p)[0]

        muid=ll['module_uid']
        muoa=ll['module_uoa']
        duid=ll['data_uid']
        duoa=ll['data_uoa']

        if duoa!=duid: dalias=duoa
        else: dalias=''

        # Get user-friendly CID
        x=muoa+':'+duoa
        if o=='con':
           # Try to check if has data name (useful for env)
           p2=os.path.join(p, cfg['subdir_ck_ext'], cfg['file_info'])
           if os.path.isfile(p2):
              r2=load_json_file({'json_file':p2})
              if r2['return']==0:
                 x2=r2['dict'].get('data_name','')
                 if x2!='' and x2!=None:
                    x='"'+x2+'"\n    '+x

        xcuoa=x+' ('+muid+':'+duid+')'

        # Check repo/module writing
        ii={'module_uoa':m, 'repo_uoa':ll['repo_uoa'], 'repo_uid':ll['repo_uid']}
        r=check_writing(ii)
        if r['return']>0: return r

        rd=r.get('repo_dict',{})
        rshared=rd.get('shared','')
        rsync=rd.get('sync','')

        # Check if there is a split of directories for this module in local config
        # to handle numerous entries (similar to MediaWiki)
        split_dirs=get_split_dir_number(rd, muid, muoa)
        if split_dirs!=0:
           pm=os.path.split(pm)[0]

        shr=i.get('share','')
        if shr=='yes': 
           rshared='git'
           rsync='yes'

        # If interactive
        to_delete=True
        if o=='con' and force!='yes':
           r=inp({'text':'Are you sure to delete CK entry '+xcuoa+' ? (y/N): '})
           c=r['string'].lower()
           if c!='y' and c!='yes': to_delete=False

        # If deleting
        if to_delete:
           # First remove alias if exists
           if dalias!='':
              # Delete alias
              r=delete_alias({'path':pm, 'data_alias':dalias, 'data_uid':duid, 'repo_dict':rd, 'share':shr})
              if r['return']>0: return r

           if rshared!='':
              pp=os.path.split(p)
              pp0=pp[0]
              pp1=pp[1]

              ppp=os.getcwd()
              os.chdir(pp0)

              ss=cfg['repo_types'][rshared]['rm'].replace('$#files#$', pp1)
              rx=os.system(ss)

           # Delete directory
           r={'return':0}
           if os.path.isdir(p):
              r=delete_directory({'path':p})

           if rshared!='':
              os.chdir(ppp)

           if r['return']>0: return r

           # Check if need to delete index
           if cfg.get('use_indexing','')=='yes' and index_module(muid,ll['repo_uid']):
              path='/'+muid+'/'+duid+'/1'
              ri=access_index_server({'request':'DELETE', 'path':path})
              if ri['return']>0: return ri

           if o=='con':
              out('   Entry '+xcuoa+' was successfully deleted!')

    return {'return':0}

##############################################################################
# Common action: delete data (module) entry -> calls rm function
#
# TARGET: CK kernel and low-level developers

def remove(i):
    """
    Input:  { See rm function }
    Output: { See rm function }

    """

    return rm(i)

##############################################################################
# Common action: delete data (module) entry -> calls rm function
#
# TARGET: CK kernel and low-level developers

def delete(i):
    """
    Input:  { See rm function }
    Output: { See rm function }

    """

    return rm(i)

##############################################################################
# Common action: rename data entry
#
# TARGET: CK kernel and low-level developers

def ren(i):
    """
    Input:  {
              (repo_uoa)         - repo UOA
              module_uoa         - module UOA
              data_uoa           - old data UOA

              new_data_uoa       - new data alias
                 or
              new_data_uid       - new data UID (leave empty to keep old one)
                 or
              xcids[0]           - {'data_uoa'} - new data UOA

              (new_uid)          - generate new UID

              (remove_alias)     - if 'yes', remove alias

              (add_uid_to_alias) - if 'yes', add UID to alias

              (share)            - if 'yes', try to remove old entry via GIT and add new one
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Check if global writing is allowed
    r=check_writing({'delete':'yes'})
    if r['return']>0: return r

    o=i.get('out','')

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    if muoa=='': return {'return':1, 'error':'module UOA is not defined'}
    if duoa=='': return {'return':1, 'error':'data UOA is not defined'}

    # Attempt to load original entry meta
    ii={'module_uoa':muoa, 'data_uoa':duoa}
    if ruoa!='': ii['repo_uoa']=ruoa
    r=load(ii)
    if r['return']>0: return r
    rdd=r

    muid=r['module_uid']
    pr=r['path_repo']
    ddi=r['info']

    duoa=r['data_uoa']
    duid=r['data_uid']
    dalias=r['data_alias']

    change_data_name=(ddi.get('data_name','')==dalias)

    p=r['path']
    pm=r['path_module'] 

    p1=os.path.join(pm, cfg['subdir_ck_ext'])
    pn=p

    # Check if writing is allowed
    ruid=r['repo_uid']
    ii={'module_uoa':muoa, 'module_uid':muid, 'repo_uoa':ruoa, 'repo_uid':ruid}
    r=check_writing(ii)
    if r['return']>0: return r

    rd=r.get('repo_dict',{})
    rshared=rd.get('shared','')
    rsync=rd.get('sync','')

    shr=i.get('share','')
    if shr=='yes': 
       rshared='git'
       rsync='yes'

    # Check if index -> delete old index
    if cfg.get('use_indexing','')=='yes' and index_module(muid,ruid):
       path='/'+muid+'/'+duid+'/1'
       ri=access_index_server({'request':'DELETE', 'path':path})
       if ri['return']>0: return ri

    # Check new data UOA
    nduoa=i.get('new_data_uoa','')
    nduid=i.get('new_data_uid','')

    if nduid=='' and i.get('new_uid','')=='yes':
       rx=gen_uid({})
       if rx['return']>0: return rx
       nduid=rx['data_uid']

    xcids=i.get('xcids',[])
    if len(xcids)>0: 
       xcid=xcids[0]
       nduoa=xcid.get('data_uoa','')

    if i.get('remove_alias','')=='yes':
       nduoa=duid

    if nduoa=='': nduoa=duoa

    if cfg.get('allowed_entry_names','')!='':
       import re

       anames=cfg.get('allowed_entry_names','')

       if not re.match(anames, nduoa) or \
          not re.match(anames, nduid):
          return {'return':1, 'error':'found disallowed characters in names (allowed: "'+anames+'")'}

    if cfg.get('force_lower','')=='yes':
       nduoa=nduoa.lower()
       nduid=nduid.lower()

    if nduid!=duid:
       # Check that new UID doesn't exist
       p2=os.path.join(p1, cfg['file_alias_u'] + nduid)
       if os.path.isfile(p2):
          return {'return':1, 'error':'new UID already exists'}

    # Check if adding UID to alias
    if i.get('add_uid_to_alias','')=='yes':
       x=nduid
       if x=='': x=duid
       nduoa+='-'+x

    if nduoa!=duoa:
       if not is_uoa(nduoa):
          return {'return':1, 'error':'alias has disallowed characters'}

       # Need to rename directory
       if os.path.isdir(nduoa):
          return {'return':1, 'error': 'new alias already exists'}

       # Check if there is a split of directories for this module in local config
       # to handle numerous entries (similar to MediaWiki)
       split_dirs=get_split_dir_number(rd, muid, muoa)

       if split_dirs!=0:
          sd1,sd2=split_name(nduoa, split_dirs)
          pm1=pm
          if sd2!='': # otherwise name is smaller than the split number
             pm1=os.path.join(pm, sd1)
             if not os.path.isdir(pm1):
                os.mkdir(pm1)

          pn=os.path.join(pm1, nduoa)
       else:
          pn=os.path.join(pm, nduoa)

       if rshared!='' and rsync=='yes':
          import shutil

          shutil.copytree(p,pn)

          ppp=os.getcwd()

          pp=os.path.split(pn)
          pp0=pp[0]
          pp1=pp[1]

          os.chdir(pp0)
          ss=cfg['repo_types'][rshared]['add'].replace('$#files#$', pp1)
          rx=os.system(ss)

          pp=os.path.split(p)
          pp0=pp[0]
          pp1=pp[1]

          ss=cfg['repo_types'][rshared]['rm'].replace('$#files#$', pp1)
          rx=os.system(ss)

          os.chdir(ppp)

          if os.path.isdir(p):
             shutil.rmtree(p, onerror=rm_read_only)

       else:
          os.rename(p, pn)

    if nduid!='' or change_data_name:
       # Change backup_data_uid in info file
       ppi=os.path.join(pn,cfg['subdir_ck_ext'],cfg['file_info'])

       if nduid!='':
          ddi['backup_data_uid']=nduid

       if change_data_name:
          ddi['data_name']=nduoa

       rx=save_json_to_file({'json_file':ppi, 'dict':ddi, 'sort_keys':'yes'})
       if rx['return']>0: return rx

    if nduid=='': nduid=duid

    # Remove old alias disambiguator
    if not is_uid(duoa):
       r=delete_alias({'path':pm, 'data_uid':duid, 'data_alias':duoa, 'share':shr})
       if r['return']>0: return r

    # Add new disambiguator, if needed
    if not is_uid(nduoa):
       if not os.path.isdir(p1):
          # Create .cm directory
          try:
             os.mkdir(p1)
          except Exception as e:
             return {'return':1, 'error':format(e)}

       # Write UOA disambiguator
       p3=os.path.join(p1, cfg['file_alias_a'] + nduoa)

       ru=save_text_file({'text_file':p3, 'string':nduid+'\n'})
       if ru['return']>0: return ru

       # Write UID disambiguator
       p2=os.path.join(p1, cfg['file_alias_u'] + nduid)

       ru=save_text_file({'text_file':p2, 'string':nduoa+'\n'})
       if ru['return']>0: return ru

       if rshared!='' and rsync=='yes':
          ppp=os.getcwd()

          pp=os.path.split(p1)
          pp0=pp[0]
          pp1=pp[1]

          os.chdir(pp0)
          ss=cfg['repo_types'][rshared]['add'].replace('$#files#$', pp1)
          rx=os.system(ss)

          os.chdir(ppp)

    # Check if index and add new
    if cfg.get('use_indexing','')=='yes' and index_module(muid,ruid):

       # Need to reload to get new dictionary with updated aliases/UIDs
       rdd=load({'repo_uoa':ruid,
                 'module_uoa':muid,
                 'data_uoa':nduid})
       if rdd['return']>0: return rdd

       if is_uid(nduoa): nduid=nduoa
       path='/'+muid+'/'+nduid+'/1'
       ri=access_index_server({'request':'DELETE', 'path':path})
       if ri['return']>0: return ri
       ri=access_index_server({'request':'PUT', 'path':path, 'dict':rdd})
       if ri['return']>0: return ri

    if o=='con':
       out('Entry was successfully renamed!')

    return {'return':0}

##############################################################################
# Common action: rename data entry -> calls 'ren' function
#
# TARGET: CK kernel and low-level developers

def rename(i):
    """
    Input:  { See ren function }
    Output: { See ren function }

    """

    return ren(i)

##############################################################################
# Common action: copy (or move) data entry
#
# TARGET: CK kernel and low-level developers

def cp(i):
    """
    Input:  {
              (repo_uoa)       - repo UOA
              module_uoa       - module UOA
              data_uoa         - data UOA

              xcids[0]         - {'repo_uoa', 'module_uoa', 'data_uoa'} - new CID
                 or
              (new_repo_uoa)   - new repo UOA
              (new_module_uoa) - new module UOA
              new_data_uoa     - new data alias
              (new_data_uid)   - new data UID (leave empty to generate new one)

              (move)           - if 'yes', remove old
              (keep_old_uid)   - if 'yes', keep old UID

              (without_files)  - if 'yes', do not move/copy files
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              Output of 'add' function
            }

    """

    move=i.get('move','')

    # Check if global writing is allowed
    r=check_writing({})
    if r['return']>0: return r

    import shutil

    o=i.get('out','')

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    if muoa=='': return {'return':1, 'error':'module UOA is not defined'}
    if duoa=='': return {'return':1, 'error':'data UOA is not defined'}

    # Attempt to load
    ii={'module_uoa':muoa, 'data_uoa':duoa}
    if ruoa!='': ii['repo_uoa']=ruoa
    r=load(ii)
    if r['return']>0: return r
    rdd=r
    muid=r['module_uid']

    duoa=r['data_uoa']
    duid=r['data_uid']

    p=r['path']

    dd=r.get('dict',{})
    di=r.get('info',{})
    du=r.get('updates',{})
    dx=r.get('desc',{})

    if move!='yes':
       control=di.get('control',{})

       control['version']=cfg['version']

       rdt=get_current_date_time({})
       control['iso_datetime']=rdt['iso_datetime']

       di['control']=control

    # Check if writing is allowed
    ruid=r['repo_uid']
    ii={'module_uoa':muoa, 'module_uid':r['module_uid'], 'repo_uoa':ruoa, 'repo_uid':ruid}
    r=check_writing(ii)
    if r['return']>0: return r

    # Check new CID
    nruoa=i.get('new_repo_uoa','')
    nmuoa=i.get('new_module_uoa','')
    nduoa=i.get('new_data_uoa','')
    nduid=i.get('new_data_uid','')

    xcids=i.get('xcids',[])
    if len(xcids)>0: 
       xcid=xcids[0]
       nduoa=xcid.get('data_uoa','')

       if nduoa=='': nduoa=duoa

       x=xcid.get('module_uoa','')
       if x!='': nmuoa=x

       x=xcid.get('repo_uoa','')
       if x!='': nruoa=x

    if i.get('keep_old_uid','')=='yes': nduid=duid

    if nmuoa=='': nmuoa=muoa
    if nruoa=='': nruoa=ruoa

    if cfg.get('allowed_entry_names','')!='':
       import re

       anames=cfg.get('allowed_entry_names','')

       if not re.match(anames, nduoa) or \
          not re.match(anames, nduid):
          return {'return':1, 'error':'found disallowed characters in names (allowed: "'+anames+'")'}

    if cfg.get('force_lower','')=='yes':
       nduoa=nduoa.lower()
       nduid=nduid.lower()
       nmuoa=nmuoa.lower()
       nruoa=nruoa.lower()

    # Adding new entry 
    if nruoa==ruoa and nmuoa==muoa and nduid==duid:
       return {'return':1, 'error':'moving within the same directory - use "rename" instead'}

    # Check if writing is allowed to the new repo
    ii={'repo_uoa':nruoa}
    r=check_writing(ii)
    if r['return']>0: return r

    rd=r.get('repo_dict',{})
    rshared=rd.get('shared','')
    rsync=rd.get('sync','')

    ii={'module_uoa':nmuoa, 'data_uoa': nduoa, 'dict':dd, 'info':di, 
        'updates':du, 'desc':dx, 'ignore_update':'yes'}
    if nduid!='': ii['data_uid']=nduid
    if nruoa!='': ii['repo_uoa']=nruoa
    r=add(ii)
    if r['return']>0: return r
    pn=r['path']
    nmuid=r['module_uid']

    # Recursively copying all files (except .cm)
    if i.get('without_files','')!='yes':
       rx=list_all_files({'path':p, 'all':'yes'})
       if rx['return']>0: return rx

       for q in rx['list']:
           if q.startswith('.cm'): continue

           p1=os.path.join(p,q)
           pn1=os.path.join(pn,q)

           # Create if dir
           pn1d=os.path.dirname(pn1)
           if not os.path.isdir(pn1d): os.makedirs(pn1d)

           shutil.copy(p1,pn1)

    if rshared!='' and rsync=='yes':
       ppp=os.getcwd()

       pp=os.path.split(pn)
       pp0=pp[0]
       pp1=pp[1]

       os.chdir(pp0)
       ss=cfg['repo_types'][rshared]['add'].replace('$#files#$', pp1)
       rx=os.system(ss)

       os.chdir(ppp)

    tt='copied'
    # If move, remove old one
    if move=='yes':
       tt='moved'

       ii={'module_uoa':muoa, 'data_uoa': duoa}
       if ruoa!='': ii['repo_uoa']=ruoa
       rx=rm(ii)
       if rx['return']>0: return rx

    # Check if index and add new
    if cfg.get('use_indexing','')=='yes' and index_module(muid,ruid):
       if is_uid(nduoa): nduid=nduoa
       path='/'+nmuid+'/'+nduid+'/1'
       ri=access_index_server({'request':'DELETE', 'path':path})
       if ri['return']>0: return ri
    if cfg.get('use_indexing','')=='yes' and index_module(muid,nruoa):
       ri=access_index_server({'request':'PUT', 'path':path, 'dict':rdd})
       if ri['return']>0: return ri

    if o=='con':
       out('Entry '+muoa+':'+duoa+' was successfully '+tt+'!')

    return r

##############################################################################
# Common action: copy (or move) data entry
#
# TARGET: CK kernel and low-level developers

def copy(i):
    """
    Input:  { See 'cp' function }
    Output: { See 'cp' function }

    """

    return cp(i)

##############################################################################
# Common action: move data entry
#
# TARGET: CK kernel and low-level developers

def mv(i):
    """
    Input:  {
              (repo_uoa)    - repo UOA
              module_uoa    - module UOA
              data_uoa      - data UOA

              xcids[0]         - {'repo_uoa', 'module_uoa', 'data_uoa'} - new CID
                 or
              (new_repo_uoa)   - new repo UOA
              (new_module_uoa) - new module UOA
              (new_data_uoa)   - new data alias
              (new_data_uid)   - new data UID (leave empty to generate new one)

            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              Output of 'copy' function
            }

    """

    # Check if global writing is allowed
    r=check_writing({'delete':'yes'})
    if r['return']>0: return r

    # Check if wild cards
    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')
    nduoa=i.get('new_data_uoa','')
    nduid=i.get('new_data_uid','')

    xcids=i.get('xcids',[])
    if len(xcids)>0: 
       xcid=xcids[0]
       nduoa=xcid.get('data_uoa','')

    if (duoa.find('*')>=0 or duoa.find('?')>=0) and nduoa=='' and nduid=='':
       r=list_data({'repo_uoa':ruoa, 'module_uoa':muoa, 'data_uoa':duoa})
       if r['return']>0: return r

       lst=r['lst']
    else:
       lst=[{'repo_uoa':ruoa, 'module_uoa':muoa, 'data_uoa':duoa}]

    i['move']='yes'
    i['keep_old_uid']='yes'

    r={'return':0}
    for ll in lst:
        i['repo_uoa']=ll['repo_uoa']
        i['module_uoa']=ll['module_uoa']
        i['data_uoa']=ll['data_uoa']
        r=copy(i)
        if r['return']>0: return r

    return r

##############################################################################
# Common action: move data entry
#
# TARGET: CK kernel and low-level developers

def move(i):
    """
    Input:  { See 'mv' function }
    Output: { See 'mv' function }

    """

    return mv(i)

##############################################################################
# Common action: delete file from an entry
#
# TARGET: CK kernel and low-level developers

def delete_file(i):
    """
    Input:  {
              (repo_uoa)  - repo UOA
              module_uoa  - module UOA
              data_uoa    - data UOA

              filename    - filename to delete including relative path
              (force)     - if 'yes', force deleting without questions
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Check if global writing is allowed
    r=check_writing({'delete':'yes'})
    if r['return']>0: return r

    o=i.get('out','')

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    # Check file
    fn=i.get('filename','')
    if fn=='':
       x=i.get('cids',[])
       if len(x)>0:
          fn=x[0]

    if fn=='':
       return {'return':1, 'error':'filename is empty'}

    if duoa=='':
       return {'return':1, 'error':'data UOA is not defined'}

    if fn=='':
       return {'return':1, 'error':'filename is not defined'}

    # Get info about entry
    r=load({'repo_uoa':ruoa, 'module_uoa':muoa, 'data_uoa':duoa})
    if r['return']>0: return r

    p=r['path']

    ruoa=r['repo_uoa']
    ruid=r['repo_uid']

    # Check repo/module writing
    ii={'module_uoa':muoa, 'repo_uoa':ruoa, 'repo_uid':ruid}
    r=check_writing(ii)
    if r['return']>0: return r

    rd=r.get('repo_dict',{})
    rshared=rd.get('shared','')
    rsync=rd.get('sync','')

    p1=os.path.normpath(os.path.join(p, fn))
    px=os.path.normpath(os.path.join(p, cfg['subdir_ck_ext']))

    if p1.startswith(px):
       return {'return':1, 'error':'path points to the special directory with meta info'}

    if not p1.startswith(p):
       return {'return':1, 'error':'path is outside entry'}

    if not os.path.isfile(p1) and not os.path.isdir(p1):
       return {'return':1, 'error':'file or directory is not found'}

    p2=os.path.split(p1)
    px0=p2[0]
    px1=p2[1]

    if rshared!='':
       ppp=os.getcwd()
       os.chdir(px0)

       ss=cfg['repo_types'][rshared]['rm'].replace('$#files#$', px1)
       rx=os.system(ss)

    if os.path.isfile(p1):
       os.remove(p1)

    if os.path.isdir(p1):
       import shutil
       shutil.rmtree(p1, onerror=rm_read_only)

    if rshared!='':
       os.chdir(ppp)

    return {'return':0}

##############################################################################
# Common action: list data entries
#
# TARGET: CK kernel and low-level developers

def list_data(i):
    """
    Input:  {
              (repo_uoa)           - repo UOA
              (module_uoa)         - module UOA
              (data_uoa)           - data UOA

              (repo_uoa_list)      - list of repos to search
              (module_uoa_list)    - list of module to search
              (data_uoa_list)      - list of data to search

              (filter_func)        - name of filter function
              (filter_func_addr)   - address of filter function

              (add_if_date_before) - add only entries with date before this date 
              (add_if_date_after)  - add only entries with date after this date
              (add_if_date)        - add only entries with this date

              (ignore_update)      - if 'yes', do not add info about update (when updating in filter)

              (search_by_name)     - search by name

              (search_dict)        - search if this dict is a part of the entry

              (ignore_case)        - ignore case when searching!

              (print_time)         - if 'yes', print elapsed time at the end

              (do_not_add_to_lst)  - if 'yes', do not add entries to lst

              (time_out)           - in secs, default=30 (if -1, no timeout)

              (limit_size)         - if !='' limit size

              (print_full)         - if 'yes', show CID (repo_uoa:module_uoa:data_uoa)
                  or
              (all)

              (print_uid)          - if 'yes', print UID in brackets

              (print_name)         - if 'yes', print name (and add info to the list)
                  or
              (name)

              (add_info)           - if 'yes', add info about entry to the list
              (add_meta)           - if 'yes', add meta about entry to the list
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              lst          - [{'repo_uoa', 'repo_uid',
                               'module_uoa', 'module_uid', 
                               'data_uoa','data_uid',
                               'path' (,info) 
                               }]

              elapsed_time - elapsed time in string

              (timed_out)  - if 'yes', timed out or limited by size
            }

    """

    import time
    start_time = time.time()

    xls=i.get('limit_size','')
    if xls=='': xls='0'
    ls=int(xls)
    ils=0

    lst=[]

    o=i.get('out','')

    debug=(cfg.get('debug','').lower()=='yes' or cfg.get('debug','').lower()=='1')

    iu=i.get('ignore_update', '')

    prf=i.get('print_full','')
    if prf=='': prf=i.get('all','')
    iprf=(prf=='yes')

    prn=i.get('print_name','')
    if prn=='': prn=i.get('name','')
    iprn=(prn=='yes')

    ipru=(i.get('print_uid','')=='yes')

    # Add info about entry to the final list 
    # (particularly when searching by special keywords, 
    # such as name or date of creation

    iaf=(i.get('add_info','')=='yes')

    iam=(i.get('add_meta','')=='yes')

    aidb=i.get('add_if_date_before','')
    aida=i.get('add_if_date_after','')
    aid=i.get('add_if_date','')

    # Support ISO and human readable time
    aidb=aidb.strip().replace(' ','T')
    aida=aida.strip().replace(' ','T')
    aid=aid.strip().replace(' ','T')

    oaidb=None
    oaida=None
    oaid=None

    sn=i.get('search_by_name','')


    if aidb!='' or aida!='' or aid!='':

       import datetime
       if aidb!='': 
          rx=convert_iso_time({'iso_datetime':aidb})
          if rx['return']>0: return rx
          oaidb=rx['datetime_obj']
       if aida!='': 
          rx=convert_iso_time({'iso_datetime':aida})
          if rx['return']>0: return rx
          oaida=rx['datetime_obj']
       if aid!='':  
          rx=convert_iso_time({'iso_datetime':aid})
          if rx['return']>0: return rx
          oaid=rx['datetime_obj']

    if oaidb!=None or oaida!=None or oaid!=None or sn!='': 
       iaf=True

    dnatl=i.get('do_not_add_to_lst','')
    idnatl=False
    if dnatl=='yes': idnatl=True

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    muid=i.get('module_uid','')
    duoa=i.get('data_uoa','')

    lruoa=i.get('repo_uoa_list',[])
    lmuoa=i.get('module_uoa_list',[])
    lduoa=i.get('data_uoa_list',[])

    # Check if need to force lower case for all entries
    if cfg.get('force_lower','')=='yes':
       ruoa=ruoa.lower()
       muoa=muoa.lower()
       muid=muid.lower()
       duoa=duoa.lower()

       lruoa=lower_list(lruoa)
       lmuoa=lower_list(lmuoa)
       lduoa=lower_list(lduoa)

    to=float(i.get('time_out','30'))
    elapsed_time=0

    if duoa=='': duoa='*'
    if muoa=='' and muid=='': muoa='*'
    if ruoa=='': ruoa='*'

    sff=i.get('filter_func','')
    ff=i.get('filter_func_addr',None)
    if sff!='':
       ff=getattr(sys.modules[__name__], sff)
    if ff!=None:
       sd=i.get('search_dict',{})
       ic=i.get('ignore_case','')
       ss=i.get('search_string','')
       if ic=='yes': ss=ss.lower()

    # Check if wild cards present (only repo or data)
    wr=''
    wm=''
    wd=''

    if ruoa.find('*')>=0 or ruoa.find('?')>=0: wr=ruoa
    if muoa.find('*')>=0 or muoa.find('?')>=0: wm=muoa
    if duoa.find('*')>=0 or duoa.find('?')>=0: wd=duoa

    if wr!='' or wm!='' or wd!='':
       import fnmatch

    zr={}

    fixed_repo=False
    if ruoa!='' and wr=='':
       # Try to load a given repository
       r=access({'action':'load',
                 'module_uoa':cfg['repo_name'],
                 'data_uoa':ruoa,
                 'common_func':'yes'})
       if r['return']>0: return r
       duid=r['data_uid']

       zr[duid]=r
       fixed_repo=True
    else:
       # Prepare all repositories
       r=reload_repo_cache({}) # Ignore errors
       if r['return']>0: return r
       zr=cache_repo_info

    # Start iterating over repositories
    ir=0
    iir=True
    zrk=list(zr.keys())
    lr=len(zrk)
    finish=False
    while iir:
       skip=False
       repo_dict={}

       if fixed_repo:
          if ir>0:
             skip=True
             iir=False
          else:
             ruid=zrk[0]
             d=zr[ruid]
             dd=d.get('dict',{})
             repo_dict=dd
             remote=dd.get('remote','')
             if remote=='yes':
                skip=True
             else:
                ruoa=d.get('data_uoa','')
                p=dd.get('path','')
                if ruid==cfg['repo_uid_default']: p=work.get('dir_default_repo','')
                elif ruid==cfg['repo_uid_local']: p=work.get('dir_local_repo','')
       elif ir==0:
          ruoa=cfg['repo_name_default']
          ruid=cfg['repo_uid_default']
          p=work.get('dir_default_repo','')
       elif ir==1:
          ruoa=cfg['repo_name_local']
          ruid=cfg['repo_uid_local']
          p=work.get('dir_local_repo','')
          if p=='': 
             skip=True
       else:
          if ir<lr+2:
             ruid=zrk[ir-2]
             d=zr[ruid]
             dd=d.get('dict',{})
             repo_dict=dd
             remote=dd.get('remote','')
             if remote=='yes':
                skip=True
             else:
                ruoa=d.get('data_uoa','')
                p=dd.get('path','')
          else:
             skip=True
             iir=False

       # Check if wild cards
       if not skip and p!='' and wr!='':
          if len(lruoa)>0 and (ruoa not in lruoa and ruid not in lruoa):
             skip=True
          elif wr=='*':
             pass
          elif is_uid(ruoa): 
             skip=True # If have wildcards, but not alias
          elif not fnmatch.fnmatch(ruoa, wr):
             skip=True

       # Check if got proper path
       if not skip and p!='':
          # Prepare modules in the current directory
          xm=[]

          if muoa!='' and wm=='': 
             xm.append(muoa)
          else:   
             # Now iterate over modules inside a given path
             try:
                lm=os.listdir(p)
             except Exception as e:
                None
             else:
                for fn in lm:
                    if os.path.isdir(os.path.join(p,fn)) and fn not in cfg['special_directories']:
                       xm.append(fn)

          # Iterate over modules
          for mu in xm:
              r=find_path_to_entry({'path':p, 'data_uoa':mu})
              if r['return']==0:
                 mp=r['path']
                 muid=r['data_uid']
                 muoa=r['data_uoa']

                 # Check if there is a split of directories for this module in local config
                 # to handle numerous entries (similar to MediaWiki)
                 split_dirs=get_split_dir_number(repo_dict, muid, muoa)

                 mskip=False

                 if wm!='':
                    if len(lmuoa)>0 and (muoa not in lmuoa and muid not in lmuoa):
                       mskip=True
                    elif wm=='*':
                       pass
                    elif is_uid(muoa): 
                       mskip=True # If have wildcards, but not alias
                    elif not fnmatch.fnmatch(muoa, wm):
                       mskip=True

                 if not mskip:
                    # Prepare data in the current directory
                    xd=[]

                    if duoa!='' and wd=='': 
                       iii={'path':mp, 'data_uoa':duoa}
                       if split_dirs!=0:
                          iii['split_dirs']=split_dirs
                       r=find_path_to_entry(iii)
                       if r['return']==0:
                          xd.append(duoa)
                    else:   
                       # Now iterate over data inside a given path
                       try:
                          ld=os.listdir(mp)
                       except Exception as e:
                          None
                       else:
                          for fn in ld:
                              if os.path.isdir(os.path.join(mp,fn)) and fn not in cfg['special_directories']:
                                 if split_dirs!=0:
                                    mp2=os.path.join(mp,fn)
                                    try:
                                       ld2=os.listdir(mp2)
                                    except Exception as e:
                                       None

                                    for fn in ld2:
                                        if os.path.isdir(os.path.join(mp2,fn)) and fn not in cfg['special_directories']:
                                           xd.append(fn)
                                 else:
                                    xd.append(fn)

                    # Iterate over data
                    if len(lduoa)>0:
                       xd=lduoa

                    for du in xd:
                        iii={'path':mp, 'data_uoa':du}
                        if split_dirs!=0:
                           iii['split_dirs']=split_dirs
                        r=find_path_to_entry(iii)
                        if r['return']!=0: continue

                        dp=r['path']
                        dpcfg=os.path.join(dp,cfg['subdir_ck_ext'])
                        dpinfo=os.path.join(dp,cfg['subdir_ck_ext'],cfg['file_info'])
                        dpmeta=os.path.join(dp,cfg['subdir_ck_ext'],cfg['file_meta'])
                        tduid=r['data_uid']
                        tduoa=r['data_uoa']

                        if os.path.isdir(dpcfg): # Check if really CK data entry
                           dskip=False

                           if wd!='':
                              if len(lduoa)>0 and (tduoa not in lduoa and tduid not in lduoa):
                                 dskip=True
                              elif wd=='*':
                                 pass
#                              elif is_uid(tduoa): 
#                                 dskip=True # If have wildcards, but not alias
                              elif not fnmatch.fnmatch(tduoa, wd):
                                 dskip=True

                           if not dskip:
                              # Iterate over data 
                              ll={'repo_uoa':ruoa, 'repo_uid':ruid,
                                 'module_uoa':muoa, 'module_uid':muid,
                                 'data_uoa':tduoa, 'data_uid':tduid,
                                 'path':dp}

                              # Need to load info?
                              if iaf or iprn:
                                 if os.path.isfile(dpinfo):
                                    y=load_json_file({'json_file':dpinfo})
                                    if y['return']>0: 
                                       if not debug: continue
                                       return y
                                    ll['info']=y['dict']

                              # Need to load meta?
                              if iam:
                                 if os.path.isfile(dpmeta):
                                    y=load_json_file({'json_file':dpmeta})
                                    if y['return']>0: 
                                       if not debug: continue
                                       return y
                                    ll['meta']=y['dict']

                              # Call filter
                              fskip=False

                              if ff!=None and ff!='':
                                 ll['out']=o
                                 ll['search_dict']=sd
                                 ll['search_string']=ss
                                 ll['ignore_case']=ic
                                 ll['ignore_update']=iu

                                 if oaidb!=None: ll['obj_date_before']=oaidb
                                 if oaida!=None: ll['obj_date_after']=oaida
                                 if oaid!=None: ll['obj_date']=oaid
                                 if sn!=None: ll['search_by_name']=sn

                                 rx=ff(ll)
                                 if rx['return']>0: 
                                    if not debug: continue
                                    return rx

                                 if rx.get('skip','')=='yes':
                                    fskip=True

                              # Append
                              if not fskip:
                                 ils+=1
 
                                 if not idnatl:
                                    lst.append(ll)

                                    if log_ck_entries:
                                       lce=cfg.get('log_ck_entries','')
                                       if lce!='':
                                          rl=save_text_file({'text_file':lce,
                                                             'string':'"action":"list", "repo_uoa":"'+
                                                                      ll.get('repo_uoa','')+'", "repo_uid":"'+
                                                                      ll.get('repo_uid','')+'", "module_uoa":"'+
                                                                      ll.get('module_uoa','')+'", "module_uid":"'+
                                                                      ll.get('module_uid','')+'", "data_uoa":"'+
                                                                      ll.get('data_uoa','')+'", "data_uid":"'+
                                                                      ll.get('data_uid','')+'"\n',
                                                             'append':'yes'})
                                          if rl['return']>0: return rl

                                 if o=='con':
                                    x=''
                                    if iprf: x=ruoa+':'+muoa+':'
                                    if sys.version_info[0]<3: 
                                       y=tduoa
                                       try: y=y.decode(sys.stdin.encoding)
                                       except Exception as e: 
                                         try: y=y.decode('utf8')
                                         except Exception as e: pass
                                       x+=y
                                    else: x+=tduoa
                                    if ipru: x+=' ('+tduid+')'
                                    if iprn:
                                       name=ll.get('info',{}).get('data_name','')
                                       if name!='':
                                          x=name+' ('+x+')'
                                    out(x)

                              # Check timeout
                              elapsed_time = time.time() - start_time
                              if to!=-1 and elapsed_time>to:
                                 finish=True
                                 break

                              # Check size
                              if ls>0 and ils==ls:
                                 finish=True
                                 break

                    if finish: break
          if finish: break

       # Finish iteration over repositories
       ir+=1

    if o=='con' and i.get('print_time','')=='yes':
       out('Elapsed time: '+str(elapsed_time)+' sec., number of entries: '+str(ils))

    rr={'return':0, 'lst':lst, 'elapsed_time':str(elapsed_time)}
    if finish: rr['timed_out']='yes'

    return rr

##############################################################################
# List data with search

def list_data2(i):
    o=i.get('out','')

    rr=list_data(i)

    lst=rr['lst']
    if len(lst)==0 and cfg.get('download_missing_components','')=='yes':
       # Search on cKnowledge.org
       import copy

       oo=''
       if o=='con': oo=o

       muoa=i.get('module_uoa','')
       duoa=i.get('data_uoa','')

#       out('')
#       out('  WARNING: checking missing components "'+muoa+':'+duoa+'" at the CK portal ...')

       # Try to download missing action/module
       ry=download({'module_uoa':muoa,
                    'data_uoa':duoa,
                    'out':'con'})
       if ry['return']>0: return ry

       # Restart local search
       rr=list_data(i)

    return rr

##############################################################################
# Common action: search entries
#
# TARGET: CK kernel and low-level developers

def search(i):
    """
    Input:  {
              (repo_uoa)           - repo UOA
              (module_uoa)         - module UOA
              (data_uoa)           - data UOA

              (repo_uoa_list)      - list of repos to search
              (module_uoa_list)    - list of module to search
              (data_uoa_list)      - list of data to search

              (add_if_date_before) - add only entries with date before this date 
              (add_if_date_after)  - add only entries with date after this date
              (add_if_date)        - add only entries with this date

              (search_by_name)     - search by name

              (print_time)         - if 'yes', print elapsed time at the end

              (search_flat_dict)   - search if these flat keys/values exist in entries
              (search_dict)        - search if this dict is a part of the entry
              (tags)               - add tags to search in format tags=x,y,z
                   or
              (search_string)      - search with expressions *?

              (ignore_case)        - if 'yes', ignore case of letters

              (time_out)           - in secs, default=30

              (internal)           - if 'yes', use internal search even if indexing is on

              (limit_size)         - by default 5000 or -1 if no limit
              (start_from)         - start from a specific entry (only for ElasticSearch)

              (print_full)         - if 'yes', show CID (repo_uoa:module_uoa:data_uoa)
              (print_uid)          - if 'yes', print UID in brackets

              (print_name)         - if 'yes', print name (and add info to the list)
              (add_info)           - if 'yes', add info about entry to the list
              (add_meta)           - if 'yes', add meta about entry to the list

              (debug)              - if 'yes', print debug info
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              lst          - [{'repo_uoa', 'repo_uid',
                               'module_uoa', 'module_uid', 
                               'data_uoa','data_uid',
                               'path'}]
              elapsed_time - elapsed time in string

              (timed_out)  - if 'yes', timed out
            }

    """

    o=i.get('out','')

    rr=search2(i)
    if rr['return']>0: return rr

    lst=rr['lst']
    if len(lst)==0 and cfg.get('download_missing_components','')=='yes':
       # Search on cKnowledge.org
       import copy

       oo=''
       if o=='con': oo=o

       muoa=i.get('module_uoa','')
       duoa=i.get('data_uoa','')

#       out('')
#       out('  WARNING: checking missing components "'+muoa+':'+duoa+'" at the CK portal ...')

       ry=download({'module_uoa':muoa,
                    'data_uoa':duoa,
                    'out':'con'})
       if ry['return']>0: return ry

       # Restart local search
       rr=search2(i)

    return rr

##############################################################################
# Original search

def search2(i):

    o=i.get('out','')

    ss=i.get('search_string','')
    sd=i.get('search_dict',{})

    ls=i.get('limit_size','5000')

    rr={'return':0}

    # Check tags
    tags=i.get('tags','')
    if tags!='':
       xtags=tags.split(',')
       xtags1=[]
       for q in xtags:
           xtags1.append(q.strip())
       sd['tags']=xtags1

    # Check if index
    if i.get('internal','')=='yes' or cfg.get('use_indexing','')!='yes' or (i.get('module_uoa','')!='' and not index_module(i['module_uoa'],i.get('repo_uoa',''))):
       if ss!='':
          i['filter_func']='search_string_filter'
       else:
          sfd=i.get('search_flat_dict',{})

          if len(sfd)>0:
             r=restore_flattened_dict({'dict':sfd})
             if r['return']>0: return r

             nd=r['dict']

             sd.update(nd)

             del (i['search_flat_dict'])

          i['filter_func']='search_filter'

       i['search_dict']=sd

       pf=i.get('print_full','')
       if pf=='': pf='yes'
       i['print_full']=pf

       rr=list_data(i)
    else:
       import time
       start_time = time.time()

       b_add_meta=(i.get('add_meta','')=='yes')
       b_add_info=(i.get('add_info','')=='yes')

       # Check if using ElasticSearch via Python client
       eec=False 
       if cfg.get('index_use_curl','')=='yes' or cfg.get('index_use_web','')=='yes':
          eec=True

       dss={} # Used with python ElasticSearch client

       ruoa=i.get('repo_uoa','')
       muoa=i.get('module_uoa','')
       duoa=i.get('data_uoa','')

       lruoa=i.get('repo_uoa_list',[])
       lmuoa=i.get('module_uoa_list',[])
       lduoa=i.get('data_uoa_list',[])

       if ruoa!='': lruoa.append(ruoa)
       if muoa!='': lmuoa.append(muoa)
       if duoa!='': lduoa.append(duoa)

       if len(lruoa)>0:
          if ss!='': ss+=' AND '
          ss+=' ('
          first=True
          for x in lruoa:
              if first: first=False
              else: ss+=' OR '

              xx1='"'
              if x.find('*')>=0 or x.find('?')>=0:
                 xx1=''

              ss+='(repo_uid:'+xx1+x+xx1+') OR (repo_uoa:'+xx1+x+xx1+')'
          ss+=')'

       if len(lmuoa)>0:
          if ss!='': ss+=' AND '
          ss+='('
          first=True
          for x in lmuoa:
              if first: first=False
              else: ss+=' OR '

              xx1='"'
              if x.find('*')>=0 or x.find('?')>=0:
                 xx1=''

              ss+='(module_uid:'+xx1+x+xx1+') OR (module_uoa:'+xx1+x+xx1+')'
          ss+=')'

       if len(lduoa)>0:
          if ss!='': ss+=' AND '
          ss+='('
          first=True
          for x in lduoa:
              if first: first=False
              else: ss+=' OR '

              xx1='"'
              if x.find('*')>=0 or x.find('?')>=0:
                 xx1=''

              ss+='(data_uid:'+xx1+x+xx1+') OR (data_uoa:'+xx1+x+xx1+')'
          ss+=')'

       # Check search keys
       first=True
       for u in sd:
           v=sd[u]

           if first: 
              first=False
              if ss=='': ss+='('
              else: ss+=' AND ('
           else: 
              ss+=' AND '

           if type(v)==list:
              first1=True
              for lk in v:
                  if first1:
                     first1=False
                  else:
                     ss+=' AND '

                  x=str(lk)

                  xx1='"'
                  if x.find('*')>=0 or x.find('?')>=0:
                     xx1=''

                  ss+=u+':'+xx1+x+xx1
           else:
              x=str(v)

              xx1='"'
              if x.find('*')>=0 or x.find('?')>=0:
                 xx1=''

              ss+=u+':'+xx1+x+xx1

       # Check special parameters
       aidb=i.get('add_if_date_before','')
       aida=i.get('add_if_date_after','')
       aid=i.get('add_if_date','')

       # Support ISO and human readable time
       aidb=aidb.strip().replace(' ','T')
       aida=aida.strip().replace(' ','T')
       aid=aid.strip().replace(' ','T')

       sn=i.get('search_by_name','')

       if sn!='':
          if first: 
             first=False
             if ss=='': ss+='('
             else: ss+=' AND ('
          else: 
             ss+=' AND '

          xx1='"'
          if sn.find('*')>=0 or sn.find('?')>=0:
             xx1=''

          ss+='data_name:'+xx1+sn+xx1

       if aidb!='' or aida!='' or aid!='':
          if first: 
             first=False
             if ss=='': ss+='('
             else: ss+=' AND ('
          else: 
             ss+=' AND '

          ss+='iso_datetime:'

          if aid!='': 
             ss+='"'+aid+'"'
          else:
             ss+='['
             if aida!='': 
                ss+='"'+aida+'"'
             else:
                ss+='*'
             if aidb!='':
                ss+=' TO "'+aidb+'"'
             ss+='] '

       # Finish query
       if not first:
          ss+=')'

       # Prepare ElasticSearch query
       try:
         import urllib.parse as ur
       except Exception as e:
         import urllib as ur

       path='/_search?'
       if ss!='': path+='q='+ur.quote_plus(ss.encode('utf-8'))
       if ls!='': path+='&size='+ls

#       dss={'query':{'filtered':{'filter':{'terms':sd}}}}
       dss={}

       if i.get('debug','')=='yes':
          out('Query string: '+ss)
          out('')

       ri=access_index_server({'request':'GET', 
                               'path':path, 
                               'dict':dss, 
                               'original_string':ss, 
                               'limit_size':ls, 
                               'start_from':i.get('start_from','')})
       if ri['return']>0: return ri

       dd=ri['dict'].get('hits',{}).get('hits',[])

       lst=[]
       for qx in dd:
           q=qx.get('_source',{})
           ruoa=q.get('repo_uoa','')
           ruid=q.get('repo_uid','')
           muoa=q.get('module_uoa','')
           muid=q.get('module_uid','')
           duoa=q.get('data_uoa','')
           duid=q.get('data_uid','')
           path=q.get('path','')

           to_add={'repo_uoa':ruoa, 'repo_uid':ruid,
              'module_uoa':muoa, 'module_uid':muid,
              'data_uoa':duoa, 'data_uid':duid,
              'path':path}

           if b_add_meta: to_add['meta']=q.get('dict')
           if b_add_info: to_add['info']=q.get('dict')

           lst.append(to_add)

           if log_ck_entries:
              lce=cfg.get('log_ck_entries','')
              if lce!='':
                 rl=save_text_file({'text_file':lce,
                                    'string':'"action":"find", "repo_uoa":"'+
                                             ruoa+'", "repo_uid":"'+
                                             ruid+'", "module_uoa":"'+
                                             muoa+'", "module_uid":"'+
                                             muid+'", "data_uoa":"'+
                                             duoa+'", "data_uid":"'+
                                             duid+'"\n',
                                    'append':'yes'})
                 if rl['return']>0: return rl

           if o=='con':
              x=ruoa+':'+muoa+':'
              if sys.version_info[0]<3: 
                 y=duoa
                 try: y=y.decode(sys.stdin.encoding)
                 except Exception as e: 
                   try: y=y.decode('utf8')
                   except Exception as e: pass
                 x+=y
              else: x+=duoa
              out(x)

       rr['lst']=lst
       rr['elapsed_time']=str(time.time() - start_time)

       if o=='con' and i.get('print_time','')=='yes':
          out('Elapsed time: '+rr['elapsed_time']+' sec., number of entries: '+str(len(lst)))

    return rr


##############################################################################
# Search filter
#
# TARGET: CK kernel and low-level developers

def search_filter(i):
    """
    Input:  {
              repo_uoa             - repo UOA
              module_uoa           - module UOA
              data_uoa             - data UOA
              path                 - path  

              (search_dict)        - search if this dict is a part of the entry
              (ignore_case)        - if 'yes', ignore case of letters
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              lst          - [{'repo_uoa', 'repo_uid',
                               'module_uoa', 'module_uid', 
                               'data_uoa','data_uid',
                               'path'}]
            }

    """

    ic=i.get('ignore_case','')

    # Check special info
    info=i.get('info',{})
    if len(info)!='':
       oaidb=i.get('obj_date_before', None)
       oaida=i.get('obj_date_after', None)
       oaid=i.get('obj_date', None)
       sn=i.get('search_by_name','')

       # Check dates
       if oaidb!=None or oaida!=None or oaid!=None:
          idt=info.get('control',{}).get('iso_datetime','')
          if idt!='':
             rx=convert_iso_time({'iso_datetime':idt})
             if rx['return']>0: return rx
             oidt=rx['datetime_obj']

             if oaidb!=None and oidt>oaidb: return {'return':0, 'skip':'yes'}
             if oaida!=None and oidt<oaida: return {'return':0, 'skip':'yes'}
             if oaid!=None and oidt!=oaid: return {'return':0, 'skip':'yes'}

       # Check if search by name
       if sn!='':
          ro=find_string_in_dict_or_list({'dict':{'string':info.get('data_name','')}, 
                                          'search_string':sn,
                                          'ignore_case':ic})
          if ro['return']>0: return ro
          if ro['found']!='yes': return {'return':0, 'skip':'yes'}

    # To be fast, load directly
    p=i['path']

    skip='yes'

    sd=i.get('search_dict',{})

    p1=os.path.join(p,cfg['subdir_ck_ext'],cfg['file_meta'])
    if not os.path.isfile(p1):
       p1=os.path.join(p,cfg['subdir_ck_ext'],cfg['file_meta_old'])
       if not os.path.isfile(p1):
          return {'return':0, 'skip':'yes'}

    r=load_json_file({'json_file':p1})
    if r['return']>0: return r
    d=r['dict']

    # Check directly
    rx=compare_dicts({'dict1':d, 'dict2':sd, 'ignore_case':ic})
    if rx['return']>0: return rx
    equal=rx['equal']
    if equal=='yes': skip='no'

    return {'return':0, 'skip':skip}

##############################################################################
# Compare 2 dictionaries (recursively)
#
# TARGET: end users

def compare_dicts(i):
    """
    Input:  {
              dict1         - dictionary 1
              dict2         - dictionary 2
              (ignore_case) - ignore case of letters

              Note that if dict1 and dict2 has lists, the results will be as follows:

              * dict1={"key":['a','b','c']}
                dict2={"key":['a','b']}
                EQUAL

              * dict1={"key":['a','b']}
                dict2={"key":['a','b','c']}
                NOT EQUAL
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              equal        - if 'yes' dictionaries are equal
            }
    """

    d1=i.get('dict1',{})
    d2=i.get('dict2',{})

    equal='yes'

    bic=False
    ic=i.get('ignore_case','')
    if ic=='yes': bic=True

    for q2 in d2:
        v2=d2[q2]
        if type(v2)==dict:
           if q2 not in d1:
              equal='no'
              break

           v1=d1[q2]

           rx=compare_dicts({'dict1':v1,'dict2':v2, 'ignore_case':ic})
           if rx['return']>0: return rx
           equal=rx['equal']
           if equal=='no':
              break
        elif type(v2)==list:
           # For now can check only values in list
           if q2 not in d1:
              equal='no'
              break

           v1=d1[q2]

           if type(v1)!=list:
              equal='no'
              break

           for m in v2:
               if m not in v1:
                  equal='no'
                  break

           if equal=='no':
              break
        else:
           if q2 not in d1:
              equal='no'
              break

           if equal=='no':
              break

           v1=d1[q2]

           if bic and type(v1)!=int and type(v1)!=float and type(v1)!=bool: 
              v1=v1.lower()
              v2=v2.lower()

           if v2!=v1:
              equal='no'
              break

    return {'return':0, 'equal':equal}

##############################################################################
# Compare two flat dictionaries
#
# TARGET: end users

def compare_flat_dicts(i):
    """
    Input:  {
              dict1            - dictionary 1
              dict2            - dictionary 2
              (ignore_case)    - ignore case of letters
              (space_as_none)  - if 'yes', consider "" as None
              (keys_to_ignore) - list of keys to ignore (can be wildcards)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              equal        - if 'yes' dictionaries are equal
            }
    """

    d1=i.get('dict1',{})
    d2=i.get('dict2',{})

    equal='yes'

    ic=False
    x=i.get('ignore_case','')
    if x=='yes': ic=True

    san=None
    x=i.get('space_as_none','')
    if x=='yes': san=''

    # Create common set of keys
    keys=list(d1.keys())
    for q in d2:
        if q not in keys:
           keys.append(q)

    # If keys to ignore
    kti=i.get('keys_to_ignore',[])
    if len(kti)>0:
       import fnmatch

       x=[]
       for q in keys:
           skip=False
           for k in kti:
               if fnmatch.fnmatch(q,k):
                  skip=True
           if not skip:
              x.append(q)
       keys=x

    # Compare all keys
    for q in keys:
        v1=d1.get(q, san)
        v2=d2.get(q, san)

        if ic and type(v1)!=int and type(v1)!=float and type(v1)!=bool: 
           v1=v1.lower()
           v2=v2.lower()

        if v1!=v2:
           equal='no'
           break

    return {'return':0, 'equal':equal}

##############################################################################
# Find string in dict
#
# TARGET: end users

def find_string_in_dict_or_list(i):
    """
    Input:  {
              dict            - dictionary 1
              (search_string) - search string
              (ignore_case)   - ignore case of letters
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              found        - if 'yes', string found
            }
    """

    d=i.get('dict',{})

    found='no'

    wc=False
    ss=i.get('search_string','')
    if ss.find('*')>=0 or ss.find('?')>=0:
       wc=True
       import fnmatch

    bic=False
    ic=i.get('ignore_case','')
    if ic=='yes': 
       bic=True
       ss=ss.lower()

    for q in d:
        if type(d)==dict:   v=d[q]
        elif type(d)==list: v=q
        else:               v=str(q)

        if type(v)==dict or type(v)==list:
           rx=find_string_in_dict_or_list({'dict':v, 'search_string':ss, 'ignore_case':ic})
           if rx['return']>0: return rx
           found=rx['found']
           if found=='yes':
              break
        else:
           try: v=str(v)
           except Exception as e: pass

           if bic: 
              v=v.lower()

           if (wc and fnmatch.fnmatch(v, ss)) or v==ss:
              found='yes'
              break

    return {'return':0, 'found':found}

##############################################################################
# Search filter
#
# TARGET: CK kernel and low-level developers

def search_string_filter(i):
    """
    Input:  {
              repo_uoa             - repo UOA
              module_uoa           - module UOA
              data_uoa             - data UOA
              path                 - path  

              (search_string)      - search with expressions *?
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              lst          - [{'repo_uoa', 'repo_uid',
                               'module_uoa', 'module_uid', 
                               'data_uoa','data_uid',
                               'path'}]
            }

    """

    # To be fast, load directly
    p=i['path']

    skip='yes'

    ss=i.get('search_string','')
    if ss=='':
       skip='no'
    else:
       ic=i.get('ignore_case','')

       p1=os.path.join(p,cfg['subdir_ck_ext'],cfg['file_meta'])
       if not os.path.isfile(p1):
          p1=os.path.join(p,cfg['subdir_ck_ext'],cfg['file_meta_old'])
          if not os.path.isfile(p1):
             return {'return':0, 'skip':'yes'}

       r=load_json_file({'json_file':p1})
       if r['return']>0: return r
       d=r['dict']

       # Check directly
       rx=find_string_in_dict_or_list({'dict':d, 'search_string':ss, 'ignore_case':ic})
       if rx['return']>0: return rx
       found=rx['found']
       if found=='yes': skip='no'

    return {'return':0, 'skip':skip}

##############################################################################
# Access index server
#
# TARGET: CK kernel and low-level developers

def access_index_server(i):
    """
    Input:  {
              request        - request type ('PUT' | 'DELETE' | 'TEST' | 'GET')
              (path)         - path  
              (dict)         - query as dict to send
              (limit_size)   - limit queries with this number (if 'GET')
              (start_from)   - start from a given entry in a query
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              dict         - returned dict
            }

    """

    request=i['request']

    # Prepare URL
    host=cfg.get('index_host','')
    if host=='':
       return {'return':1, 'error':'index host is not defined in configuration'}

    url=host
    port=cfg.get('index_port','')
    if port!='':
       url+=':'+port

    path=i.get('path','')
    xpath=path.split('/')

    dd=i.get('dict',{})
    ddo={}

    if cfg.get('index_use_curl','')=='yes':
       url+=path

       import tempfile

       fd1, fn1=tempfile.mkstemp(suffix='.tmp', prefix='ck-')
       os.close(fd1)
       os.remove(fn1)

       fd2, fn2=tempfile.mkstemp(suffix='.tmp', prefix='ck-')
       os.close(fd2)
       os.remove(fn2)

       r=save_json_to_file({'json_file':fn1, 'dict':dd})
       if r['return']>0: return r

       cmd='curl -X'+request+' '+url+' -d @'+fn1+' -s -o '+fn2
       os.system(cmd)

       # Read output
       if not os.path.isfile(fn2):
          return {'return':1, 'error':'problem accessing indexing server - maybe indexing server is down?'}

       r=load_json_file({'json_file':fn2})

       if os.path.isfile(fn1): os.remove(fn1)
       if os.path.isfile(fn2): os.remove(fn2)

       if r['return']>0: return r
       ddo=r['dict']
    elif cfg.get('index_use_web','')=='yes':
       url+=path

       try:
          import urllib.request as urllib2
       except:
          import urllib2

       try:
          from urllib.parse import urlencode
       except:
          from urllib import urlencode

       # Prepare post variables
       r=dumps_json({'dict':dd, 'skip_indent':'yes'})
       if r['return']>0: return r
       s=r['string'].encode('utf8')

       rq = urllib2.Request(url, s)
       if request=='DELETE':
          rq.get_method = lambda: request

       not_found=False
       try:
          f=urllib2.urlopen(rq)
       except urllib2.URLError as e:
          se=format(e)
          if request=='DELETE' and se.find('404')>0:
             not_found=True
          else:
             return {'return':1, 'error':'problem accessing indexing server ('+se+')'}

       if not not_found:
          try:
             s=f.read()
             f.close()
          except Exception as e:
             return {'return':1, 'error':'can\'t parse output during indexing ('+format(e)+')'}

          if sys.version_info[0]>2:
             s=s.decode('utf8')

          r=convert_json_str_to_dict({'str':s, 'skip_quote_replacement':'yes'})
          if r['return']>0: 
             return {'return':1, 'error':'can\'t parse output from index server ('+r['error']+')'}
          ddo=r['dict']
    else:
       # Check that elastic search client is installed
       found_elasticsearch=True
       try:
          import elasticsearch
       except Exception as e:
          found_elasticsearch=False
          pass

       if not found_elasticsearch:
          return {'return':1, 'error':'Python elasticsearch client library was not found; try to install it via "pip install elasticsearch"'}

       # Init ElasticSearch
       try:
          es=elasticsearch.Elasticsearch([url])
       except elasticsearch.ElasticsearchException as e:
          return {'return':1, 'error':'problem initializing ElasticSearch ('+format(e)+')'}

       es_index='ck'
       es_doc_type='_doc'

       # Check commands
       if request=='TEST':
          # Normally we already connected fine above

          ddo=es.info()
          ddo['health']=es.cluster.health()
          ddo['status']=200

       else:
          es_id=''
          if len(xpath)>1:
              es_id+=xpath[1]
          if len(xpath)>2:
              es_id+='_'+xpath[2]

          if request=='GET':
             lsize=i.get('limit_size','')
             if lsize!='' and lsize!=None:
                lsize=int(lsize)
             else:
                lsize=1000

             start_from=i.get('start_from','')
             if start_from!='' and start_from!=None:
                start_from=int(start_from)
             else:
                start_from=0

             s=i.get('original_string','')
             try:
                ddo = es.search(index="ck", 
                                body={"query": {
                                  "query_string":{
                                     "query":s,
                                     "analyze_wildcard":True
                                  }
                                }, 
                                "from":start_from, 
                                "size":lsize})
             except elasticsearch.ElasticsearchException as e:
                se=format(e)
                return {'return':33, 'error':'problem 33 accessing indexing server ('+se+')'}
          elif request=='DELETE':
             if path=='/_all':
                try:
                   ddo=es.indices.delete(index=es_index, ignore=[400, 404])
                except elasticsearch.ElasticsearchException as e:
                   se=format(e)
                   return {'return':2, 'error':'problem 2 accessing indexing server ('+se+')'}
             else:
                exists=True
                try:
                   ddo=es.get(index=es_index, doc_type=es_doc_type, id=es_id)
                except elasticsearch.ElasticsearchException as e:
                   es_status=e.info.get('status',0)
                   if es_status==404 or e.info.get('found')==False:
                      exists=False

                if exists:
                   try:
                      ddo=es.delete(index=es_index, doc_type=es_doc_type, id=es_id)
                   except elasticsearch.ElasticsearchException as e:
                      se=format(e)
                      return {'return':3, 'error':'problem 3 accessing indexing server ('+se+')'}

          elif request=='PUT':
            try:
               ddo=es.index(index=es_index, doc_type=es_doc_type, id=es_id, body=dd)
            except elasticsearch.ElasticsearchException as e:
               se=format(e)
               return {'return':4, 'error':'problem 4 accessing indexing server ('+se+')'}

    return {'return':0, 'dict':ddo}

##############################################################################
# Add action to a module
#
# TARGET: CK kernel and low-level developers

def add_action(i):
    """
    Input:  {
              (repo_uoa)                  - repo UOA
              module_uoa                  - normally should be 'module' already
              data_uoa                    - UOA of the module to be created

              func                        - action
              (desc)                      - desc

              (for_web)                   - if 'yes', make it a web API, i.e. allow an access to this function in the CK server

              (skip_appending_dummy_code) - if 'yes', do not append code
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

               Output of 'update' function
            }

    """

    # Check if global writing is allowed
    r=check_writing({})
    if r['return']>0: return r

    o=i.get('out','')

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    func=i.get('func','')

    desc=i.get('desc','')

    fweb=i.get('for_web','')

    if muoa=='':
       return {'return':1, 'error':'module UOA is not defined'}

    if duoa!='':
       muoa=duoa
       duoa=''

    # Find path to module
    ii={'module_uoa':cfg['module_name'],
        'data_uoa':muoa}
    if ruoa!='': ii['repo_uoa']=ruoa
    r=load(ii)
    if r['return']>0: return r

    pp=r['path']
    dd=r['dict']

    actions=dd.get('actions',{})
    actions_redirect=dd.get('actions_redirect',{})

    # Check func and desc
    if o=='con':
       if func=='':
          r=inp({'text':'Add action function (or Enter to stop): '})
          func=r['string']

       if func!='':
#          if fweb=='':
#             r1=inp({'text':'Support web (y/N):                         '})
#             fweb=r1['string'].lower()
#             if fweb=='y' or fweb=='yes': fweb='yes'
#             else: fweb=''

          if desc=='':
             r1=inp({'text':'Add action description:                 '})
             desc=r1['string']

    # Check if empty
    if func=='':
       return {'return':1, 'error':'action (function) is not defined'}

    if len(func)>0 and func[0].isdigit():
       return {'return':1, 'error':'action name should not start from a number'}

    if cfg.get('allowed_action_names','')!='':
       import re

       anames=cfg.get('allowed_action_names','')

       if not re.match(anames, func):
          return {'return':1, 'error':'found disallowed characters in the action name (allowed: "'+anames+'")'}

    if func in actions:
       return {'return':1, 'error':'action (function) already exists in the module'}

    if '-' in func:
       func1=func.replace('-','_')
       actions_redirect[func]=func1

    # Adding actions
    actions[func]={}
    if desc!='': actions[func]['desc']=desc
    if fweb!='': actions[func]['for_web']=fweb

    dd['actions']=actions
    dd['actions_redirect']=actions_redirect

    if i.get('skip_appending_dummy_code','')!='yes':
       ii={'module_uoa':cfg['module_name'],
           'data_uoa':cfg['module_name']}
       r=load(ii)
       if r['return']>0: return r

       px=r['path']
       pd=r['dict']

       pma=os.path.join(px, pd['dummy_module_action'])

       # Load module action dummy
       r=load_text_file({'text_file':pma})
       if r['return']>0: return r
       spma=r['string']

       # Load current module
       pmx=os.path.join(pp, cfg['module_full_code_name'])
       r=load_text_file({'text_file':pmx})
       if r['return']>0: return r
       spm=r['string']

       # Update
       if func in actions_redirect:
          func=actions_redirect[func]
       spm+='\n'+spma.replace('$#action#$', func).replace('$#desc#$',desc)

       # Write current module
       rx=save_text_file({'text_file':pmx, 'string':spm})
       if rx['return']>0: return rx

    # Update data entry
    if o=='con': out('')
    ii={'module_uoa':cfg['module_name'],
        'data_uoa':muoa,
        'dict':dd,
        'out':o,
        'sort_keys':'yes'}
    if ruoa!='': ii['repo_uoa']=ruoa
    r=update(ii)
    if r['return']>0: return r

    return r

##############################################################################
# Remove action from a module
#
# TARGET: CK kernel and low-level developers

def remove_action(i):
    """
    Input:  {
              (repo_uoa)  - repo UOA
              module_uoa  - normally should be 'module' already
              data_uoa    - UOA of the module to be created

              func        - action
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

               Output of 'update' function
            }

    """
    # Check if global writing is allowed
    r=check_writing({})
    if r['return']>0: return r

    o=i.get('out','')

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    func=i.get('func','')

    if muoa=='':
       return {'return':1, 'error':'module UOA is not defined'}

    if duoa!='':
       muoa=duoa
       duoa=''

    # Find path to module
    ii={'module_uoa':cfg['module_name'],
        'data_uoa':muoa}
    if ruoa!='': ii['repo_uoa']=ruoa
    r=load(ii)
    if r['return']>0: return r

    pp=r['path']
    dd=r['dict']

    actions=dd.get('actions',{})

    # Check func and desc
    if o=='con':
       if func=='':
          r=inp({'text':'Enter function to be removed (or Enter to quit) - note that we remove only reference to this function from the module meta: '})
          func=r['string']

    # Check if empty
    if func=='':
       return {'return':1, 'error':'action (function) is not defined'}

    if func not in actions:
       return {'return':1, 'error':'action (function) is not found in the module'}

    del (actions[func])

    dd['actions']=actions

    # Update data entry
    if o=='con': out('')
    ii={'module_uoa':cfg['module_name'],
        'data_uoa':muoa,
        'dict':dd,
        'substitute':'yes',
        'sort_keys':'yes',
        'out':o}
    if ruoa!='': ii['repo_uoa']=ruoa
    r=update(ii)
    if r['return']>0: return r

    if o=='con':
       out('')
       out('Reference to the function "'+func+'" was removed from module meta. Function body was not removed from the python code')

    return r

##############################################################################
# List actions in a module
#
# TARGET: CK kernel and low-level developers

def list_actions(i):
    """
    Input:  {
              (repo_uoa)   - repo UOA
              (module_uoa) - module_uoa, if =="", use kernel
              (data_uoa)  
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              actions      - list of actions
            }

    """

    o=i.get('out','')

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    if muoa!='':
       if duoa!='':
          muoa=duoa
          duoa=''

       # Find path to module 'module' to get dummies
       ii={'action':'load',
           'module_uoa':cfg['module_name'],
           'data_uoa':muoa,
           'common_func':'yes'}
       if ruoa!='': ii['repo_uoa']=ruoa

       r=access(ii)
       if r['return']>0: return r

       dd=r['dict']
   
       actions=dd.get('actions',{})
    else:
       actions=cfg['actions']

    # If console, print actions
    if o=='con':
       for q in sorted(actions.keys()):
           s=q

           desc=actions[q].get('desc','')
           if desc!='': s+=' - '+desc

           out(s)

    return {'return':0, 'actions':actions}

##############################################################################
# Pull data
#
# TARGET: CK kernel and low-level developers

def pull(i):
    """
    Input:  {
              (repo_uoa)      - repo UOA, if needed
              module_uoa      - module UOA 
              data_uoa        - data UOA

              (filename)      - filename (with path) (if empty, set archive to 'yes')
                  or
              (cid[0])
                                if empty, create an archive of the entry
              (archive)       - if 'yes' pull whole entry as zip archive using filename or ck_archive.zip
              (all)           - if 'yes' and archive, add even special directories (.cm, .svn, .git, etc)


              (out)           - if 'json' or 'json_file', encode file and return in r
              (skip_writing)  - if 'yes', do not write file (not archive) to current directory

              (pattern)       - return only files with this pattern
              (patterns)      - multiple patterns (useful to pack mutiple points in experiments)

              (encode_file)   - if 'yes', encode file

              (skip_tmp)      - if 'yes', skip tmp files and directories
            }

    Output: {
              return                - return code =  0, if successful
                                                  >  0, if error
              (error)               - error text if return > 0
              (file_content_base64) - if i['to_json']=='yes', encoded file
              (filename)            - filename to record locally
            }

    """

    o=i.get('out','')

    tj=False
    if o=='json' or o=='json_file' or i.get('encode_file','')=='yes':
       tj=True

    st=i.get('skip_tmp','')

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    pat=i.get('pattern','')
    pats=i.get('patterns',[])
    if pat!='':
       pats.append(pat)

    fn=i.get('filename','')
    if fn=='':
       x=i.get('cids',[])
       if len(x)>0:
          fn=x[0]

    # Attempt to load data (to find path, etc)
    r=load({'repo_uoa':ruoa, 'module_uoa':muoa, 'data_uoa':duoa})
    if r['return']>0: return r

    p=r['path']
    muoa=r['module_uoa']
    duoa=r['data_uoa']
    dd=r['dict']

    # How output
    sw=i.get('skip_writing','')

    # Prepare output
    rr={'return':0}

    # Check what to pull
    pfn=''

    if fn=='': 
       i['archive']='yes'

    delete_file=''

    if i.get('archive','')!='yes':
       # Get file
       pfn=os.path.normpath(os.path.join(p,fn))

       # Check that file is not getting outside paths ...
       if not pfn.startswith(p):
          return {'return':1, 'error':'path of file is outside entry'}

       if not os.path.isfile(pfn):
          return {'return':1, 'error':'file not found'}

       if not tj and sw!='yes':
          # Copy file to current directory
          if os.path.isfile(fn):
             return {'return':1, 'error':'file already exists in the current directory'}

          # Copy file
          import shutil
          shutil.copyfile(pfn,fn)

       py=os.path.split(fn)
       rr['filename']=py[1]

    else:
       # Prepare archive name
       if fn!='': 
          # Check that file is not getting outside paths ...
          fn=os.path.normpath(os.path.join(os.getcwd(),fn))
          if not pfn.startswith(os.getcwd()):
             return {'return':1, 'error':'archive filename should not have path'}

       else:
          if tj:
             # Generate tmp file
             import tempfile
             fd, fn=tempfile.mkstemp(suffix='.tmp', prefix='ck-') # suffix is important - CK will delete such file!
             os.close(fd)
             os.remove(fn)
             delete_file=fn
          else:
             fn=cfg['default_archive_name']
       pfn=fn

       if os.path.isfile(pfn):
          return {'return':1, 'error':'archive file already exists in the current directory'}

       # Prepare archive
       import zipfile

       zip_method=zipfile.ZIP_DEFLATED

       gaf=i.get('all','')

       fl={}

       if len(pats)>0:
          for q in pats:
              r=list_all_files({'path':p, 'all':gaf, 'pattern':q})
              if r['return']>0: return r

              flx=r['list']

              for k in flx:
                  fl[k]=flx[k]
       else:
          r=list_all_files({'path':p, 'all':gaf})
          if r['return']>0: return r

          fl=r['list']

       # Write archive
       try:
          f=open(pfn, 'wb')
          z=zipfile.ZipFile(f, 'w', zip_method)
          for fn in fl:
              if st!='yes' or not fn.startswith('tmp'):
                 p1=os.path.join(p, fn)
                 z.write(p1, fn, zip_method)
          z.close()
          f.close()

       except Exception as e:
          return {'return':1, 'error':'failed to prepare archive ('+format(e)+')'}

    # If add to JSON
    if tj:
       r=convert_file_to_upload_string({'filename':pfn})
       if r['return']>0: return r

       rr['file_content_base64']=r['file_content_base64']

       if delete_file!='': os.remove(delete_file)

    return rr

##############################################################################
# Push data
#
# TARGET: CK kernel and low-level developers

def push(i):
    """
    Input:  {
              (repo_uoa)            - repo UOA, if needed
              module_uoa            - module UOA 
              data_uoa              - data UOA

              (filename)            - local filename 
                  or
              (cid[0])

              (extra_path)          - extra path inside entry (create if doesn't exist)

              (file_content_base64) - if !='', take its content and record into filename

              (archive)             - if 'yes' push to entry and unzip ...

              (overwrite)           - if 'yes', overwrite files
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Check if global writing is allowed
    r=check_writing({})
    if r['return']>0: return r

    o=i.get('out','')

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    # Check file
    fn=i.get('filename','')
    if fn=='':
       x=i.get('cids',[])
       if len(x)>0:
          fn=x[0]

    if fn=='':
       return {'return':1, 'error':'filename is empty'}

    fcb=False
    if 'file_content_base64' in i:
       import base64

       bin=base64.urlsafe_b64decode(i['file_content_base64'].encode('utf8')) # convert from unicode to str since base64 works on strings
                                                                   # should be safe in Python 2.x and 3.x
       fcb=True
    else:
       if not os.path.isfile(fn):
          return {'return':1, 'error':'file '+fn+' not found'}

    # Attempt to load data (to find path, etc)
    rx=load({'repo_uoa':ruoa, 'module_uoa':muoa, 'data_uoa':duoa})
    if rx['return']>0: return rx

    p=rx['path']
    muoa=rx['module_uoa']
    duoa=rx['data_uoa']
    dd=rx['dict']

    px=os.path.normpath(os.path.join(p, cfg['subdir_ck_ext']))

    ruoa=rx['repo_uoa']
    ruid=rx['repo_uid']

    # Check repo/module writing
    ii={'module_uoa':muoa, 'repo_uoa':ruoa, 'repo_uid':ruid}
    r=check_writing(ii)
    if r['return']>0: return r
    rd=r.get('repo_dict',{})

    rshared=rd.get('shared','')
    rsync=rd.get('sync','')

    # Prepare path
    p1=i.get('extra_path','')
    if p1!='':
       p2=os.path.normpath(os.path.join(p,p1))
       if not p2.startswith(p):
          return {'return':1,'error':'extra path is outside entry'}

       p=p2

    # Create missing dirs
    if not os.path.isdir(p): os.makedirs(p)

    overwrite=i.get('overwrite','')

    # Copy or record file
    p3=os.path.normpath(os.path.join(p, fn))
    if not p3.startswith(p3):
       return {'return':1,'error':'extra path is outside entry'}

    if p3.startswith(px):
       return {'return':1, 'error':'path points to the special directory with meta info'}

    if os.path.isfile(p3) and overwrite!='yes':
       return {'return':1,'error':'file already exists in the entry'}

    if fcb:
       try:
         f=open(p3, 'wb')
         f.write(bin)
         f.close()
       except Exception as e:
          return {'return':1, 'error':'problem writing text file='+p3+' ('+format(e)+')'}
    else:
       import shutil
       shutil.copyfile(fn, p3)

    # Process if archive
    y=''
    if i.get('archive','')=='yes':
       rx=unzip_file({'archive_file':p3,
                      'path':p,
                      'overwrite':overwrite,
                      'delete_after_unzip':'yes'})
       if rx['return']>0: return rx
       y='and unziped '

    if rshared!='':
       ppp=os.getcwd()

       pp=os.path.split(p)
       pp0=pp[0]
       pp1=pp[1]

       os.chdir(pp0)

       ss=cfg['repo_types'][rshared]['add'].replace('$#files#$', pp1)
       rx=os.system(ss)

       os.chdir(ppp)

    if o=='con':
       out('File was pushed '+y+'successfully!')

    return {'return':0}

##############################################################################
# List files in a given entry
#
# TARGET: end users

def unzip_file(i):
    """
    Input:  {
              archive_file         - full path to zip file  
              (path)               - path where unzip (current if empty)
              (overwrite)          - if 'yes', overwrite
              (delete_after_unzip) - if 'yes', delete original zip file after unzipping
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              skipped       - list of files which was not overwritten
           }

    """

    import zipfile

    p=i.get('path','')
    if p=='':
       p=os.getcwd()

    p3=i['archive_file']

    overwrite=i.get('overwrite','')

    dau=i.get('delete_after_unzip','')

    s=[]

    f=open(p3,'rb')
    z=zipfile.ZipFile(f)
    for d in z.namelist():
        if not d.startswith('.') and not d.startswith('/') and not d.startswith('\\'):
           pp=os.path.join(p,d)
           if d.endswith('/'): 
              # create directory 
              if not os.path.exists(pp): os.makedirs(pp)
           else:
              ppd=os.path.dirname(pp)
              if not os.path.exists(ppd): os.makedirs(ppd)

              # extract file
              if os.path.isfile(pp) and overwrite!='yes':
                 s.append(d)
              else:
                 fo=open(pp, 'wb')
                 fo.write(z.read(d))
                 fo.close()
    f.close()

    if dau=='yes':
       os.remove(p3)

    return {'return':0, 'skipped':s}

##############################################################################
# List files in a given entry
#
# TARGET: end users

def list_files(i):
    """
    Input:  {
              (repo_uoa)   
              (module_uoa) 
              (data_uoa)  

              parameters for function 'list_all_files'
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              Output of list all files
            }

    """

    o=i.get('out','')

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    # Get info about entry
    r=load({'repo_uoa':ruoa, 'module_uoa':muoa, 'data_uoa':duoa})
    if r['return']>0: return r

    p=r['path']

    # Get files
    ii={'path':p}
    if i.get('limit','')!='': ii['limit']=i['limit']
    if i.get('number','')!='': ii['number']=i['number']
    if i.get('all','')!='': ii['all']=i['all']

    r=list_all_files(ii)
    if r['return']>0: return r

    if o=='con':
       for q in r.get('list',[]):
           out(q)

    return r

##############################################################################
# convert_cm_to_ck
#
# TARGET: internal use

def convert_cm_to_ck(i): # pragma: no cover
    """

    Input:  {
              (repo_uoa)   - repo UOA with wild cards
              (module_uoa) - module UOA with wild cards
              (data_uoa)   - data UOA with wild cards

              (print_full) - if 'yes', show CID (repo_uoa:module_uoa:data_uoa)

              (print_time) - if 'yes'. print elapse time at the end

              (ignore_update) - if 'yes', do not add info about update

              (time_out)   - in sec. (default -1, i.e. no timeout)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import sys

    o=i.get('out','')

    # Check wildcards
    lst=[]

    to=i.get('time_out','')
    if to=='': to='-1'

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    if ruoa=='': ruoa='*'
    if muoa=='': muoa='*'
    if duoa=='': duoa='*'

    pf=i.get('print_full','')
    if pf=='': pf='yes'

    ii={}
    ii['out']=o
    ii['repo_uoa']=ruoa
    ii['module_uoa']=muoa
    ii['data_uoa']=duoa
    ii['filter_func_addr']=getattr(sys.modules[__name__], 'filter_convert_cm_to_ck')
    ii['do_not_add_to_lst']='yes'
    ii['print_time']=i.get('print_time','')
    ii['print_time']=i.get('print_time','')
    ii['print_full']=pf
    ii['time_out']=to
    ii['ignore_update']=i.get('ignore_update','')
    return list_data(ii)

##############################################################################
# convet cm to ck filter
#
# TARGET: internal use

def filter_convert_cm_to_ck(i): # pragma: no cover
    """

    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')
    i['out']=''
    rx=load(i)
    i['out']=o

    if rx['return']>0: return rx

    ruid=rx['repo_uid']
    muid=rx['module_uid']
    duid=rx['data_uid']

    d=rx['dict']
    info=rx.get('info',{})

    # Converting 
    if 'cm_access_control' in d:
       if 'cm_outdated' not in info: info['cm_outdated']={}
       info['cm_outdated']['cm_access_control']=d['cm_access_control']
       del (d['cm_access_control'])

    if 'cm_display_as_alias' in d:
       info['data_name']=d['cm_display_as_alias']
       del(d['cm_display_as_alias'])

    if 'powered_by' in d:
       if 'cm_outdated' not in info: info['cm_outdated']={}
       info['cm_outdated']['powered_by']=d['powered_by']
       del(d['powered_by'])

    if 'cm_description' in d:
       info['description']=d['cm_description']
       del(d['cm_description'])

    if 'cm_updated' in d:
       dcu=d['cm_updated'][0]
       cidate=dcu.get('cm_iso_datetime','')
       cuoa=dcu.get('cm_user_uoa','')

       if 'control' not in info:
          info['control']={}

       if cidate!='': 
          info['control']['iso_datetime']=cidate

       if cuoa!='':
          info['control']['author_uoa']=cuoa

       info['control']['engine']='CM'
       info['control']['version']=[]

       del(d['cm_updated'])

    if 'version' in info: del(info['version'])

    # Saving
    ii={'action':'update',
        'repo_uoa':ruid,
        'module_uoa':muid,
        'data_uoa':duid,
        'substitute':'yes',
        'dict':d,
        'info':info,
        'ignore_update':i.get('ignore_update','')
       }
    rx=update(ii)
    return rx

##############################################################################
# add index
#
# TARGET: CK kernel and low-level developers

def add_index(i):
    """

    Input:  {
              (repo_uoa)   - repo UOA with wild cards
              (module_uoa) - module UOA with wild cards
              (data_uoa)   - data UOA with wild cards

              (print_full)         - if 'yes', show CID (repo_uoa:module_uoa:data_uoa)

              (print_time) - if 'yes'. print elapse time at the end

              (time_out)   - in sec. (default -1, i.e. no timeout)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import sys

    o=i.get('out','')

    # Check wildcards
    lst=[]

    to=i.get('time_out','')
    if to=='': to='-1'

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    if ruoa=='': ruoa='*'
    if muoa=='': muoa='*'
    if duoa=='': duoa='*'

    pf=i.get('print_full','')
    if pf=='': pf='yes'

    ii={}
    ii['out']=o
    ii['repo_uoa']=ruoa
    ii['module_uoa']=muoa
    ii['data_uoa']=duoa
    ii['filter_func_addr']=getattr(sys.modules[__name__], 'filter_add_index')
    ii['do_not_add_to_lst']='yes'
    ii['print_time']=i.get('print_time','')
    ii['print_full']=pf
    ii['time_out']=to

    return list_data(ii)

##############################################################################
# zip entries (call repo)
#
# TARGET: CK kernel and low-level developers

def zip(i):
    """

    Input:  {
              (repo_uoa)   - repo UOA with wild cards
              (module_uoa) - module UOA with wild cards
              (data_uoa)   - data UOA with wild cards

              (archive_path) - if '' create inside repo path

              (archive_name) - if !='' use it for zip name
              (auto_name)    - if 'yes', generate name name from data_uoa: ckr-<repo_uoa>.zip
              (bittorent)    - if 'yes', generate zip name for BitTorrent: ckr-<repo_uid>-YYYYMMDD.zip

              (overwrite)    - if 'yes', overwrite zip file
              (store)        - if 'yes', store files instead of packing

            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    if i.get('data_uoa','')!='': del(i['data_uoa'])

    ruoa=i.get('repo_uoa','')
    if ruoa!='':
       if ruoa.find('*')<0 and ruoa.find('?')<0:
          i['data_uoa']=ruoa
       else:
          del(i['repo_uoa'])

    i['module_uoa']=cfg['module_repo_name']
    i['data']=i.get('cid','')

    if i.get('cid','')!='': del(i['cid'])

    return access(i)

##############################################################################
# add index filter
#
# TARGET: CK kernel and low-level developers

def filter_add_index(i):
    """

    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')
    i['out']=''
    rx=load(i)
    i['out']=o

    if rx['return']>0: return rx

    muid=rx['module_uid']
    duid=rx['data_uid']
    path='/'+muid+'/'+duid+'/1'
    r=access_index_server({'request':'DELETE', 'path':path})
    if r['return']>0: return r
    r=access_index_server({'request':'PUT', 'path':path, 'dict':rx})
    return r

##############################################################################
# delete index
#
# TARGET: CK kernel and low-level developers

def delete_index(i):
    """

    Input:  {
              (repo_uoa)   - repo UOA with wild cards
              (module_uoa) - module UOA with wild cards
              (data_uoa)   - data UOA with wild cards

              (print_time) - if 'yes'. print elapse time at the end

              (time_out)   - in sec. (default -1, i.e. no timeout)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import sys

    o=i.get('out','')

    # Check wildcards
    lst=[]

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    if ruoa=='': ruoa='*'
    if muoa=='': muoa='*'
    if duoa=='': duoa='*'

    ii={}
    ii['out']=o
    ii['repo_uoa']=ruoa
    ii['module_uoa']=muoa
    ii['data_uoa']=duoa
    ii['filter_func_addr']=getattr(sys.modules[__name__], 'filter_delete_index')
    ii['do_not_add_to_lst']='yes'

    return list_data(ii)

##############################################################################
# add index filter
#
# TARGET: CK kernel and low-level developers

def filter_delete_index(i):
    """

    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')
    i['out']=''
    r=load(i)
    i['out']=o

    if r['return']>0: return r

    muid=r['module_uid']
    duid=r['data_uid']

    path='/'+muid+'/'+duid+'/1'

    return access_index_server({'request':'DELETE', 'path':path})

##############################################################################
# Remove files and dirs even if read only
#
# TARGET: internal use

def rm_read_only(f,p,e):
    import os
    import stat
    import errno

    ex=e[1]

    os.chmod(p,stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)
    f(p)

    return

############################################################################
# Universal access to all CK functions (Unified JSON/dictionary API)
#
# TARGET: end users

def access(i):

    """
    Input:  Can be dictionary or string (string will be converted to dictionary)

            {
               action

               module_uoa or CID -> converted to cid
                 or
               (cid1)            -  if doesn't have = and doesn't start from -- or - or @ -> appended to cids[]
               (cid2)            -  if doesn't have = and doesn't start from -- or - or @ -> appended to cids[]
               (cid3)            -  if doesn't have = and doesn't start from -- or - or @ -> appended to cids[]
                 or
               (repo_uoa)
               (module_uoa)
               (data_uoa)

               (out=type)     Module output
                              == ''              - none
                              == 'con'           - console interaction (if from CMD, default)
                              == 'json'          - return dict as json to console
                              == 'json_with_sep' - separation line and return dict as json to console
                              == 'json_file'     - return dict as json to file

               (out_file)     Output file if out=='json_file'

               (con_encoding) - force encoding for IO
               (ck_profile)   - if 'yes', profile CK

               INPUT TO A GIVEN FUNCTION


               NOTE: If INPUT is a string and it will be converted to INPUT dictionary as follows (the same as CK command line):

                     ck key1=value1    -> converted to {key1:value1}

                        -key10         -> converted to {key10:"yes"}
                        -key11=value11 -> converted to {key11:value11}

                        --key12         -> converted to {key12:"yes"}
                        --key13=value13 -> converted to {key13:value13}


                     @file_json         -> JSON from this file will be merged with INPUT
                     @@                 -> CK will ask user ot enter manually JSON from console and merge with INPUT
                     @@key              -> Enter JSON manually from console and merge with INPUT under this key

                     @@@cmd_json        -> convert string to JSON (special format) and merge with INPUT

                     -- xyz             -> add everything after -- to "unparsed_cmd" key in INPUT

                     When string is converted to INPUT dictionary, "cmd" variable is set to True
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              OUTPUT FROM A GIVEN FUNCTION
            }

    """

    global con_encoding

#    # Set fresh configuration for each access - very costly
#    if cfg.get('loading_config','') == '':
#        cfg['loading_config'] = 'yes'
#        r=access({'action':'load',
#                  'repo_uoa':cfg['repo_name_default'],
#                  'module_uoa':cfg['subdir_kernel'],
#                  'data_uoa':cfg['subdir_kernel_default']})
#        if r['return']==0:
#           cfg.update(r['dict'])
#
#        r=access({'action':'load',
#                  'repo_uoa':cfg['repo_name_local'],
#                  'module_uoa':cfg['subdir_kernel'],
#                  'data_uoa':cfg['subdir_kernel_default']})
#        if r['return']==0:
#           cfg.update(r['dict'])
#        cfg['loading_config'] = ''

    rr={'return':0}
    ii={}
    cmd=False
    o=''

    ### If input is string, split into list and process in the next condition
    if type(i)==str:
       cmd=True
       x=i.split(' ')
       i=x 

    ### If input is a list
    if type(i)==list:
       if len(i)==1 and i[0].strip()=='test_install':
          return rr # installation test

       cmd=True
       rr=convert_ck_list_to_dict(i)
       if rr['return']==0:
          i=rr.get('ck_dict',{})

          if i.get('out','')=='': i['out']='con' # Default output is console 
                                                 # if called from CMD or with string

    o=''
    if rr['return']==0:
       # Check output mode
       o=i.get('out','')

       ### If profile
       cp=i.get('ck_profile','')
       if cp=='yes':
          import time
          start_time = time.time()

       ### Process request ######################################

       if i.get('con_encoding','')!='': con_encoding=i['con_encoding']

       ### Process action ###################################
       rr=init({})
       if rr['return']==0:
          # Run module with a given action
          rr=perform_action(i)
          if rr.get('out','')!='': o=rr['out']

       if cp=='yes':
          elapsed_time=time.time()-start_time
          rr['ck_profile_time']=elapsed_time
          if o=='con':
             out('CK profile time: '+str(elapsed_time)+' sec.')

    # Finalize call (check output) ####################################
    if o=='json' or o=='json_with_sep':
       if o=='json_with_sep': out(cfg['json_sep'])

       rr1=dumps_json({'dict':rr})
       if rr1['return']==0:
          s=rr1['string']
          out(s)

    elif o=='json_file':
       fn=i.get('out_file','')
       if fn=='':
          rr['return']=1
          rr['error']='out==json_file but out_file is not defined in kernel access function'
       else:
          rr1=save_json_to_file({'json_file':fn, 'dict':rr})
          if rr1['return']>0:
             rr['return']=1
             rr['error']=rr1['error']

    # If error and CMD, output error to console
    if cmd:
       if rr['return']>0:
          x=''
          if type(i)==dict:
             x=i.get('module_uoa','')
             if x!='':
                x='['+x+'] '
          #FGG added this to fix temporal error with ElasticSearch indexing when index is empty
          out(str(cfg['error'])+x+str(rr['error'])+'!')

    return rr

##############################################################################
if __name__ == "__main__":

   r=access(sys.argv[1:])

   if 'return' not in r:
      raise Exception('CK access function should always return key \'return\'!')

   exit(int(r['return']))
