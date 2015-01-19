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
sep='======================================================================='

import sys
import os

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
              (group)      - if !='', configure only this group:
                             * install - install as python library
                             * content - related to content 
                             * editing - related to editing
                             * writing - related to writing control 
                             * indexing - related to indexing
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Get OS
    r=ck.get_platform({})
    if r['return']>0: return r
    plat=r['platform']

    # Check groups 
    param=i.get('param','')
    if param=='':
       if i.get('content','')=='yes': param='content'
       elif i.get('install','')=='yes': param='install'
       elif i.get('editing','')=='yes': param='editing'
       elif i.get('writing','')=='yes': param='writing'
       elif i.get('indexing','')=='yes': param='indexing'

    # Get current configuration
    cfg={}

    ck.out(sep)
    ck.out('Loading current configuration ...')

    r=ck.access({'action':'load',
                 'repo_uoa':ck.cfg['repo_name_default'],
                 'module_uoa':ck.cfg['subdir_kernel'],
                 'data_uoa':ck.cfg['subdir_kernel_default']})
    if r['return']==0: 
       cfg.update(r['dict'])

    r=ck.access({'action':'load',
                 'repo_uoa':ck.cfg['repo_name_local'],
                 'module_uoa':ck.cfg['subdir_kernel'],
                 'data_uoa':ck.cfg['subdir_kernel_default']})
    if r['return']==0: 
       cfg.update(r['dict'])

    # Install options
    if param=='' or param=='install':
       ck.out(sep)
       ck.out('*** Installation of CK as python library ***')

       installed=True
       try:
          import ck.kernel as ckx
       except Exception as e:
          installed=False

       if param=='install' or (param=='' and not installed and cfg.get('skip_ck_install','')!='yes'):
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
                cfg['skip_ck_install']='yes'

          if d=='yes':
             p=ck.work['env_root']
             ck.out('')
             ck.out('* Changing directory to '+p+' ...')
             os.chdir(p)

             c=ck.cfg['install_ck_as_lib']

             # Get OS
             r=ck.get_platform({})
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
    if param=='' or param=='content':
       ck.out(sep)
       ck.out('*** Content authorship ***')

       ck.out('')
       ck.out('Current author/developer of the content: '+cfg.get('default_developer', ck.cfg.get('default_developer','')))
       ck.out('Current author/developer email :         '+cfg.get('default_developer_email', ck.cfg.get('default_developer_email','')))
       ck.out('Current author/developer webpage :       '+cfg.get('default_developer_webpage', ck.cfg.get('default_developer_webpage','')))
       ck.out('Current copyright of the content:        '+cfg.get('default_copyright', ck.cfg.get('default_copyright','')))
       ck.out('Current license of the content:          '+cfg.get('default_license', ck.cfg.get('default_license','')))

       ck.out('')

       r=ck.inp({'text': 'Change author/developer of the content (or Enter to keep previous): '})
       d=r['string']
       if d!='': cfg['default_developer']=d

       r=ck.inp({'text': 'Change author/developer email (or Enter to keep previous):          '})
       d=r['string']
       if d!='': cfg['default_developer_email']=d

       r=ck.inp({'text': 'Change author/developer webpage (or Enter to keep previous):        '})
       d=r['string']
       if d!='': cfg['default_developer_webpage']=d

       r=ck.inp({'text': 'Change copyright of the content (or Enter to keep previous):        '})
       d=r['string']
       if d!='': cfg['default_copyright']=d

       r=ck.inp({'text': 'Change license of the content (or Enter to keep previous):          '})
       d=r['string']
       if d!='': cfg['default_license']=d

    # Editing options
    if param=='' or param=='editing':
       ck.out(sep)
       ck.out('*** Editing control ***')

       ck.out('')
       ck.out('CMD to edit meta-description of entries: '+cfg.get('external_editor',ck.cfg.get('external_editor',{})).get(plat,''))

       ck.out('')
       r=ck.inp({'text': 'Enter CMD to enter meta-description using $#filename#$ to substitute filename (Enter to keep previous): '})
       d=r['string']
       if d!='': 
          if 'external_editor' not in cfg: cfg['external_editor']={}
          cfg['external_editor'][plat]=d

    # Writing options
    if param=='' or param=='writing':
       ck.out(sep)
       ck.out('*** Writing control ***')

       ck.out('')
       ck.out('Forbid all writing operations (useful for permanent web-based repositories):     '+cfg.get('forbid_global_writing' ,ck.cfg.get('forbid_global_writing','')))
       ck.out('Forbid delete/rename operations (useful for aggregating web-based repositories): '+cfg.get('forbid_global_delete' ,ck.cfg.get('forbid_global_delete','')))
       ck.out('Forbid writing modules (adding/updating/removing):                               '+cfg.get('forbid_writing_modules', ck.cfg.get('forbid_writing_modules','')))
       ck.out('Forbid writing to default repo:                                                  '+cfg.get('forbid_writing_to_default_repo' ,ck.cfg.get('forbid_writing_to_default_repo','')))
       ck.out('Forbid writing to local repo:                                                    '+cfg.get('forbid_writing_to_local_repo', ck.cfg.get('forbid_writing_to_local_repo','')))
       ck.out('Allow writing only to allowed individual repos:                                  '+cfg.get('allow_writing_only_to_allowed', ck.cfg.get('allow_writing_only_to_allowed','')))

       ck.out('')
       r=ck.inp({'text': 'Forbid all writing operations (yes or Enter to keep previous)?:                  '})
       d=r['string'].lower()
       if d=='y': d=='yes'
       if d!='': cfg['forbid_global_writing']=d

       r=ck.inp({'text': 'Forbid all delete operations (yes or Enter to keep previous)?:                   '})
       d=r['string'].lower()
       if d=='y': d=='yes'
       if d!='': cfg['forbid_global_delete']=d

       r=ck.inp({'text': 'Forbid adding new modules (yes or Enter to keep previous)?:                      '})
       d=r['string'].lower()
       if d=='y': d=='yes'
       if d!='': cfg['forbid_writing_modules']=d

       r=ck.inp({'text': 'Forbid writing to default repo (yes or Enter to keep previous)?:                 '})
       d=r['string'].lower()
       if d=='y': d=='yes'
       if d!='': cfg['forbid_writing_to_default_repo']=d

       r=ck.inp({'text': 'Forbid writing to local repo (yes or Enter to keep previous)?:                   '})
       d=r['string'].lower()
       if d=='y': d=='yes'
       if d!='': cfg['forbid_writing_to_local_repo']=d

       r=ck.inp({'text': 'Allow writing only to allowed individual repos (yes or Enter to keep previous)?: '})
       d=r['string'].lower()
       if d=='y': d=='yes'
       if d!='': cfg['allow_writing_only_to_allowed']=d

    # Indexing options
    if param=='' or param=='indexing':
       ck.out(sep)
       ck.out('*** Indexing control (through ElasticSearch) ***')

       ck.out('')
       ck.out('Use indexing: '+cfg.get('use_indexing' ,ck.cfg.get('use_indexing','')))

       ck.out('')
       r=ck.inp({'text': 'Use indexing (yes or Enter to keep previous)?: '})
       d=r['string'].lower()
       if d=='y': d=='yes'
       if d!='': cfg['use_indexing']=d

    # Writing/updating configuration
    ck.out(sep)

    fc=ck.work['dir_work_cfg']
    if os.path.isfile(fc):
       ck.out('Writing local configuration (directly) ...')
       r=ck.save_json_to_file({'json_file':fc, 'dict':cfg})
    else:
       ck.out('Adding local configuration ...')
       ii={'action':'update',
           'repo_uoa':ck.cfg['repo_name_local'],
           'module_uoa':work['self_module_uoa'],
           'data_uoa':ck.cfg['subdir_kernel_default'],
           'dict':cfg,
           'substitute':'yes',
           'ignore_update':'yes'}
       r=ck.access(ii)

    if r['return']>0: return r

    ck.out('')
    ck.out('Configuration successfully recorded to '+fc+' ...')

    return {'return':0}
