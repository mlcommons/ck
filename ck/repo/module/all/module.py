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
              (kernel) - if 'yes', pull kernel too (unless installed as a package)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    o=i.get('out','')

    if i.get('kernel','')=='yes':
       ck_root=ck.work['env_root']
       os.chdir(ck_root)

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

    return ck.access({'action':'pull',
                      'module_uoa':'repo',
                      'out':o})
