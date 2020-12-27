#
# Global configuration
#
# Developer(s): Grigori Fursin
#               Herve Guillou
#

# CK entry to keep client configuration info
CK_CFG_REPO_UOA="local"
CK_CFG_DATA_UOA="cbench"
CK_CFG_MODULE_UID="b34231a3467566f8" # ck info module:cfg

CK_CFG_MODULE_REPO_UOA="befd7892b0d469e9" # CK module UOA for REPO

CR_DEFAULT_SERVER="https://cKnowledge.io"
CR_DEFAULT_SERVER_URL=CR_DEFAULT_SERVER+"/api/v1/?"
CR_DEFAULT_SERVER_USER="crowd-user"
CR_DEFAULT_SERVER_API_KEY="43fa84787ff65c2c00bf740e3853c90da8081680fe1025e8314e260888265033"

PACK_SIZE_WARNING=5000000

CR_WORK_DIR='CR'
CR_SOLUTIONS_DIR='solutions'

CR_MODULE_UOA='solution'

PACK_FILE='pack.zip'

CR_ENV_USERNAME='CR_USER'
CR_ENV_API_KEY='CR_KEY'

CR_LINE='**************************************************************************'

CR_SOLUTION_CK_COMPONENTS=[
 {'cid':'module:device', 'version':'1.0.0'},
 {'cid':'module:env', 'version':'1.1.0'},
 {'cid':'module:machine', 'version':'1.0.0'},
 {'cid':'module:misc', 'version':'1.0.0'},
 {'cid':'module:os', 'version':'1.0.0'},
 {'cid':'module:package', 'version':'1.2.0'},
 {'cid':'module:platform*', 'version':'1.0.0'},
 {'cid':'module:script', 'version':'1.0.0'},
 {'cid':'module:soft', 'version':'1.2.0'},
 {'cid':'module:docker', 'version':'1.0.0'},
 {'cid':'module:event', 'version':'1.0.0'},
 {'cid':'module:lib', 'version':'1.0.0'},
 {'cid':'module:program', 'version':'1.0.3'},
 {'cid':'module:result', 'version':'1.0.0'},
 {'cid':'module:solution', 'version':'1.0.0'},
 {'cid':'os:*', 'version':'1.0.0'},
 {'cid':'platform.init:*', 'version':'1.0.0'},
 {'cid':'script:download-and-install-package', 'version':'1.0.0'},
 {'cid':'soft:compiler.python', 'version':'1.0.0'},
 {'cid':'soft:tool.adb', 'version':'1.0.0'},
]

import ck.kernel as ck

bootstrapping=False

##############################################################################
# Load client configuration

def load(i):
    """
    Input:  {
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 

              dict    [dict]   - configuration dictionary
              path    [str]    - path to CK cfg entry
            }
    """

    global bootstrapping

    import os

    # Get current configuration
    cfg={
          'server_url':CR_DEFAULT_SERVER_URL   # Default
        }
    path=''

    ii={'action':'load',
        'repo_uoa':CK_CFG_REPO_UOA,
        'module_uoa':CK_CFG_MODULE_UID,
        'data_uoa':CK_CFG_DATA_UOA}

    r=ck.access(ii)
    if (r['return']>0 and r['return']!=16): return r

    if r['return']==0: 
       cfg=r['dict']
       path=r['path']

    if not bootstrapping and (r['return']==16 or cfg.get('bootstrapped','')!='yes'):
       rx=update({'cfg':cfg})
       if rx['return']>0: return rx

    # Check overriding by env
    v=os.environ.get(CR_ENV_USERNAME,'')
    if v!='': cfg['username']=v
    v=os.environ.get(CR_ENV_API_KEY,'')
    if v!='': cfg['api_key']=v

    return {'return':0, 'dict':cfg, 'path':path}

##############################################################################
# Update CK modules and configuration

def update(i):
    """
    Input:  {
              (force) [bool] - if True, force update
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """

    import os

    global bootstrapping
    bootstrapping=True

    force=i.get('force')
    cfg=i.get('cfg',{})

    from . import obj

    title='Bootstrapping'
    if cfg.get('bootstrapped','')=='yes': title='Updating'

    ck.out(title+' cBench to support portable actions and workflows:')
    ck.out('')

    # Check release notes 
    server_url=cfg.get('server_url','')
    if server_url=='': server_url='https://cKnowledge.io/api/v1/?'

    from . import comm_min
    r=comm_min.send({'url':server_url,
                     'action':'event', 
                     'dict':{'type':'get-cbench-bootstrap-notes'}})

    notes=r.get('notes','')
    if notes!='':
       ck.out('***********************************************')
       ck.out(notes)
       ck.out('***********************************************')

    lst_all=[]

    sbf=os.environ.get('CB_SAVE_BOOTSTRAP_FILES','')

    if sbf=='':
       fboot='cb-bootstrap-20200529'
       files=[fboot+'.json']

       if os.name=='nt':
          files.append(fboot+'-win.json')

       for fn in files:
           r=ck.gen_tmp_file({'prefix':'cb-bootstrap-', 'suffix':'.json'})
           if r['return']>0: return r
           ftmp=r['file_name']

           burl=CR_DEFAULT_SERVER+'/static/bootstrap/'+fn

           ck.out('Downloading '+burl)

           from . import comm

           rx=comm.download_file({'url':burl, 'file':ftmp})
           if rx['return']>0: return rx

           rx=ck.load_json_file({'json_file':ftmp})
           if rx['return']>0: return rx

           lst_all+=rx['dict']

           os.remove(ftmp)

       r=obj.download({'components':lst_all, 'force':force})
       if r['return']>0 and r['return']!=8: return r

    else:
       for x in CR_SOLUTION_CK_COMPONENTS:
           r=obj.download({'cid':x['cid'], 'version':x.get('version',''), 'force':force})
           if r['return']>0: 
              if r['return']!=8: return r
              else: ck.out('    Skipped - already exists!')
           else:
              lst_all+=r['components']

       rx=ck.save_json_to_file({'json_file':sbf, 'dict':lst_all, 'sort_keys':'yes'})
       if rx['return']>0: return rx

    ck.out('')

    # Update cfg
    cfg['bootstrapped']='yes'

    ii={'action':'update',
        'repo_uoa':CK_CFG_REPO_UOA,
        'module_uoa':CK_CFG_MODULE_UID,
        'data_uoa':CK_CFG_DATA_UOA,
        'dict':cfg,
        'sort_keys':'yes'}

    r=ck.access(ii)

    ck.out(title+' finished!')
    ck.out('')

    return r

##############################################################################
# Get path to work directory in a USER space

def get_work_dir(i):
    """
    Input:  {
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 

              path    [str]    - path to work dir
            }
    """

    import os

    # Get home user directory
    from os.path import expanduser
    home = expanduser("~")

    work_dir=os.path.join(home, CR_WORK_DIR)
    if not os.path.isdir(work_dir):
       os.makedirs(work_dir)

    return {'return':0, 'path':work_dir}
