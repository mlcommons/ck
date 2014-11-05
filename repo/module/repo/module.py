#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details
# See CK Copyright.txt for copyright details
#
# Developer: Grigori Fursin
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

# Local settings

import os

##############################################################################
# Initialize module

def init(i):
    """
    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)  - error text if return > 0
            }

    """
    return {'return':0}

##############################################################################
# Create repository in a given directory and record info in CK

def add(i):
    """
    Note, that we can't create repos in parallel (recording to repo cache may fail).
    However, for now, we do not expect such cases (i.e. repos are created rarely)

    Input:  {
              (repo_uoa)  - repo UOA (where to create entry)
              uoa         - data UOA
              (uid)       - data UID (if uoa is an alias)
              (name)      - user friendly data name

              (cids[0])   - as uoa or full CID

              (path)      - if =='' - get current path
              (default)   - if 'yes', no path is used, 
                            but the repository is taken either 
                            from the CK directory or from CK_LOCAL_REPO

              type        - type == ''    - normal (local)
                                    'git' - synchronized with GIT repository

              (url)       - if type=='git', URL of the git repository
              (sync)      - if type=='git' and =='yes', sync repo after each write operation
            }

    output: {
              return - 0, if successful
              error  - error text if return > 0
            }

    """

    o=i.get('out','')

    a=i.get('repo_uoa','')
    d=i.get('data_uoa','')
    di=i.get('data_uid','')
    dn=i.get('data_name','')

    t=i.get('type','')
    url=i.get('url','')
    sync=i.get('sync','')

    df=i.get('default','')

    # Get path
    p=i.get('path','')
    if p=='': p=os.getcwd()

    # Normalize path
    p=os.path.normpath(p)

    if not os.path.isdir(p):
       return {'return':1, 'error':'path '+p+' doesn\'t exist'}

    # Check if repository is already registered with this path
    r=ck.find_repo_by_path({'path':p})
    if r['return']==0:
       return {'return':1, 'error':'repository with a given path is already registered in CK'}
    elif r['return']!=16: 
       return r

    py=os.path.join(p,ck.cfg['repo_file']) # Local description file

    # Check if already registered
    r=ck.find_repo_by_path({'path':p})
    if r['return']>0 and r['return']!=16: return r

    # If console mode, first, check if shared (GIT, etc)
    if o=='con':
       # Asking for type
       if t=='':
          r=ck.inp({'text':'What is the type of this repository (Enter for local or "git" for shared through GIT): '})
          t=r['string'].lower()

       # Check additional parameters if git
       if t=='git' and url=='':
          r=ck.inp({'text': 'Enter URL of GIT repo (for example, https://github.com/gfursin/cm-ctuning-shared.git): '})
          url=r['string'].lower()

       # Check additional parameters if git
       if t=='git' and sync=='':
          r=ck.inp({'text': 'Would you like to sync repo each time after writing to it ("yes" or "no"/Enter)?:      '})
          sync=r['string'].lower()

    # If git, clone repo
    if t=='git':
       r=pull({'path':p, 'type':t, 'url':url, 'clone':'yes', 'out':o})
       if r['return']>0: return r
       if o=='con': ck.out('')

       # Check if there is a local repo description
       if os.path.isfile(py):
          r=ck.load_json_file({'json_file':py})
          if r['return']>0: return r
          dc=r['dict']

          d=dc.get('data_uoa','')
          di=dc.get('data_uid','')
          dn=dc.get('data_name','')

    # If console mode, ask different questions
    if o=='con':
       # Asking if it is a default repository
       if df=='':
          r=ck.inp({'text':'Should it be a default repository accessible via CK_LOCAL_REPO environment variable ("yes" or "no"/Enter) ?: '})
          df=r['string'].lower()

       # Asking for alias
       if df!='yes' and (d=='' or ck.is_uid(d)):
          r=ck.inp({'text':'Enter an alias for this repository: '})
          d=r['string']

       # Asking for a user-friendly name
       if df!='yes' and dn=='':
          r=ck.inp({'text':'Enter a user-friendly name of this repository: '})
          dn=r['string']

    # Prepare meta description
    dd={'type':t}

    if url!='': dd['url']=url
    if sync!='': dd['sync']=sync

    if df=='yes': dd['default']=df

    dd['path']=p

    # If not default, go to common core function to create entry
    if df!='yes':
       ii={'module_uoa':work['self_module_uoa'],
           'action':'add',
           'data_uoa':d,
           'dict':dd,
           'common_func':'yes'}
       if a!='': ii['repo_uoa']=a
       if di!='': ii['data_uid']=di
       if dn!='': ii['data_name']=dn
       rx=ck.access(ii)
       if rx['return']>0: return rx
    else:
       # Load default repo and prepare return
       ii={'module_uoa':work['self_module_uoa'],
           'action':'load',
           'data_uoa':'default',
           'common_func':'yes'}
       rx=ck.access(ii)
    px=rx['path']
    dx=rx['data_uid']
    alias=rx['data_alias']

    # Record local repo json (useful if reference is lost)
    dz={'data_uoa':d, 'data_uid':dx, 'data_alias':alias, 'path_to_repo_desc':px, 'data_name':dn, 'dict':dd}
    if not os.path.isfile(py):
       ry=ck.save_json_to_file({'json_file':py, 'dict':dz})
       if ry['return']>0: return ry

    # If sync, add it ...




    # Update repo cache if not defalut local
    if df!='yes':
       r=ck.reload_repo_cache({}) # Ignore errors
       ck.cache_repo_uoa[d]=dx
       ck.cache_repo_info[dx]=dz
       r=ck.save_repo_cache({})
       if r['return']>0: return r

    # If console mode, print various info
    if o=='con':
       ck.out('')
       ck.out('CK repository successfully registered!')
       ck.out('')

       if df=='yes':
          ck.out('Please, do not forget to add path to this repository to CK_LOCAL_REPO environment variable:')
          ck.out('')
          ck.out('  Linux: export CK_LOCAL_REPO='+p)
          ck.out('  Windows: set CK_LOCAL_REPO='+p)
       else:
          ck.out('CK repo description path = '+px)
          ck.out('CK repo UID              = '+dx)

    return rx

##############################################################################
def pull(i):
    """
    Pull from remote repo if URL

    Input:  {
              (path)  - repo UOA (where to create entry)
              (type)  - type
              (url)   - URL

                or

              (uoa)   - repo UOA

              (clone) - if 'yes', clone repo instead of update
            }

    output: {
              return - 0, if successful
              error  - error text if return > 0
            }

    """

    o=i.get('out','')

    p=i.get('path','')
    t=i.get('type','')
    url=i.get('url','')

    uoa=i.get('data_uoa','')
    cids=i.get('cids',[])
    if len(cids)>0: uoa=cids[0]

    if uoa!='':
       # Loading repo
       r=ck.access({'action':'load',
                    'module_uoa':work['self_module_uoa'],
                    'data_uoa':uoa,
                    'common':'yes'})
       if r['return']>0: return r
       d=r['dict']

       p=d['path']
       t=d['type']
       url=d.get('url','')

    # Updating ...
    if t=='git':
       tt='update'
       if i.get('clone','')=='yes': tt='clone'

       px=os.getcwd()
       os.chdir(p)

       s=ck.cfg['repo_types'][t][tt].replace('$#url#$', url).replace('$#path#$', p)
       
       if o=='con':
          ck.out('')
          ck.out('Executing command: '+s)

       r=os.system(s)

       os.chdir(px) # Restore path

       if r>0:
          return {'return':1, 'error':'repository update likely failed - exit code '+str(r)}
    else:
       if o=='con':
          ck.out('CK warning: this repository is not shared!')

    return {'return':0}

##############################################################################
def create(i):
    """
    Create repository in a given directory and record info in CK
    See function 'add'

    """

    return add(i)

##############################################################################
def reindex(i):
    """
    Reindex all repositories in cache

    """




    return {'return':0}
