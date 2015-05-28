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
              return   - return code =  0, if successful
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
              (repo_uoa)                 - repo UOA (where to create entry)
              data_uoa                   - data UOA
              (data_uid)                 - data UID (if uoa is an alias)
              (data_name)                - user friendly data name

              (cids[0])                  - as uoa or full CID

              (path)                     - if !='' - creat in this path
              (here)                     - if =='yes', create in current path
              (use_default_path)         - if 'yes' create repository in the default path (CK_REPOS)
                                           instead of the current path (default is 'yes')

              (use_current_path)         - if 'yes' create repository in the current path
                                           (default is 'no')

              (default)                  - if 'yes', no path is used, 
                                           but the repository is taken either 
                                           from the CK directory or from CK_LOCAL_REPO

              (import)                   - if 'yes', register repo in the current directory in CK
                                           (when received from someone else)

              (remote)                   - if 'yes', remote repository
              (remote_repo_uoa)          - if !='' and type=='remote' repository UOA on the remote CK server

              (shared)                   - if not remote and =='git', repo is shared/synced through GIT
              (share)                    - (for user-friendly CMD) if 'yes', set shared=git

              (allow_writing)            - if 'yes', allow writing 
                                           (useful when kernel is set to allow writing only to such repositories)

              (url)                      - if type=='remote' or 'git', URL of remote repository or git repository
              (githubuser)               - if shared repo, use this GITHUB user space instead of default "ctuning"
              (sync)                     - if 'yes' and type=='git', sync repo after each write operation

              (gitzip)                   - if 'yes', download as zip from GITHUB
              (zip)                      - path to zipfile (local or remote http/ftp)
              (overwrite)                - if 'yes', overwrite files when unarchiving

              (quiet)                    - if 'yes', do not ask questions unless really needed

              (skip_reusing_remote_info) - if 'yes', do not reuse remote .cmr.json description of a repository

              (current_repos)            - if resolving dependencies on other repos, list of repos being updated (to avoid infinite recursion)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Check if global writing is allowed
    r=ck.check_writing({})
    if r['return']>0: return r

    o=i.get('out','')

    a=i.get('repo_uoa','')
    d=i.get('data_uoa','')
    di=i.get('data_uid','')
    dn=i.get('data_name','')

    cr=i.get('current_repos',[])

    quiet=i.get('quiet','')

    zp=i.get('zip','')
    overwrite=i.get('overwrite','')

    gz=i.get('gitzip','')
    ptr=''
    if gz=='yes':
       zp=ck.cfg['default_shared_repo_url']+'/'+d+'/archive/master.zip'
       ptr=d+'-master/'
       quiet='yes'

    remote=i.get('remote','')
    rruoa=i.get('remote_repo_uoa','')
    shared=i.get('shared','')
    if shared=='yes': shared='git'

    share=i.get('share','')
    if share=='yes' and shared=='': shared='git'

    url=i.get('url','')
    sync=i.get('sync','')
    df=i.get('default','')

    eaw=i.get('allow_writing','')

    udp=i.get('use_default_path','yes')
    ucp=i.get('use_current_path','')
    if ucp=='yes': udp=''

    # Get repo path (unless 'here' later)
    px=i.get('path','')

    # Check if import
    imp=i.get('import','')
    if imp=='yes': 
       if px=='': i['here']='yes'

    # Get 'here' path
    if i.get('here','')=='yes': px=os.getcwd()
    p=px

    if imp=='yes': 
       py=os.path.join(p,ck.cfg['repo_file'])
       if os.path.isfile(py):
          r=ck.load_json_file({'json_file':py})
          if r['return']>0: return r
          dc=r['dict']

          d=dc.get('data_uoa','')
          di=dc.get('data_uid','')
          dn=dc.get('data_name','')

    if p=='' and udp=='yes': p=os.path.join(ck.work['dir_repos'], d)

    # Normalize path
    p=os.path.normpath(p)

    # If console mode, first, check if shared (GIT, etc)
    if o=='con':
       # Asking for alias
       if df!='yes' and (d=='' or ck.is_uid(d)):
          r=ck.inp({'text':'Enter an alias for this repository (or Enter to skip it): '})
          d=r['string']
          if d=='': d=di
          if d=='':
             r=ck.gen_uid({})
             if r['return']>0: return r
             di=r['data_uid']
             d=di

       # Asking for a user-friendly name
       if df!='yes' and dn=='':
          if quiet!='yes':
             r=ck.inp({'text':'Enter a user-friendly name of this repository (or Enter to reuse alias): '})
             dn=r['string']
          if dn=='': dn=d

       # Asking if remote
       if df!='yes' and remote=='':
          if quiet!='yes':
             r=ck.inp({'text':'Is this repository a remote CK web service (y/N)? '})
             remote=r['string'].lower()
          if remote=='yes' or remote=='y': remote='yes'
          else: remote=''

       # Asking for a user-friendly name
       if px=='' and df!='yes' and remote!='yes' and udp=='':
          if quiet!='yes':
             r=ck.inp({'text':'Would you like to create repo in the directory from CK_REPOS variable (Y/n): '})
             x=r['string'].lower()
             if x=='' or x=='yes' or x=='y':
                p=os.path.join(ck.work['dir_repos'], d)

       # Asking for remote url
       if df!='yes' and remote=='yes' and url=='':
          if quiet!='yes':
             r=ck.inp({'text':'Enter URL of remote CK repo (example: http://localhost:3344/ck?): '})
             url=r['string'].lower()
          if url=='':
             return {'return':1, 'error':'URL is empty'}

       # Asking for remote repo UOA
       if df!='yes' and remote=='yes' and rruoa=='':
          if quiet!='yes':
             r=ck.inp({'text':'Enter remote repo UOA or Enter to skip: '})
             rruoa=r['string'].lower()

       # Asking for shared
       if remote=='' and shared=='' and share=='':
          if quiet!='yes':
             r=ck.inp({'text':'Is this repository shared via GIT (y/N)? '})
             x=r['string'].lower()
             if x=='yes' or x=='y':
                share='yes'

       if share=='yes' and shared=='': shared='git'

       # Check additional parameters if git
       ghu=i.get('githubuser','')
       if shared=='git' and url=='':

          if ghu!='': 
             durl=ck.cfg.get('github_repo_url','')
             if not durl.endswith('/'): durl+='/'
             durl+=ghu
          else: durl=ck.cfg.get('default_shared_repo_url','')

          if not durl.endswith('/'): durl+='/'
          durl+=d
#          if durl.startswith('http://') or durl.startswith('https://'):
#             durl+='.git'

          if quiet!='yes':
             s='Enter URL of GIT repo '
             if d=='': s+='(for example, https://github.com/ctuning/ck-analytics.git)'
             else:     s+='(or Enter for '+durl+')'
             r=ck.inp({'text': s+': '})
             url=r['string'].lower()
          if url=='': url=durl

       # Check additional parameters if git
       if shared=='git' and sync=='':
          if quiet!='yes':
             r=ck.inp({'text': 'Would you like to sync repo each time after writing to it (y/N)?: '})
             x=r['string'].lower()
             if x=='yes' or x=='y':
                sync='yes'

       # Asking for a user-friendly name
       if df!='yes' and remote!='yes' and eaw=='':
          if quiet!='yes':
             r=ck.inp({'text':'Would you like to explicitly allow writing to this repository in case kernel disables all writing (y/N): '})
             x=r['string'].lower()
             if x=='yes' or x=='y':
                eaw='yes'

    # Check if already registered (if not remote)
    if remote!='yes':
       r=ck.find_repo_by_path({'path':p})
       if r['return']>0 and r['return']!=16: 
          return r

    # Check if repository is already registered with this path
    r=ck.find_repo_by_path({'path':p})
    if r['return']==0:
       return {'return':1, 'error':'repository with a given path is already registered in CK'}
    elif r['return']!=16: 
       return r

    # Prepare local description file
    py=os.path.join(p,ck.cfg['repo_file'])

    # Create dummy if doesn't exist
    if remote!='yes' and not os.path.isdir(p):
       os.makedirs(p)

    # If zip, get (download) and unzip file ...
    if zp!='':

       rz=get_and_unzip_archive({'zip':zp, 'path':p, 'path_to_remove':ptr, 'overwrite':overwrite, 'out':o})
       if rz['return']>0: return rz

    # If git, clone repo
    if remote!='yes' and shared=='git':
       r=pull({'path':p, 'type':shared, 'url':url, 'clone':'yes', 'out':o})
       if r['return']>0: return r

       # Check if there is a local repo description
       if os.path.isfile(py):
          r=ck.load_json_file({'json_file':py})
          if r['return']>0: return r
          dc=r['dict']

          xd=dc.get('data_uoa','')
          xdi=dc.get('data_uid','')
          xdn=dc.get('data_name','')

          if o=='con':
             ck.out('Cloned repository has the following info:')
             ck.out(' UID                = '+xdi)
             ck.out(' UOA                = '+xd)
             ck.out(' User friendly name = '+xdn)
             ck.out('')
             if i.get('skip_reusing_remote_info','')!='yes':
                d=xd
                di=xdi
                dn=xdn

    # Prepare meta description
    dd={}
    if df=='yes': 
       dd['default']='yes'
    if remote=='yes': 
       dd['remote']='yes'
       if rruoa!='': 
          dd['remote_repo_uoa']=rruoa
    if shared!='':
       dd['shared']=shared
       if sync!='': 
          dd['sync']=sync
    if url!='': 
       dd['url']=url
    if remote!='yes': 
       dd['path']=p
    if eaw=='yes':
       dd['allow_writing']='yes'

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

    # Update repo cache if not default local
    dz={'data_uoa':d, 'data_uid':dx, 'data_alias':alias, 'path_to_repo_desc':px, 'data_name':dn, 'dict':dd}

    if df!='yes':
       r=ck.reload_repo_cache({}) # Ignore errors
       ck.cache_repo_uoa[d]=dx
       ck.cache_repo_info[dx]=dz
       r=ck.save_repo_cache({})
       if r['return']>0: return r

    # Record local info of the repo (just in case)
    if remote!='yes':
       if 'path_to_repo_desc' in dz: del (dz['path_to_repo_desc'])        # Avoid recording some local info
       if dz.get('dict',{}).get('path','')!='': del (dz['dict']['path'])  # Avoid recording some local info
       if not os.path.isfile(py):
          ry=ck.save_json_to_file({'json_file':py, 'dict':dz})
          if ry['return']>0: return ry

    # If sync, add it ...
    if sync=='yes':
       ppp=os.getcwd()

       os.chdir(p)
       ss=ck.cfg['repo_types'][shared]['add'].replace('$#path#$', px).replace('$#files#$', ck.cfg['repo_file'])
       os.system(ss)

       os.chdir(ppp)

    # If console mode, print various info
    if o=='con':
       ck.out('')
       ck.out('CK repository successfully registered!')
       ck.out('')

       if df!='yes':
          ck.out('CK repo description path = '+px)
          ck.out('CK repo UID              = '+dx)

    # Check deps
    if o=='con':
       ck.out('  ******************************************************************')
       ck.out('  Checking dependencies on other repos ...')
       ck.out('')

    how='pull'
    if gz=='yes': how='add'
    r=deps({'path':p,
            'current_path':cr,
            'how':how,
            'out':o})
    if r['return']>0: return r

    # Print if default
    if df=='yes' and o=='con':
       ck.out('')
       ck.out('Please, do not forget to add path to this repository to CK_LOCAL_REPO environment variable:')
       ck.out('')
       ck.out('  Linux: export CK_LOCAL_REPO='+p)
       ck.out('  Windows: set CK_LOCAL_REPO='+p)

    return rx

##############################################################################
# Update repository in a given directory and record info in CK

def update(i):
    """
    Update repository info

    Input:  {
              data_uoa                   - data UOA of the repo

              (shared)                   - if not remote and =='git', shared through GIT

              (url)                      - if type=='git', URL of remote repository or git repository
              (sync)                     - if 'yes' and type=='git', sync repo after each write operation
              (allow_writing)            - if 'yes', allow writing 
                                           (useful when kernel is set to allow writing only to such repositories)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Check if global writing is allowed
    r=ck.check_writing({})
    if r['return']>0: return r

    o=i.get('out','')

    duoa=i.get('data_uoa','')

    remote=i.get('remote','')
    rruoa=i.get('remote_repo_uoa','')
    shared=i.get('shared','')
    url=i.get('url','')
    sync=i.get('sync','')

    eaw=i.get('allow_writing','')

    # Get configuration
    r=ck.load_repo_info_from_cache({'repo_uoa':duoa})
    if r['return']>0: return r

    dn=r.get('data_name','')
    d=r['dict']

    remote=d.get('remote','')

    changed=False

    # Check user-friendly name
    if dn!='':
       ck.out('Current user-friendly name of this repository: '+dn)
       ck.out('')

    r=ck.inp({'text':'Enter a user-friendly name of this repository (or Enter to keep old value): '})
    x=r['string']
    if x!='': 
       dn=x
       changed=True

    # If remote, update URL
    shared=d.get('shared','')
    if remote=='yes':
       url=d.get('url','')
       ck.out('Repository is remote ...')
       ck.out('')
       ck.out('Current URL: '+url)
       ck.out('')
       rx=ck.inp({'text':'Enter new URL (or Enter to leave old one): '})
       x=rx['string']
       if x!='': 
          d['url']=x
          changed=True
    elif shared!='':
       url=d.get('url','')
       ck.out('Repository is shared ...')
       ck.out('')
       ck.out('Current URL: '+url)

       if shared=='git':
          sync=d.get('sync','')
          ck.out('')
          if sync!='':
             ck.out('Current sync setting: '+sync)
          r=ck.inp({'text': 'Would you like to sync repo each time after writing to it (y/N)?: '})
          x=r['string'].lower()
          if x=='yes' or x=='y':
             d['sync']='yes'
             changed=True

    # Asking for a user-friendly name
    if remote!='yes' and eaw=='':
       if eaw=='': eaw=d.get('allow_writing','')
       ck.out('')
       if eaw!='':
          ck.out('Current "allow writing" setting: '+eaw)

       r=ck.inp({'text':'Would you like to allow explicit writing to this repository when kernel disables all writing (y/N): '})
       x=r['string'].lower()
       if x=='yes' or x=='y':
          d['allow_writing']='yes'
          changed=True

    # Write if changed
    if changed:
       if o=='con':
          ck.out('')
          ck.out('Updating repo info ...')

       rx=ck.access({'action':'update',
                     'module_uoa':ck.cfg['repo_name'],
                     'data_uoa':duoa,
                     'data_name':dn,
                     'dict':d,
                     'common_func':'yes',
                     'overwrite':'yes'})
       if rx['return']>0: return rx

       # Recaching
       if o=='con':
          ck.out('')

       r=recache({'out':o})
       if r['return']>0: return r

    return {'return':0}

##############################################################################
# Pull from shared repo if URL

def pull(i):
    """
    Input:  {
              (path)  - repo UOA (where to create entry)
              (type)  - type
              (url)   - URL

                or

              (data_uoa)      - repo UOA

              (clone)         - if 'yes', clone repo instead of update

              (current_repos) - if resolving dependencies on other repos, list of repos being updated (to avoid infinite recursion)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    pp=[]
    px=i.get('path','')
    t=i.get('type','')
    url=i.get('url','')

    cr=i.get('current_repos',[])

    tt='pull'
    if i.get('clone','')=='yes': tt='clone'

    if px!='': 
       pp.append({'path':px, 'type':t, 'url':url})

    uoa=i.get('data_uoa','')
    cids=i.get('cids',[])
    if len(cids)>0: uoa=cids[0]

    if uoa=='' and len(pp)==0: uoa='*'

    if uoa!='':
       if uoa.find('*')>=0 or uoa.find('?')>=0:
          r=ck.list_data({'module_uoa':work['self_module_uoa'], 'data_uoa':uoa})
          if r['return']>0: return r

          lst=r['lst']
          for q in lst:
              # Loading repo
              r=ck.access({'action':'load',
                           'module_uoa':work['self_module_uoa'],
                           'data_uoa':q['data_uoa'],
                           'common':'yes'})
              if r['return']>0: return r
              d=r['dict']
              t=d.get('shared','')
              duoa=r['data_uoa']

              if t!='':
                 p=d.get('path','')
                 url=d.get('url','')
                 pp.append({'path':p, 'type':t, 'url':url, 'data_uoa':duoa})
       else:
          # Loading repo
          r=ck.access({'action':'load',
                       'module_uoa':work['self_module_uoa'],
                       'data_uoa':uoa,
                       'common':'yes'})
          if r['return']>0: 
             if r['return']==16:
                # If not found, try to add from GIT

                i['action']='add'
                i['shared']='yes'
                x=i.get('quiet','')
                if x=='': x='yes'
                i['quiet']=x
                i['current_repos']=cr

                return add(i)
             else:
                return r

          d=r['dict']
          duoa=r['data_uoa']

          p=d['path']
          t=d.get('shared','')
          url=d.get('url','')

          pp.append({'path':p, 'type':t, 'url':url, 'data_uoa':duoa})

    # Updating ...
    for q in pp:
        p=q.get('path','')
        duoa=q.get('data_uoa','')
        t=q.get('type','')
        url=q.get('url','')

        if o=='con' and tt!='clone':
           ck.out('******************************************************************')
           ck.out('Trying to update repo "'+duoa+'" ('+p+') ...')

        if t=='git':
           px=os.getcwd()

           if not os.path.isdir(p):
              os.makedirs(p)

           if o=='con':
              ck.out('')
              ck.out('  cd '+p+' ...')
           os.chdir(p)

           s=ck.cfg['repo_types'][t][tt].replace('$#url#$', url).replace('$#path#$', p)

           if o=='con':
              ck.out('  '+s)
              ck.out('')

           r=os.system(s)

           if o=='con': 
              ck.out('')

           os.chdir(px) # Restore path

           if r>0:
              return {'return':1, 'error':'repository update likely failed - exit code '+str(r)}
        else:
           if o=='con':
              ck.out('CK warning: this repository is not shared!')

        # Check deps
        if tt!='clone': # clone is done in add ...
           if o=='con':
              ck.out('  ******************************************************************')
              ck.out('  Checking dependencies on other repos ...')
              ck.out('')

           r=deps({'path':p,
                   'current_path':cr,
                   'how':'pull',
                   'out':o})
           if r['return']>0: return r

    return {'return':0}

##############################################################################
# Push and commit to shared repo if URL

def push(i):
    """
    Input:  {
              (path)  - repo UOA (where to create entry)
              (type)  - type
              (url)   - URL

                or

              (data_uoa)  - repo UOA

              (clone) - if 'yes', clone repo instead of update
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    pp=[]
    px=i.get('path','')
    t=i.get('type','')
    url=i.get('url','')

    if px!='': 
       pp.append({'path':px, 'type':t, 'url':url})

    uoa=i.get('data_uoa','')
    cids=i.get('cids',[])
    if len(cids)>0: uoa=cids[0]

    if uoa=='' and len(pp)==0: uoa='*'

    if uoa!='':
       if uoa.find('*')>=0 or uoa.find('?')>=0:
          r=ck.list_data({'module_uoa':work['self_module_uoa'], 'data_uoa':uoa})
          if r['return']>0: return r

          lst=r['lst']
          for q in lst:
              # Loading repo
              r=ck.access({'action':'load',
                           'module_uoa':work['self_module_uoa'],
                           'data_uoa':q['data_uoa'],
                           'common':'yes'})
              if r['return']>0: return r
              d=r['dict']
              t=d.get('shared','')
              if t!='':
                 p=d.get('path','')
                 url=d.get('url','')
                 pp.append({'path':p, 'type':t, 'url':url})
       else:
          # Loading repo
          r=ck.access({'action':'load',
                       'module_uoa':work['self_module_uoa'],
                       'data_uoa':uoa,
                       'common':'yes'})
          if r['return']>0: return r
          d=r['dict']

          p=d['path']
          t=d.get('shared','')
          url=d.get('url','')

          pp.append({'path':p, 'type':t, 'url':url})

    # Pushing ...
    for q in pp:
        p=q.get('path','')
        t=q.get('type','')
        url=q.get('url','')

        if o=='con':
           ck.out('')
           ck.out('Trying to update '+p+' ...')

        if t=='git':
           px=os.getcwd()

           if not os.path.isdir(p):
              return {'return':1, 'error':'local path to repository is not found'}

           if o=='con':
              ck.out('')
              ck.out('cd '+p+' ...')

           os.chdir(p)

           s=ck.cfg['repo_types'][t]['commit'].replace('$#url#$', url).replace('$#path#$', p)
           if o=='con':
              ck.out('')
              ck.out('Executing command: '+s)
              ck.out('')
           r=os.system(s)

           if o=='con': 
              ck.out('')

           s=ck.cfg['repo_types'][t]['push'].replace('$#url#$', url).replace('$#path#$', p)
           if o=='con':
              ck.out('')
              ck.out('Executing command: '+s)
              ck.out('')
           r=os.system(s)

           if o=='con': 
              ck.out('')

           os.chdir(px) # Restore path

           if r>0:
              return {'return':1, 'error':'repository update likely failed - exit code '+str(r)}
        else:
           if o=='con':
              ck.out('CK warning: this repository is not shared!')

    return {'return':0}

##############################################################################
# Create repository in a given directory and record info in CK

def create(i):
    """
    See function 'add'

    """

    return add(i)

##############################################################################
# Recache all repositories in cache

def recache(i):
    """
    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """

    o=i.get('out','')

    # Listing all repos
    r=ck.access({'action':'list',
                 'module_uoa':ck.cfg['repo_name']})
    if r['return']>0: return r
    l=r['lst']

    cru={}
    cri={}

    # Processing repos
    for q in l:
        ruoa=q['repo_uoa']
        muoa=q['module_uoa']
        duoa=q['data_uoa']
        duid=q['data_uid']

        if duid==ck.cfg['repo_uid_default'] or duid==ck.cfg['repo_uid_local']:
           if o=='con':
              ck.out('Skipping repo '+duoa+' ...')
        else:
           if o=='con':
              ck.out('Processing repo '+duoa+' ...')

           # Load repo (do not use repo, since may not exist in cache)
           rx=ck.access({'action':'load',
                         'module_uoa':muoa,
                         'data_uoa':duoa})
           if rx['return']>0: return rx
           dt=rx['dict']
           dname=rx['data_name']
           dalias=rx['data_alias']
           dp=rx['path']

           if duoa!=duid:
              cru[duoa]=duid

           dd={'dict':dt}

           dd['data_uid']=duid
           dd['data_uoa']=duoa
           dd['data_alias']=dalias
           dd['data_name']=dname
           dd['path_to_repo_desc']=dp

           cri[duid]=dd

    # Recording 
    ck.cache_repo_uoa=cru
    ck.cache_repo_info=cri

    if o=='con':
       ck.out('')
       ck.out('Recording repo cache ...')

    rx=ck.save_repo_cache({})
    if rx['return']>0: return rx

    if o=='con':
       ck.out('')
       ck.out('Repositories was successfully recached!')

    return {'return':0}

##############################################################################
# Remove information about repository

def rm(i):
    """
    Input:  {
              (repo_uoa)            - repo UOA (where to delete entry about repository)
              uoa                   - data UOA
              (force)               - if 'yes', force removal
              (with_files) or (all) - if 'yes', remove files as well
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """

    # Check if global writing is allowed
    r=ck.check_writing({})
    if r['return']>0: return r

    global cache_repo_uoa, cache_repo_info

    ruoa=i.get('repo_uoa','')
    uoa=i.get('data_uoa','')

    o=i.get('out','')

    if uoa=='': 
       return {'return':1, 'error':'UOA of the repository is not defined'}

    wf=i.get('with_files','')
    if wf=='': wf=i.get('all','')

    force=i.get('force','')

    r=ck.access({'action':'load',
                 'repo_uoa':ruoa,
                 'module_uoa':work['self_module_uoa'],
                 'data_uoa':uoa,
                 'common_func':'yes'})
    if r['return']>0: return r
    duid=r['data_uid']
    duoa=r['data_uoa']

    d=r['dict']
    p=d.get('path','')

    to_delete=True
    if o=='con' and force!='yes':
       r=ck.inp({'text':'Are you sure to delete information about repository '+duoa+' (y/N): '})
       c=r['string'].lower()
       if c!='yes' and c!='y': to_delete=False

    if to_delete and o=='con' and force!='yes' and wf=='yes':
       r=ck.inp({'text':'You indicated that you want to DELETE ALL ENTRIES IN THE REPOSITORY! Are you sure (y/N): '})
       x=r['string'].lower()
       if x!='yes' and x!='y': wf=''

    if to_delete:
       if o=='con': 
          ck.out('')
          ck.out('Reloading repo cache ...')
       r=ck.reload_repo_cache({}) # Ignore errors
       if r['return']>0: return r

       if o=='con': ck.out('Removing from cache ...')
       if duoa in ck.cache_repo_uoa: del (ck.cache_repo_uoa[duoa])
       if duid in ck.cache_repo_info: del (ck.cache_repo_info[duid])

       if o=='con': ck.out('Rewriting repo cache ...')
       r=ck.save_repo_cache({})
       if r['return']>0: return r

       if o=='con': ck.out('Removing entry ...')
       r=ck.access({'action':'remove',
                    'repo_uoa':ruoa,
                    'module_uoa':work['self_module_uoa'],
                    'data_uoa':uoa,
                    'common_func':'yes'})
       if r['return']>0: return r

       if wf=='yes' and p!='':
          if o=='con': ck.out('Removing entries from the repository ...')
          import shutil
          shutil.rmtree(p)

       if o=='con': 
          ck.out('')
          ck.out('Information about repository was removed successfully!')
          if wf!='yes':
             ck.out('Note: repository itself was not removed!')

    return {'return':0}

##############################################################################
# Remove information about repository

def remove(i):
    """
    Input:  { See 'rm' function }
    Output: { See 'rm' function }
    """

    return rm(i)

##############################################################################
# Remove information about repository

def delete(i):
    """
    Input:  { See 'rm' function }
    Output: { See 'rm' function }
    """

    return rm(i)

##############################################################################
# find path to a local repository

def where(i):
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

    duoa=i.get('data_uoa','')
    r=ck.find_path_to_repo({'repo_uoa':duoa})
    if r['return']>0: return r

    p=r['path']

    if o=='con':
       ck.out(p)

    return r

##############################################################################
# archive repository

def zip(i):
    """
    Input:  {
              data_uoa       - repo UOA
              (archive_name) - if '' use <data_uoa>.zip as archive_name
              (archive_path) - if '' create inside repo path
              (auto_name)    - if 'yes', generate name from data_uoa: ckr-<data_uoa>.zip
              (overwrite)    - if 'yes', overwrite zip file
              (store)        - if 'yes', store files instead of packing

              (data)         - CID allowing to add only these entries with pattern (can be from another archive)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    duoa1=i.get('data_uoa','')

    # Find path to repo
    r=ck.find_path_to_repo({'repo_uoa':duoa1})
    if r['return']>0: return r

    duoa=r['repo_uoa']
    path=r['path']

    an=i.get('archive_name','')
#    if an=='': an='ckr.zip'
    if an=='': 
       if duoa1=='': an='ckr.zip'
       else: an='ckr-'+duoa1+'.zip'

    if i.get('auto_name','')=='yes':
       an='ckr-'+duoa+'.zip'

    ap=i.get('archive_path','')
#    if ap=='': ap=path

    pfn=os.path.join(ap, an)

    if os.path.isfile(pfn):
       if i.get('overwrite','')=='yes':
          os.remove(pfn)
       else:
          return {'return':1, 'error':'archive '+pfn+' already exists'}

    if o=='con':
       ck.out('Creating archive '+pfn+' - please wait, it may take some time ...')

    # Prepare archive
    import zipfile

    zip_method=zipfile.ZIP_DEFLATED
    if i.get('store','')=='yes':
       zip_method=zipfile.ZIP_STORED

    # Prepare list of files
    fl={}

    data=i.get('data','')
    if data!='':
       xpm={}

       rx=ck.access({'action':'search',
                     'cid':data})
       if rx['return']>0: return rx
       lst=rx['lst']
       for q in lst:
           pp=q['path']

           pm1,pd=os.path.split(pp)
           pr,pm=os.path.split(pm1)

           if pr not in fl:
              fl[pr]=[]

           ry=ck.find_path_to_entry({'path':pr, 'data_uoa':pm})
           if ry['return']>0: return ry
           pm_uid=ry['data_uid']
           pm_alias=ry['data_alias']

           if pm_alias!='':
              if pm_alias not in xpm:
                 xpm[pm_alias]=pm_uid
                 fl[pr].append(os.path.join(ck.cfg['subdir_ck_ext'], ck.cfg['file_alias_a'] + pm_alias))
                 fl[pr].append(os.path.join(ck.cfg['subdir_ck_ext'], ck.cfg['file_alias_u'] + pm_uid))

           ry=ck.find_path_to_entry({'path':pm1, 'data_uoa':pd})
           if ry['return']>0: return ry
           pd_uid=ry['data_uid']
           pd_alias=ry['data_alias']

           if pd_alias!='':
              fl[pr].append(os.path.join(pm, ck.cfg['subdir_ck_ext'], ck.cfg['file_alias_a'] + pd_alias))
              fl[pr].append(os.path.join(pm, ck.cfg['subdir_ck_ext'], ck.cfg['file_alias_u'] + pd_uid))

           r=ck.list_all_files({'path':pp, 'all':'yes', 'ignore_names':ck.cfg.get('ignore_directories_when_archive_repo',[])})
           if r['return']>0: return r
           for q in r['list']:
               fx=os.path.join(pm,pd,q)
               fl[pr].append(fx)

    else:
       r=ck.list_all_files({'path':path, 'all':'yes', 'ignore_names':ck.cfg.get('ignore_directories_when_archive_repo',[])})
       if r['return']>0: return r
       fl[path]=r['list']

    # Write archive
    try:
       f=open(pfn, 'wb')
       z=zipfile.ZipFile(f, 'w', zip_method)
       for path in fl:
           fl1=fl[path]
           for fn in fl1:
               p1=os.path.join(path, fn)
               z.write(p1, fn, zip_method)
       z.close()
       f.close()

    except Exception as e:
       return {'return':1, 'error':'failed to prepare archive ('+format(e)+')'}

    return {'return':0}

##############################################################################
# unzip entries to a given repo

def unzip(i):
    """
    Input:  {
              (data_uoa)    - repo UOA where to unzip (default, if not specified)
              zip           - path to zipfile (local or remote http/ftp)
              (overwrite)   - if 'yes', overwrite files when unarchiving
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    duoa=i.get('data_uoa','')
    if duoa=='': duoa='local'

    overwrite=i.get('overwrite','')

    zip=i.get('zip','')
    if zip=='': zip='ckr.zip'

    # Find path to repo
    r=ck.find_path_to_repo({'repo_uoa':duoa})
    if r['return']>0: return r

    path=r['path']

    # Unzipping archive
    rz=get_and_unzip_archive({'zip':zip, 'path':path, 'overwrite':overwrite, 'out':o})
    if rz['return']>0: return rz

    return {'return':0}

##############################################################################
# received from web (if needed) and unzip archive

def get_and_unzip_archive(i):
    """
    Input:  {
              zip              - zip filename or URL
              path             - path to extract
              (overwrite)      - if 'yes', overwrite files when unarchiving
              (path_to_remove) - if !='', remove this part of the path from extracted archive
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    zp=i['zip']
    p=i['path']
    pr=i.get('path_to_remove','')

    overwrite=i.get('overwrite','')

    # If zip, get (download) and unzip file ...
    rm_zip=False
    if zp.find('://')>=0:
       if o=='con':
          ck.out('Downloading CK archive ('+zp+') - it may take some time ...')

       rm_zip=True

       # Generate tmp file
       import tempfile
       fd, fn=tempfile.mkstemp(suffix='.tmp', prefix='ck-') # suffix is important - CK will delete such file!
       os.close(fd)
       os.remove(fn)

       # Import modules compatible with Python 2.x and 3.x
       import urllib

       try:
          import urllib.request as urllib2
       except:
          import urllib2

       # Prepare request
       request = urllib2.Request(zp)

       # Connect
       try:
          f=urllib2.urlopen(request)
       except Exception as e:
          return {'return':1, 'error':'Failed downloading CK archive ('+format(e)+')'}

       import time
       t = time.time()
       t0 = t

       chunk=32767
       size=0

       try:
          fo=open(fn, 'wb')
       except Exception as e:
          return {'return':1, 'error':'problem opening file='+fn+' ('+format(e)+')'}

       # Read from Internet
       try:
          while True:
             s=f.read(chunk)
             if not s: break
             fo.write(s)

             size+=len(s)

             if o=='con' and (time.time()-t)>3:
                speed='%.1d' % (size/(1000*(time.time()-t0)))
                ck.out('  Downloaded '+str(int(size/1000))+' KB ('+speed+' KB/sec.) ...')
                t=time.time()

          f.close()
       except Exception as e:
          return {'return':1, 'error':'Failed downlading CK archive ('+format(e)+')'}

       fo.close()

       zp=fn

    # Unzip if zip
    if zp!='':
       if o=='con':
          ck.out('  Extracting to '+p+' ...')

       import zipfile
       f=open(zp,'rb')
       z=zipfile.ZipFile(f)
       for dx in z.namelist():
           dx1=dx
           if pr!='' and dx.startswith(pr): 
              dx1=dx1[len(pr):]

           if dx1!='':
              pp=os.path.join(p,dx1)
              if dx.endswith('/'): 
                 # create directory 
                 if not os.path.exists(pp): os.makedirs(pp)
              else:
                 # extract file
                 ppd=os.path.dirname(pp)
                 if not os.path.exists(ppd): os.makedirs(ppd)

                 if os.path.isfile(pp) and overwrite!='yes':
                    if o=='con':
                       ck.out('File '+dx+' already exists in the entry - skipping ...')
                 else:
                    fo=open(pp, 'wb')
                    fo.write(z.read(dx))
                    fo.close()
       f.close()

       if rm_zip:
          os.remove(zp)

    return {'return':0}

##############################################################################
# import repo from current path

def import_repo(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['import']='yes'
    return add(i)

##############################################################################
# resolve dependencies for a repo

def deps(i):
    """
    Input:  {
              (data_uoa)      - repo UOA
                  or
              (path)          - path to .cmr.json

              (current_repos) - list of repos being updated (to avoid infinite recursion)

              (how)           - 'pull' (default) or 'add'
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    o=i.get('out','')

    duoa=i.get('data_uoa','')

    cr=i.get('current_repos',[])

    how=i.get('how','')
    if how=='': how='pull'

    p=i.get('path','')
    if p=='':
       r=ck.access({'action':'load',
                    'module_uoa':work['self_module_uoa'],
                    'data_uoa':duoa})
       if r['return']>0: return r
       dr=r['dict']
       p=dr.get('path','')

    if p!='':
       # path to repo description
       pp=os.path.join(p, ck.cfg['repo_file'])
       if not os.path.isfile(pp):
          return {'return':1, 'error':'repository description ('+pp+') is not found'}

       r=ck.load_json_file({'json_file':pp})
       if r['return']>0: return r

       d=r['dict']

       rp1=d.get('repo_deps',[])
       rp2=[]
       rp=[]

       if len(rp1)>0:
          for ruoa in rp1:
              if ruoa not in cr:
                 rp2.append(ruoa)

       if len(rp2)==0:
          if o=='con':
             ck.out('  No dependencies on other repositories found!')
       else:
          for ruoa in rp2:
              x='  Dependency on repository '+ruoa+' '

              # Check if this repo exists
              r=ck.access({'action':'load',
                           'module_uoa':work['self_module_uoa'],
                           'data_uoa':ruoa})
              if r['return']>0: 
                 if r['return']!=16: return r
                 rp.append(ruoa)
                 x+=': should be resolved ...'
              else:
                 x+=': Ok'

              if o=='con':
                 ck.out(x)
          
       if len(rp)>0:
          for ruoa in rp:
              if o=='con':
                 ck.out('')
                 ck.out('  Resolving dependency on repo:'+ruoa)
                 ck.out('')

              cr.append(ruoa)

              ii={'action':how,
                  'module_uoa':work['self_module_uoa'],
                  'data_uoa':ruoa,
                  'current_repos':cr,
                  'out':o}
              if how=='add': ii['gitzip']='yes'
              r=ck.access(ii)
              if r['return']>0: return r

    return {'return':0, 'current_repos':cr}
