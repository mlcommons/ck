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
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    param=i.get('param','')

    # Check if local repo
    dlrp=ck.work['dir_default_repo']
    if dlrp=='':
       ck.out(sep)
       ck.out('Local repository is not defined:')
       ck.out('* environment variable '+ck.cfg['env_key_local_repo']+' is empty!')
       ck.out('')
       ck.out('We strongly recommend you to set up local repository to avoid polluting CK:')
       ck.out('')
       ck.out('* Select directory where local or downloaded repositories will reside (for example, /home/user/ck-repos).')
       ck.out('')
       ck.out('* Add environment variable CK_REPOS pointing to this directory to your profile.')
       ck.out('  (for example, export CK_REPOS=/home/user/ck-repos or set CK_REPOS=/home/user/ck-repos')
       ck.out('')
       ck.out('* Create "local-repo" directory there (for example, $CK_REPOS/local or %CK_REPOS%\\local)')
       ck.out('')
       ck.out('* Add environment variable CK_LOCAL_REPO pointing to this directory to your profile.')
       ck.out('  (for example, export CK_LOCAL_REPO=$CK_REPOS/local or set CK_LOCAL_REPO=%CK_REPOS%\\local')
 
       return {'return':0}

    # Install options
    if param=='' or param=='install':
       ck.out(sep)
       ck.out('*** Installation of CK as python library ***')

       installed=True
       try:
          import ck.kernel as ckx
       except Exception as e:
          installed=False

       if installed:
          ck.out('')
          ck.out('CK is installed as python library. Testing ...')
          ck.out('')
          ckx.test()
       else:
          ck.out('')
          ck.out('CK is not installed as Python library.')

       if not installed or param=='install':
          ck.out('')
          r=ck.inp({'text':'Would you like to install CK as root library (yes or no/Enter): '})
          d=r['string'].lower()
          if d=='yes':

             p=ck.work['env_root']
             ck.out('')
             ck.out('* Changing directory to '+p+' ...')
             os.chdir(p)

             c='python setup.py install'
             ck.out('')
             ck.out('* Executing command "'+c+'" ...')
             os.system(c)

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

    # Developer options
    if param=='' or param=='content':
       ck.out(sep)
       ck.out('*** Content authorship ***')

       ck.out('')
       ck.out('Current author/developer of the content: '+cfg.get('default_developer' ,ck.cfg.get('default_developer','')))
       ck.out('Current copyright of the content:        '+cfg.get('default_copyright', ck.cfg.get('default_copyright','')))
       ck.out('Current license of the content:          '+cfg.get('default_license', ck.cfg.get('default_license','')))

       ck.out('')
       r=ck.inp({'text': 'Change author/developer of the content (or Enter to keep previous): '})
       d=r['string']
       if d!='': cfg['default_developer']=d

       r=ck.inp({'text': 'Change copyright of the content (or Enter to keep previous):        '})
       d=r['string']
       if d!='': cfg['default_copyright']=d

       r=ck.inp({'text': 'Change license of the content (or Enter to keep previous):          '})
       d=r['string']
       if d!='': cfg['default_license']=d






    # Writing/updating configuration
    ck.out(sep)
    ck.out('Writing local configuration ...')

    r=ck.access({'action':'update',
                 'repo_uoa':ck.cfg['repo_name_local'],
                 'module_uoa':ck.cfg['subdir_kernel'],
                 'data_uoa':ck.cfg['subdir_kernel_default'],
                 'dict':cfg,
                 'substitute':'yes',
                 'ignore_update':'yes'})
    if r['return']>0: return r

    p=r['path']

    ck.out('')
    ck.out('Configuration successfully recorded to entry '+p+' ...')

    return {'return':0}
