#
# Collective Knowledge (some common operations for all CK)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin, Grigori.Fursin@cTuning.org, http://cTuning.org/lab/people/gfursin
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
# update CK and all repos

def pull(i):
    """
    Input:  {
              (kernel)  - if 'yes', pull kernel too (unless installed as a package)
              (install) - if 'yes', install CK kernel as python module (via python setup.py install)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    o=i.get('out','')

    kernel=i.get('kernel','')
    install=i.get('install','')

    if kernel=='yes' or install=='yes':
       ck_root=ck.work['env_root']

       if not os.path.isdir(ck_root):
          return {'return':1, 'error':'Can\'t find CK in '+ck_root+' - please check CK_ROOT env'}

       os.chdir(ck_root)

    if kernel=='yes':
       cont=True
       if not os.path.isdir(os.path.join(ck_root,'.git')) and i.get('force','')!='yes':
          ck.out('WARNING: seems like your CK_ROOT installation is not from GitHub - skipping kernel update ...')
          ck.out('')
          cont=False

       if cont:
          if o=='con':
             ck.out('Updating CK from GitHub ...')
             ck.out('')
             ck.out('  cd '+ck_root)
             ck.out('  git pull')
             ck.out('')

          rx=os.system('git pull')
          if rx>0: 
             return {'return':1, 'error':'CK update failed'}

          if o=='con':
             ck.out('')

    if install=='yes':
       c=ck.cfg['install_ck_as_lib']

       py=os.getenv('CK_PYTHON','')
       if py!='':
          c=c.replace('python ',py+' ')

       ck.out('')
       ck.out('Installing CK kernel as python module ...')

       ck.out('')
       ck.out('  cd '+ck_root)

       # Get OS
       r=ck.get_os_ck({})
       if r['return']>0: return r
       plat=r['platform']
       if plat!='win':
          c=ck.cfg.get('linux_sudo','')+' '+c

       ck.out('  '+c)
       ck.out('')
       os.system(c)

    return ck.access({'action':'pull',
                      'module_uoa':'repo',
                      'out':o})
