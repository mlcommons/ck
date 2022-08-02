#
# Collective Knowledge ()
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
# joke

def make(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    cids=i.get('cids',[])

    x=''
    if len(cids)>0:
       x=cids[0]

    if x=='':
       ck.out('happy ...')

    elif x=='happy':
       ck.out('Of course!')

    elif x=='unhappy':
       ck.out('What??????')

    else:
       ck.out('Are you sure? Ok, CK will try to make you '+x+' ...')

    ck.out('')
    ck.out('CK rules:')
    ck.out('')
    ck.out('1) CK always makes you happy!')
    ck.out('2) If CK doesn\'t make you happy - see rule 1')

    return {'return':0}
