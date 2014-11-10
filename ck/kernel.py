#              6
# Collective Knowledge (CK)
#
# See CK LICENSE.txt for licensing details
# See CK Copyright.txt for copyright details
#
# Developer: Grigori Fursin
#

# CK kernel

# Extra modules global for the whole kernel
import sys
import json
import os
import imp   # Loading Python modules

initialized=False      # True if initialized
allow_print=True       # Needed to supress all output
con_encoding=''        # Use non-default console encoding

cfg={
      "name":"Collective Knowledge",
      "desc":"exposing ad-hoc experimental setups to extensible repository and big data predictive analytics",
      "cmd":"ck <action> $#module_uoa#$ (cid1/uid1) (cid2/uid2) (cid3/uid3) key_i=value_i ... @file.json",

      "wiki_data_web":"https://github.com/ctuning/ck/wiki/Description",
      "help_web":"More info: https://github.com/ctuning/ck",
      "ck_web":"https://github.com/ctuning/ck",

      "default_license":"See CK LICENSE.txt for licensing details",
      "default_copyright":"See CK Copyright.txt for copyright details",
      "default_developer":"cTuning foundation",

      "version":["0", "1", "140810", "beta"],
      "error":"CK error: ",
      "json_sep":"*** ### --- CK JSON SEPARATOR --- ### ***",
      "default_module":"data",
      "module_name":"module",
      "repo_name":"repo",
      "module_code_name":"module",
      "module_full_code_name":"module.py",

      "env_key_root":"CK_ROOT",
      "env_key_local_repo":"CK_LOCAL_REPO",
      "env_key_repos":"CK_REPOS",

      "subdir_default_repos":"repos",

      "subdir_default_repo":"repo",
      "subdir_kernel":"kernel",
      "subdir_kernel_default":"default",
      "subdir_ck_ext":".cm", # keep compatibility with Collective Mind V1.x

      "special_directories":[".cm", ".svn", ".git"], # special directories that should be ignored when copying/moving entries

      "file_meta_old":"data.json", # keep compatibility with Collective Mind V1.x
      "file_meta":"meta.json",
      "file_info":"info.json",
      "file_updates":"updates.json",

      "file_alias_a": "alias-a-", 
      "file_alias_u": "alias-u-",

      "repo_file":".ckr.json",

      "file_cache_repo_uoa":".ck.cache_repo_uoa.json",
      "file_cache_repo_info":".ck.cache_repo_info.json",

      "default_web_service_host":"",
      "default_web_service_port":"3344",

      "detached_console":{"win":{"cmd":"start $#cmd#$", "use_create_new_console_flag":"yes"},
                          "linux":{"cmd":"xterm -hold -e \"$#cmd#$\""}},

      "repo_name_default":"default",
      "repo_uid_default":"604419a9fcc7a081",
      "repo_name_local":"local",
      "repo_uid_local":"9a3280b14a4285c9",

      "repo_types":{
                     "git":{
                            "clone":"git clone $#url#$ $#path#$",
                            "update":"git pull"
                           }
                   },

      "actions":{
                 "uid":{"desc":"generate UID"},
                 "version":{"desc":"print CK version"},

                 "help":{"desc":"<CID> print help about data (module) entry"},
                 "webhelp":{"desc":"<CID> open browser with online help (description) for a data (module) entry"}, 
                 "info":{"desc":"<CID> print help about data entry"},

                 "add":{"desc":"<CID> add entry"},
                 "update":{"desc":"<CID> update entry"},
                 "load":{"desc":"<CID> load meta description of entry"},

                 "find":{"desc":"<CID> find path to entry"},
                 "path":{"desc":"<CID> detect CID in the current directory"},

                 "rm":{"desc":"<CID> delete entry"},
                 "remove":{"desc":"see 'rm'"},
                 "delete":{"desc":"see 'rm'"},

                 "ren":{"desc":"<CID> <new name) (data_uid) (remove_alias) rename entry"},
                 "rename":{"desc":"see 'ren' function"},

                 "cp":{"desc":"<CID> <CID1> copy entry"},
                 "copy":{"desc":"see 'cp'"},

                 "mv":{"desc":"<CID> <CID1> move entry"},
                 "move":{"desc":"see 'mv'"},

                 "list":{"desc":"<CID> list entries"},

                 "add_action":{"desc":"add action (function) to existing module"},
                 "remove_action":{"desc":"remove action (function) from existing module"},
                 "list_actions":{"desc":"list actions (functions) in existing module"}
                },

      "actions_redirect":{"list":"list_data"},

      "common_actions":["webhelp", "help", "info", "path",
                        "add", 
                        "load", "find",
                        "rm", "remove", "delete",
                        "update",
                        "ren", "rename",
                        "cp",
                        "copy",
                        "mv",
                        "move",
                        "list",
                        "add_action",
                        "remove_action",
                        "list_actions"]
    }

work={
      "env_root":"",

      "dir_default_repo":"",
      "dir_default_kernel":"",
      "dir_default_cfg":"",

      "dir_local_repo":"",
      "dir_local_kernel":"",
      "dir_local_cfg":"",

      "dir_work_repo":"",
      "dir_work_cfg":"",

      "dir_repos":"",

      "dir_cache_repo_uoa":"",
      "dir_cache_repo_info":"",

      "repo_name_work":"",
      "repo_uid_work":""
     }

paths_repos=[]     # First path to local repo (if exist), than global

cache_repo_init=False # True, if initialized
paths_repos_all=[]    # Path to all repos
cache_repo_uoa={}     # Disambiguate repo UOA to repo UID
cache_repo_info={}    # Cache repo info with path and type

##############################################################################
# Universal print of unicode string in UTF-8 that supports Python 2.x and 3.x

def out(s):
    """
    Input:  s - unicode string to print

    Output: Nothing
    """

    if allow_print: 
       if con_encoding=='':
          x=sys.stdin.encoding
          if x==None: 
             b=s.encode(x, errors='ignore')
          else:
             b=s.encode()
       else:
          b=s.encode(con_encoding, errors='ignore')

       if sys.version_info[0]>2:
          sys.stdout.buffer.write(b)
          sys.stdout.buffer.write(b'\n')
       else:
          print(b)

    sys.stdout.flush()

    return None

##############################################################################
# Universal input of unicode string in UTF-8 that supports Python 2.x and 3.x

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

    if sys.version_info[0]>2:
       s=input(t)
    else:
       s=raw_input(t).decode(sys.stdin.encoding).encode('utf8')

    return {'return':0, 'string':s}

##############################################################################
# Simple test of CK installation

def test():
    """
    Input:  None

    Output: {
              return       - return code =  0
            }

    """
    out(cfg['name'])

    out('')
    out('Test function executed successfully')

    return {'return':0}

##############################################################################
# Get CK version

def get_version(i):
    """
    Input:  {}

    Output: {
              return       - return code =  0

              version      - list starting from major version number
              version_str  - version string
            }

    """

    s=''

    for q in cfg['version']:
        if s!='': s+='.'
        s+=q

    return {'return':0, 'version':cfg['version'], 'version_str':s}

##############################################################################
# Get platform (currently win or linux)

def get_platform(i):
    """
    Input: {}

    Output: {
              return   - return code =  0
              platform - win or linux
            }
    """

    import platform

    plat='linux'

    if platform.system().lower().startswith('win'):
       plat='win'

    return {'return':0, 'platform':plat}

##############################################################################
# Generate CK UID

def gen_uid(i):
    """
    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              uid          - UID in string format (16 characters 0..9,a..f)
            }
    """

    import uuid
    import random

    uid=str(uuid.uuid4().hex)

    if len(uid)!=32:
       return {'return':1, 'error':'problem generating UID : len='+str(len(uid))+' !=32'}

    random.seed

    x=random.randrange(0,16)
    return {'return':0, 'data_uid':uid[x:x+16]}

##############################################################################
# Check if string is CK UID

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
# Check if string is allowed CK UOA

def is_uoa(str):
    """
    Input:  string to check

    Output: True if allowed UOA, False otherwise
    """

    if str.find('#')>=0: return False
    if str.find('*')>=0: return False
    if str.find('?')>=0: return False

    return True

##############################################################################
# Convert string of a special format to json

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
# Load json from file into dict

def load_json_file(i):
    """
    Input:  {
              json_file - name of file with json
            }

    Output: {
              return       - return code =  0, if successful
                                         = 16, if file not found (may be warning)
                                         >  0, if error
              (error)  - error text if return > 0

              dict     - dict from json file
            }
    """

    fn=i['json_file']

    try:
      if sys.version_info[0]>2:
         f=open(fn, 'r', encoding='utf8')
      else:
         f=open(fn, 'r')
    except Exception as e:
       return {'return':16, 'error':'problem opening json file='+fn+' ('+format(e)+')'}

    try:
      s=f.read()
    except Exception as e:
       f.close()
       return {'return':1, 'error':'problem reading json file='+fn+' ('+format(e)+')'}

    f.close()

    try:
      if sys.version_info[0]>2:
         d=json.loads(s)
      else:
         d=json.loads(s, encoding='utf8')
    except Exception as e:
       return {'return':1, 'error':'problem parsing json from file='+fn+' ('+format(e)+')'}

    return {'return':0, 'dict': d}

##############################################################################
# Load text file into string

def load_text_file(i):
    """
    Input:  {
              text_file     - name of text file
              (keep_as_bin) - if 'yes', return only bin
            }

    Output: {
              return       - return code =  0, if successful
                                         = 16, if file not found (may be warning)
                                         >  0, if error
              (error)  - error text if return > 0

              bin      - bin
              string   - loaded text (with removed \r)
            }
    """

    fn=i['text_file']

    try:
       f=open(fn, 'rb')
    except Exception as e:
       return {'return':16, 'error':'problem opening text file='+fn+' ('+format(e)+')'}

    try:
       b=f.read()
    except Exception as e:
       f.close()
       return {'return':1, 'error':'problem reading text file='+fn+' ('+format(e)+')'}

    f.close()

    r={'return':0, 'bin':b}

    if i.get('keep_as_bin','')!='yes':
       s=b.decode('utf8').replace('\r','') # decode into Python string (unicode in Python3)
       r['string']=s

    return r

##############################################################################
# Dump json to sring

def dumps_json(i):
    """
    Input:  {
              dict          - dictionary
              (skip_indent) - if 'yes', skip indent
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error

              string       - json string (in utf8)
            }
    """

    d=i['dict']
    si=i.get('skip_indent','')

    try:
       if sys.version_info[0]>2:
          if si=='yes': s=json.dumps(d, ensure_ascii=False)
          else:         s=json.dumps(d, indent=2, ensure_ascii=False)
       else:
          if si=='yes': s=json.dumps(d, ensure_ascii=False, encoding='utf8')
          else:         s=json.dumps(d, indent=2, ensure_ascii=False, encoding='utf8')
    except Exception as e:
       return {'return':1, 'error':'problem converting dict to json ('+format(e)+')'}

    return {'return':0, 'string':s}

##############################################################################
# Save dict as json file

def save_json_to_file(i):
    """
    Input:  {
              json_file - file name
              dict      - dict to save
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """

    fn=i['json_file']
    d=i['dict']

    r=dumps_json(i)
    if r['return']>0: return r
    s=r['string']

    try:
       if sys.version_info[0]>2:
          f=open(fn,'wb')
       else:
          f=open(fn,'w')
    except Exception as e:
       return {'return':1, 'error':'problem writing dict to file='+fn+' ('+format(e)+')'}

    try:
       f.write(s.encode('utf8'))
    except Exception as e:
       f.close()
       return {'return':1, 'error':'problem writing dict to file='+fn+' ('+format(e)+')'}

    f.close()

    return {'return':0}

##############################################################################
# save string into text file

def save_text_file(i):
    """
    Input:  {
              text_file - name of text file
              string    - string to write (with removed \r)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)  - error text if return > 0
            }
    """

    fn=i['text_file']
    s=i['string'].replace('\r','')

    try:
      if sys.version_info[0]>2:
         f=open(fn, 'wb')
         f.write(s.encode('utf8'))
      else:
         f=open(fn,'w')
         f.write(s)
    except Exception as e:
       return {'return':1, 'error':'problem writing text file='+fn+' ('+format(e)+')'}

    f.close()

    return {'return':0}

##############################################################################
# Merge intelligently dict1 with dict2 key by key in contrast with dict1.update(dict2)

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
# Convert CK list to CK dict (unification of interfaces)

def convert_ck_list_to_dict(i):
    """
    Input:  CK list
            [
               action
               module_uoa or CID -> converted to cid
                 or
               (cidx)            -  if doesn't have = and doesn't start from -- or - or @ -> appended to cids[]
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
               ...
               key1=value1
               key2=value2
               ...
               -key10
               -key11=value11
               --key12
               --key13=value13
               @file_json
               @@cmd_json
               --
               unparsed_cmd
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

              obj['unparsed']=i[x+1:]
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
           elif p.startswith("@@"):
              cx=False
              jd=p[2:]
              if len(jd)<2:
                 return {'return':1, 'error':'can\'t parse command line option '+p}

              y=convert_json_str_to_dict({'str':jd})
              if y['return']>0: return y

              merge_dicts({'dict1':obj, 'dict2':y['dict']})

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

def init(i):
    """
    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """

    global cfg, work, initialized, paths_repos

    if initialized:
       return {'return':1, 'error': 'CK is already initialized'}

    # Check CK_ROOT environment variable
    if not cfg['env_key_root'] in os.environ.keys():
       return {'return':1, 'error':cfg['env_key_root']+' environment variable is not defined'}

    s=os.environ[cfg['env_key_root']].strip()
    if s=='':
       return {'return':1, 'error':cfg['env_key_root']+' environment variable is empty'}

    work['env_root']=os.path.realpath(s)

    # Check default repo
    work['dir_default_repo']=os.path.join(work['env_root'], cfg['subdir_default_repo'])
    work['dir_default_kernel']=os.path.join(work['dir_default_repo'], cfg['subdir_kernel'])
    work['dir_default_cfg']=os.path.join(work['dir_default_kernel'], cfg['subdir_kernel_default'], cfg['subdir_ck_ext'], cfg['file_meta'])

    work['dir_work_repo']=work['dir_default_repo']
    work['dir_work_kernel']=work['dir_default_kernel']
    work['dir_work_cfg']=work['dir_default_cfg']

    work['repo_name_work']=cfg['repo_name_default']
    work['repo_uid_work']=cfg['repo_uid_default']

    # Check CK_LOCAL_REPO environment variable - if exists, override
    if cfg['env_key_local_repo'] in os.environ.keys():
       s=os.environ[cfg['env_key_local_repo']].strip()
       if s!='':
          work['dir_local_repo']=os.path.realpath(s)
          work['dir_local_kernel']=os.path.join(work['dir_local_repo'], cfg['subdir_kernel'])
          work['dir_local_cfg']=os.path.join(work['dir_local_kernel'], cfg['subdir_kernel_default'], cfg['subdir_ck_ext'], cfg['file_meta'])

          # Update work repo!
          work['dir_work_repo']=work['dir_local_repo']
          work['dir_work_kernel']=work['dir_local_kernel']
          work['dir_work_cfg']=work['dir_local_cfg']

          work['repo_name_work']=cfg['repo_name_local']
          work['repo_uid_work']=cfg['repo_uid_local']

          paths_repos.append(work['dir_local_repo'])

    paths_repos.append(work['dir_default_repo'])

    # Prepare repo cache
    work['dir_cache_repo_uoa']=os.path.join(work['dir_work_repo'],cfg['file_cache_repo_uoa'])
    work['dir_cache_repo_info']=os.path.join(work['dir_work_repo'],cfg['file_cache_repo_info'])

    # Read kernel configuration (if exists)
    if os.path.isfile(work['dir_work_cfg']):
       r=load_json_file({'json_file':work['dir_work_cfg']})
       if r['return']>0: return r
       cfg1=r['dict']

       # Update cfg
       r=merge_dicts({'dict1':cfg, 'dict2':cfg1})
       if r['return']>0: return r

    # Check external repos
    rps=os.environ.get(cfg['env_key_repos'],'')
    if rps=='': rps=os.path.join(work['env_root'],cfg['subdir_default_repos'])
    work['dir_repos']=rps

    inintialized=True

    return {'return':0}

##############################################################################
# List all files recursively in a given directory

def list_all_files(i):
    """
    Input:  {
              path            - top level path
              (path_ext)      - path extension (needed for recursion)
              (limit)         - limit number of files (if directories with a large number of files)
              (number)        - current number of files
              (get_all_files) - if 'yes' do not ignore special directories (like .cm)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              list         - list of all files
              number       - number of files in a current directory (needed for recursion)
            }
    """

    number=0
    if i.get('number','')!='': 
       number=int(i['number'])

    limit=-1
    if i.get('limit','')!='': 
       limit=int(i['limit'])

    a=[] 

    pe=''
    if i.get('path_ext','')!='': 
       pe=i['path_ext']

    po=i.get('path','')

    try:
       dirList=os.listdir(po)
    except Exception as e:
        None
    else:
        for fn in dirList:
            p=os.path.join(po, fn)

            if i.get('get_all_files','')=='yes' or fn not in cfg['special_directories']:
               if os.path.isdir(p):
                  r=list_all_files({'path':os.path.join(p), 'path_ext':os.path.join(pe, fn), 'number':str(number)})
                  if r['return']>0: return r
                  a.extend(r['list'])
               else:
                  a.append(os.path.join(pe, fn))

                  number=len(a)
                  if limit!=-1 and number>limit: break
 
    return {'return':0, 'list':a, 'number':str(number)}

##############################################################################
# Reload repo cache 

def reload_repo_cache(i):
    """
    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """

    global cache_repo_uoa, cache_repo_info, paths_repos_all, cache_repo_init

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
        p=qq['dict'].get('path','')
        if p!='':
           paths_repos_all.append(os.path.normpath(p))

    cache_repo_init=True

    return {'return':0}

##############################################################################
# Save repo cache 

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
            }
    """

    ruoa=i['repo_uoa']
    ruid=ruoa
    
    if not is_uid(ruoa): 
       ruid=cache_repo_uoa.get(ruoa,'')
       if ruid=='':
          return {'return':1, 'error':'repository is not found in the cache'}

    d=cache_repo_info.get(ruid,{})
    if len(d)==0:
       return {'return':1, 'error':'repository is not found in the cache'}

    r={'return':0}
    r.update(d)

    return r

##############################################################################
# Find repo by path

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
       if not cache_repo_init:
          r=reload_repo_cache({}) # Ignore errors
          if r['return']>0: return r

       for q in cache_repo_info:
           qq=cache_repo_info[q]
           if p==qq['dict'].get('path',''):
              uoa=qq['data_uoa']
              uid=qq['data_uid']
              alias=uid
              if not is_uid(uoa): alias=uoa
              found=True
              break

    if not found:
       return {'return':16, 'error': 'repository not found in this path'}

    return {'return':0, 'repo_uoa': uoa, 'repo_uid': uid, 'repo_alias':alias}

##############################################################################
# Find path to a given repo

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

              path         - path to repo

              repo_uoa     - repo UOA
              repo_uid     - repo UID
              repo_alias   - repo alias
            }
    """

    a=i.get('repo_uoa','')
    ai=a

    pr=''
    if a!='':
       if a==cfg['repo_name_default']:
          pr=work['dir_default_repo']
          uoa=cfg['repo_name_default']
          uid=cfg['repo_uid_default']
          alias=uoa
       elif a==cfg['repo_name_local']:
          pr=work['dir_local_repo']
          uoa=cfg['repo_name_local']
          uid=cfg['repo_uid_local']
          alias=uoa
       else:
          # Reload cache if not initialized
          if not cache_repo_init:
             r=reload_repo_cache({}) # Ignore errors
             if r['return']>0: return r

          if not is_uid(a):
             ai=cache_repo_uoa.get(a,'')
             if ai=='':
                return {'return':1, 'error':'repository "'+a+'" was not found in cache'}

          cri=cache_repo_info.get(ai, {})
          pr=cri.get('dict',{}).get('path','')

          if pr=='':
             return {'return':1, 'error':'path for repository "'+a+'" was not found in cache'}

          uoa=cri['data_uoa']
          uid=cri['data_uid']
          alias=cri['data_alias']

    else:
       # Get current repo path
       pr=work['dir_work_repo']
       uoa=work['repo_name_work']
       uid=work['repo_uid_work']
       alias=uoa

    return {'return':0, 'path':pr, 'repo_uoa':uoa, 'repo_uid':uid, 'repo_alias':alias}

##############################################################################
# Find path to data (first search in default repo, then local one and then all other repos)

def find_path_to_data(i):
    """
    Input:  {
              (repo_uoa) - repo UOA
              module_uoa - module UOA
              uoa        - data UOA
            }

    Output: {
              return       - return code =  0, if successful
                                           16, if data not found (may be warning)
                                         >  0, if error
              (error)      - error text if return > 0
              path         - path to data
              path_module  - path to module entry with this entry
              path_repo    - path to the repository of this entry
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
    if ruoa!='':
       r=find_path_to_repo({'repo_uoa':ruoa})
       if r['return']>0: return r
       ps=[r['path']]
       ruid=r['repo_uid']
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
           if not cache_repo_init:
              r=reload_repo_cache({}) # Ignore errors
              if r['return']>0: return r
           ps=paths_repos_all

        for pr in ps:
            r=find_path_to_entry({'path':pr, 'data_uoa':muoa})
            if r['return']>0 and r['return']!=16: return r
            elif r['return']==0:
               muoa=r['data_uoa']
               muid=r['data_uid']
               malias=r['data_alias']
               pm=r['path']
               r1=find_path_to_entry({'path':pm, 'data_uoa':duoa})
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
       if ruoa!='': s+=ruoa+':'
       s+=muoa+':'+duoa+'" ('
       if ruoa!='': 
          if ruid!='':s+=ruid+':'
          else: s+='?:'
       s+=muid+':'+duid+')'

       return {'return':16, 'error':'can\'t find path to data "'+s}

    return {'return':0, 'path':pd, 'path_module':pm, 'path_repo':pr,
                        'module_uoa':muoa, 'module_uid':muid, 'module_alias':malias,
                        'data_uoa':duoa, 'data_uid':duid, 'data_alias':dalias}

##############################################################################
# Find path to an UOA entry (check UID or alias)

def find_path_to_entry(i):
    """
    Input:  {
              path     - path to a repository
              data_uoa - data UOA
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

    if duoa=='':
       raise Exception('data_uoa is empty')

    # Disambiguate UOA
    alias=''
    if is_uid(duoa):
       # If UID
       uid=duoa

       # Check if alias exists
       p1=os.path.join(p, cfg['subdir_ck_ext'], cfg['file_alias_u'] + uid)
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
          p2=os.path.join(p, alias)
          return {'return':0, 'path':p2, 'data_uid':uid, 'data_alias':alias, 'data_uoa':alias}

       p2=os.path.join(p, uid)
       if os.path.isdir(p2):
          return {'return':0, 'path':p2, 'data_uid':uid, 'data_alias':'', 'data_uoa':uid}

       return {'return':-1}

    # If alias
    alias=duoa

    p1=os.path.join(p, alias).encode('utf-8')
    if os.path.isdir(p1):
       # Check uid for this alias
       p2=os.path.join(p, cfg['subdir_ck_ext'], cfg['file_alias_a'] + alias)
       try:
          f=open(p2)
          uid=f.readline().strip()
          f.close()
       except Exception as e:
          return {'return':10, 'error':'inconsistent entry: alias "'+alias+'" exists, but not the UID in file '+p2, 
                               'path':p1, 'data_alias':alias}

       return {'return':0, 'path':p1, 'data_uid':uid, 'data_alias':alias, 'data_uoa':alias}

    return {'return':16}

##############################################################################
# Load meta description from a path

def load_meta_from_path(i):
    """
    Input:  {
              path     - path to a data entry
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
            }
    """

    p=i['path']

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
       p3=os.path.join(p, cfg['subdir_ck_ext'], cfg['file_updates'])
       if os.path.isfile(p3):
          r=load_json_file({'json_file':p3})
          if r['return']>0: return r
          rx['path_updates']=p3
          rx['updates']=r['dict']

       return rx
    else:
       return {'return':1, 'error':'meta description is not found in path '+p}

##############################################################################
# Load CK module

def load_module_from_path(i):
    """
    Input:  {
              path - module path
              cfg  - module cfg
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              code         - python code object
            }
    """

    p=i['path']
    u=i['cfg']

    # Check module name
    n=u.get('module_name',cfg['module_code_name'])

    # Find module
    try:
       x=imp.find_module(n, [p])
    except ImportError as e:
       return {'return':1, 'error':'can\'t find module code (path='+p+', name='+n+', err='+format(e)+')'}

    # Generate uid for the run-time extension of the loaded module 
    # otherwise modules with the same extension (key.py for example) 
    # will be reloaded ...

    r=gen_uid({})
    if r['return']>0: return r
    ruid='rt-'+r['data_uid']

    try:
       c=imp.load_module(ruid, x[0], x[1], x[2])
    except ImportError as e:
       return {'return':1, 'error':'can\'t load module code (path='+p+', name='+n+', err='+format(e)+')'}

    x[0].close()

    # Initialize module with this CK instance 
    c.ck=sys.modules[__name__]
    c.cfg=u

    # Initialize module
    r=c.init(i)
    if r['return']>0: return r

    return {'return':0, 'code':c}
   
##############################################################################
# Perform action

def perform_remote_action(i):
    """
    Input:  { See 'perform_action' function }
    Output: { See 'perform_action' function }
    """

    # Import modules compatible with Python 2.x and 3.x
    import urllib

    try:
       import urllib.request as urllib2
    except:
       import urllib2

    try:
       from urllib.parse import urlencode
    except:
       from urllib import urlencode

    #URL
    url=i.get('remote_server_url','')

    # Process i
    if 'cid' in i: del (i['cid'])
    if 'repo_uoa' in i: del(i['repo_uoa'])
    if 'remote_server_url' in i: del(i['remote_server_url'])

    # Prepare post variables
    r=dumps_json({'dict':i, 'skip_indent':'yes'})
    if r['return']>0: return r
    s=r['string'].encode('utf8')

    post=urlencode({'ck_json':s})
    if sys.version_info[0]>2: post=post.encode('utf8')

#    url="http://localhost:3344/json?"

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

    # Try to convert output to dictionary
    r=convert_json_str_to_dict({'str':s, 'skip_quote_replacement':'yes'})
    if r['return']>0: 
       return {'return':1, 'error':'can\'t parse output from remote CK server ('+r['error']+')'}

    return r['dict']

##############################################################################
# Perform action (find module or use kernel)

def perform_action(i):
    """
    Input:  {
              all parameters from function 'access'

              (common_func) - if 'yes', ignore search for modules 
                                        and call common func from the CK kernel
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
    if action=='' or action=='-?' or action=='-h' or action=='--help':
       action='help'

    # Substitute # in CIDs
    cid=i.get('cid','')
    cids=i.get('cids',[])

    out=i.get('out','')

    need_subst=False
    rc={} # If CID from current directory

    if cid.startswith('#'):
       need_subst=True
    else:
       for c in cids:
           if c.startswith('#'): 
              need_subst=True
              break

    # If need to substitute #, attempt to detect current CID
    if need_subst:
       rc=detect_cid_in_current_path({})
       if rc['return']>0: return rc

    # Process cid (module or CID)
    module_uoa=cid
    if cid.find(':')>=0 or cid.startswith('#'):
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
    ruoa=i.get('repo_uoa','')
    rs=i.get('remote_server_url','')
    if rs!='':
       if out!='json_file': 
          i['out']='json'   # For remote web service return JSON

       r=perform_remote_action(i)
       if out!='json_file': 
          r['out']='json'   # For remote web service return JSON
       return r

    # Process and parse cids -> xcids
    xcids=[]

    for c in cids:
       r=parse_cid({'cid':c, 'cur_cid':rc})
       if r['return']>0: return r
       xcids.append(r)
    i['xcids']=xcids

    # Check if common function
    cf=i.get('common_func','')

    if cf!='yes' and module_uoa!='' and module_uoa.find('*')<0 and module_uoa.find('?')<0:
       # Find module and load meta description
       rx=load({'module_uoa':cfg['module_name'], 
                'data_uoa':module_uoa})
       if rx['return']>0: return rx

       u=rx['dict']
       p=rx['path']

       # Check if action in actions
       if action in u.get('actions',{}):
          # Load module
          r=load_module_from_path({'path':p, 'cfg':u})
          if r['return']>0: return r

          c=r['code']
          c.work['self_module_uid']=rx['data_uid']
          c.work['self_module_uoa']=rx['data_uoa']
          c.work['self_module_alias']=rx['data_alias']

          action1=u.get('actions_redirect',{}).get(action,'')
          if action1!='': action=action1

          a=getattr(c, action)
          return a(i)

    # Check if action == special keyword (add, delete, list, etc)
    if (module_uoa!='' and action in cfg['common_actions']) or \
       (module_uoa=='' and action in cfg['actions']):
       # Check function redirect - needed if action 
       #   is the same as internal python keywords such as list
       action1=cfg['actions_redirect'].get(action,'')
       if action1!='': action=action1

       a=getattr(sys.modules[__name__], action)
       return a(i)

    # Prepare error
    if module_uoa=='':
       er='in kernel'
    else:
       er='in module "'+module_uoa+'"'

    return {'return':1,'error':'action not found '+er}

##############################################################################
# Convert CID to dict and add missing parts in CID with current path if #

def parse_cid(i):
    """
    Input:  {
              cid       - in format (REPO_UOA:)MODULE_UOA:DATA_UOA 
              (cur_cid) - output of function 'detect_cid_in_current_path'
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

    cc=i.get('cur_cid', {})

    a0=cc.get('repo_uoa','')
    m0=cc.get('module_uoa','')
    d0=cc.get('data_uoa','')

    if c.startswith('#'):
       c=c[1:]

    x=c.split(':')
    if len(x)<2 and m0=='':
       return {'return':1, 'error':'unknown CID format'}

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
       return {'return':1, 'error':'unknown CID format'}

    return r

##############################################################################
# Create an UOA entry in a given path

def create_entry(i):
    """
    Input:  {
              path       - path where to create an entry
              (data_uoa) - data UOA
              (data_uid) - if uoa is an alias, we can force data UID
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
          r=find_path_to_entry({'path':p0, 'data_uoa':uid})
          if r['return']>0 and r['return']!=16: return r
          elif r['return']==0:
             r['return']=16
             return r

       alias=''
    else:
       # Check if already exists
       r=find_path_to_entry({'path':p0, 'data_uoa':d})
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

    if alias!='':
       p=os.path.join(p0, alias)
    else:
       p=os.path.join(p0, uid)

    # Check alias disambiguation
    if alias!='':
       p1=os.path.join(p0, cfg['subdir_ck_ext'])
       if not os.path.isdir(p1):
          # Create .cm directory
          try:
             os.mkdir(p1)
          except Exception as e:
             return {'return':1, 'error':format(e)}

       # Check if alias->uid exist
       p3=os.path.join(p1, cfg['file_alias_a'] + alias)
       if os.path.isfile(p3):
          try:
             fx=open(p3)
             uid1=fx.readline().strip()
             fx.close()
          except Exception as e:
             None

          if uid1!=uid:
             return {'return':1, 'error':'different alias->uid disambiguator already exists in '+p3}

       try:
          f=open(p3, 'w')
          f.write(uid+'\n')
          f.close()
       except Exception as e:
          None

       # Check if uid->alias exist
       p2=os.path.join(p1, cfg['file_alias_u'] + uid)
       if os.path.isfile(p2):
          try:
             fx=open(p2)
             alias1=fx.readline().strip()
             fx.close()
          except Exception as e:
             None

          if alias1!=alias:
             return {'return':1, 'error':'different uid->alias disambiguator already exists in '+p2}

       try:
          f=open(p2, 'w')
          f.write(alias+'\n')
          f.close()
       except Exception as e:
          None

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

def delete_alias(i):
    """
    Input:  {
              path         - path to the entry
              data_uid     - data UID
              (data_alias) - data alias
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """

    p=i['path']
    alias=i.get('data_alias','')
    uid=''
    if alias!='' and os.path.isdir(p):
       p1=os.path.join(p, cfg['subdir_ck_ext'], cfg['file_alias_a'] + alias)
       if os.path.isfile(p1):
          try:
             f=open(p1)
             uid=f.readline().strip()
             f.close()
          except Exception as e:
             None
          os.remove(p1)

       if uid=='': uid=i['data_uid']

       if uid!='':
          p1=os.path.join(p, cfg['subdir_ck_ext'], cfg['file_alias_u'] + uid)
          if os.path.isfile(p1):
             os.remove(p1)

    return {'return':0}

##############################################################################
# Delete a given directory with subdirectories (be careful)

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

    if not os.path.isdir(p):
       return {'return':1, 'error':p+' is not a directory'}

    shutil.rmtree(p)

    return {'return':0}

##############################################################################
# Convert dictionary into CK flat format

def flatten_dict(i):
    """
    Any list item is converted to @number=value
    Any dict item is converted to #key=value
    # is always added at the beginning 

    Input:  {
              dict    - python dictionary
              prefix  - prefix (for recursion)
            }

    Output: {
              return  - return code =  0, if successful
                                    >  0, if error
              (error) - error text if return > 0
              dict    - flattened dictionary
            }
    """

    prefix='#'
    if i.get('prefix','')!='': prefix=i['prefix']

    a=i['dict']
    aa={}

    flatten_dict_internal(a, aa, prefix)

    return {'return':0, 'dict': aa}

##############################################################################
# Convert dictionary into CK flat format (internal, used for recursion)

def flatten_dict_internal(a, aa, prefix):
    # Start flattening
    if type(a) is dict or type(a) is list:
       i=0
       for x in a:
           if type(a) is dict: 
              v=a[x] 
              prefix1=prefix+'#'+x
           else: 
              prefix1=prefix+'@'+str(i)
              v=x
           if type(v) is dict or type(v) is list:
              flatten_dict_internal(v, aa, prefix1)
           else:
              aa[prefix1]=v
           i+=1
    else:
       aa[prefix]=a

    return {'return':0, 'dict': a}

##############################################################################
# Get value from dict by flat key

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
              if len(a)<=long(k1): break
              a=a[long(k1)]
           k1=''
           kt=y
        else:
           k1+=y

        if x>=len(k): break

    if k1!='' and kt!='':
       if kt=='#':   
          if k1 in a: v=a[k1]
       else:         
          if len(a)>long(k1): v=a[long(k1)]

    return {'return':0, 'value': v}

##############################################################################
# Set value in array using flattened key

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
              if len(a)<=long(k1): 
                 for q in range(len(a)-1,long(k1)):
                     if y=='#': a.append({})
                     else: a.append([])
              a=a[long(k1)]
           k1=''
           kt=y
        else:
           k1+=y

        if x>=len(k): break

    if k1!='' and kt!='':
       if kt=='#':   
          a[k1]=v
       else:         
          if len(a)<=long(k1): 
             for q in range(len(a)-1,long(k1)):
                 if y=='#': a.append({})
                 else: a.append([])
          a[long(k1)]=v

    return {'return':0, 'dict': i['dict']}

##############################################################################
# Restore flattened dict

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
# Get current date and time

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
# \n=======================================================

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

    # Check info about module
    ld=len(dirs)
    if ld>0:
       m=dirs[ld-1]

       rx=find_path_to_entry({'path':p, 'data_uoa':m})
       if rx['return']>0 and rx['return']!=16: return rx
       elif rx['return']==0:
          r['module_uoa']=rx['data_uoa']
          r['module_uid']=rx['data_uid']
          r['module_alias']=rx['data_alias']
       
       # Check info about data
       if ld>1:
          d=dirs[ld-2]

          rx=find_path_to_entry({'path':os.path.join(p,m), 'data_uoa':d})
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
# Convert info about entry to CID
# \n=======================================================

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

def webhelp(i):
    """
    Input:  { from acess function }

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

       rx=convert_entry_to_cid(r)
       if rx['return']>0: return rx

       cuoa=rx['cuoa']
       cid=rx['cid']
       xcuoa=rx['xcuoa']
       xcid=rx['xcid']

       # Prepare URL
       url+='_'+cid.replace(':','_')

    out('Opening web page '+url+' ...')

    import webbrowser
    webbrowser.open(url)

    return {'return':0}

#########################################################
# Common action: print help for a given module

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

    h+='\n'
    h+='  Module actions:\n'

    if m=='<module_uoa>':
       # Internal actions (for this kernel)
       for q in sorted(cfg['actions']):
           if q not in cfg['common_actions']:
              s=q
              desc=cfg['actions'][q].get('desc','')
              if desc!='': s+=' - '+desc
              h+='    '+s+'\n'
    else:
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
              h+='    '+s+'\n'

    h+='\n'
    h+='  Common actions:\n'

    for q in sorted(cfg['common_actions']):
        s=q
        desc=cfg['actions'][q].get('desc','')
        if desc!='': s+=' - '+desc
        h+='    '+s+'\n'

    h+='\n'
    h+=cfg['help_web']

    if o=='con': out(h)

    return {'return':0, 'help':h}

#########################################################
# Common action: print info about a given CK entry
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

def path(i):
    """
    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              Output from from 'detect_cid_in_current_path' function

              cuoa         - module_uoa:data_uoa           (substituted with ? if can't find)
              cid          - module_uid:data_uid           (substituted with ? if can't find)
              xcuoa        - repo_uoa:module_uoa:data_uoa  (substituted with ? if can't find)
              xcid         - repo_uid:module_uid:data_uid  (substituted with ? if can't find)
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

#########################################################
# Common action: load data (module) meta description

def load(i):
    """
    Input:  {
              (repo_uoa)       - repo UOA
              module_uoa       - module UOA
              data_uoa         - data UOA
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              dict         - entry meta description
              (info)       - entry info
              (updates)    - entry updates

              path         - path to data entry
              path_module  - path to module entry with this entry
              path_repo    - path to the repository of this entry
              module_uoa   - module UOA 
              module_uid   - module UID
              module_alias - module alias
              data_uoa     - data UOA
              data_uid     - data UID
              data_alias   - data alias
              data_name    - user friendly name
            }
    """

    o=i.get('out','')

    a=i.get('repo_uoa','')
    m=i.get('module_uoa','')
    d=i.get('data_uoa','')

    if d=='':
       return {'return':1, 'error':'data UOA is not defined'}

    r=find_path_to_data({'repo_uoa':a, 'module_uoa':m, 'data_uoa':d})
    if r['return']>0: return r
    p=r['path']

    # Load meta description
    r1=load_meta_from_path({'path':p})
    if r1['return']>0: return r1

    r.update(r1)
    r['path']=p

    r['data_name']=r1.get('info',{}).get('data_name','')

    # If console mode, print json
    if o=='con':
       rr=dumps_json({'dict':r})
       if rr['return']==0:
          out(rr['string'])

    return r

#########################################################
# Common action: find data (module) - uses 'load' function

def find(i):
    """
    Input:  {
              (repo_uoa)  - repo UOA
              module_uoa  - module UOA
              data_uoa    - data UOA
            }

    Output: { 
              Output of the 'load' function 
            }
    """

    o=i.get('out','')
    i['out']=''
    r=load(i)
    i['out']=o

    if r['return']>0: return r
    p=r['path']

    # If console mode, print path
    if o=='con':
       out(p)

    return r

##############################################################################
# Common action: add data (module) meta-description to a repository
# \n=======================================================

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
              (merge_dict)           - if 'yes' and update=='yes' merge dictionaries, either substitute!

              (info)                 - entry info to record - normally, should not use it!
              (updates)              - entry updates info to record - normally, should not use it!
              (ignore_update)        - if 'yes', do not add info about update
            }

    Output: {
              return       - return code =  0, if successful
                                           16, if data entry already exists
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

    up=i.get('update','')

    # Get repo path
    r=find_path_to_repo({'repo_uoa':ra})
    if r['return']>0: return r
    pr=r['path']

    # Load info about module
    r=load({'module_uoa':cfg['module_name'],
            'data_uoa':m})
    if r['return']>0: return r
    elif r['return']==16: 
       return {'return':8, 'error':'can\'t find path to module "'+m+'"'}
    uid=r['data_uid']
    alias=r['data_alias']
    if alias=='': alias=uid
    module_desc=r['dict']

    # Ask additional questions
    if o=='con':
       # Asking for alias
       if d=='' or is_uid(d):
          r=inp({'text':'Enter an alias (or Enter to skip it): '})
          d=r['string']

       # Asking for user-friendly name
       if dn=='' and up!='yes':
          r=inp({'text':'Enter a user-friendly name of this entry (or Enter to reuse alias): '})
          dn=r['string']
          if dn=='' and not is_uid(d):
             dn=d

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
    if d!='': i1['data_uoa']=d
    if di!='': i1['data_uid']=di
    rr=create_entry(i1)
    if rr['return']>0 and rr['return']!=16: return rr

    duid=rr['data_uid']

    # Preparing meta-description
    a={}
    info={}
    updates={}

    p2=rr['path']
    p3=os.path.join(p2, cfg['subdir_ck_ext'])
    p4=os.path.join(p3, cfg['file_meta'])
    p4i=os.path.join(p3, cfg['file_info'])
    p4u=os.path.join(p3, cfg['file_updates'])

    # If last entry exists
    if rr['return']==16:
       if up=='yes':
          t='updated'
          # Entry exists, load configuration if update
          r2=load_meta_from_path({'path':p2})
          if r2['return']>0: return r2
          a=r2['dict']
          info=r2.get('info',{})
          updates=r2.get('updates',{})
       else:
          return {'return':1,'error':'entry already exists in path ('+p2+')'}
    else:
       # Create configuration directory
       if not os.path.isdir(p3):
          try:
             os.mkdir(p3)
          except Exception as e:
             return {'return':1, 'error':format(e)}

    if dfduoa!='':
       r=merge_dicts({'dict1':a, 'dict2':df})
       if r['return']>0: return r

    # If dict, info and updates are in input, try to merge ...
    cma=i.get('dict',{})
    if i.get('merge_dict','')=='yes':
       r=merge_dicts({'dict1':a, 'dict2':cma})
       if r['return']>0: return r
    else:
       a=cma

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
    if dn!='': info['data_name']=dn

    # Add control info
    x={'engine':'CK',
       'version':cfg['version']}
    if 'user_name' in cfg:
       x['user_name']=cfg['user_name']
    if 'license_for_data' in cfg:
       x['license']=cfg['license_for_data'] 
    r=get_current_date_time({})
    x['iso_datetime']=r['iso_datetime']

    y=info.get('control',{})
    if i.get('ignore_update','')!='yes':
       if len(y)==0:
          info['control']=x
       else:
          y=updates.get('control',[])
          y.append(x)
          updates['control']=y

    if len(updates)>0:
       # Record updates
       rx=save_json_to_file({'json_file':p4u, 'dict':updates})
       if rx['return']>0: return rx

    # Record meta description
    rx=save_json_to_file({'json_file':p4, 'dict':a})
    if rx['return']>0: return rx

    # Record info
    rx=save_json_to_file({'json_file':p4i, 'dict':info})
    if rx['return']>0: return rx

    if o=='con':
       out('Entry '+t+' successfully!')
       out('')
       out('Path = '+p2)
       out('UID  = '+duid)

    rr['return']=0

    return rr

##############################################################################
# Common action: update data (module) meta-description to a repository

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

              (info)                 - entry info to record - normally, should not use it!
              (updates)              - entry updates info to record - normally, should not use it!
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              Output from the 'create_entry' function
            }

    """

    # Try to load entry, if doesn't exist, add entry
    dd={}

    o=i.get('out','')
    i['out']=''

    r=load(i)
    i['out']=o

    if r['return']==0: 
       i['update']='yes'

    # Try to add or updated
    return add(i)

##############################################################################
# Common action: delete data (module) entry

def rm(i):
    """
    Input:  {
              (repo_uoa)  - repo UOA
              module_uoa  - module UOA
              data_uoa    - data UOA
              force       - if 'yes', force deleting without questions
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    a=i.get('repo_uoa','')
    m=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    if duoa=='':
       return {'return':1, 'error':'data UOA is not defined'}

    lst=[]

    # Check wildcards
    if a.find('*')>=0 or a.find('?')>=0 or m.find('*')>=0 or m.find('?')>=0 or duoa.find('*')>=0 or duoa.find('?')>=0: 
       r=list_data({'repo_uoa':a, 'module_uoa':m, 'data_uoa':duoa})
       if r['return']>0: return r

       lst=r['lst']
    else:
       # Find path to data
       r=find_path_to_data({'repo_uoa':a, 'module_uoa':m, 'data_uoa':duoa})
       if r['return']>0: return r
       p=r['path']
       muoa=r.get('module_uoa','')
       muid=r.get('module_uid','')
       duid=r.get('data_uid','')
       duoa=r.get('data_alias','')
       if duoa=='': duoa=duid

       lst.append({'path':p, 'module_uoa':muoa, 'module_uid':muid, 'data_uoa':duoa, 'data_uid': duid})

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
        xcuoa=muoa+':'+duoa+' ('+muid+':'+duid+')'

        # If interactive
        to_delete=True
        if o=='con' and i.get('force','')!='yes':
           r=inp({'text':'Are you sure to delete CK entry '+xcuoa+' (Y/yes or N/no/Enter): '})
           c=r['string'].lower()
           if c!='y' and c!='yes': to_delete=False

        # If deleting
        if to_delete:
           # First remove alias if exists
           if dalias!='':
              # Delete alias
              r=delete_alias({'path':pm, 'data_alias':dalias, 'data_uid':duid})
              if r['return']>0: return r

           # Delete directory
           r=delete_directory({'path':p})
           if r['return']>0: return r

           if o=='con':
              out('   Entry '+xcuoa+' was successfully deleted!')

    return {'return':0}

##############################################################################
# Common action: delete data (module) entry -> calls rm function

def remove(i):
    """
    Input:  { See rm function }
    Output: { See rm function }

    """

    return rm(i)

##############################################################################
# Common action: delete data (module) entry -> calls rm function

def delete(i):
    """
    Input:  { See rm function }
    Output: { See rm function }

    """

    return rm(i)

##############################################################################
# Common action: rename data entry

def ren(i):
    """
    Input:  {
              (repo_uoa)     - repo UOA
              module_uoa     - module UOA
              data_uoa       - data UOA

              xcids[0]       - {'data_uoa'} -new data UOA
                 or
              new_data_uoa   - new data alias
                 or
              new_data_uid   - new data UID (leave empty to keep old one)

              (remove_alias) - if 'yes', remove alias
              
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

    if muoa=='': return {'return':1, 'error':'module UOA is not defined'}
    if duoa=='': return {'return':1, 'error':'data UOA is not defined'}

    # Attempt to load
    ii={'module_uoa':muoa, 'data_uoa':duoa}
    if ruoa!='': ii['repo_uoa']=ruoa
    r=load(ii)
    if r['return']>0: return r

    duoa=r['data_uoa']
    duid=r['data_uid']
    p=r['path']
    pm=r['path_module'] 
    p1=os.path.join(pm, cfg['subdir_ck_ext'])
    pn=p

    # Check new data UOA
    nduoa=i.get('new_data_uoa','')
    nduid=i.get('new_data_uid','')

    xcids=i.get('xcids',[])
    if len(xcids)>0: 
       xcid=xcids[0]
       nduoa=xcid.get('data_uoa','')

    if i.get('remove_alias','')=='yes':
       nduoa=duid

    if nduoa=='': nduoa=duoa

    if nduid!=duid:
       # Check that new UID doesn't exist
       p2=os.path.join(p1, cfg['file_alias_u'] + nduid)
       if os.path.isfile(p2):
          return {'return':1, 'error':'new UID already exists'}

    if nduoa!=duoa:
       if not is_uoa(nduoa):
          return {'return':1, 'error':'alias has disallowed characters'}

       # Need to rename directory
       if os.path.isdir(nduoa):
          return {'return':1, 'error': 'new alias already exists'}

       pn=os.path.join(pm, nduoa)
       os.rename(p, pn)

    if nduid=='': nduid=duid

    # Remove old alias disambiguator
    if not is_uid(duoa):
       r=delete_alias({'path':pm, 'data_uid':duid, 'data_alias':duoa})
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
       try:
          f=open(p3, 'w')
          f.write(nduid+'\n')
          f.close()
       except Exception as e:
          None

       # Write UID disambiguator
       p2=os.path.join(p1, cfg['file_alias_u'] + nduid)
       try:
          f=open(p2, 'w')
          f.write(nduoa+'\n')
          f.close()
       except Exception as e:
          None

    if o=='con':
       out('Entry was successfully renamed!')

    return {'return':0}

##############################################################################
# Common action: rename data entry -> calls 'ren' function

def rename(i):
    """
    Input:  { See ren function }
    Output: { See ren function }

    """

    return ren(i)

##############################################################################
# Common action: copy (or move) data entry

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
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              Output of 'add' function
            }

    """

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

    duoa=r['data_uoa']
    duid=r['data_uid']

    p=r['path']

    dd=r.get('dict',{})
    di=r.get('info',{})
    du=r.get('updates',{})

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

    # Adding new entry 
    if nruoa==ruoa and nmuoa==muoa and nduid==duid:
       return {'return':1, 'error':'moving within the same directory - use "rename" instead'}

    ii={'module_uoa':nmuoa, 'data_uoa': nduoa, 'dict':dd, 'info':di, 
        'updates':du, 'ignore_update':'yes'}
    if nduid!='': ii['data_uid']=nduid
    if nruoa!='': ii['repo_uoa']=nruoa
    r=add(ii)
    if r['return']>0: return r
    pn=r['path']

    # Recursively copying all files (except .cm)
    rx=list_all_files({'path':p})
    if rx['return']>0: return rx

    for q in rx['list']:
        p1=os.path.join(p,q)
        pn1=os.path.join(pn,q)

        # Create if dir
        pn1d=os.path.dirname(pn1)
        if not os.path.isdir(pn1d): os.makedirs(pn1d)

        shutil.copyfile(p1,pn1)

    tt='copied'
    # If move, remove old one
    if i.get('move','')=='yes':
       tt='moved'

       ii={'module_uoa':muoa, 'data_uoa': duoa}
       if ruoa!='': ii['repo_uoa']=ruoa
       rx=rm(ii)
       if rx['return']>0: return rx

    if o=='con':
       out('Entry '+muoa+':'+duoa+' was successfully '+tt+'!')

    return r

##############################################################################
# Common action: copy (or move) data entry

def copy(i):
    """
    Input:  { See 'cp' function }
    Output: { See 'cp' function }

    """

    return cp(i)

##############################################################################
# Common action: move data entry

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

def move(i):
    """
    Input:  { See 'mv' function }
    Output: { See 'mv' function }

    """

    return mv(i)

##############################################################################
# Common action: list data entries

def list_data(i):
    """
    Input:  {
              (repo_uoa)   - repo UOA
              (module_uoa) - module UOA
              (data_uoa)   - data UOA
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

    lst=[]

    o=i.get('out','')

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')
    muid=i.get('module_uid','')

    # Check if wild cards present (only repo or data)
    wr=''
    wm=''
    wd=''

    if ruoa.find('*')>=0 or ruoa.find('?')>=0: wr=ruoa
    if muoa.find('*')>=0 or muoa.find('?')>=0: wm=muoa
    if duoa.find('*')>=0 or duoa.find('?')>=0: wd=duoa

    if wr!='' or wd!='':
       import fnmatch

    zr={}

    if ruoa!='' and wr=='':
       # Try to load a given repository
       r=access({'action':'load',
                 'module_uoa':cfg['repo_name'],
                 'data_uoa':ruoa,
                 'common_func':'yes'})
       if r['return']>0: return r
       duid=r['data_uid']

       zr[duid]=r
    else:
       # Prepare all repositories
       if not cache_repo_init:
          r=reload_repo_cache({}) # Ignore errors
          if r['return']>0: return r
       zr=cache_repo_info 

    # Start iterating over repositories
    ir=0
    iir=True
    zrk=zr.keys()
    lr=len(zrk)
    while iir:
       skip=False
       if ir==0:
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
          if wr=='*':
             pass
          elif is_uid(ruoa): 
             skip=True # If have wildcards, but not alias
          else:
             if not fnmatch.fnmatch(ruoa, wr):
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
                    if fn not in cfg['special_directories']:
                       xm.append(fn)

          # Iterate over modules
          for mu in xm:
              r=find_path_to_entry({'path':p, 'data_uoa':mu})
              if r['return']==0:
                 mp=r['path']
                 muid=r['data_uid']
                 muoa=r['data_uoa']

                 mskip=False

                 if wm!='':
                    if wm=='*':
                       pass
                    elif is_uid(muoa): 
                       mskip=True # If have wildcards, but not alias
                    else:
                       if not fnmatch.fnmatch(muoa, wm):
                          mskip=True

                 if not mskip:
                    # Prepare data in the current directory
                    xd=[]

                    if duoa!='' and wd=='': 
                       xd.append(duoa)
                    else:   
                       # Now iterate over data inside a given path
                       try:
                          ld=os.listdir(mp)
                       except Exception as e:
                          None
                       else:
                          for fn in ld:
                              if fn not in cfg['special_directories']:
                                 xd.append(fn)

                    # Iterate over data
                    for du in xd:
                        r=find_path_to_entry({'path':mp, 'data_uoa':du})
                        if r['return']==0:
                           dp=r['path']
                           dpcfg=os.path.join(dp,cfg['subdir_ck_ext'])
                           duid=r['data_uid']
                           duoa=r['data_uoa']

                           if os.path.isdir(dpcfg): # Check if really CK data entry
                              dskip=False

                              if wd!='':
                                 if wd=='*':
                                    pass
                                 elif is_uid(duoa): 
                                    dskip=True # If have wildcards, but not alias
                                 else:
                                    if not fnmatch.fnmatch(duoa, wd):
                                       dskip=True

                              if not dskip:
                                 # Iterate over data 
                                 ll={'repo_uoa':ruoa, 'repo_uid':ruid,
                                    'module_uoa':muoa, 'module_uid':muid,
                                    'data_uoa':duoa, 'data_uid':duid,
                                    'path':dp}
                                     
                                 # Call filter
                                 fskip=False

                                 # Append
                                 if not fskip:
                                    lst.append(ll)

                                    if o=='con':
                                       x=ruoa+':'+muoa+':'+duoa
                                       print x

       # Finish iteration over repositories
       ir+=1

    return {'return':0, 'lst':lst}

##############################################################################
# Add action to a module

def add_action(i):
    """
    Input:  {
              (repo_uoa)                  - repo UOA
              module_uoa                  - normally should be 'module' already
              data_uoa                    - UOA of the module to be created

              func                        - action
              (desc)                      - desc

              (skip_appending_dummy_code) - if 'yes', do not append code
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

               Output of 'update' function
            }

    """

    o=i.get('out','')

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    func=i.get('func','')
    desc=i.get('desc','')

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
          r=inp({'text':'Add action function (or Enter to stop):    '})
          func=r['string']

       if desc=='':
          r1=inp({'text':'Add action description (or Enter to stop): '})
          desc=r1['string']

    # Check if empty
    if func=='':
       return {'return':1, 'error':'action (function) is not defined'}

    if func in actions:
       return {'return':1, 'error':'action (function) already exists in the module'}

    # Adding actions
    actions[func]={}
    if desc!='': actions[func]['desc']=desc
    dd['actions']=actions

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
       spm+='\n'+spma.replace('$#action#$', func).replace('$#desc#$',desc)

       # Write current module
       rx=save_text_file({'text_file':pmx, 'string':spm})
       if rx['return']>0: return rx

    # Update data entry
    if o=='con': out('')
    ii={'module_uoa':cfg['module_name'],
        'data_uoa':muoa,
        'dict':dd,
        'out':o}
    if ruoa!='': ii['repo_uoa']=ruoa
    r=update(ii)
    if r['return']>0: return r

    return r

##############################################################################
# Remove action from a module

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
          r=inp({'text':'Add action function (or Enter to stop): '})
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
        'out':o}
    if ruoa!='': ii['repo_uoa']=ruoa
    r=update(ii)
    if r['return']>0: return r

    return r

##############################################################################
# List actions in a module

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

############################################################################
# Main universal access function that can access all CK resources!

def access(i):

    """
    Input:  Either string or list or dictionary

            If string or list convert them to CK dictionary and set cmd=True

            {
               function
               module_uoa
               (cid1)
               (cid2)
               (cid3)
               (out=type)     Module output
                              == ''              - none
                              == 'con'           - console interaction (if from CMD, default)
                              == 'json'          - return dict as json to console
                              == 'json_with_sep' - separation line and return dict as json to console
                              == 'json_file'     - return dict as json to file
               (out_file)     Output file if out=='json_file'
               ...
               key1=value1
               key2=value2
               ...
               -key10
               -key11=value11
               --key12
               --key13=value13
               @file_json
               @@cmd_json
               --
               unparsed_cmd
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    global con_encoding

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

       ### Process request ######################################

       if i.get('con_encoding','')!='': con_encoding=i['con_encoding']

       ### Process action ###################################
       rr=init({})
       if rr['return']==0:
          # Run module with a given action
          rr=perform_action(i)
          if rr.get('out','')!='': o=rr['out']

    # Finalize call (check output) ####################################
    if o=='json' or o=='json_with_sep':
       if o=='json_with_sep': out(cfg['json_sep'])

       rr=dumps_json({'dict':rr})
       if rr['return']==0:
          s=rr['string']
          out(s)

    elif o=='json_file':
       fn=i.get('out_file','')
       if fn=='':
          rr['return']=1
          rr['error']='out==json_file but out_file is not defined in kernel access function'
       else:
          rr=save_json_to_file({'json_file':fn, 'dict':rr})

    # If error and CMD, output error to console
    if cmd:
       if rr['return']>0:
          out(cfg['error']+rr['error']+'!')

    return rr

##############################################################################
if __name__ == "__main__":
   r=access(sys.argv[1:])

   if 'return' not in r:
      raise Exception('CK access function should always return key \'return\'!')

   exit(int(r['return']))
