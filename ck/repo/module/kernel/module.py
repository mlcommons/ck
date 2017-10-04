#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel)

# Local settings
sep='======================================================================='

import sys
import os
import copy

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
# CK kernel setup

def setup(i):
    """

    Input:  {
              (param)      - if !='', configure only this group:
                             * recache - recache repos (needed during first run for remote repos)
                             * install - install as python library
                             * update - check for update
                             * content - related to content
                             * repos - related to repositories
                             * git - related to git repos
                             * editing - related to editing
                             * writing - related to writing control
                             * wfe - related to web front end
                             * indexing - related to indexing
                             * (vars) - internal - update/print kernel variables
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Get OS
    r=ck.get_os_ck({})
    if r['return']>0: return r
    plat=r['platform']

    # Check groups of parameters
    param=i.get('param','')
    if param=='':
       if i.get('content','')=='yes': param='content'
       elif i.get('install','')=='yes': param='install'
       elif i.get('update','')=='yes': param='update'
       elif i.get('editing','')=='yes': param='editing'
       elif i.get('git','')=='yes': param='git'
       elif i.get('repos','')=='yes': param='repos'
       elif i.get('writing','')=='yes': param='writing'
       elif i.get('wfe','')=='yes': param='wfe'
       elif i.get('indexing','')=='yes': param='indexing'

    # Check if var
    vr={}
    for k in i:
        if k.startswith('var.'):
           vr[k[4:]]=i[k]

    if len(i.get('cids',[]))>0:
       for k in i['cids']:
           if k.startswith('var.'):
               vr[k[4:]]=None

    if len(vr)>0 and param=='':
       param='vars' # to avoid selecting all sub-scenarios below

    # Get current configuration
    xcfg={}

    ck.out(sep)
    ck.out('Loading current configuration ...')

    r=ck.access({'action':'load',
                 'repo_uoa':ck.cfg['repo_name_default'],
                 'module_uoa':ck.cfg['subdir_kernel'],
                 'data_uoa':ck.cfg['subdir_kernel_default']})
    if r['return']==0:
       xcfg.update(r['dict'])

    r=ck.access({'action':'load',
                 'repo_uoa':ck.cfg['repo_name_local'],
                 'module_uoa':ck.cfg['subdir_kernel'],
                 'data_uoa':ck.cfg['subdir_kernel_default']})
    if r['return']==0:
       xcfg.update(r['dict'])

    copy_xcfg=copy.deepcopy(xcfg) # to check if changed

    # Recaching repos
    if param=='' or param=='recache':
       ck.out(sep)
       ck.out('*** Caching all repos (to speed up search) ***')

       ck.out('')
       r=ck.inp({'text':'Would you like to (re)cache all repos (y/N): '})
       d=''
       x=r['string'].lower()
       if x=='y' or x=='yes':
          ck.out('')

          r=ck.access({'action':'recache',
                       'module_uoa':cfg['module_deps']['repo'],
                       'out':'con'})
          if r['return']>0: return r

    # Install options
    if param=='' or param=='install':
       ck.out(sep)
       ck.out('*** Installation of CK as python library ***')

       installed=True
       try:
          import ck.kernel as ckx
       except Exception as e:
          installed=False

       if param=='install' or (param=='' and not installed and xcfg.get('skip_ck_install','')!='yes'):
          ck.out('')
          r=ck.inp({'text':'Would you like to install CK as root library (y/N): '})
          d=''
          x=r['string'].lower()
          if x=='y' or x=='yes':
             d='yes'
          else:
             r1=ck.inp({'text':'Do not ask this question again (Y/n): '})
             d1=''
             x1=r1['string'].lower()
             if x1=='y' or x1=='yes':
                xcfg['skip_ck_install']='yes'

          if d=='yes':
             p=ck.work['env_root']
             ck.out('')
             ck.out('* Changing directory to '+p+' ...')
             os.chdir(p)

             c=ck.cfg['install_ck_as_lib']

             # Get OS
             r=ck.get_os_ck({})
             if r['return']>0: return r
             plat=r['platform']
             if plat!='win':
                c=ck.cfg.get('linux_sudo','')+' '+c

             ck.out('')
             ck.out('* Executing command "'+c+'" ...')
             os.system(c)

       installed=True
       try:
          import ck.kernel as ckx
       except Exception as e:
          installed=False

       if installed:
          ck.out('')
          ck.out('CK is now installed as python library. Testing ...')
          ck.out('')
          ckx.test()
       else:
          ck.out('')
          ck.out('CK was not installed as Python library.')

    # Content authorship options
    if param=='' or param=='update':
       ck.out(sep)
       ck.out('*** Check latest version ***')

       ck.out('')
       r=ck.inp({'text': 'Would you like to check if your version is up-to-date (Y/n): '})
       x=r['string'].lower()
       if x!='n' and x!='no':
          ck.out('')
          ck.status({'out':'con'})

    # Content authorship options
    if param=='' or param=='content':
       ck.out(sep)
       ck.out('*** Content authorship ***')

       ck.out('')
       ck.out('Current author/developer of the content: '+xcfg.get('default_developer', ck.cfg.get('default_developer','')))
       ck.out('Current author/developer email :         '+xcfg.get('default_developer_email', ck.cfg.get('default_developer_email','')))
       ck.out('Current author/developer webpage :       '+xcfg.get('default_developer_webpage', ck.cfg.get('default_developer_webpage','')))
       ck.out('Current copyright of the content:        '+xcfg.get('default_copyright', ck.cfg.get('default_copyright','')))
       ck.out('Current license of the content:          '+xcfg.get('default_license', ck.cfg.get('default_license','')))

       ck.out('')

       r=ck.inp({'text': 'Change author/developer of the content (or Enter to keep previous): '})
       d=r['string']
       if d!='': xcfg['default_developer']=d

       r=ck.inp({'text': 'Change author/developer email (or Enter to keep previous):          '})
       d=r['string']
       if d!='': xcfg['default_developer_email']=d

       r=ck.inp({'text': 'Change author/developer webpage (or Enter to keep previous):        '})
       d=r['string']
       if d!='': xcfg['default_developer_webpage']=d

       r=ck.inp({'text': 'Change copyright of the content (or Enter to keep previous):        '})
       d=r['string']
       if d!='': xcfg['default_copyright']=d

       r=ck.inp({'text': 'Change license of the content (or Enter to keep previous):          '})
       d=r['string']
       if d!='': xcfg['default_license']=d

    # Repo options
    if param=='' or param=='repos':
       ck.out(sep)
       ck.out('*** Repositories control ***')

       ck.out('')
       x=xcfg.get('default_shared_repo_url','')
       if x=='':
          x=ck.cfg.get('default_shared_repo_url','')
       ck.out('Default URL for shared repositories: '+x)

       ck.out('')
       r=ck.inp({'text': 'Enter new URL (Enter to keep current): '})
       x=r['string']
       if x!='':
          xcfg['default_shared_repo_url']=x

    # Editing options
    if param=='' or param=='editing':
       ck.out(sep)
       ck.out('*** Editing control ***')

       ck.out('')
       ck.out('CMD to edit meta-description of entries: '+xcfg.get('external_editor',ck.cfg.get('external_editor',{})).get(plat,''))

       ck.out('')
       r=ck.inp({'text': 'Enter CMD to enter meta-description using $#filename#$ to substitute filename (Enter to keep previous): '})
       d=r['string']
       if d!='':
          if 'external_editor' not in xcfg: xcfg['external_editor']={}
          xcfg['external_editor'][plat]=d

    # Git options
    if param=='' or param=='git':
       ck.out(sep)
       ck.out('*** Set up GIT repos ***')

       ck.out('')
       ck.out('Current URL of default GIT repo with user : '+xcfg.get('default_shared_repo_url', ck.cfg.get('default_shared_repo_url','')))
       ck.out('Current URL of default GIT repo :           '+xcfg.get('github_repo_url', ck.cfg.get('github_repo_url','')))

       ck.out('')

       r=ck.inp({'text': 'Change URL of default GIT repo with user (or Enter to keep previous): '})
       d=r['string']
       if d!='': xcfg['default_shared_repo_url']=d

       r=ck.inp({'text': 'Change URL of default GIT repo (or Enter to keep previous):           '})
       d=r['string']
       if d!='': xcfg['github_repo_url']=d

    # Writing options
    if param=='' or param=='writing':
       ck.out(sep)
       ck.out('*** Writing control ***')

       ck.out('')
       ck.out('Forbid all writing operations (useful for permanent web-based repositories):     '+xcfg.get('forbid_global_writing' ,ck.cfg.get('forbid_global_writing','')))
       ck.out('Forbid delete/rename operations (useful for aggregating web-based repositories): '+xcfg.get('forbid_global_delete' ,ck.cfg.get('forbid_global_delete','')))
       ck.out('Forbid writing modules (adding/updating/removing):                               '+xcfg.get('forbid_writing_modules', ck.cfg.get('forbid_writing_modules','')))
       ck.out('Forbid writing to default repo:                                                  '+xcfg.get('forbid_writing_to_default_repo' ,ck.cfg.get('forbid_writing_to_default_repo','')))
       ck.out('Forbid writing to local repo:                                                    '+xcfg.get('forbid_writing_to_local_repo', ck.cfg.get('forbid_writing_to_local_repo','')))
       ck.out('Allow writing only to allowed individual repos:                                  '+xcfg.get('allow_writing_only_to_allowed', ck.cfg.get('allow_writing_only_to_allowed','')))

       ck.out('')
       r=ck.inp({'text': 'Forbid all writing operations (yes or Enter to keep previous)?:                  '})
       d=r['string'].lower()
       if d=='y': d=='yes'
       if d!='': xcfg['forbid_global_writing']=d

       r=ck.inp({'text': 'Forbid all delete operations (yes or Enter to keep previous)?:                   '})
       d=r['string'].lower()
       if d=='y': d=='yes'
       if d!='': xcfg['forbid_global_delete']=d

       r=ck.inp({'text': 'Forbid adding new modules (yes or Enter to keep previous)?:                      '})
       d=r['string'].lower()
       if d=='y': d=='yes'
       if d!='': xcfg['forbid_writing_modules']=d

       r=ck.inp({'text': 'Forbid writing to default repo (yes or Enter to keep previous)?:                 '})
       d=r['string'].lower()
       if d=='y': d=='yes'
       if d!='': xcfg['forbid_writing_to_default_repo']=d

       r=ck.inp({'text': 'Forbid writing to local repo (yes or Enter to keep previous)?:                   '})
       d=r['string'].lower()
       if d=='y': d=='yes'
       if d!='': xcfg['forbid_writing_to_local_repo']=d

       r=ck.inp({'text': 'Allow writing only to allowed individual repos (yes or Enter to keep previous)?: '})
       d=r['string'].lower()
       if d=='y': d=='yes'
       if d!='': xcfg['allow_writing_only_to_allowed']=d

    # Web front-end options
    if param=='' or param=='wfe':
       ck.out(sep)
       ck.out('*** Web front-end control (via CK web server, or third-party web server and CK PHP connector) ***')

       ck.out('')

       x=xcfg.get('wfe_host','')
       if x=='': x=ck.cfg.get('wfe_host','')
       ck.out('Current web front-end host: '+x)

       x=xcfg.get('wfe_port','')
       if x=='': x=ck.cfg.get('wfe_port','')
       ck.out('Current web front-end port: '+x)

       x=xcfg.get('wfe_template','')
       if x=='': x=ck.cfg.get('wfe_template','')
       ck.out('Current web front-end template: '+x)

       ck.out('')

       r=ck.inp({'text': 'Enter new web front-end host (Enter to keep previous): '})
       x=r['string']
       if x!='': xcfg['wfe_host']=x

       r=ck.inp({'text': 'Enter new web front-end port (Enter to keep previous): '})
       x=r['string']
       if x!='': xcfg['wfe_port']=x

       r=ck.inp({'text': 'Enter new web front-end template (Enter to keep previous): '})
       x=r['string']
       if x!='': xcfg['wfe_template']=x

    # Indexing options
    if param=='' or param=='indexing':
       ck.out(sep)
       ck.out('*** Indexing control (through ElasticSearch) ***')

       ck.out('')
       ck.out('Use indexing: '+xcfg.get('use_indexing' ,ck.cfg.get('use_indexing','')))

       ck.out('')
       r=ck.inp({'text': 'Use indexing (yes or Enter to keep previous)?: '})
       d=r['string'].lower()
       if d=='y': d=='yes'
       if d!='': xcfg['use_indexing']=d

    # Checking vars
    if param=='vars':
       ck.out('')
       ck.out('Kernel variables:')
       ck.out('')

       if len(vr)==0:
          r=ck.flatten_dict({'dict':xcfg})
          if r['return']>0: return r
          xd=r['dict']

          for k in sorted(xd):
              vv=str(xd[k])
              if vv=='': vv='""'
              ck.out(' * '+k+' = '+vv)

       else:
          for k in vr:
              kk=k
              if not kk.startswith('#'):
                 kk='##'+kk

              r=ck.get_by_flat_key({'dict':xcfg, 'key':kk})
              if r['return']>0: return r
              v=r['value']

              if v==None: # If empty, try from internal configuration
                 r=ck.get_by_flat_key({'dict':ck.cfg, 'key':kk})
                 if r['return']>0: return r
                 v=r['value']

              vc=str(v) # current value

              v=vr[k] # new value (or print current if none)
              vv=str(v)

              x1=vc
              x2=''
              if v!=None and vc!=vv:
                 r=ck.set_by_flat_key({'dict':xcfg, 'key':kk, 'value':v})
                 if r['return']>0: return r

                 if vc=='': vc='""'
                 x1=vv
                 x2=' (changed from '+vc+')'

              if x1=='': x1='""'

              ck.out(' * '+k+' = '+x1+x2)

       ck.out('')

    # Writing/updating configuration
    if xcfg!=copy_xcfg:
       ck.out(sep)

       fc=ck.work['dir_work_cfg']
       if os.path.isfile(fc):
          ck.out('Updating local configuration (directly) ...')
          r=ck.save_json_to_file({'json_file':fc, 'dict':xcfg, 'sort_keys':'yes'})
       else:
          ck.out('Adding local configuration ...')
          ii={'action':'update',
              'repo_uoa':ck.cfg['repo_name_local'],
              'module_uoa':work['self_module_uoa'],
              'data_uoa':ck.cfg['subdir_kernel_default'],
              'dict':xcfg,
              'substitute':'yes',
              'ignore_update':'yes',
              'sort_keys':'yes'}
          r=ck.access(ii)

       if r['return']>0: return r

       ck.out('')
       ck.out('Configuration successfully recorded to '+fc+' ...')

    return {'return':0}

##############################################################################
# set variable in kernel

def set(i):
    """
    Input:  {
              (kernel key) (=xyz)
                 or
              var.(kernel key) (=xyz) 
                               for example, "ck set kernel var.install_to_env" will print install_to_env var
                                            "ck set kernel var.install_to_env=yes" will set install_to_env var to yes
                                            "ck set kernel var.install_to_env=" will set install_to_env var to ""
                                            "ck set kernel" will print all vars
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['param']='vars'
    return setup(i)
