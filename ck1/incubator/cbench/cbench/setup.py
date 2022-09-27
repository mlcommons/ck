#
# Setup client
#
# Developer(s): Grigori Fursin
#               Herve Guillou
#

from . import config
from . import comm

import ck.kernel as ck

import json

##############################################################################
# Setup cBench

def setup(i):

    """
    Input:  {
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """


    # Get current configuration
    cfg={}

    ii={'action':'load',
        'repo_uoa':config.CK_CFG_REPO_UOA,
        'module_uoa':config.CK_CFG_MODULE_UID,
        'data_uoa':config.CK_CFG_DATA_UOA}

    r=ck.access(ii)
    if (r['return']>0 and r['return']!=16): ck.err(r) 

    if r['return']==0: cfg=r['dict']

    # Check commands

    # Username ##########################################################
    username=cfg.get('username','')

    if i.get('username')!=None: username=i['username']

    if username=='' or username==None:
       r=ck.inp({'text':'Enter cK username: '})
       if r['return']>0: ck.err(r)

       username=r['string'].strip()

    if username==None: username=''

    cfg['username']=username

    # API key ###########################################################        
    api_key=cfg.get('api_key','')

    if i.get('api_key')!=None: api_key=i['api_key']

    if api_key=='' or api_key==None:
       r=ck.inp({'text':'Enter your cK API key: '})
       if r['return']>0: ck.err(r)

       api_key=r['string'].strip()

    if api_key==None: api_key=''

    cfg['api_key']=api_key

    # Server URL ###########################################################        
    server_url=cfg.get('server_url','')

    if i.get('server_url')!=None and i.get('server_url')!='': server_url=i['server_url']

    if server_url==None or server_url=='': server_url=config.CR_DEFAULT_SERVER_URL

    cfg['server_url']=server_url

    # Server User ###########################################################        
    server_user=cfg.get('server_user','')

    if i.get('server_user')!=None and i.get('server_user')!='': server_user=i['server_user']

    if server_user!=None and server_user!='': cfg['server_user']=server_user

    # Server Pass ###########################################################        
    server_pass=cfg.get('server_pass','')

    if i.get('server_pass')!=None and i.get('server_pass')!='': server_pass=i['server_pass']

    if server_pass!=None and server_pass!='': cfg['server_pass']=server_pass

    # Server Skip Certificate Validation ###########################################################        
    server_skip_validation=cfg.get('server_skip_validation','')

    if i.get('server_skip_validation')!=None and i.get('server_skip_validation')!='': server_skip_validation=i['server_skip_validation']

    if server_skip_validation=='yes': cfg['server_skip_validation']=server_skip_validation

    # Save configuration
    r=ck.access({'action':'update',
                 'repo_uyoa':config.CK_CFG_REPO_UOA,
                 'module_uoa':config.CK_CFG_MODULE_UID,
                 'data_uoa':config.CK_CFG_DATA_UOA,
                 'dict':cfg,
                 'sort_keys':'yes'})
    if r['return']>0: ck.err(r)

    # Print (new/updated) configuration
    ck.out('')
    ck.out('Current cBench configuration:')

    ck.out('')
    ck.out(json.dumps(cfg, indent=2, sort_keys=True))

    return 0

########################################################################################
# Test login to the cK portal

def login(i):

    """
    Input:  {
              (username) [str]
              (api_key) [str]
              (server_url) [str]
              (server_user) [str]
              (server_pass) [str]
              (server_skip_validation) [str]
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """

    # Get current configuration
    cfg={}

    ii={'action':'load',
        'repo_uoa':config.CK_CFG_REPO_UOA,
        'module_uoa':config.CK_CFG_MODULE_UID,
        'data_uoa':config.CK_CFG_DATA_UOA}

    r=ck.access(ii)
    if (r['return']>0 and r['return']!=16): ck.err(r) 

    # If not found, setup client
    if r['return']==16:
       setup(i)

    # Load again
    cfg={}

#    ii={'action':'load',
#        'repo_uoa':config.CK_CFG_REPO_UOA,
#        'module_uoa':config.CK_CFG_MODULE_UID,
#        'data_uoa':config.CK_CFG_DATA_UOA}
#
#    r=ck.access(ii)
#    if r['return']>0: ck.err(r) 

    r=config.load({})
    if r['return']>0: return r
    cfg=r.get('dict',{})

    # Update cfg
    for k in ['username', 'api_key', 'server_url', 'server_user', 'server_pass', 'server_skip_validation']:
        v=i.get(k,'')
        if v==None: v=''
        if v!='': cfg[k]=v 

    # Sending request to test connection
    r=comm.send({'config':cfg,
                 'action':'login'
                })
    if r['return']>0: ck.err(r)

    # Success
    ck.out('cK login tested successfully!')

    return 0
