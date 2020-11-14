#
# Collective Knowledge (artifact description (reproducibility, ACM meta, etc))
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
def recursive_repos(i):

    import os

    repo=i['repo']
    repo_deps=i.get('repo_deps',[])
    level=i.get('level','')
    ilevel=i.get('ilevel',0)

    if ilevel>8:
       # Somewhere got into loop - quit
#       ck.out('Warning: you have a cyclic dependency in your repositories ...')
       return {'return':0, 'repo_deps':repo_deps}

    # Load repo
    r=ck.access({'action':'load',
                 'module_uoa':cfg['module_deps']['repo'],
                 'data_uoa':repo})
    if r['return']>0: return r

    d=r['dict']

    # Note that sometimes we update .ckr.json while CK keeps old deps cached
    p=d.get('path','')
    p1=os.path.join(p, ck.cfg['repo_file'])
    if os.path.isfile(p1):
       r=ck.load_json_file({'json_file':p1})
       if r['return']==0:
          d=r['dict'].get('dict',{})
    
    rd=d.get('repo_deps',{})

#    print (level+repo)

    for q in rd:
        drepo=q['repo_uoa']

        if drepo!=repo:
           repo_deps.append(drepo)

           r=recursive_repos({'repo':drepo, 'repo_deps':repo_deps, 'level':level+'   ', 'ilevel':ilevel+1})
           if r['return']>0: return r

    return {'return':0, 'repo_deps':repo_deps}


##############################################################################
# prepare artifact snapshot

def snapshot(i):
    """
    Input:  {
              repo         - which repo to snapshot with all deps
              (file_name)  - customize name ("ck-artifacts-" by default)
              (no_deps)    - if 'yes', do not process repo dependencies (useful for results repo accompanying main repos)
              (copy_repos) - if 'yes', copy repositories instead of zipping
              (date)       - use this date (YYYYMMDD) instead of current one
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import platform
    import zipfile
    import shutil

    o=i.get('out','')

    repo=i.get('repo','')
    if repo=='':
       return {'return':1, 'error': '"repo" to snapshot is not defined'}

    no_deps=i.get('no_deps','')=='yes'

    copy_repos=i.get('copy_repos','')=='yes'
    force_clean=i.get('force_clean','')=='yes'

    # Preparing tmp directory where to zip repos and add scripts ...
    curdir0=os.getcwd()

#    ptmp=os.path.join(curdir0, 'tmp')
    import tempfile
    ptmp=os.path.join(tempfile.gettempdir(),'tmp-snapshot')
    if o=='con':
       ck.out('Temp directory: '+ptmp)
       ck.out('')

    if os.path.isdir(ptmp) and force_clean:
       shutil.rmtree(ptmp, onerror=ck.rm_read_only)

    if os.path.isdir(ptmp):
       r=ck.inp({'text':'Directory "'+ptmp+'" exists. Delete (Y/n)?'})
       if r['return']>0: return r

       ck.out('')

       x=r['string'].strip().lower()
       if x=='' or x=='y' or x=='yes': 
          r=ck.delete_directory({'path':ptmp})
          if r['return']>0: return r

    if not os.path.isdir(ptmp):
       os.makedirs(ptmp)

    os.chdir(ptmp)

    curdir=os.getcwd()

    # Checking repo deps
    final_repo_deps=[]
    if not no_deps:
       if o=='con':
          ck.out('Checking dependencies on other repos ...')

       r=recursive_repos({'repo':repo})
       if r['return']>0: return r

       # Removing redundant
       for q in reversed(r['repo_deps']):
           if q not in final_repo_deps:
              final_repo_deps.append(q)

    if repo not in final_repo_deps:
       final_repo_deps.append(repo)

    if o=='con':
       ck.out('')
       for q in final_repo_deps:
           ck.out(' * '+q)

       ck.out('')
       ck.out('Collecting revisions, can take some time ...')
       ck.out('')

    r=ck.reload_repo_cache({}) # Ignore errors

    pp=[]
    pp2={}
    il=0

    path_to_main_repo=''

    for xrepo in final_repo_deps:
        # Reload repo to get UID
        r=ck.access({'action':'load',
                     'module_uoa':cfg['module_deps']['repo'],
                     'data_uoa':xrepo})
        if r['return']>0: return r

        ruid=r['data_uid']

        if ruid not in ck.cache_repo_info:
           return {'return':1, 'error':'"'+q+'" repo is not in cache - strange!'}

        # Get repo info
        qq=ck.cache_repo_info[ruid]

        d=qq['dict']
        p=d.get('path','')

        if xrepo==repo:
           path_to_main_repo=p

        t=d.get('shared','')

        duoa=qq['data_uoa']

        if t!='':
           if len(duoa)>il: il=len(duoa)

           url=d.get('url','')

           branch=''
           checkout=''

           if os.path.isdir(p):
              # Detect status
              pc=os.getcwd()

              os.chdir(p)

              # Get current branch
              r=ck.run_and_get_stdout({'cmd':['git','rev-parse','--abbrev-ref','HEAD']})
              if r['return']==0 and r['return_code']==0: 
                 branch=r['stdout'].strip()

              # Get current checkout
              r=ck.run_and_get_stdout({'cmd':['git','rev-parse','--short','HEAD']})
              if r['return']==0 and r['return_code']==0: 
                 checkout=r['stdout'].strip()

              os.chdir(pc)

           x={'branch':branch, 'checkout':checkout, 'path':p, 'type':t, 'url':url, 'data_uoa':duoa}
        else:
           x={'path':p, 'type':t, 'data_uoa':duoa}

        pp.append(x)
        pp2[duoa]=x


        if copy_repos:
           pu=os.path.join(ptmp,'CK')
           if not os.path.isdir(pu):
              os.mkdir(pu)
           pu1=os.path.join(pu,xrepo)

           if o=='con':
              ck.out(' * Copying repo '+xrepo+' ...')

           shutil.copytree(p,pu1,ignore=shutil.ignore_patterns('*.pyc', 'tmp', 'tmp*', '__pycache__'))

    # Copying Readme if exists
    fr='README.md'
    pr1=os.path.join(path_to_main_repo, fr)
    if os.path.isfile(pr1):
       pr2=os.path.join(ptmp, fr)
       if os.path.isfile(pr2):
          os.remove(pr2)

       shutil.copy(pr1,pr2)

    # Print
    if o=='con':
       ck.out('')

    for q in pp:
        name=q['data_uoa']

        x=' * '+name+' '*(il-len(name))

        branch=q.get('branch','')
        checkout=q.get('checkout','')
        url=q.get('url','')

        if branch!='' or checkout!='' or url!='':
           x+=' ( '+branch+' ; '+checkout+' ; '+url+' )'

        ck.out(x)

    os.chdir(curdir)

    # Archiving
    if o=='con':
       ck.out('')
       ck.out('Archiving ...')

    # Add some dirs and files to ignore
    for q in ['__pycache__', 'tmp', 'module.pyc', 'customize.pyc']:
        if q not in ck.cfg['ignore_directories_when_archive_repo']:
           ck.cfg['ignore_directories_when_archive_repo'].append(q)

    # Get current date in YYYYMMDD
    date=i.get('date','')

    if date=='':
       r=ck.get_current_date_time({})
       if r['return']>0: return r

       a=r['array']

       a1=str(a['date_year'])

       a2=str(a['date_month'])
       a2='0'*(2-len(a2))+a2

       a3=str(a['date_day'])
       a3='0'*(2-len(a3))+a3

       date=a1+a2+a3

    date=date.strip()

    if not copy_repos:
       zips=[]
       for repo in final_repo_deps:
           if o=='con':
              ck.out('')
              ck.out(' * '+repo)
              ck.out('')

           an='ckr-'+repo

           if pp2[repo].get('branch','')!='':
              an+='--'+pp2[repo]['branch']

           if pp2[repo].get('checkout','')!='':
              an+='--'+pp2[repo]['checkout']

           an+='.zip'

           zips.append(an)

           r=ck.access({'action':'zip',
                        'module_uoa':cfg['module_deps']['repo'],
                        'data_uoa':repo,
                        'archive_name':an,
                        'overwrite':'yes',
                        'out':o})
           if r['return']>0: return r

       # Print sequence of adding CK repos (for self-sustainable virtual CK artifact)
       if o=='con':
          ck.out('')

          for z in zips:
              ck.out('ck add repo --zip='+z)

    # Cloning CK master
    if o=='con':
       ck.out('')
       ck.out('Cloning latest CK version ...')
       ck.out('')

    os.system('git clone https://github.com/ctuning/ck ck-master')

    # Prepare scripts
    if o=='con':
       ck.out('')
       ck.out('Preparing scripts ...')

    for tp in ['win','linux']:

        f1=cfg['bat_prepare_virtual_ck']
        f2=cfg['bat_start_virtual_ck']

        if tp=='win':
           f1+='.bat'
           f2+='.bat'
           f3='\\'
           f4='%~dp0'+f3

           s='set PATH='+f4+'ck-master\\bin;%PATH%\n'
           s+='set PYTHONPATH='+f4+'ck-master;%PYTHONPATH%\n'
           s+='\n'
           s+='set CK_REPOS='+f4+'CK\n'
           s+='set CK_TOOLS='+f4+'CK-TOOLS\n'
           s+='\n'

           s1=s+'mkdir %CK_REPOS%\n'
           s1+='mkdir %CK_TOOLS%\n'
           s1+='\n'

           s2=s+'rem uncomment next line to install tools to CK env entries rather than CK_TOOLS directory\n'
           s2+='rem ck set kernel var.install_to_env=yes\n'
           s2+='\n'

           s2+='call ck ls repo\n\n'
           s2+='cmd\n'

           s3='call '

        else:
           f1+='.sh'
           f2+='.sh'
           f3='/'
           f4='$PWD'+f3

           s='#! /bin/bash\n'
           s+='\n'
           s+='export PATH='+f4+'ck-master/bin:$PATH\n'
           s+='export PYTHONPATH='+f4+'ck-master:$PYTHONPATH\n'
           s+='\n'
           s+='export CK_REPOS='+f4+'CK\n'
           s+='export CK_TOOLS='+f4+'CK-TOOLS\n'
           s+='\n'

           s1=s+'mkdir ${CK_REPOS}\n'
           s1+='mkdir ${CK_TOOLS}\n'
           s1+='\n'

           s2=s+'# uncomment next line to install tools to CK env entries rather than CK_TOOLS directory\n'
           s2+='# ck set kernel var.install_to_env=yes\n'
           s2+='\n'

           s2+='ck ls repo\n\n'
           s2+='bash\n'

           s3=''

        # importing repos
        if copy_repos:
           for repo in final_repo_deps:
               s1+=s3+'ck import repo --quiet --path='+f4+'CK'+f3+repo+'\n'

        else:
           for z in zips:
               s1+=s3+'ck add repo --zip='+z+'\n'

        # Recording scripts
        r=ck.save_text_file({'text_file':f1, 'string':s1})
        if r['return']>0: return r
        r=ck.save_text_file({'text_file':f2, 'string':s2})
        if r['return']>0: return r

        # If non-Windows, set 755
        if tp!='win':
           os.system('chmod 755 '+f1)
           os.system('chmod 755 '+f2)

    # Generating final zip pack
    fn=i.get('file_name','')
    if fn=='': fn='ck-artifacts-'
    fname=fn+date+'.zip'

    # Write archive
    os.chdir(ptmp)

    if o=='con':
       ck.out('')
       ck.out('Recording '+fname+' ...')

    r=ck.list_all_files({'path':'.', 'all':'yes'})
    if r['return']>0: return r

    flx=r['list']

    try:
       f=open(os.path.join(curdir0,fname), 'wb')
       z=zipfile.ZipFile(f, 'w', zipfile.ZIP_DEFLATED)

       for fn in flx:
           z.write(fn, fn, zipfile.ZIP_DEFLATED)

       # ck-install.json
       z.close()
       f.close()

    except Exception as e:
       return {'return':1, 'error':'failed to prepare CK artifact collections ('+format(e)+')'}

    os.chdir(curdir0)

    if os.path.isdir(ptmp) and force_clean:
       shutil.rmtree(ptmp, onerror=ck.rm_read_only)

    return {'return':0}
